# SPDX-FileCopyrightText: 2025 cswimr <copyright@csw.im>
# SPDX-License-Identifier: MPL-2.0

from importlib.util import find_spec
from warnings import warn

if not find_spec("redbot_orm"):
    msg = "redbot-orm is not installed, but the `tidegear.sentinel` module was imported! Did you install tidegear with the `sentinel` extra?"
    raise ImportError(msg)

if not find_spec("class_registry"):
    msg = "phx-class-registry is not installed, but the `tidegear.sentinel` module was imported! Did you install tidegear with the `sentinel` extra?"
    raise ImportError(msg)

from .cog import SentinelCog
from .db import AbstractPartial, Change, Moderation, PartialChannel, PartialGuild, PartialUser
from .exceptions import HandlerError, LoggedHandlerError, UpsertError
from .type import ModerationMetadataEntry, ModerationType, moderation_type_registry

__all__ = [
    "AbstractPartial",
    "Change",
    "SentinelCog",
    "Moderation",
    "PartialChannel",
    "PartialGuild",
    "PartialUser",
    "ModerationMetadataEntry",
    "ModerationType",
    "moderation_type_registry",
    "HandlerError",
    "LoggedHandlerError",
    "UpsertError",
]

warn("Tidegear Sentinel is still a heavy work-in-progress, and it has been imported!")
