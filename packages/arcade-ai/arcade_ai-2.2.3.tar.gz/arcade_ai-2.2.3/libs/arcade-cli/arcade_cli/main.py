import asyncio
import os
import threading
import traceback
import uuid
import webbrowser
from pathlib import Path
from typing import Any, Optional

import httpx
import typer
from arcadepy import Arcade
from arcadepy.types import AuthorizationResponse
from openai import OpenAI, OpenAIError
from rich.console import Console
from rich.markup import escape
from rich.text import Text
from tqdm import tqdm

import arcade_cli.worker as worker
from arcade_cli.authn import LocalAuthCallbackServer, check_existing_login
from arcade_cli.constants import (
    CREDENTIALS_FILE_PATH,
    LOCALHOST,
    PROD_CLOUD_HOST,
    PROD_ENGINE_HOST,
)
from arcade_cli.deployment import Deployment
from arcade_cli.display import (
    display_arcade_chat_header,
    display_eval_results,
    display_tool_messages,
)
from arcade_cli.show import show_logic
from arcade_cli.toolkit_docs import generate_toolkit_docs
from arcade_cli.utils import (
    OrderCommands,
    compute_base_url,
    compute_login_url,
    get_eval_files,
    get_today_context,
    get_user_input,
    handle_chat_interaction,
    handle_tool_authorization,
    handle_user_command,
    is_authorization_pending,
    load_eval_suites,
    log_engine_health,
    require_dependency,
    validate_and_get_config,
    version_callback,
)

cli = typer.Typer(
    cls=OrderCommands,
    add_completion=False,
    no_args_is_help=True,
    pretty_exceptions_enable=True,
    pretty_exceptions_show_locals=False,
    pretty_exceptions_short=True,
    rich_markup_mode="markdown",
)


cli.add_typer(
    worker.app,
    name="worker",
    help="Manage deployments of tool servers (logs, list, etc)",
    rich_help_panel="Deployment",
)


console = Console()


def handle_cli_error(
    message: str,
    error: Optional[Exception] = None,
    debug: bool = True,
    should_exit: bool = True,
) -> None:
    """Handle CLI error reporting with optional debug traceback and exit."""
    if error and debug:
        console.print(f"❌ {message}: {traceback.format_exc()}", style="bold red")
    elif error:
        console.print(f"❌ {message}: {escape(str(error))}", style="bold red")
    else:
        console.print(f"❌ {message}", style="bold red")

    if should_exit:
        raise typer.Exit(code=1)


@cli.command(help="Log in to Arcade Cloud", rich_help_panel="User")
def login(
    host: str = typer.Option(
        PROD_CLOUD_HOST,
        "-h",
        "--host",
        help="The Arcade Cloud host to log in to.",
    ),
    port: Optional[int] = typer.Option(
        None,
        "-p",
        "--port",
        help="The port of the Arcade Cloud host (if running locally).",
    ),
    callback_host: str = typer.Option(
        None,
        "--callback-host",
        help="The host to use to complete the auth flow - this should be the same as the host that the CLI is running on. Include the port if needed.",
    ),
    debug: bool = typer.Option(False, "--debug", "-d", help="Show debug information"),
) -> None:
    """
    Logs the user into Arcade Cloud.
    """

    if check_existing_login():
        console.print("\nTo log out and delete your locally-stored credentials, use ", end="")
        console.print("arcade logout", style="bold green", end="")
        console.print(".\n")
        return

    # Start the HTTP server in a new thread
    state = str(uuid.uuid4())
    auth_server = LocalAuthCallbackServer(state)
    server_thread = threading.Thread(target=auth_server.run_server)
    server_thread.start()

    try:
        # Open the browser for user login
        login_url = compute_login_url(host, state, port, callback_host)

        console.print("Opening a browser to log you in...")
        if not webbrowser.open(login_url):
            console.print(
                f"If a browser doesn't open automatically, copy this URL and paste it into your browser: {login_url}",
                style="dim",
            )

        # Wait for the server thread to finish
        server_thread.join()
    except KeyboardInterrupt:
        auth_server.shutdown_server()
    except Exception as e:
        handle_cli_error("Login failed", e, debug)
    finally:
        if server_thread.is_alive():
            server_thread.join()  # Ensure the server thread completes and cleans up


