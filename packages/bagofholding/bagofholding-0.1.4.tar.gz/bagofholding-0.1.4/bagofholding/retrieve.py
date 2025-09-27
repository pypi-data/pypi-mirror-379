"""
Helper functions for managing the relationship between strings and imports.
"""

from __future__ import annotations

import importlib
from typing import Any

from bagofholding.exceptions import StringNotImportableError


def import_from_string(library_path: str) -> Any:
    split_path = library_path.split(".", 1)
    if len(split_path) == 1:
        module_name, path = split_path[0], ""
    else:
        module_name, path = split_path
    obj = importlib.import_module(module_name)
    for k in path.split("."):
        try:
            obj = getattr(obj, k)
        except AttributeError:
            # Try importing as a submodule
            # This can be necessary of an __init__.py is empty and nothing else has
            # referenced the module yet
            current_path = f"{obj.__name__}.{k}"
            try:
                obj = importlib.import_module(current_path)
            except ImportError as e:
                raise AttributeError(
                    f"module '{obj.__name__}' has no attribute '{k}'"
                ) from e
    return obj


def get_importable_string_from_string_reduction(
    string_reduction: str, reduced_object: object
) -> str:
    """
    Per the pickle docs:

    > If a string is returned, the string should be interpreted as the name of a global
      variable. It should be the object’s local name relative to its module; the pickle
      module searches the module namespace to determine the object’s module. This
      behaviour is typically useful for singletons.

    To then import such an object from a non-local caller, we try scoping the string
    with the module of the object which returned it.
    """
    try:
        import_from_string(string_reduction)
        importable = string_reduction
    except ModuleNotFoundError:
        importable = reduced_object.__module__ + "." + string_reduction
        try:
            import_from_string(importable)
        except (ModuleNotFoundError, AttributeError) as e:
            raise StringNotImportableError(
                f"Couldn't import {string_reduction} after scoping it as {importable}. "
                f"Please contact the developers so we can figure out how to handle "
                f"this edge case."
            ) from e
    return importable
