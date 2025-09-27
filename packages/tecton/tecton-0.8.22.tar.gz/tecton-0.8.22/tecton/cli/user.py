import sys

import click

from tecton._internals import metadata_service
from tecton.cli import printer
from tecton.cli.command import TectonGroup
from tecton_proto.metadataservice import metadata_service_pb2


@click.group("user", cls=TectonGroup)
def user():
    """Manage users"""


@user.command("invite", help="Invite Users to Tecton Cluster")
@click.option("-u", "--user", default=None, help="User email")
@click.option("-f", "--file", default=None, help="Newline separated list of user emails", type=click.File("r"))
def invite(user, file):
    if file is not None:
        if user:
            msg = "Please use exactly one of --user or --file"
            raise click.ClickException(msg)
        _bulk_invite_users(file)
    elif user is not None:
        _invite_user(user)
    else:
        msg = "Please submit one of --user or --file."
        raise click.ClickException(msg)


def _invite_user(user):
    try:
        request = metadata_service_pb2.CreateClusterUserRequest(login_email=user)
        metadata_service.instance().CreateClusterUser(request)
    except Exception as e:
        printer.safe_print(f"Failed to invite [{user}]: {e}", file=sys.stderr)
        sys.exit(1)
    printer.safe_print(f"Successfully invited [{user}]")


def _bulk_invite_users(file):
    for user_email in [line.strip() for line in file.readlines() if len(line.strip()) > 0]:
        _invite_user(user_email)