@cli.command(help="Log out of Arcade Cloud", rich_help_panel="User")
def logout(
    debug: bool = typer.Option(False, "--debug", "-d", help="Show debug information"),
) -> None:
    """
    Logs the user out of Arcade Cloud.
    """
    try:
        # If the credentials file exists, delete it
        if os.path.exists(CREDENTIALS_FILE_PATH):
            os.remove(CREDENTIALS_FILE_PATH)
            console.print("You're now logged out.", style="bold")
        else:
            console.print("You're not logged in.", style="bold red")
    except Exception as e:
        handle_cli_error("Logout failed", e, debug)


@cli.command(
    help="Create a new toolkit package directory. Example usage: arcade new my_toolkit",
    rich_help_panel="Tool Development",
)
def new(
    toolkit_name: str = typer.Argument(
        help="The name of the toolkit to create",
        metavar="TOOLKIT_NAME",
    ),
    directory: str = typer.Option(os.getcwd(), "--dir", help="tools directory path"),
    debug: bool = typer.Option(False, "--debug", "-d", help="Show debug information"),
) -> None:
    """
    Creates a new toolkit with the given name, description, and result type.
    """
    from arcade_cli.new import create_new_toolkit

    try:
        create_new_toolkit(directory, toolkit_name)
    except Exception as e:
        handle_cli_error("Failed to create new Toolkit", e, debug)


@cli.command(
    help="Show the installed toolkits or details of a specific tool",
    rich_help_panel="Tool Development",
)
def show(
    toolkit: Optional[str] = typer.Option(
        None, "-T", "--toolkit", help="The toolkit to show the tools of"
    ),
    tool: Optional[str] = typer.Option(
        None, "-t", "--tool", help="The specific tool to show details for"
    ),
    host: str = typer.Option(
        PROD_ENGINE_HOST,
        "-h",
        "--host",
        help="The Arcade Engine address to show the tools/toolkits of.",
    ),
    local: bool = typer.Option(
        False,
        "--local",
        "-l",
        help="Show the local environment's catalog instead of an Arcade Engine's catalog.",
    ),
    port: Optional[int] = typer.Option(
        None,
        "-p",
        "--port",
        help="The port of the Arcade Engine.",
    ),
    force_tls: bool = typer.Option(
        False,
        "--tls",
        help="Whether to force TLS for the connection to the Arcade Engine. If not specified, the connection will use TLS if the engine URL uses a 'https' scheme.",
    ),
    force_no_tls: bool = typer.Option(
        False,
        "--no-tls",
        help="Whether to disable TLS for the connection to the Arcade Engine.",
    ),
    worker: bool = typer.Option(
        False,
        "--worker",
        "-w",
        help="Show full worker response structure including error, logs, and authorization fields (only applies when used with -t/--tool).",
    ),
    debug: bool = typer.Option(False, "--debug", "-d", help="Show debug information"),
) -> None:
    """
    Show the available toolkits or detailed information about a specific tool.
    """
    if worker and not tool:
        console.print(
            "⚠️  The -w/--worker flag only affects output when used with -t/--tool flag",
            style="bold yellow",
        )

    show_logic(
        toolkit=toolkit,
        tool=tool,
        host=host,
        local=local,
        port=port,
        force_tls=force_tls,
        force_no_tls=force_no_tls,
        worker=worker,
        debug=debug,
    )


