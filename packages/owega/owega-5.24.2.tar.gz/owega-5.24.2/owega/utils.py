"""Utilities that don't fit anywhere else."""
import os
import sys
import tempfile
from typing import Literal

import json5 as json
import openai

try:
    import sounddevice as sd
    import soundfile as sf
    audio_lib = "sounddevice"
except ImportError:
    sd = None
    sf = None
    audio_lib = None

try:
    import tiktoken
except ModuleNotFoundError:
    def __internal_get_tokens(s: str) -> int:
        return len(s) // 4
else:
    def __internal_get_tokens(s: str) -> int:
        encoder = tiktoken.encoding_for_model("gpt-4")
        return len(encoder.encode(s))

from . import getLogger
from .config import baseConf, get_home_dir, info_print, debug_print
from .colors import clrtxt
from .conversation import Conversation

try:
    import rich
    from rich.markdown import Markdown
except ModuleNotFoundError:
    def markdown_print(s: str) -> None:
        print(s)
else:
    def markdown_print(s: str) -> None:
        if baseConf.get("fancy", False):
            rich.print(Markdown(s))
        else:
            print(s)


def set_term_title(new_title: str) -> None:
    print(f"\033]0;{new_title}\a", end='')


def get_temp_file() -> str:
    """Get a temp file location."""
    tmp = tempfile.NamedTemporaryFile(
        prefix="owega_temp.",
        suffix=".json",
        delete=False
    )
    filename = tmp.name
    tmp.close()
    return filename


def command_text(msg) -> str:
    """Print a command message."""
    return ' ' + clrtxt("red", "COMMAND") + ": " + msg


def success_msg() -> str:
    """Return the standard success message."""
    return '  ' + clrtxt("cyan", " INFO ") + ": Owega exited successfully!"


def genconfig(conf_path="") -> None:
    """Generate the config file if it doesn't exist already."""
    _ = conf_path
    conf_dir = os.path.expanduser('~/.config/owega')
    conf_file = os.path.join(conf_dir, 'config.json5')
    conf_file_api = os.path.join(conf_dir, 'api.json5')
    if not os.path.exists(conf_dir):
        os.mkdir(conf_dir)
    else:
        if not os.path.isdir(conf_dir):
            info_print('Error: "~/.config/owega" is not a directory.')
    config_noapi = {}
    config_api = {}
    for key, val in baseConf.items():
        if "api" in key.lower():
            if not isinstance(val, str):
                val = ""
            config_api[key] = val
        else:
            config_noapi[key] = val

    if not os.path.exists(conf_file_api):
        with open(conf_file_api, "w") as f:
            f.write('// vim: set ft=json5:\n')
            f.write(str(json.dumps(config_api, indent=4)))
        info_print(f"saved api keys as ~/.config/owega/api.json5 !")

    should_write = True
    if os.path.isfile(conf_file):
        should_write = False
        print(
            clrtxt('red', ' WARNING ')
            + ": YOU ALREADY HAVE A CONFIG FILE AT "
            + "~/.config/owega/config.json5"
        )
        print(
            clrtxt('red', ' WARNING ')
            + ": DO YOU REALLY WANT TO OVERWRITE IT???")

        inps = clrtxt("red", "   y/N   ") + ': '
        inp = input(inps).lower().strip()
        if inp:
            if inp[0] == 'y':
                should_write = True

    if should_write:
        with open(conf_file, "w") as f:
            f.write('// vim: set ft=json5:\n')
            f.write(str(json.dumps(config_noapi, indent=4)))
        info_print("saved configuration as ~/.config/owega/config.json5 !")
        return

    info_print("Sorry, not sorry OwO I won't let you nuke your config file!!!")


def play_opus(location: str) -> None:
    """Play an OPUS audio file."""
    _ = location
    if audio_lib == "sounddevice" and sf is not None and sd is not None:
        try:
            data, fs = sf.read(location)
            sd.play(data, fs)
            sd.wait()  # wait until file is done playing
        except Exception as e:
            info_print(f"Could not play audio: {e}")
    else:
        info_print("Could not play audio, missing audio library.")


