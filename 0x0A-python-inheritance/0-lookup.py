#!/usr/bin/python3

"""Module that defines an object attribute lookup function.."""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
