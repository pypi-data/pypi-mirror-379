import multiprocessing
import typer
from smart_logger.core.db_handler import DBHandler
from smart_logger.ui.server import start_ui_server
import json
from pathlib import Path

LIBRARY_HOME = Path.home() / ".smart_logger"
CONFIG_POINTER = LIBRARY_HOME / "config_path"   # file me config ka path hoga
CONFIG_FILE_NAME = "smart-logger.conf"

app = typer.Typer(help="Smart Logger CLI commands.")

# @app.command()
# def ui(host: str = "127.0.0.1", port: int = 8000, workers: int = 1):
#     """
#     Launch Smart Logger FastAPI UI server.
#     """
#     print(f"Starting Smart Logger UI on {host}:{port} with {workers} worker(s)...")
#     start_ui_server(host=host, port=port, workers=workers)

@app.command("ui")
def ui(
    host: str = "127.0.0.1",
    port: int = 8000,
    workers: int = 1,
    reload: bool = typer.Option(False, help="Enable auto-reload for development")
):
    # 🌀 isolate server in separate process
    p = multiprocessing.Process(
        target=start_ui_server, args=(host, port, workers, reload), daemon=True
    )
    p.start()
    p.join()

@app.command()
def init_db():
    """
    Create Smart Logger metadata tables.
    """
    db = DBHandler()
    db.create_tables()
    print("Smart Logger tables created successfully!")


@app.command()
def set_config():
    """
    Set the smart-logger.conf from the current project directory as global config.
    """
    project_dir = Path.cwd()
    config_file = project_dir / "smart-logger.conf"

    if not config_file.exists():
        typer.echo(f"[!] No smart-logger.conf found in current directory ({project_dir}). Run `make-smart-logger-conf` first.")
        raise typer.Exit(code=1)

    # ensure ~/.smart_logger exists
    LIBRARY_HOME.mkdir(parents=True, exist_ok=True)

    # store absolute path in global pointer
    CONFIG_POINTER.write_text(str(config_file.resolve()))
    typer.echo(f"[+] Smart Logger global config set to: {config_file.resolve()}")
   

@app.command()
def show_config():
    """
    Show the currently active smart-logger.conf and its contents.
    """
    if not CONFIG_POINTER.exists():
        typer.echo("[!] No global config set. Run `set_config` first.")
        raise typer.Exit(code=1)

    config_file = Path(CONFIG_POINTER.read_text().strip())

    if not config_file.exists():
        typer.echo(f"[!] Config file not found at {config_file}. Please re-run `set_config`.")
        raise typer.Exit(code=1)

    try:
        with open(config_file, "r") as f:
            data = json.load(f)

        typer.echo(f"Active config file: {config_file}\n")
        typer.echo(json.dumps(data, indent=4))

    except Exception as e:
        typer.echo(f"[!] Failed to read config: {e}")

@app.command("create-admin-user")
def create_admin_user():
    """
    Create an admin user for Smart Logger.
    """
    from smart_logger.cli.create_user import create_logger_user_cli
    create_logger_user_cli()

@app.command("change-password")
def change_password(email: str = typer.Argument(..., help="Email of the user to change password for")):
    """ Change password for an existing user.
    """
    from smart_logger.cli.create_user import change_password
    change_password(email)   


@app.command("forgot-password") 
def forgot_password(email: str = typer.Argument(..., help="Email of the user to reset password for")):
    """ Reset password for an existing user without old password.
    """
    from smart_logger.cli.create_user import forgot_password
    forgot_password(email)      


@app.command("list-users")
def list_users():
    """
    List all users in the database.
    """
    from smart_logger.core.user_db_handler import UserDBHandler
    db = UserDBHandler()
    users = db.list_logger_users()
    if not users:
        print("No users found.")
        return
    print(f"{'ID':<5} {'First Name':<15} {'Last Name':<15} {'Email':<30}")
    print("-" * 70)
    for user in users:
        print(f"{user.id:<5} {user.first_name:<15} {user.last_name:<15} {user.email:<30}")      

@app.command("delete-user")
def delete_user(email: str = typer.Argument(..., help="Email of the user to delete")):
    """ Delete a user by email.
    """                                                         
    from smart_logger.core.user_db_handler import UserDBHandler
    db = UserDBHandler()
    user = db.get_logger_user_by_email(email)
    if not user:
        print("User not found!")
        return
    db.delete_logger_user(email)
    print(f"User {email} deleted successfully.")


@app.command("make-smart-logger-default-conf")
def make_smart_logger__default_conf():
    from smart_logger.cli.commands_service import make_smart_logger__default_conf as create_default_conf
    """
    Create a default smart-logger.conf file.
    """
    create_default_conf()                       



def main():
    """
    Entry point for CLI. Can be linked in setup.py console_scripts.
    """
    app()