@cli.command(
    help="Start a chat with a model in the terminal to test tools",
    rich_help_panel="Tool Development",
)
def chat(
    model: str = typer.Option("gpt-4o", "-m", "--model", help="The model to use for prediction."),
    stream: bool = typer.Option(
        False, "-s", "--stream", is_flag=True, help="Stream the tool output."
    ),
    prompt: str = typer.Option(None, "--prompt", help="The system prompt to use for the chat."),
    debug: bool = typer.Option(False, "--debug", "-d", help="Show debug information"),
    host: str = typer.Option(
        PROD_ENGINE_HOST,
        "-h",
        "--host",
        help="The Arcade Engine address to send chat requests to.",
    ),
    port: Optional[int] = typer.Option(
        None,
        "-p",
        "--port",
        help="The port of the Arcade Engine.",
    ),
    force_tls: bool = typer.Option(
        False,
        "--tls",
        help="Whether to force TLS for the connection to the Arcade Engine. If not specified, the connection will use TLS if the engine URL uses a 'https' scheme.",
    ),
    force_no_tls: bool = typer.Option(
        False,
        "--no-tls",
        help="Whether to disable TLS for the connection to the Arcade Engine.",
    ),
) -> None:
    """
    Chat with a language model.
    """
    try:
        import readline
    except ImportError:
        console.print(
            "Readline is not available on this platform. Command history will be limited.",
            style="dim",
        )

    config = validate_and_get_config()
    base_url = compute_base_url(force_tls, force_no_tls, host, port)

    client = Arcade(api_key=config.api.key, base_url=base_url)
    user_email = config.user.email if config.user else None

    try:
        # start messages conversation
        history: list[dict[str, Any]] = []

        # Ground the LLM with today's date and day of the week to help when calling date-related tools
        # in case the user refers to relative dates (e.g. next Monday, last month, etc)
        today_context = get_today_context()

        if prompt:
            prompt = f"{today_context} {prompt}"
        else:
            prompt = today_context

            history.append({"role": "system", "content": prompt})

        display_arcade_chat_header(base_url, stream)

        # Try to hit /health endpoint on engine and warn if it is down
        log_engine_health(client)

        while True:
            console.print(
                f"\n[magenta][bold]User[/bold] {user_email}: [/magenta]"
                + "([bold][default]/?[/default][/bold] for help)"
            )

            user_input = get_user_input()

            # Add the input to history
            readline.add_history(user_input)

            if handle_user_command(
                user_input, history, host, port, force_tls, force_no_tls, show_logic
            ):
                continue

            history.append({"role": "user", "content": user_input})

            try:
                # TODO fixup configuration to remove this + "/v1" workaround
                openai_client = OpenAI(api_key=config.api.key, base_url=base_url + "/v1")
                chat_result = handle_chat_interaction(
                    openai_client, model, history, user_email, stream
                )

                history = chat_result.history
                tool_messages = chat_result.tool_messages
                tool_authorization = chat_result.tool_authorization

                # wait for tool authorizations to complete, if any
                if tool_authorization and is_authorization_pending(tool_authorization):
                    chat_result = handle_tool_authorization(
                        client,
                        AuthorizationResponse.model_validate(tool_authorization),
                        history,
                        openai_client,
                        model,
                        user_email,
                        stream,
                    )
                    history = chat_result.history
                    tool_messages = chat_result.tool_messages

            except OpenAIError as e:
                handle_cli_error("Arcade Chat failed", e, debug, should_exit=False)
                continue
            if debug:
                display_tool_messages(tool_messages)

    except KeyboardInterrupt:
        console.print("Chat stopped by user.", style="bold blue")
        typer.Exit()

    except RuntimeError as e:
        handle_cli_error("Failed to run tool", e, debug)


