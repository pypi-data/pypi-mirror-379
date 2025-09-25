from __future__ import annotations

import json
import operator
from functools import lru_cache, reduce
from typing import Any

from jsonschema import Draft7Validator

from splink.internals.misc import read_resource


@lru_cache()
def get_schema():
    path = "files/settings_jsonschema.json"
    return json.loads(read_resource(path))


def get_from_dict(dataDict, mapList):
    return reduce(operator.getitem, mapList, dataDict)


def get_comparison_level(e, settings_dict):
    comparison_level = None
    path = list(e.path)

    try:
        index_of_comparison_levels = path.index("comparison_levels")
    except ValueError:
        index_of_comparison_levels = None
    if index_of_comparison_levels is not None:
        comparison_level = get_from_dict(
            settings_dict, path[: index_of_comparison_levels + 2]
        )
    return comparison_level


def get_comparison(e, settings_dict):
    path = list(e.path)
    comparison = None
    try:
        index_of_comparison = path.index("comparisons")
    except ValueError:
        index_of_comparison = None
    if index_of_comparison is not None:
        comparison = get_from_dict(settings_dict, path[: index_of_comparison + 2])
    return comparison


def validate_settings_against_schema(settings_dict: dict[str, Any]) -> None:
    """Validate a splink settings object against its jsonschema"""

    schema = get_schema()

    v = Draft7Validator(schema)

    e = next(v.iter_errors(settings_dict), None)

    if e:
        comparison_level = get_comparison_level(e, settings_dict)
        comparison = get_comparison(e, settings_dict)

        error_in = ""
        if comparison_level:
            error_in += f"The comparison level is: {json.dumps(comparison_level)}\n\n"

        if comparison:
            error_in += f"The comparison is: {json.dumps(comparison)}\n\n"

        if error_in == "":
            error_in = (
                "The error is in the main settings object, not in the "
                "comparison columns or levels."
            )

        path = list(e.path)
        message = (
            f"There was at least one error in your settings dictionary.\n\n"
            f"The first error was:   {e.message}\n\n"
            f"The path to the error is:\n     {json.dumps(path)}\n\n"
            f"The part of your settings dictionary containing this error is:\n"
            f"{json.dumps(e.instance)}\n"
            f"{error_in}\n"
        )
        raise ValueError(message)
