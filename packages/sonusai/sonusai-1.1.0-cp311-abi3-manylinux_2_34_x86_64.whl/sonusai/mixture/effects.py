from ..datatypes import AudioT
from ..datatypes import Effects
from .mixdb import MixtureDatabase


def get_effect_rules(location: str, config: dict, test: bool = False) -> dict[str, list[Effects]]:
    from ..datatypes import Effects
    from ..utils.dataclass_from_dict import list_dataclass_from_dict
    from .mixdb import MixtureDatabase

    mixdb = MixtureDatabase(location, test)

    rules: dict[str, list[Effects]] = {}
    for category, source in config["sources"].items():
        processed_rules: list[dict] = []
        for rule in source["effects"]:
            rule = _parse_ir_rule(rule, mixdb.num_ir_files)
            processed_rules = _expand_effect_rules(processed_rules, rule)
        rules[category] = list_dataclass_from_dict(list[Effects], processed_rules)

    validate_rules(mixdb, rules)
    return rules


def _expand_effect_rules(expanded_rules: list[dict], rule: dict) -> list[dict]:
    from copy import deepcopy

    from ..parse.expand import expand

    for key in ("pre", "post"):
        if key in rule:
            value = rule[key]
            for idx in range(len(value)):
                new_rules = expand(value[idx])
                if len(new_rules) > 1:
                    for new_rule in new_rules:
                        expanded_effect = deepcopy(rule)
                        new_value = deepcopy(value)
                        new_value[idx] = new_rule
                        expanded_effect[key] = new_value
                        _expand_effect_rules(expanded_rules, expanded_effect)
                    return expanded_rules

    expanded_rules.append(rule)
    return expanded_rules


def _parse_ir_rule(rule: dict, num_ir: int) -> dict:
    from ..datatypes import EffectList
    from .helpers import generic_ids_to_list

    def _resolve_str(parameters: str) -> str:
        if parameters.startswith("rand") or parameters.startswith("choose") or parameters.startswith("expand"):
            return f"ir {parameters}"

        irs = generic_ids_to_list(num_ir, parameters)

        if not all(ro in range(num_ir) for ro in irs):
            raise ValueError(f"Invalid ir of {parameters}")

        if len(irs) == 1:
            return f"ir {irs[0]}"
        return f"ir expand({', '.join(map(str, irs))})"

    def _process(rules_in: EffectList) -> EffectList:
        rules_out: EffectList = []

        for rule_in in rules_in:
            parts = rule_in.split(maxsplit=1)

            name = parts[0]
            if name != "ir":
                rules_out.append(rule_in)
                continue

            if len(parts) == 1:
                continue

            parameters = parts[1]
            if parameters.isnumeric():
                ir = int(parameters)
                if ir not in range(num_ir):
                    raise ValueError(f"Invalid ir of {parameters}")
                rules_out.append(rule_in)
                continue

            if isinstance(parameters, str):
                rules_out.append(_resolve_str(parameters))
                continue

            raise ValueError(f"Invalid ir of {parameters}")

        return rules_out

    for key in ("pre", "post"):
        if key in rule:
            rule[key] = _process(rule[key])

    return rule


def apply_effects(
    mixdb: MixtureDatabase,
    audio: AudioT,
    effects: Effects,
    pre: bool = True,
    post: bool = True,
) -> AudioT:
    """Apply effects to audio data

    :param mixdb: Mixture database
    :param audio: Input audio
    :param effects: Effects
    :param pre: Apply pre-truth effects
    :param post: Apply post-truth effects
    :return: Output audio
    """
    from ..datatypes import EffectList
    from .ir_effects import apply_ir
    from .ir_effects import read_ir
    from .sox_effects import apply_sox_effects

    def _process(audio_in: AudioT, effects_in) -> AudioT:
        _effects: EffectList = []
        for effect in effects_in:
            if effect.startswith("ir "):
                # Apply effects gathered so far
                audio_in = apply_sox_effects(audio_in, _effects)

                # Then empty the list of effects
                _effects = []

                # Apply IR
                index = int(effect.split()[1])
                audio_in = apply_ir(
                    audio=audio_in,
                    ir=read_ir(
                        name=mixdb.ir_file(index),
                        delay=mixdb.ir_delay(index),
                        use_cache=mixdb.use_cache,
                    ),
                )
            else:
                _effects.append(effect)

        return apply_sox_effects(audio_in, _effects)

    audio_out = audio.copy()

    if pre:
        audio_out = _process(audio_out, effects.pre)

    if post:
        audio_out = _process(audio_out, effects.post)

    return audio_out