@cli.command(help="Run tool calling evaluations", rich_help_panel="Tool Development")
def evals(
    directory: str = typer.Argument(".", help="Directory containing evaluation files"),
    show_details: bool = typer.Option(False, "--details", "-d", help="Show detailed results"),
    max_concurrent: int = typer.Option(
        1,
        "--max-concurrent",
        "-c",
        help="Maximum number of concurrent evaluations (default: 1)",
    ),
    models: str = typer.Option(
        "gpt-4o",
        "--models",
        "-m",
        help="The models to use for evaluation (default: gpt-4o). Use commas to separate multiple models.",
    ),
    host: str = typer.Option(
        LOCALHOST,
        "-h",
        "--host",
        help="The Arcade Engine address to send chat requests to.",
    ),
    cloud: bool = typer.Option(
        False,
        "--cloud",
        help="Whether to run evaluations against the Arcade Cloud Engine. Overrides the 'host' option.",
    ),
    port: Optional[int] = typer.Option(
        None,
        "-p",
        "--port",
        help="The port of the Arcade Engine.",
    ),
    force_tls: bool = typer.Option(
        False,
        "--tls",
        help="Whether to force TLS for the connection to the Arcade Engine. If not specified, the connection will use TLS if the engine URL uses a 'https' scheme.",
    ),
    force_no_tls: bool = typer.Option(
        False,
        "--no-tls",
        help="Whether to disable TLS for the connection to the Arcade Engine.",
    ),
    debug: bool = typer.Option(False, "--debug", help="Show debug information"),
) -> None:
    """
    Find all files starting with 'eval_' in the given directory,
    execute any functions decorated with @tool_eval, and display the results.
    """
    require_dependency(
        package_name="arcade_evals",
        command_name="evals",
        install_command=r"pip install 'arcade-ai\[evals]'",
    )
    # Although Evals does not depend on the TDK, some evaluations import the
    # ToolCatalog class from the TDK instead of from arcade_core, so we require
    # the TDK to run the evals CLI command to avoid possible import errors.
    require_dependency(
        package_name="arcade_tdk",
        command_name="evals",
        install_command=r"pip install arcade-tdk",
    )

    config = validate_and_get_config()

    host = PROD_ENGINE_HOST if cloud else host
    base_url = compute_base_url(force_tls, force_no_tls, host, port)

    models_list = models.split(",")  # Use 'models_list' to avoid shadowing

    eval_files = get_eval_files(directory)
    if not eval_files:
        return

    console.print(
        Text.assemble(
            ("\nRunning evaluations against Arcade Engine at ", "bold"),
            (base_url, "bold blue"),
        )
    )

    # Try to hit /health endpoint on engine and warn if it is down
    with Arcade(api_key=config.api.key, base_url=base_url) as client:
        log_engine_health(client)

    # Use the new function to load eval suites
    eval_suites = load_eval_suites(eval_files)

    if not eval_suites:
        console.print("No evaluation suites to run.", style="bold yellow")
        return

    if show_details:
        suite_label = "suite" if len(eval_suites) == 1 else "suites"
        console.print(
            f"\nFound {len(eval_suites)} {suite_label} in the evaluation files.",
            style="bold",
        )

    async def run_evaluations() -> None:
        all_evaluations = []
        tasks = []
        for suite_func in eval_suites:
            console.print(
                Text.assemble(
                    ("Running evaluations in ", "bold"),
                    (suite_func.__name__, "bold blue"),
                )
            )
            for model in models_list:
                task = asyncio.create_task(
                    suite_func(
                        config=config,
                        base_url=base_url,
                        model=model,
                        max_concurrency=max_concurrent,
                    )
                )
                tasks.append(task)

        # Track progress and results as suite functions complete
        with tqdm(total=len(tasks), desc="Evaluations Progress") as pbar:
            results = []
            for f in asyncio.as_completed(tasks):
                results.append(await f)
                pbar.update(1)

        # TODO error handling on each eval
        all_evaluations.extend(results)
        display_eval_results(all_evaluations, show_details=show_details)

    try:
        asyncio.run(run_evaluations())
    except Exception as e:
        handle_cli_error("Failed to run evaluations", e, debug)


@cli.command(
    help="Start tool server worker with locally installed tools",
    rich_help_panel="Launch",
)
def serve(
    host: str = typer.Option(
        "127.0.0.1",
        help="Host for the app, from settings by default.",
        show_default=True,
    ),
    port: int = typer.Option(
        "8002",
        "-p",
        "--port",
        help="Port for the app, defaults to ",
        show_default=True,
    ),
    disable_auth: bool = typer.Option(
        True,
        "--no-auth",
        help="Disable authentication for the worker. Not recommended for production.",
        show_default=True,
    ),
    otel_enable: bool = typer.Option(
        False, "--otel-enable", help="Send logs to OpenTelemetry", show_default=True
    ),
    mcp: bool = typer.Option(
        False, "--mcp", help="Run as a local MCP server over stdio", show_default=True
    ),
    debug: bool = typer.Option(False, "--debug", "-d", help="Show debug information"),
    reload: bool = typer.Option(
        False,
        "--reload",
        help="Enable auto-reloading when toolkit or server files change.",
        show_default=True,
    ),
) -> None:
    """
    Start a local Arcade Worker server.
    """
    require_dependency(
        package_name="arcade_serve",
        command_name="serve",
        install_command=r"pip install 'arcade-serve'",
    )

    from arcade_cli.serve import serve_default_worker

    try:
        serve_default_worker(
            host,
            port,
            disable_auth=disable_auth,
            enable_otel=otel_enable,
            debug=debug,
            mcp=mcp,
            reload=reload,
        )
    except KeyboardInterrupt:
        typer.Exit()
    except Exception as e:
        handle_cli_error("Failed to start Arcade Worker", e, debug)


