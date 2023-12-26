#!/usr/bin/env python
# coding: utf-8

import argparse
import sys
import socket

import click
import psutil


def python_version():
    return sys.version_info


def ip_addresses():
    hostname = socket.gethostname()
    addresses = socket.getaddrinfo(hostname, None)
    address_info = []
    for address in addresses:
        address_info.append((address[0].name, address[4][0]))
    return address_info


def cpu_load():
    return psutil.cpu_percent(interval=0.1)


def ram_available():
    return psutil.virtual_memory().available


@click.command(help="Displays the values of the sensors")
def show_sensors():
    head = {"bold": True,
            "nl": False}
    click.secho("Version Python: ", **head)
    click.echo("{0.major}.{0.minor}".format(python_version()))
    for address in ip_addresses():
        click.secho("IP-addresses: ", **head)
        click.echo(f"{address[1]} ({address[0]})")
    click.secho("CPU load: ", **head)
    click.echo(f"{cpu_load():.1f}")
    click.secho("RAM available: ", **head)
    click.echo(f"{ram_available() / 1024 ** 2} MiB")


def command_line(argv):
    parser = argparse.ArgumentParser(
        description='Show sensor',
        add_help=True,
    )
    arguments = parser.parse_args()
    show_sensors()


if __name__ == "__main__":
    command_line(sys.argv)



