import click
from rich.console import Console

from vcp.datasets.api import get_dataset_api
from vcp.datasets.download import S3Credentials, download_locations
from vcp.utils.token import TokenManager

console = Console()

TOKEN_MANAGER = TokenManager()

EPILOG = f"""
{click.style("Examples:", fg="cyan", bold=True)} \n
\t {click.style("vcp data download <id>", fg="green")} \n
"""


@click.command("download", epilog=EPILOG)
@click.argument("dataset_id")
@click.option(
    "-o",
    "--outdir",
    type=click.Path(file_okay=False, dir_okay=True, writable=True, path_type=str),
    default=".",
    help="Directory to write the files.",
)
def download_command(dataset_id: str, outdir: str):
    """
    Download a specific dataset by id. If you do not know the id, first use the search command to find the id.
    """
    # TODO: this should be able to download multiple datasets

    # session management
    tokens = TOKEN_MANAGER.load_tokens()
    if tokens is None:
        console.print("[red]Tokens not present: Login required[/red]")
        return None

    # call data api
    try:
        data = get_dataset_api(tokens.id_token, dataset_id, download=True)

        if getattr(data, "error", None) or getattr(data, "credentials", None) is None:
            console.print(f"[red]Error: {data.error}[/red]")
            return None
        else:
            credentials = S3Credentials(**data.credentials)
            download_locations(data.locations, credentials, outdir)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        return None


@click.command("credentials")
@click.argument("dataset_id")
def generate_credentials_command(dataset_id: str):
    """
    Get the credentials for a specific dataset by id. If you do not know the id, first use the search command to find the id.
    """
    # TODO: this should be able to download multiple datasets

    # session management
    tokens = TOKEN_MANAGER.load_tokens()
    if tokens is None:
        console.print("[red]Tokens not present: Login required[/red]")
        return None

    # call data api
    try:
        data = get_dataset_api(tokens.id_token, dataset_id, download=True)

        if getattr(data, "error", None) or getattr(data, "credentials", None) is None:
            console.print(f"[red]Error: {data['error']}[/red]")
            return None
        else:
            credentials = S3Credentials(**data.credentials)
            print(credentials.model_dump())
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        return None