@cli.command(
    help="Start a server with locally installed Arcade tools",
    rich_help_panel="Launch",
    hidden=True,
)
def workerup(
    host: str = typer.Option(
        "127.0.0.1",
        help="Host for the app, from settings by default.",
        show_default=True,
    ),
    port: int = typer.Option(
        "8002",
        "-p",
        "--port",
        help="Port for the app, defaults to ",
        show_default=True,
    ),
    disable_auth: bool = typer.Option(
        False,
        "--no-auth",
        help="Disable authentication for the worker. Not recommended for production.",
        show_default=True,
    ),
    otel_enable: bool = typer.Option(
        False, "--otel-enable", help="Send logs to OpenTelemetry", show_default=True
    ),
    debug: bool = typer.Option(False, "--debug", "-d", help="Show debug information"),
) -> None:
    """
    Starts the worker with host, port, and reload options. Uses
    Uvicorn as ASGI worker. Parameters allow runtime configuration.
    """
    require_dependency(
        package_name="arcade_serve",
        command_name="worker",
        install_command=r"pip install 'arcade-serve'",
    )

    from arcade_cli.serve import serve_default_worker

    try:
        serve_default_worker(
            host,
            port,
            disable_auth=disable_auth,
            enable_otel=otel_enable,
            debug=debug,
        )
    except KeyboardInterrupt:
        typer.Exit()
    except Exception as e:
        handle_cli_error("Failed to start Arcade Toolkit Server", e, debug)


@cli.command(help="Deploy toolkits to Arcade Cloud", rich_help_panel="Deployment")
def deploy(
    deployment_file: str = typer.Option(
        "worker.toml",
        "--deployment-file",
        "-d",
        help="The deployment file to deploy.",
    ),
    cloud_host: str = typer.Option(
        PROD_CLOUD_HOST,
        "--cloud-host",
        "-c",
        help="The Arcade Cloud host to deploy to.",
        hidden=True,
    ),
    cloud_port: Optional[int] = typer.Option(
        None,
        "--cloud-port",
        "-cp",
        help="The port of the Arcade Cloud host.",
        hidden=True,
    ),
    host: str = typer.Option(
        PROD_ENGINE_HOST,
        "--host",
        "-h",
        help="The Arcade Engine host to register the worker to.",
    ),
    port: Optional[int] = typer.Option(
        None,
        "--port",
        "-p",
        help="The port of the Arcade Engine host.",
    ),
    force_tls: bool = typer.Option(
        False,
        "--tls",
        help="Whether to force TLS for the connection to the Arcade Engine. If not specified, the connection will use TLS if the engine URL uses a 'https' scheme.",
    ),
    force_no_tls: bool = typer.Option(
        False,
        "--no-tls",
        help="Whether to disable TLS for the connection to the Arcade Engine.",
    ),
    debug: bool = typer.Option(False, "--debug", help="Show debug information"),
) -> None:
    """
    Deploy a worker to Arcade Cloud.
    """

    config = validate_and_get_config()
    engine_url = compute_base_url(force_tls, force_no_tls, host, port)
    engine_client = Arcade(api_key=config.api.key, base_url=engine_url)
    cloud_url = compute_base_url(force_tls, force_no_tls, cloud_host, cloud_port)
    cloud_client = httpx.Client(
        base_url=cloud_url, headers={"Authorization": f"Bearer {config.api.key}"}
    )

    # Fetch deployment configuration
    try:
        deployment = Deployment.from_toml(Path(deployment_file))
    except Exception as e:
        handle_cli_error("Failed to parse deployment file", e, debug)

    with console.status(f"Deploying {len(deployment.worker)} workers"):
        for worker in deployment.worker:
            console.log(f"Deploying '{worker.config.id}...'", style="dim")
            try:
                # Attempt to deploy worker
                worker.request().execute(cloud_client, engine_client)
                console.log(
                    f"✅ Worker '{worker.config.id}' deployed successfully.",
                    style="dim",
                )
            except Exception as e:
                handle_cli_error(f"Failed to deploy worker '{worker.config.id}'", e, debug)


