"""The CLI to interface with the Celestical European Serverless Cloud."""
from typing import Optional
import typer
from celestical.utils.display import cli_panel, print_console, print_text
from celestical.config import Config
from celestical.session import Session
from celestical.user import User
#from celestical.commands.select import Select
# Prepare is Enrich+etc
#from celestical.commands.prepare import Prepare
from celestical.docker.docker import DockerMachine
from celestical.utils.version_check import check_cli_version


user = User()
user.config.logger.info("Starting CLI.")


app = typer.Typer(pretty_exceptions_short=False,
                  no_args_is_help=True,
                  context_settings={
                      "help_option_names": ["help", "-h", "--help"]},
                  help=user.welcome(),
                  rich_markup_mode="rich")


# @app.callback(invoke_without_command=False)
# def default_base(ctx: typer.Context):
#     """ This function runs only and before when user calls commands
#     no_args_is_help must be True for this to work properly
#     when defining the context to the main Typer APP.
#     """
#     # print_console(user.welcome())
#     print_text(f"[grey50]Executing command: {ctx.invoked_subcommand}[/grey50]")
#


@app.command("help")
def default_help(ctx: typer.Context,
                 cmd: Optional[str] =
                    typer.Argument(
                        default="",
                        help="Command name to get help from")
                ):
    """
     Display this help message similarly to -h or --help
     or about a command if specified
    """
    if ctx is None:
        typer.echo(ctx.get_help())
        return

    if ctx.parent is None:
        typer.echo(ctx.get_help())
        return

    if cmd == "":
        # Show general help
        typer.echo(ctx.parent.get_help())
        return

    # Show help for specific command
    try:
        # Get the command from the parent app
        command = ctx.parent.command.commands.get(cmd)
        if command:
            # Simple approach: show command info
            print(f"\nHelp for command: {cmd}")
            print("=" * 50)
            if hasattr(command, 'help') and command.help:
                print(command.help)
                # print(help(command))
                command_context = command.context_class(command)
                print("\nUsage:")
                print(f"  celestical {cmd}")
                print(command_context.get_help())
                # print(CCC.command.get_help(CCC))
            else:
                print(f"No detailed help available for '{cmd}'")
        else:
            print_text(f"Command '{cmd}' not found. Available commands:",
                      worry_level="oops")
            typer.echo(ctx.parent.get_help())
    except (ValueError, AttributeError, KeyError) as e:
        print_text(f"Error getting help for command '{cmd}': {e}",
                  worry_level="oops")
        typer.echo(ctx.parent.get_help())


# @app.callback(invoke_without_command=True)
@app.command()
def apps():
    """ List all apps from current user."""
    # Check CLI version compatibility before proceeding
    if not check_cli_version():
        raise typer.Exit(1)

    session = Session(needs_login=True)
    # If delete mode
    # session.delete_app(delete_app_id, force=force_delete, )

    # Else display the apps for beginner and inform the actions of
    # delete/select active an app
    session.app_actions()


@app.command()
def login() -> None:
    """Login to Celestical Cloud Services via the CLI.
        The session is explicitly set to force relogin.
    """
    # Check CLI version compatibility before proceeding
    if not check_cli_version():
        raise typer.Exit(1)

    session = Session(needs_login=True, force_login=True)
    if session.user is not None:
        print_console(session.user.to_rich())


@app.command()
def register():
    """Register as a user for Celestical Cloud Services via the CLI."""
    flag = user.user_register()
    config = user.config.load_config()
    if flag == 0:
        print_text("User already exists or We could not connect.")
    if flag in (1, 3):
        mgs = "You can now login with user "
        mgs += f"[yellow]{config['username']}[/yellow] using [blue]celestical login[/blue]"
        cli_panel(mgs)


@app.command()
def images():
    """ List all local docker images for you.
        Similar to 'docker image ls'.
    """
    docker_machine = DockerMachine()
    table = docker_machine.list_local_images()

    if table is None:
        cli_panel("Docker service is [red]unaccessible[/red]\n")
    else:
        cli_panel("The following are your local docker images\n"
                  + f"{table}")


@app.command()
def deploy(compose_path: Optional[str] =
             typer.Argument(
                 default="./",
                 help="Path(str) to compose file. Default current directory"),
           api_host: Optional[str] =
             typer.Option(
                 default="",
                 help="Custom host (including port) for API connections. "
                 + "Mostly used for testing."),
           api_scheme: Optional[str] =
             typer.Option(
                 default="",
                 help="Custom connection scheme; http or https. "
                 + "Mostly used for testing.")):
    """ Select or create, prepare and push your applications
    (docker-compose.yml) to the Celestical Cloud.

    """
    # - Notes:
    #    1. Deploying means necessity to connect, so creating connected Session
    #    2. Select the application or create a new one
    #    3. Check if enrichment is necessary
    #        3.1. enrich
    #    4. Push ecompose images (todo check which image to push)

    # Check CLI version compatibility before proceeding
    if not check_cli_version():
        raise typer.Exit(1)

    config = None
    if len(api_host) > 3 or len(api_scheme) > 3:
        config = Config(host=api_host, scheme=api_scheme)

    session = Session(needs_login=True, config=config)

    if session.select_app() is True:
        # Enrich using the input compose file
        if session.app.enrich(compose_path):
            # Push (and deploy) the necessary images
            session.app.push()
