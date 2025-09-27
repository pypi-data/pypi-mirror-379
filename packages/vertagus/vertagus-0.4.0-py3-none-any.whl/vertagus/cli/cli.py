import logging
import os
import click
from .commands import (
    validate_cmd,
    create_tag_cmd,
    create_aliases_cmd,
    list_rules_cmd,
    list_aliases_cmd,
    list_manifests_cmd,
    list_scms_cmd,
    bump_cmd,
    list_bumpers_cmd,
    init_cmd,
    show_version_cmd,
    show_alias_cmd,
)


logging.basicConfig(level=os.environ.get("VERTAGUS_LOG_LEVEL", "INFO"), format="{message}", style="{")


@click.group()
def cli():
    pass


cli.add_command(init_cmd)
cli.add_command(validate_cmd)
cli.add_command(create_tag_cmd)
cli.add_command(create_aliases_cmd)
cli.add_command(list_rules_cmd)
cli.add_command(list_aliases_cmd)
cli.add_command(list_manifests_cmd)
cli.add_command(list_scms_cmd)
cli.add_command(bump_cmd)
cli.add_command(list_bumpers_cmd)
cli.add_command(show_version_cmd)
cli.add_command(show_alias_cmd)