def tts_to_opus(
    loc: str,
    text: str,
    voice: Literal['alloy', 'echo', 'fable', 'onyx', 'nova', 'shimmer'] = 'nova'
) -> None:
    """Generate TTS audio from given text and save it to an opus file."""
    tts_answer = openai.audio.speech.create(
        model='tts-1',
        voice=voice,
        input=text
    )
    tts_answer.write_to_file(loc)


def play_tts(
    text: str,
    voice: Literal['alloy', 'echo', 'fable', 'onyx', 'nova', 'shimmer'] = 'nova'
) -> None:
    """Generate TTS audio from given text and play it."""
    tmpfile = tempfile.NamedTemporaryFile(
        prefix="owegatts.",
        suffix=".opus",
        delete=False
    )
    tmpfile.close()
    tts_to_opus(tmpfile.name, text, voice)
    play_opus(tmpfile.name)
    os.remove(tmpfile.name)


def estimated_tokens(ppt: str, messages: Conversation, functions: list) -> int:
    """Estimate the history tokens."""
    try:
        req = ""
        req += ppt
        req += str(json.dumps(messages.get_messages()))
        req += str(json.dumps(functions))
        return __internal_get_tokens(req)
    except Exception as e:
        logger = getLogger.getLogger(__name__, baseConf.get("debug", False))
        logger.info("An error has occured while estimating tokens:")
        logger.info(e)
        return 0


def estimated_cost(
    input_tokens: int, model: str, output_tokens: int = 4096
) -> float:
    # ppt = price per token: tuple (input, output)
    per_k = 1000
    per_m = 1000 * per_k
    ppt_table = {
        '00:gpt-4o': (5 / per_m, 15 / per_m),
        '01:gpt-3': (0.5 / per_m, 1.5 / per_m),
        '02:gpt-4-turbo': (10 / per_m, 30 / per_m),
        '03:gpt-4-32k': (60 / per_m, 120 / per_m),
        '04:gpt-4-': (30 / per_m, 60 / per_m),
        '05:open-mistral-7b': (0.25 / per_m, 0.25 / per_m),
        '06:open-mixtral-8x7b': (0.7 / per_m, 0.7 / per_m),
        '07:open-mixtral-8x22b': (2 / per_m, 6 / per_m),
        '08:mistral-small': (1 / per_m, 3 / per_m),
        '09:mistral-medium': (2.7 / per_m, 8.1 / per_m),
        '10:mistral-large': (4 / per_m, 12 / per_m),
    }
    ppt_indexes_sorted = list(sorted(ppt_table.keys()))
    for index in ppt_indexes_sorted:
        model_start = ':'.join(index.split(':')[1:])
        if model.startswith(model_start):
            ppt = ppt_table[index]
            return (input_tokens * ppt[0]) + (output_tokens * ppt[1])
    return 0


def estimated_tokens_and_cost(
    ppt: str,
    messages: Conversation,
    functions: list,
    model: str,
    output_tokens: int = 4096
) -> tuple[int, float]:
    input_tokens = estimated_tokens(ppt, messages, functions)
    cost = estimated_cost(input_tokens, model, output_tokens)
    return (input_tokens, cost)


def do_quit(
    msg="", value=0, temp_file="", is_temp=False, should_del=False
) -> None:
    """Quit and delete the given file if exists."""
    if (temp_file):
        if should_del:
            try:
                os.remove(temp_file)
            except OSError:
                pass
        else:
            if is_temp:
                try:
                    with open(temp_file, 'r') as f:
                        contents = json.loads(f.read())
                        if isinstance(contents, dict):
                            if not (
                                (len(contents.get("messages", [])) > 0)
                                or (len(contents.get("souvenirs", [])) > 0)
                            ):
                                os.remove(temp_file)
                except (OSError, ValueError):
                    pass
    if (msg):
        print()
        print(msg)
    sys.exit(value)


def print_help(commands_help=None) -> None:
    """Print the command help."""
    if commands_help is None:
        commands_help = {}
    commands = list(commands_help.keys())
    longest = 0
    for command in commands:
        if len(command) > longest:
            longest = len(command)
    longest += 1
    print()
    info_print(
        "Enter your question after the user prompt, "
        + "and it will be answered by OpenAI")
    info_print("other commands are:")
    for cmd, hstr in commands_help.items():
        command = '/' + cmd
        info_print(f"   {command:>{longest}}  - {hstr}")
    print()