@cli.command(help="Open the Arcade Dashboard in a web browser", rich_help_panel="User")
def dashboard(
    host: str = typer.Option(
        PROD_ENGINE_HOST,
        "-h",
        "--host",
        help="The Arcade Engine host that serves the dashboard.",
    ),
    port: Optional[int] = typer.Option(
        None,
        "-p",
        "--port",
        help="The port of the Arcade Engine.",
    ),
    local: bool = typer.Option(
        False,
        "--local",
        "-l",
        help="Open the local dashboard instead of the default remote dashboard.",
    ),
    force_tls: bool = typer.Option(
        False,
        "--tls",
        help="Whether to force TLS for the connection to the Arcade Engine.",
    ),
    force_no_tls: bool = typer.Option(
        False,
        "--no-tls",
        help="Whether to disable TLS for the connection to the Arcade Engine.",
    ),
    debug: bool = typer.Option(False, "--debug", "-d", help="Show debug information"),
) -> None:
    """Opens the Arcade Dashboard in a web browser.

    The Dashboard is a web-based Arcade user interface that is served by the Arcade Engine.
    """
    try:
        if local:
            host = "localhost"

        # Construct base URL (for both health check and dashboard)
        base_url = compute_base_url(force_tls, force_no_tls, host, port)
        dashboard_url = f"{base_url}/dashboard"

        # Try to hit /health endpoint on engine and warn if it is down
        config = validate_and_get_config()
        with Arcade(api_key=config.api.key, base_url=base_url) as client:
            log_engine_health(client)

        # Open the dashboard in a browser
        console.print(f"Opening Arcade Dashboard at {dashboard_url}")
        if not webbrowser.open(dashboard_url):
            console.print(
                f"If a browser doesn't open automatically, copy this URL and paste it into your browser: {dashboard_url}",
                style="dim",
            )
    except Exception as e:
        handle_cli_error("Failed to open dashboard", e, debug)


@cli.command(
    help=(
        "Generate documentation for a toolkit. "
        "Note: make sure to have the toolkit installed in your current Python environment "
        "before running this command."
    ),
    rich_help_panel="Tool Development",
)
def docs(
    toolkit_name: str = typer.Option(
        ..., "--toolkit-name", "-n", help="The name of the toolkit to generate documentation for."
    ),
    toolkit_dir: str = typer.Option(
        ...,
        "--toolkit-dir",
        "-t",
        help=(
            "The path to the toolkit root directory (where the toolkit code is implemented). "
            "Works with relative and absolute paths."
        ),
    ),
    docs_dir: str = typer.Option(
        ...,
        "--docs-dir",
        "-r",
        help="The path to the root of the Arcade docs repository. Works with relative and absolute paths.",
    ),
    docs_section: str = typer.Option(
        "",
        "--docs-section",
        "-s",
        help=(
            "The section of the docs to generate documentation for. E.g. 'productivity', 'sales'. "
            "This should be the name of the folder in /pages/toolkits. "
            "Defaults to an empty string (generate the docs in the root of /pages/toolkits)"
        ),
    ),
    openai_model: str = typer.Option(
        "gpt-5-mini",
        "--openai-model",
        "-m",
        help=(
            "A few parts of the documentation are generated using OpenAI API. "
            "Choose one of the 'gpt-4o' and 'gpt-5' series models."
        ),
        show_default=True,
    ),
    openai_api_key: str = typer.Option(
        None,
        "--openai-api-key",
        "-o",
        help="The OpenAI API key. If not provided, will get it from the `OPENAI_API_KEY` env var.",
    ),
    skip_tool_call_examples: bool = typer.Option(
        False,
        "--skip-tool-call-examples",
        "-se",
        help="Whether to skip generating tool call examples in Python and Javascript.",
        show_default=True,
    ),
    debug: bool = typer.Option(False, "--debug", "-d", help="Show debug information"),
) -> None:
    if not openai_model.startswith("gpt-4o") and not openai_model.startswith("gpt-5"):
        console.print(
            f"Attention: '{openai_model}' is not a valid OpenAI model. "
            "Please choose one of the 'gpt-4o' and 'gpt-5' series models.",
            style="bold red",
        )
        raise typer.Exit()

    try:
        success = generate_toolkit_docs(
            console=console,
            toolkit_name=toolkit_name,
            toolkit_dir=toolkit_dir,
            docs_dir=docs_dir,
            docs_section=docs_section,
            openai_model=openai_model,
            openai_api_key=openai_api_key,
            tool_call_examples=not skip_tool_call_examples,
            debug=debug,
        )
    except Exception as error:
        handle_cli_error(
            message=f"Failed to generate documentation for '{toolkit_name}' in '{docs_dir}'",
            error=error,
            debug=debug,
        )
        success = False

    if success:
        console.print(
            f"Generated documentation for '{toolkit_name}' in '{docs_dir}'",
            style="bold green",
        )
    else:
        console.print(
            f"Failed to generate documentation for '{toolkit_name}' in '{docs_dir}'",
            style="bold red",
        )


