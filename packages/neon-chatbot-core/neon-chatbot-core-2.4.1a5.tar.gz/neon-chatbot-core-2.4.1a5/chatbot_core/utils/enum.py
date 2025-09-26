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

from enum import IntEnum
from neon_data_models.enum import CcaiState as ConversationState


class ConversationControls:
    RESP = " asks us to consider:"
    DISC = "Please Discuss"
    VOTE = "Voting on the response to "
    PICK = "Tallying the votes for the responses to "
    NEXT = "I'm ready for the next prompt."
    HIST = "history"
    WAIT = " may respond to the next prompt."


class BotTypes:
    PROCTOR = 'proctor'
    SUBMIND = 'submind'
    OBSERVER = 'observer'
    FACILITATOR = 'facilitator'


CONVERSATION_STATE_ANNOUNCEMENTS = {
    ConversationState.RESP: 'Accepting responses from subminds ({interval} seconds)',
    ConversationState.DISC: 'Discussing responses from subminds ({interval} seconds)',
    ConversationState.VOTE: 'Voting for candidate responses ({interval} seconds)',
    ConversationState.PICK: 'Selecting a winner among participants'
}
