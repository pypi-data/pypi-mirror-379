import keyword
import re

from marshmallow import ValidationError


def is_reserved(name: str) -> bool:
    """Check name is a reserved keyword.

    :param name:
    :return: ``True`` if reserved, ``False`` otherwise
    """
    if keyword.iskeyword(name):
        # name is a reserved python3 keyword
        return True
    if name in ["_stats"]:
        # name in deseasion reserved keywords
        return True
    return False


def validate_name(name: str):
    """Check name is a valid name.

    :param name:
    :raise ValidationError:
        * if `name` is not a valid name
    """
    pattern = re.compile("[a-zA-Z][0-9a-zA-Z_]*")
    if pattern.fullmatch(name) is None:
        # name is not a valid variable name
        raise ValidationError('"{}" is not a valid name'.format(name))


def validate_varname(name: str):
    """Check name is a valid variable name and unreserved keyword.

    :param name:
    :raise ValidationError:
        * if `name` is not a valid identifier
        * if `name` is a reserved python keyword
        * if `name` is a reserved deseasion keyword
    """
    if keyword.iskeyword(name):
        # name is a reserved python3 keyword
        raise ValidationError('"{}" is a reserved python keyword'.format(name))
    if name in ["_stats"]:
        # name in deseasion reserved keywords
        raise ValidationError(
            '"{}" is a reserved deseasion keyword'.format(name)
        )
    validate_name(name)


def safe_attrname(name: str) -> str:
    """Convert string to a valid attribute name.

    :param name:
    :return: valid attribute name
    """
    # Remove every character before the first letter
    res = re.sub(r"^[^A-Za-z]+", "", name)

    # Replace invalid characters with underscore
    res = re.sub(r"\W|^(?=\d)", "_", res)

    # Remove trailing underscores
    res = re.sub(r"_+$", "", res)

    # Default value if every other character is invalid
    if not res:
        res = "attr"

    return res


def safe_varname(name: str) -> str:
    """Convert string to a valid variable name.

    :param name:
    :return: valid variable name
    """
    # Remove every character before the first letter
    res = re.sub(r"^[^A-Za-z]+", "", name)

    # Replace invalid characters with underscore
    res = re.sub(r"\W|^(?=\d)", "_", res)

    # Remove trailing underscores
    res = re.sub(r"_+$", "", res)

    # Default value if every other character is invalid
    if not res:
        res = "data"

    # Ensure not a reserved keyword
    while is_reserved(res):
        res += "_"

    return res
