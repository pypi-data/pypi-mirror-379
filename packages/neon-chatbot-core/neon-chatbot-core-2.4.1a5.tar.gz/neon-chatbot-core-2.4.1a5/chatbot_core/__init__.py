# NEON AI (TM) SOFTWARE, Software Development Kit & Application Development System
#
# Copyright 2008-2025 Neongecko.com Inc. | All Rights Reserved
#
# Notice of License - Duplicating this Notice of License near the start of any file containing
# a derivative of this software is a condition of license for this software.
# Friendly Licensing:
# No charge, open source royalty free use of the Neon AI software source and object is offered for
# educational users, noncommercial enthusiasts, Public Benefit Corporations (and LLCs) and
# Social Purpose Corporations (and LLCs). Developers can contact developers@neon.ai
# For commercial licensing, distribution of derivative works or redistribution please contact licenses@neon.ai
# Distributed on an "AS IS” basis without warranties or conditions of any kind, either express or implied.
# Trademarks of Neongecko: Neon AI(TM), Neon Assist (TM), Neon Communicator(TM), Klat(TM)
# Authors: Guy Daniels, Daniel McKnight, Regina Bloomstine, Elon Gasper, Richard Leeds
#
# Specialized conversational reconveyance options from Conversation Processing Intelligence Corp.
# US Patents 2008-2021: US7424516, US20140161250, US20140177813, US8638908, US8068604, US8553852, US10530923, US10530924
# China Patent: CN102017585  -  Europe Patent: EU2156652  -  Patents Pending

from os import environ
environ.setdefault("OVOS_CONFIG_BASE_FOLDER", "neon")
environ.setdefault("OVOS_CONFIG_FILENAME", "chatbots.yaml")

from neon_utils.decorators import module_property


@module_property
def _ChatBot():
    from chatbot_core.utils.version_utils import get_class
    return get_class()


@module_property
def _ConversationControls():
    from ovos_utils.log import log_deprecation
    log_deprecation("import from `chatbot_core.utils.enum` directly",
                    "3.0.0")
    from chatbot_core.utils.enum import ConversationControls
    return ConversationControls


@module_property
def _ConversationState():
    from ovos_utils.log import log_deprecation
    log_deprecation("import from `chatbot_core.utils.enum` directly",
                    "3.0.0")
    from chatbot_core.utils.enum import ConversationState
    return ConversationState


def generate_random_response(*args, **kwargs):
    from ovos_utils.log import log_deprecation
    log_deprecation("import from `chatbot_core.utils.bot_utils` directly",
                    "3.0.0")
    from chatbot_core.utils.bot_utils import generate_random_response
    return generate_random_response(*args, **kwargs)


def clean_up_bot(*args, **kwargs):
    from ovos_utils.log import log_deprecation
    log_deprecation("import from `chatbot_core.utils.bot_utils` directly",
                    "3.0.0")
    from chatbot_core.utils.bot_utils import clean_up_bot
    return clean_up_bot(*args, **kwargs)


def grammar_check(*args, **kwargs):
    from ovos_utils.log import log_deprecation
    log_deprecation("import from `chatbot_core.utils.bot_utils` directly",
                    "3.0.0")
    from chatbot_core.utils.bot_utils import grammar_check
    return grammar_check(*args, **kwargs)
