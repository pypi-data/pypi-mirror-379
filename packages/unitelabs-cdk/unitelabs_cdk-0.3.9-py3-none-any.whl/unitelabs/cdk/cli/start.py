import logging
import os
import pathlib
import typing

import click

from unitelabs.cdk import utils
from unitelabs.cdk.logging import configure_logging

from ..main import run


class TLSConfigurationError(Exception):
    """TLS Configuration is invalid."""


@click.command()
@click.option(
    "--app",
    type=str,
    metavar="IMPORT",
    default=utils.find_factory,
    show_default=False,
    help="The application factory function to load, in the form 'module:name'.",
)
@click.option(
    "--tls/--no-tls",
    required=False,
    default=None,
    envvar="SILA_SERVER__TLS",
    help="Use TLS encryption. Alone, this will assume cert and key exist in `certificate.generate` default location.",
)
@click.option(
    "-C",
    "--cert",
    required=False,
    envvar="SILA_SERVER__CERT",
    default=None,
    help="The path to the certificate chain file, overriding .env setting of `SILA_SERVER__CERT`, default: ./cert.pem",
)
@click.option(
    "-K",
    "--key",
    required=False,
    envvar="SILA_SERVER__KEY",
    default=None,
    help="The path to the private key file, overriding .env setting of `SILA_SERVER__KEY`, default: ./key.pem",
)
@click.option(
    "-v",
    "--verbose",
    count=True,
    help="Increase the verbosity of the default logger. Use a custom log-config for fine grained handling.",
)
@click.option(
    "--log-config",
    type=click.Path(exists=True),
    default=None,
    help="The path to the logging configuration file. Supported formats: .ini, .json, .yaml.",
)
@utils.coroutine
async def start(app, tls, cert, key, verbose: int, log_config: typing.Optional[str]) -> None:  # noqa: ANN001
    """Application Entrypoint."""

    configure_logging(log_config, logging.WARNING - verbose * 10)

    if tls is not None:
        os.environ["SILA_SERVER__TLS"] = str(tls)

    if tls:
        cert = pathlib.Path(cert) if cert else pathlib.Path("./cert.pem")
        key = pathlib.Path(key) if key else pathlib.Path("./key.pem")
        cert = cert.resolve()
        key = key.resolve()

        msg = ""
        if not cert.exists():
            msg += f"Certificate file at {cert} does not exist. Specify path with --cert. "

        if not key.exists():
            msg += f"Private key file at {key} does not exist. Specify path with --key."

        if msg:
            raise TLSConfigurationError(msg)

        os.environ["SILA_SERVER__CERTIFICATE_CHAIN"] = cert.read_text()
        os.environ["SILA_SERVER__PRIVATE_KEY"] = key.read_text()

    await run(app)
