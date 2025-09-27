# ΦωΦ (pronounced owega)
ΦωΦ is a command-line interface for conversing with GPT models (from OpenAI)

Pypi:
[![PyPI - Status](https://img.shields.io/pypi/status/owega)](https://pypi.org/project/owega/)
[![PyPI - Version](https://img.shields.io/pypi/v/owega)](https://pypi.org/project/owega/)
[![Downloads](https://static.pepy.tech/badge/owega)](https://pepy.tech/project/owega) [![Downloads](https://static.pepy.tech/badge/owega/month)](https://pepy.tech/project/owega)
[![PyPI - License](https://img.shields.io/pypi/l/owega)](https://git.pyrokinesis.fr/darkgeem/owega/-/blob/main/LICENSE)
[![PyPI - Format](https://img.shields.io/pypi/format/owega)](https://pypi.org/project/owega/)
[![PyPI - Implementation](https://img.shields.io/pypi/implementation/owega)](https://pypi.org/project/owega/)

AUR:
[![AUR Version](https://img.shields.io/aur/version/python-owega)](https://aur.archlinux.org/packages/python-owega)
[![AUR Last Modified](https://img.shields.io/aur/last-modified/python-owega?logo=archlinux&label=AUR%20update)](https://aur.archlinux.org/packages/python-owega)
[![AUR License](https://img.shields.io/aur/license/python-owega)](https://git.pyrokinesis.fr/darkgeem/owega/-/blob/main/LICENSE)
[![AUR Maintainer](https://img.shields.io/aur/maintainer/python-owega)](https://aur.archlinux.org/packages/python-owega)
[![AUR Votes](https://img.shields.io/aur/votes/python-owega)](https://aur.archlinux.org/packages/python-owega)

Gitlab:
[![GitLab Tag](https://img.shields.io/gitlab/v/tag/81?gitlab_url=https%3A%2F%2Fgit.pyrokinesis.fr)](https://git.pyrokinesis.fr/darkgeem/owega)
[![GitLab Issues](https://img.shields.io/gitlab/issues/open/81?gitlab_url=https%3A%2F%2Fgit.pyrokinesis.fr)](https://git.pyrokinesis.fr/darkgeem/owega)
[![GitLab Merge Requests](https://img.shields.io/gitlab/merge-requests/open/81?gitlab_url=https%3A%2F%2Fgit.pyrokinesis.fr)](https://git.pyrokinesis.fr/darkgeem/owega)
[![GitLab License](https://img.shields.io/gitlab/license/81?gitlab_url=https%3A%2F%2Fgit.pyrokinesis.fr)](https://git.pyrokinesis.fr/darkgeem/owega/-/blob/main/LICENSE)

[![Discord](https://img.shields.io/discord/1171384402438275162?style=social&logo=discord)](https://discord.gg/KdRmyRrA48)



## ΦωΦ's homepage
You can check on the source code [on its gitlab page](https://git.pyrokinesis.fr/darkgeem/owega)!

Also, here's the [discord support server](https://discord.gg/KdRmyRrA48), you
can even get pinged on updates, if you want!


## Features
ΦωΦ has quite a lot of features!

These include:
- Saving/loading conversation to disk as json files.
- Autocompletion for commands, file search, etc...
- History management.
- Temp files to save every message, so that you can get back the conversation
  if you ever have to force-quit ΦωΦ.
- Config file to keep settings like api key, preferred model, command execution
  status...
- Command execution: if enabled, allows ΦωΦ to execute commands on your system
  and interpret the results.
- File creation: if commands are enabled, also allows ΦωΦ to create files on
  your system and fill them with desired contents.
- GET requests: allows ΦωΦ to get informations from online pages, through
  http(s) GET requests.
- Long-term memory: allows for ΦωΦ to store memories, which will not be deleted
  as the older messages are, to keep requests under the available tokens per
  request.
- Context management: allows to set the AI context prompt (example: "you are a
  cat. cats don't talk. you can only communicate by meowing, purring, and
  actions between asterisks" will transform ΦωΦ into a cat!!)
- Meow.
- Meow meow.
- MEOW MEOW MEOW MEOW!!!!


## Installation
Just do ``pipx install owega`` to get the latest version (with pipx)

An archlinux package `python-owega` is also available on the AUR.


## Optional requirements
- [rich](https://pypi.org/project/rich/) - for rich markdown formatting
- [tiktoken](https://pypi.org/project/tiktoken) - for better token estimation
- [markdownify](https://pypi.org/project/markdownify/) - for better html to markdown (with web functions)


## Command-line arguments
Do you really need me to do ``owega --help`` for you?

```
usage: owega [-h] [-d] [-c] [-l] [-v] [-f CONFIG_FILE] [-i HISTORY] [-a ASK]
             [-o OUTPUT] [-t] [-s TTSFILE] [-T] [-e]

Owega main application

options:
  -h, --help            show this help message and exit
  -d, --debug           Enable debug output
  -c, --changelog       Display changelog and exit
  -l, --license         Display license and exit
  -v, --version         Display version and exit
  -f CONFIG_FILE, --config-file CONFIG_FILE
                        Specify path to config file
  -i HISTORY, --history HISTORY
                        Specify the history file to import
  -a ASK, --ask ASK     Asks a question directly from the command line
  -o OUTPUT, --output OUTPUT
                        Saves the history to the specified file
  -t, --tts             Enables TTS generation when asking
  -s TTSFILE, --ttsfile TTSFILE
                        Outputs a generated TTS file single-ask mode
  -T, --training        outputs training data from -i file
  -e, --estimate        shows estimate token usage / cost from a request from
                        -i file
```


## Markdown formatting and syntax highlighting
To allow ΦωΦ to print its output nicely, you can just install the rich python
module: ``pip install rich``


## Showcase
See ΦωΦ in action!

### Demos made with ΦωΦ 5.7.5
[![asciicast](https://asciinema.org/a/659607.png)](https://asciinema.org/a/659607)
[Youtube demo](https://youtu.be/_LGSc6mj-EM)


## CHANGELOG:

```
OWEGA v5.24.2 CHANGELOG:


2.0.0: WTFPL license
2.0.1: added genconf command

2.1.0: added file_input command
2.1.1: added file_input in help command

2.2.0: added context command to change GPT's definition
2.2.1: added license and version info in command line (-l and -v)
2.2.2: stripped user input (remove trailing spaces/tabs/newlines)
2.2.3: genconf now saves the current conf instead of a blank template
2.2.4: automatic temp file save


3.0.0: changed conversation save from pickle to json
3.0.1: added changelog
3.0.2: added conversion script
3.0.3: quitting with EOF will now discard the temp file (^C will still keep it)

3.1.0: BMU (Better Module Update)!
       modified MSGS:
         - added last_question()
         - changed last_answer()
       modified ask() to allow for blank prompt,
         which will reuse the last question
3.1.1: now handling the service unavailable error

3.2.0: FUNCTION CALLING UPDATE:
       added function calling, now openchat is able to run commands
       on your computer, as long as you allow it to
       (you will be prompted on each time it tries to run a command)
       !!! only available on -0613 models (gpt-3.5-turbo-0613, gpt-4-0613) !!!
       will be available on all gpt models from 2023-06-27, with the latest
       openchat 3.2.X patch
3.2.1: fixed a space missing in openchat's function calling
3.2.2: fixed openchat sometimes not detecting the command has been ran
3.2.3: added create_file as a function OpenAI can call
3.2.4: fixed variables and ~ not expanding when executing a command
3.2.4-fix1: fixed a missing parenthesis
3.2.5: now handling non-zero exit status when running a command
3.2.6: reversed the changelog order, fixed function calling chains
3.2.7: fixed json sometimes not correctly formatted when writing multiple lines
       files
3.2.8: fixed command execution stderr handling
3.2.9: changed execute's subprocess call to shell=True, now handling pipes...
3.2.10: added a command line option for specifying the config file
3.2.11: now, the default gpt models implement function calling, no need for
        0613 anymore

3.3.0: implemented prompt_toolkit, for better prompt handling, newlines with
       control+n
3.3.1: added tokens command, to change the amount of requested tokens

3.4.0: CLI update:
         - added command-line options to change input/output files
         - added command-line option to ask a question from command line

3.5.0: WEB update: now added a flask app, switched repos to its own
3.5.1: added "commands" command, to enable/disable command execution
3.5.2: added infos on bottom bar

3.6.0: PREFIX update:
         - added prefixes for command (changeable in the config)
         - reformatted most of the main loop code to split it in handlers

3.7.0: DIRECT CONTEXT COMMANDS update:
         - now, you can use commands in one line, instead of waitingfor prompt
             example: /save hello.json
             (instead of typing /save, then enter, then typing hello.json
              works on all commands, the only specific case being file_input.)
         - file_input as a direct command takes only one argument: the file
             to load (e.g. /load ./src/main.c). The pre-prompt will be asked
             directly instead of having to do it in three steps
               (/load, then filename, then pre-prompt)
         - also, fixed /tokens splitting the prompt instead of the user input

3.8.0: WEB download update
         - added a get_page function for openchat to get pages without the need
             for curl
3.8.1: added a debug option for devs

3.9.0: Windows update
         - Do I really need to explain that update?
3.9.1: fixed an issue when the openai api key does not exist anywhere
3.9.2: changed the temp file creation method for non-unix systems
3.9.3: fixed api key not saving with /genconf
3.9.4: changed default values


4.0.0: LTS: Long-Term-Souvenirs
       The AI now have long-term memory!!!
       Huge update: full refactoring, the code is now readable!
       Also, the name is now Owega (it's written with unicode characters though)
       You can see the new code here: https://git.pyrokinesis.fr/darkgeem/owega
       Also, the project is now available on PyPI so, just go pip install owega!
4.0.1: oops, forgot to change the setup.py and now I messed up my 4.0.0! >:C
4.0.2: Fixed a typo where owega wouldn't send the memory
4.0.3: Added README to pypi page
4.0.4: Fixed context not working correctly

4.1.0: Changed the getpage function to strip the text
4.1.1: Removed a warning due to beautifulsoup4

4.2.0: VERY IMPORTANT UPDATE: NOW COMPATIBLE WITH OPENAI 1.1.1

4.3.0: Added token estimation
4.3.1: Added time taken per request in debug output
4.3.2: Fixed 4.3.1 :p
4.3.3: Changed time taken to only show up to ms
4.3.4: Re-added server unavailable error handling
4.3.5: Added exception handling for token estimation
4.3.6: Re-added handling of invalid request, mostly for too large requests

4.4.0: Changed from json to json5 (json-five)

4.5.0: Added support for organization specification
4.5.1: fixed owega bash script for systems that still have PYTHON 2 AS DEFAULT
       WTF GUYS GET OVER IT, IT'S BEEN DEPRECATED SINCE 2020
4.5.2: Now removes temp files even if ctrl+c if they are empty
4.5.3: Fixed files being removed everytime

4.6.0: Fine tweaking update
       - added command for changing the temperature
       - added top_p command and parameter
       - added frequency penalty command and parameter
       - added presence penalty command and parameter
       - fixed /quit and /exit not working
       - fixed tab completion
4.6.1: Added support for overwriting config file
4.6.2: Oops, forgot to check help, help should be fixed now

4.7.0: Added TTS (using pygame)
4.7.1: Now prints message before reading TTS
       Also, removes the pygame init message
4.7.2: Fixed a bug where the output tts file could not be set to mp3
         (it was previously checking for mp4 extension, lol)
4.7.3: Added ctrl+C handling when playing TTS to stop speaking.

4.8.0: Edit update
       - you can now edit the history from the TUI
       - on a side note, I also improved completion for files
           and numeric values (temperature, top_p, penalties...)
4.8.1: Oops, forgot to add requirements to setup.py
       Automated the process, should be good now
4.8.2: - added infos to pypi page
       - changed to automatic script generation (setup.py)

4.9.0: - added system command

4.10.0: - added system souvenirs (add_sysmem/del_sysmem)
4.10.1: - added support server in readme and pypi
4.10.2: - added cost estimation in token estimation
4.10.3: - changed from OpenAI to Owega in term display

4.11.0: Huge refactor, added TTS as config parameter
4.11.1: Oops, last version broke owega, fixed here
        (Problem was I forgot to export submodules in setup.py)
4.11.2: Fixed -a / single_ask
4.11.3: Fixed /genconf
4.11.4: Fixed edit with blank message (remove message)
4.11.5: Fixed requirements in setup.py not working when getting
        the source from PyPI

4.12.0: Added -T/--training option to generate training line
4.12.1: Added -e/--estimate option to estimate consumption
4.12.2: Fixed TUI-mode TTS
4.12.3: Fixed requirements to be more lenient
4.12.4: Fixed requirements to use json5 instead of json-five
4.12.5: Fixed emojis crashing the history because utf16
4.12.6: Fixed emojis crashing the edit function because utf16
4.12.7: Fixed a minor bug where /file_input would insert a "'"
          after the file contents.
        Also, added filetype information on codeblocks with
          /file_input, depending on the file extension
4.12.8: Added a vim modeline to history files
          to specify it's json5, not json.
4.12.9: Added badges to the README :3
4.12.10: Added docstrings
         Switched from tabs to spaces (PEP8)
         Changed default available models
         Changed estimation token cost values


5.0.0: ADDED VISION
5.0.1: Added support for local images for vision
       Also, better crash handling...
5.0.2: Changed the /image given handling, now you can give it
         both the image, then a space, then the pre-image prompt.
5.0.3: Added a play_tts function for using owega as a module.
5.0.4: Added better given handling for handlers.

5.1.0: Added silent flag for handlers.
5.1.1: Fixed handle_image

5.2.0: Changed file_input behavior to only add the prompt and
       not immediately request an answer.
5.2.1: Fixed the create_file function, disabled get_page.
5.2.2: Suppressed pygame-related warnings
       (i.e. avx2 not enabled).

5.3.0: Added /dir_input
5.3.1: Re-enabled get_page with better parsing

5.4.0: Added default_prompt variable in configuration

5.5.0: Added basic support for Mistral's API (beta feature)
5.5.1: Removed useless available_mistral and mistral_model
        variables.
5.5.2: Added debug info on mistral's part of ask()
       Added matching for mixtral
5.5.3: Removed debug lines that shouldn't have been left there.
5.5.4: Fixed a debug_print never showing.
5.5.5: Now using openai module to ask mistral API.
       (the code is waaaay cleaner)

5.6.0: Added basic support for Chub's API
       (chub mars, mercury, mixtral)
       Also, Mi(s/x)tral support is no more in beta :D
5.6.1: Added extensive logging for errors.
5.6.2: Added terminal title status :3
5.6.3: Fixes config's api_key not being used.
       Better docstrings on handlers.
5.6.4: Fix for ask.ask() crashing if OPENAI_API_KEY isn't set.

5.7.0: Changed the license to the DarkGeem Public License v1.0.
5.7.1: Fixed a non-ascii character in the DGPL.
5.7.2: Added vision support for GPT-4o.
5.7.3: Better cost estimation, including input/output costs.
       (added support for all GPT model as of 2024-05-14)
       (added support for all mistral API models as of today)
       (all other models return a cost of 0)
5.7.4: Added pretty print if the rich module is installed.
5.7.5: Fixed the bottom toolbar being cut short when terminal
       doesn't have enough columns.
       (also, added gpt-4o and mixtral-8x22b to default list)

5.8.0: Added time-aware mode...
5.8.1: Oops, I broke the build system again, my bad! :P
5.8.2: Oops, I didn't completely fix it last time~ Awoo! >w<\
5.8.3: Fixed some error handling.
5.8.4: Fixed an issue with time-aware mode which would create
       new lines with just the date when sending an empty
       message, instead of just prompting with same history.
5.8.5: Changed setup.py to package the VERSION and CHANGELOG
       files.
5.8.6: Updated the README with 5.7.5 demos.

5.9.0: Fixed a huge issue where owega couldn't be imported if
       the terminal wasn't interactive.
       Added owega.__version__
5.9.1: Changed type hinting and fixed some code style!
5.9.2: Added a tts_to_opus function in owega.utils.
5.9.3: Added __all__ variable to __init__.py files.
5.9.4: Fixed a circular import, which technically wasn't really
       an issue, due to an old AWFUL AF fix...
       Also, fixed most type hinting.

5.10.0: Moved single_ask to owega.ask, moved markdown_print to
        owega.utils.

5.11.0: Added support for Anthropic's Claude.

5.12.0: Added /fancy, for toggling fancy printing.

5.13.0: Dependency removal update.
        - Changed markdownify dep from required to optional.
        - Changed pygame dep from required to optional.
5.13.1: - Changed tiktoken dep from required to optional.
5.13.2: - Fixed compatibility with python <3.11 by removing
          typing.Self references.
5.13.3: - Fixed errors with some versions of python-editor which
          don't have editor.edit but editor.editor()???
          Somehow... I don't know maaaan, I'm tireeeed =w='

5.14.0: Image generation update.
        Allows for the AI to generate images using DALLE

5.15.0: OpenAI o1 update.
        Adds support for OpenAI's o1 models, which are limited,
        as they lack support for temperature, top_p, penalties,
        vision, and function calling.
5.15.1: - Added o1-preview and o1-mini to default models list.
5.15.2: - Fixed 5.15.1, as I mistyped 4o-(preview/mini)
          insead of o1-(preview/mini)

5.16.0: Rewrite ask.py, better handling
5.16.1: Fixed vision support for Anthropic's claude
5.16.2: Fixed vision support for Anthropic's claude... Again.
5.16.3: Added a .md prefix to the temp file with /edit
        (for editor syntax highlighting)
5.16.4: Fix for claude: enforce non-streaming mode
        (fixes the 'overloaded_error' errors)

5.17.0: Added xAI (grok) support!
        Supports everything, even function calling and vision!
5.17.1: Fixed logger error preventing owega from opening on
        Windows... I am so sorry I didn't catch this earlier!
        >w<
5.17.2: Cleaned up codebase a little, thanks pycharm...

5.18.0: Fixed function calling for mistral.
5.18.1: Added fancy err message for flagged messages (OpenAI).

5.19.0: Added /reprint, which supersedes /history as it supports
        fancy markdown printing (continue using /history to get
        the raw text without disabling fancy mode)
        (Also, updated build system to use pyproject.toml)
5.19.1: Fixed issues with custom models.

5.20.0: Fixed model detection for MistralAI models.
        Fixed MistralAI not able to respond when last message is
          from assistant.
5.20.1: Changed the append_blank_user to "" instead of ".".
5.20.2: Moved the preferred config location to
          $HOME/.config/owega/config.json5

5.21.0: Changed the config loading logic to load all
          .json/.json5 files in ~/.config/owega/ or given dirs
          to allow saving API keys in a dedicated config file.
        Moved the defaults to owega/constants.py to replace
          hardcoded values.
5.21.1: Added a /send alias to dir_input, fixed relative files
          being refused because 'parent dir does not exist',
          allows /dir_input to take files, with an automatic
          pre-prompt ('dir/filename.ext:' before file contents)
5.21.2: Moved clr and clrtxt to owega/colors.py
5.21.3: Refactored bool/float input handlers to use centralized
          helper setter functions.
          (owega/OweHandlers/helpers.py)
5.21.4: Removed redundant info_print and debug_print in utils.py
          This does not affect anything, as utils.py
          still imports them from owega.config
        Changed /genconf and genconfig() behavior to generate
          ~/.config/owega/, and split api key/non api key values
          to the api.json5 and config.json5 files respectively.

5.22.0: = The model update =
        - Added openrouter integration!!!
        - Added new model naming schemes:
            [provider]:[model]
            custom:[model]@[base_url]
          Provider list:
          - anthropic (anthropic.com - claude-3.7-sonnet...)
          - chub (chub.ai)
          - mistral (mistral.ai - mistral/mixtral/codestral...)
          - openai (openai.com - GPT-4o/GPT-4.1/o1...)
          - openrouter (openrouter.ai - recommended)
          - xai (x.ai - grok)
          - custom
        - Cleaned up some code in ask.py
        - Added some error handling so errors won't throw you
          out of owega anymore.
        - Handles ctrl+c to cancel a pending request.
          (so it doesn't throw you out of owega anymore either.)
5.22.1: Changed the default model list and added openrouter_api
          as a default blank parameter.
5.22.2: Fixed the config file loading order, config files will
          now load in alphabetical order (python string sort)
5.22.3: Added function calling for openrouter!
5.22.4: Fixed a bug where some unicode characters would not load
          properly, and prevent the user from using owega if
          their Conversation contained invalid ones.
        Also fixed a bug where get_page would try and run
          debug_print with an old syntax.
        Note to self: Please, replace all debug_print uses with
                      getLogger loggers.

5.23.0: Added /web command to enable/disable
          the web access feature.
5.23.1: Added /lts command to enable/disable long term souvenirs
          and permanently disabled the image generation 'tool'
          as a function to be called by the AI.
        This should not have been hardcoded in the first place.
5.23.2: Added optional argument to /reprint to only reprint N
          last messages.
5.23.3: Changed TTS requirements: pygame not needed anymore,
          now requiring soundfile and sounddevice

5.24.0: PROMPT INJECTION UPDATE
        ---
        So basically, there are 8 new variables:
        6 message injectors (string):
        - pre_user / pre_assistant / pre_system
          ^ these will be prefixing each message from their role
        - post_user / post_assistant / post_system
          ^ these will be suffixing each message from their role
        2 history injectors (list of message dicts):
        - pre_history / post_history
        Basically, each message dict must contain a "role" key
          and a "content" key.
          "role" should be one of: user/assistant/system
          and "content is the actual message content"
        You can just take a message history dict from a /save,
          these are loaded the same.
        
        Note that history injectors won't be affected by message
          injectors!
5.24.1: Fixed broken symlinks crashing /send, added message ID
          to files sent with /send, symlinks are now sent as
          their location instead of their content
5.24.2: Added \x1b\r as newline, just like claude (smort!)

```
