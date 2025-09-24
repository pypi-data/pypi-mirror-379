"""Provide set-config CLI command."""

import argparse
import sys
from pathlib import Path
from typing import Optional

from spotter.client.commands.config_commands.config_set import config_set
from spotter.client.utils import CommonParameters, UsagePrefixRawDescriptionHelpFormatter, get_absolute_path


def add_parser(subparsers: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
    """
    Add a new parser for set-config command to subparsers.

    :param subparsers: Subparsers action
    """
    parser = subparsers.add_parser(
        "set-config",
        argument_default=argparse.SUPPRESS,
        formatter_class=lambda prog: UsagePrefixRawDescriptionHelpFormatter(
            prog,
            usage_prefix="Set organization-level file with configuration (e.g., for enforcing and skipping checks)",
            max_help_position=48,
        ),
        usage="spotter set-config [OPTIONS] <CONFIG_PATH>",
        add_help=False,
    )
    parser.add_argument("-h", "--help", action="help", help="Show this help message and exit")
    parser.add_argument(
        "--organization-id",
        type=str,
        default=None,
        help="UUID of an existing Steampunk Spotter organization to set configuration for "
        "(default organization will be used if not specified)",
    )
    parser.add_argument("config_path", type=get_absolute_path, help="Path to the configuration file (JSON/YAML)")
    parser.set_defaults(func=_parser_callback)


def _parser_callback(args: argparse.Namespace, project_root: Path) -> None:
    """
    Execute callback for set-config command.

    :param args: Argparse arguments
    :param project_root: The root directory of the project.
    """
    print("Warning: the set-config command is deprecated. Use config set instead.", file=sys.stderr)
    common_params = CommonParameters.from_args(args)

    config_path: Path = args.config_path
    if not config_path.is_file():
        print(f"Error: path at {config_path} is not a valid file.", file=sys.stderr)
        sys.exit(2)

    set_config(
        common_params.api_endpoint,
        common_params.storage_path,
        common_params.api_token,
        common_params.username,
        common_params.password,
        common_params.timeout,
        args.organization_id,
        config_path,
        common_params.debug,
        common_params.cacert,
        common_params.verify,
    )


def set_config(
    api_endpoint: str,
    storage_path: Path,
    api_token: Optional[str],
    username: Optional[str],
    password: Optional[str],
    timeout: Optional[int],
    organization_id: Optional[str],
    config_path: Path,
    debug: bool,
    cacert: Optional[Path],
    verify: bool,
) -> None:
    """
    Set configuration file for organization.

    By default, this will set configuration for the default organization.

    :param api_endpoint: Steampunk Spotter API endpoint
    :param storage_path: Path to storage
    :param api_token: Steampunk Spotter API token
    :param username: Steampunk Spotter username
    :param password: Steampunk Spotter password
    :param timeout: Steampunk Spotter API timeout (in seconds)
    :param organization_id: UUID of an existing Steampunk Spotter organization to set configuration for
    :param config_path: Path to the configuration file (JSON/YAML)
    :param debug: Enable debug mode
    :param cacert: Path to file containing root CA certificates. If not listed, system's default will be used.
    :param verify: Verify server certificate
    """
    config_set(
        api_endpoint,
        storage_path,
        api_token,
        username,
        password,
        timeout,
        organization_id,
        config_path,
        debug,
        cacert,
        verify,
    )
