from pathlib import Path


def tokenized_expand(name: str | bytes | Path) -> tuple[str, dict[str, str]]:
    """Expand shell variables of the forms $var, ${var} and %var%.
    Unknown variables are left unchanged.

    Expand paths containing shell variable substitutions. The following rules apply:
        - no expansion within single quotes
        - '$$' is translated into '$'
        - '%%' is translated into '%' if '%%' are not seen in %var1%%var2%
        - ${var} is accepted
        - $varname is accepted
        - %var% is accepted
        - vars can be made out of letters, digits and the characters '_-'
        (though is not verified in the ${var} and %var% cases)

    :param name: String to expand
    :return: Tuple of (expanded string, dictionary of tokens)
    """
    import os

    from pyaaware.env_vars import tokenized_expand

    from ..constants import DEFAULT_NOISE

    os.environ["default_noise"] = str(DEFAULT_NOISE)  # noqa: SIM112

    return tokenized_expand(name)


def tokenized_replace(name: str, tokens: dict[str, str]) -> str:
    """Replace text with shell variables.

    :param name: String to replace
    :param tokens: Dictionary of replacement tokens
    :return: replaced string
    """
    from pyaaware.env_vars import tokenized_replace

    return tokenized_replace(name, tokens)