def estimate_effected_length(
    samples: int,
    effects: Effects,
    frame_length: int = 1,
    pre: bool = True,
    post: bool = True,
) -> int:
    """Estimate the effected audio length

    :param samples: Original length in samples
    :param effects: Effects
    :param frame_length: Length will be a multiple of this
    :param pre: Apply pre-truth effects
    :param post: Apply post-truth effects
    :return: Estimated length in samples
    """
    from .pad_audio import get_padded_length

    def _update_samples(s: int, e: str) -> int:
        import re

        # speed factor[c]
        speed_pattern = re.compile(r"^speed\s+(-?\d+(\.\d+)*)(c?)$")
        result = re.search(speed_pattern, e)
        if result:
            value = float(result.group(1))
            if result.group(3):
                value = float(2 ** (value / 1200))
            return int(s / value + 0.5)

        # tempo [-q] [-m|-s|-l] factor [segment [search [overlap]]]
        tempo_pattern = re.compile(r"^tempo\s+(-q\s+)?(((-m)|(-s)|(-l))\s+)?(\d+(\.\d+)*)")
        result = re.search(tempo_pattern, e)
        if result:
            value = float(result.group(7))
            return int(s / value + 0.5)

        # other effects which do not affect length
        return s

    length = samples

    if pre:
        for effect in effects.pre:
            length = _update_samples(length, effect)

    if post:
        for effect in effects.post:
            length = _update_samples(length, effect)

    return get_padded_length(length, frame_length)


def effects_from_rules(mixdb: MixtureDatabase, rules: Effects) -> Effects:
    from copy import deepcopy

    from ..parse.rand import rand

    effects = deepcopy(rules)
    for key in ("pre", "post"):
        entries = getattr(effects, key)
        for idx, entry in enumerate(entries):
            if entry.find("rand") != -1:
                entries[idx] = rand(entry)
            if entry.startswith("ir choose"):
                entries[idx] = _choose_ir(mixdb, entry)
        setattr(effects, key, entries)

    return effects


def conform_audio_to_length(audio: AudioT, length: int, loop: bool, start: int) -> AudioT:
    """Conform audio to the given length

    :param audio: Audio to conform
    :param length: Length of output
    :param loop: Loop samples or pad
    :param start: Starting sample offset
    :return: Conformed audio
    """
    import numpy as np

    if loop:
        return np.take(audio, range(start, start + length), mode="wrap")

    # Non-loop mode
    audio_slice = audio[start : start + length]

    if len(audio_slice) >= length:
        # We have enough samples, truncate
        return audio_slice[:length]
    else:
        # We need padding
        padding_needed = length - len(audio_slice)
        return np.pad(audio_slice, (0, padding_needed))


def validate_rules(mixdb: MixtureDatabase, rules: dict[str, list[Effects]]) -> None:
    from .sox_effects import validate_sox_effects

    for rule_list in rules.values():
        for rule in rule_list:
            sox_effects: list[str] = []
            effects = effects_from_rules(mixdb, rule)

            for effect in effects.pre:
                if not effect.startswith("ir"):
                    sox_effects.append(effect)

            for effect in effects.post:
                for check in ("speed", "tempo"):
                    if check in effect:
                        raise ValueError(f"'{check}' effect is not allowed in post-truth effect chain.")

                if not effect.startswith("ir"):
                    sox_effects.append(effect)

            validate_sox_effects(sox_effects)


def _choose_ir(mixdb: MixtureDatabase, directive: str) -> str:
    """Evaluate the 'choose' directive for an ir.

    The directive is used to choose a random ir file from the database
    and may take one of the following forms:

    # choose a random ir file
    ir choose()

    # choose a random ir file between a and b, inclusive
    ir choose(a, b)

    # choose a random ir file with the specified tag
    ir choose(tag)

    :param mixdb: Mixture database
    :param directive: Directive to evaluate
    :return: Resolved value
    """
    import re
    from random import choice
    from random import randint

    choose_pattern = re.compile(r"^ir choose\(\)$")
    choose_range_pattern = re.compile(r"^ir choose\((\d+),\s*(\d+)\)$")
    choose_tag_pattern = re.compile(r"^ir choose\((\w+)\)$")

    def choose_range_repl(m) -> str:
        lower = int(m.group(1))
        upper = int(m.group(2))
        if (
            lower < 0
            or lower >= mixdb.num_ir_files
            or upper < 0
            or upper >= mixdb.num_ir_files
            or lower >= upper
            or str(lower) != m.group(1)
            or str(upper) != m.group(2)
        ):
            raise ValueError(
                f"Invalid rule: '{directive}'. Values must be integers between 0 and {mixdb.num_ir_files - 1}."
            )
        return f"ir {randint(lower, upper)}"  # noqa: S311

    def choose_tag_repl(m) -> str:
        return m.group(1)

    if re.match(choose_pattern, directive):
        return f"ir {randint(0, mixdb.num_ir_files - 1)}"  # noqa: S311

    if re.match(choose_range_pattern, directive):
        try:
            return f"ir {eval(re.sub(choose_range_pattern, choose_range_repl, directive))}"  # noqa: S307
        except Exception as e:
            raise ValueError(
                f"Invalid rule: '{directive}'. Values must be integers between 0 and {mixdb.num_ir_files - 1}."
            ) from e

    if re.match(choose_tag_pattern, directive):
        tag = re.sub(choose_tag_pattern, choose_tag_repl, directive)
        if tag in mixdb.ir_tags:
            return f"ir {choice(mixdb.ir_file_ids_for_tag(tag))}"  # noqa: S311

        raise ValueError(f"Invalid rule: '{directive}'. Tag, '{tag}', not found in database.")

    raise ValueError(f"Invalid rule: '{directive}'.")