@cli.command(
    name="generate-toolkit-docs",
    help=(
        "Generate documentation for a toolkit. "
        "Note: make sure to have the toolkit installed in your current Python environment "
        "before running this command. "
        "Obs.: this command is here for backwards compatibility, use `arcade docs` instead."
    ),
    rich_help_panel="Tool Development",
    hidden=True,
)
def generate_toolkit_docs_command(
    toolkit_name: str = typer.Option(
        ..., "--toolkit-name", "-n", help="The name of the toolkit to generate documentation for."
    ),
    toolkit_dir: str = typer.Option(
        ...,
        "--toolkit-dir",
        "-t",
        help=(
            "The path to the toolkit root directory (where the toolkit code is implemented). "
            "Works with relative and absolute paths."
        ),
    ),
    docs_dir: str = typer.Option(
        ...,
        "--docs-dir",
        "-r",
        help="The path to the root of the Arcade docs repository. Works with relative and absolute paths.",
    ),
    docs_section: str = typer.Option(
        "",
        "--docs-section",
        "-s",
        help=(
            "The section of the docs to generate documentation for. E.g. 'productivity', 'sales'. "
            "This should be the name of the folder in /pages/toolkits. "
            "Defaults to an empty string (generate the docs in the root of /pages/toolkits)"
        ),
    ),
    openai_model: str = typer.Option(
        "gpt-4o-mini",
        "--openai-model",
        "-m",
        help=(
            "A few parts of the documentation are generated using OpenAI API. "
            "This argument controls which OpenAI model to use. "
            "E.g. 'gpt-4o', 'gpt-4o-mini'."
        ),
        show_default=True,
    ),
    openai_api_key: str = typer.Option(
        None,
        "--openai-api-key",
        "-o",
        help="The OpenAI API key. If not provided, will get it from the `OPENAI_API_KEY` env var.",
    ),
    tool_call_examples: bool = typer.Option(
        True,
        "--tool-call-examples",
        "-e",
        help="Whether to generate tool call examples in Python and Javascript.",
        show_default=True,
    ),
    debug: bool = typer.Option(False, "--debug", "-d", help="Show debug information"),
) -> None:
    skip_tool_call_examples = not tool_call_examples
    docs(
        toolkit_name=toolkit_name,
        toolkit_dir=toolkit_dir,
        docs_dir=docs_dir,
        docs_section=docs_section,
        openai_model=openai_model,
        openai_api_key=openai_api_key,
        skip_tool_call_examples=skip_tool_call_examples,
        debug=debug,
    )


@cli.callback()
def main_callback(
    ctx: typer.Context,
    _: Optional[bool] = typer.Option(
        None,
        "-v",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Print version and exit.",
    ),
) -> None:
    excluded_commands = {
        login.__name__,
        logout.__name__,
        serve.__name__,
        workerup.__name__,
        dashboard.__name__,
    }
    if ctx.invoked_subcommand in excluded_commands:
        return

    if not check_existing_login(suppress_message=True):
        console.print("Not logged in to Arcade CLI. Use ", style="bold red", end="")
        console.print("arcade login", style="bold green")
        raise typer.Exit()
