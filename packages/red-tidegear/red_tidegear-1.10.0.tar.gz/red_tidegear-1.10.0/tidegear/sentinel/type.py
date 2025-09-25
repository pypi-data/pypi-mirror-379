# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0.
# If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.
# © 2025 cswimr

"""Defines the base class for Sentinel moderation types."""

from types import CoroutineType
from typing import TYPE_CHECKING, Any, Callable, Mapping

from class_registry.registry import ClassRegistry
from discord import Member, Permissions, Thread, User, abc
from discord.utils import MISSING
from redbot.core import commands
from typing_extensions import override

from tidegear.utils import class_overrides_attribute

if TYPE_CHECKING:
    from tidegear.sentinel.cog import SentinelCog
    from tidegear.sentinel.db.tables import Moderation


class ModerationType:
    r"""This is a base class for Sentinel moderation types.

    Example:
        ```python
        from discord import Member, Permissions, User
        from redbot.core import commands
        from typing_extensions import override

        from tidegear import chat_formatting as cf
        from tidegear.sentinel import SentinelCog, Moderation, PartialGuild, PartialUser, ModerationType


        class Warn(ModerationType):
            key = "warn"
            string = "warn"
            verb = "warned"
            permissions = Permissions(moderate_members=True)

            @override
            @classmethod
            async def user_target_handler(cls, ctx: commands.Context, target: User | Member, reason: str) -> Moderation:
                assert ctx.guild
                response = await ctx.send(
                    content=f"{target.mention} has {cls.embed_desc}{cls.verb}!\n{cf.bold(text='Reason')} - {cf.inline(text=reason)}"
                )

                partial_target = await PartialUser.upsert(user=target)
                partial_moderator = await PartialUser.upsert(user=ctx.author)
                partial_guild = await PartialGuild.upsert(guild=ctx.guild)
                moderation = Moderation(
                    _data={
                        Moderation.guild_id: partial_guild.id,
                        Moderation.type_key: cls.key,
                        Moderation.target_user_id: partial_target.id,
                        Moderation.moderator_id: partial_moderator.id,
                        Moderation.reason: reason,
                    }
                )
                await moderation.save()
                await response.edit(
                    content=(
                        f"{target.mention} has {cls.embed_desc}{cls.verb}! (Case: {cf.inline(f'#{moderation.id:,}')})"
                        f"\n{cf.bold(text='Reason:')} {cf.inline(text=reason)}"
                    )
                )
                return moderation

            @override
            @classmethod
            async def resolve_handler(cls, cog: SentinelCog, moderation: Moderation) -> None:
                return
        ```

    Attributes:
        key: The key to use for this type. This should be unique, as this is how the type is registered internally.
            Changing this key will break existing cases with this type.
            Defaults to `type`.
        string: The string to display for this type. Defaults to `type`.
        verb: The verb to use for this type. Defaults to `typed`.
        embed_desc: The string to use for embed descriptions. Defaults to `been `.
        removes_from_guild: Whether this type's handler removes the target from the guild,
            or if the moderation is expected to occur whenever the user is not in the guild.
            This does not actually remove the target from the guild; the handler method is responsible for that.
            **Moderation types that remove users from guilds are responsible for contacting users using the
            [`SentinelCog.contact_target`][tidegear.sentinel.SentinelCog.contact_target] method *before* removing them from the guild.**
            Defaults to `False`.
        permissions: The Discord permissions required for this type's moderation handler to function.
            Defaults to [`Permissions.none`][discord.Permissions.none].
        history_metadata: A mapping of metadata keys to make visible in the output of [`SentinelCog.history`][tidegear.sentinel.SentinelCog.history].
            Values will be passed through the given function before being output in history,
            to allow for storing raw values and then formatting them later. Defaults to [`dict`][].
    """

    key: str = "type"
    string: str = "type"
    verb: str = "typed"
    embed_desc: str = "been "
    removes_from_guild: bool = False
    permissions: Permissions = Permissions.none()
    history_metadata: Mapping[str, Callable[[str], str]] = {}

    @property
    def can_edit_duration(self) -> bool:
        """Check whether or not this type overrides the `edit_duration_handler` method.

        Returns:
            If this type supports editing the duration of moderations.
        """
        return class_overrides_attribute(child=type(self), parent=ModerationType, attribute="duration_edit_handler")

    @property
    def can_expire(self) -> bool:
        """Check whether or not this type overrides the `expiry_handler` method.

        Returns:
            If this type supports moderation expiry.
        """
        return class_overrides_attribute(child=type(self), parent=ModerationType, attribute="expiry_handler")

    @property
    def can_target_channels(self) -> bool:
        """Check whether or not this type overrides the `channel_target_handler` method.
        Consider using [`.handler`][tidegear.sentinel.ModerationType.handler] instead
        if you just want to retrieve the correct handler for a [`User`][discord.User] or [`GuildChannel`][discord.abc.GuildChannel] object.

        Returns:
            If this type supports targeting channels.
        """
        return class_overrides_attribute(child=type(self), parent=ModerationType, attribute="channel_target_handler")

    @property
    def can_target_members(self) -> bool:
        """Check whether or not this type overrides the `member_target_handler` method.
        Consider using [`.handler`][tidegear.sentinel.ModerationType.handler] instead
        if you just want to retrieve the correct handler for a [`User`][discord.User] or [`GuildChannel`][discord.abc.GuildChannel] object.

        Returns:
            If this type supports targeting users.
        """
        return class_overrides_attribute(child=type(self), parent=ModerationType, attribute="member_target_handler")

    @property
    def can_target_users(self) -> bool:
        """Check whether or not this type overrides the `user_target_handler` method.
        Consider using [`.handler`][tidegear.sentinel.ModerationType.handler] instead
        if you just want to retrieve the correct handler for a [`User`][discord.User] or [`GuildChannel`][discord.abc.GuildChannel] object.

        Returns:
            If this type supports targeting users.
        """
        return class_overrides_attribute(child=type(self), parent=ModerationType, attribute="user_target_handler")

    @property
    def is_resolvable(self) -> bool:
        """Check whether or not this type overrides the `resolve_handler` method.

        Returns:
            If this type supports being resolved.
        """
        return class_overrides_attribute(child=type(self), parent=ModerationType, attribute="resolve_handler")

    @property
    def name(self) -> str:
        """Returns the string to display for this type. This is an alias for the `string` attribute."""
        return self.string

    @override
    def __str__(self) -> str:
        """Return the value of `self.string`."""
        return self.string

    @override
    def __repr__(self) -> str:
        attrs = [
            ("key", self.key),
            ("removes_from_guild", self.removes_from_guild),
        ]
        joined = " ".join(f"{key}={value!r}" for key, value in attrs)
        return f"<{self.__class__.__name__} {joined}>"

    def handler(self, target: Member | User | abc.GuildChannel | Thread) -> "Callable[..., CoroutineType[Any, Any, Moderation]]":
        """Returns the proper handler method for the given target type.

        Example:
            ```python
            # assuming `ctx` is a `commands.Context` object,
            # this runs the `user_target_handler` for the `Warn` type if it is defined.
            await Warn().handler(target=ctx.author)(ctx=ctx, target=target)
            ```

        Args:
            target: The target you'd like to retrieve the handler for.

        Raises:
            TypeError: Raised if the type does not support targeting the target type given,
                or if the target type given does not match this method's typehints.

        Returns:
            The resulting handler method.
        """
        if isinstance(target, (Member, User)):
            if isinstance(target, Member) and self.can_target_members:
                return self.member_target_handler
            if not self.can_target_users:
                if isinstance(target, User) and self.can_target_members:
                    msg = f"Moderation type {self.__class__.__name__} only supports targeting members of the current guild!"
                else:
                    msg = f"Moderation type {self.__class__.__name__} does not support targeting users!"
                raise TypeError(msg)
            return self.user_target_handler

        if isinstance(target, (abc.GuildChannel, Thread)):
            if not self.can_target_channels:
                msg = f"Moderation type {self.__class__.__name__} does not support targeting channels!"
                raise TypeError(msg)
            return self.channel_target_handler

        msg = f"Type {type(target).__name__} is an invalid target type!"
        raise TypeError(msg)

    @classmethod
    async def member_target_handler(
        cls, *, cog: "SentinelCog", ctx: commands.Context, target: Member, silent: bool = MISSING, **kwargs: Any
    ) -> "Moderation":
        """This method should be overridden by any child classes that can target members but **not** users,
        and should retain the same starting keyword arguments.
        If your child class can target people outside of the current guild,
        consider using [`.user_target_handler`][tidegear.sentinel.ModerationType.user_target_handler] instead.

        Args:
            cog: A cog instance of a Sentinel cog.
            ctx: The context of the command.
            target: The target of the moderation.
            silent: Whether or not to direct message the user.
                This will be ignored if the type has [`removes_from_guild`][tidegear.sentinel.ModerationType] set to `False`.
            **kwargs (dict[str, Any]): Any additional keyword arguments;
                will be passed in by the [`SentinelCog.moderate`][tidegear.sentinel.SentinelCog.moderate] function.

        Returns:
            The resulting moderation.
        """
        raise NotImplementedError

    @classmethod
    async def user_target_handler(
        cls, *, cog: "SentinelCog", ctx: commands.Context, target: Member | User, silent: bool = MISSING, **kwargs: Any
    ) -> "Moderation":
        """This method should be overridden by any child classes that can target users, but should retain the same starting keyword arguments.

        Args:
            cog: A cog instance of a Sentinel cog.
            ctx: The context of the command.
            target: The target of the moderation.
            silent: Whether or not to direct message the user.
                This will be ignored if the type has [`removes_from_guild`][tidegear.sentinel.ModerationType] set to `False`.
            **kwargs (dict[str, Any]): Any additional keyword arguments;
                will be passed in by the [`SentinelCog.moderate`][tidegear.sentinel.SentinelCog.moderate] function.

        Returns:
            The resulting moderation.
        """
        raise NotImplementedError

    @classmethod
    async def channel_target_handler(
        cls, *, cog: "SentinelCog", ctx: commands.Context, target: abc.GuildChannel | Thread, **kwargs: Any
    ) -> "Moderation":
        """This method should be overridden by any child classes that can target channels or threads,
            but should retain the same starting keyword arguments.

        Args:
            cog: A cog instance of a Sentinel cog.
            ctx: The context of the command.
            target: The target of the moderation.
            **kwargs (dict[str, Any]): Any additional keyword arguments;
                will be passed in by the [`SentinelCog.moderate`][tidegear.sentinel.SentinelCog.moderate] function.

        Returns:
            The resulting moderation.
        """
        raise NotImplementedError

    @classmethod
    async def resolve_handler(cls, cog: "SentinelCog", moderation: "Moderation") -> None:
        """This method should be overridden by any resolvable child classes, but should retain the same keyword arguments.
            If your moderation type should not be resolvable, do not override this.
            This handler should be called after the moderation is marked as resolved within the database.

        Args:
            cog: A cog instance of a Sentinel cog.
            moderation: The moderation being resolved.
        """
        raise NotImplementedError

    @classmethod
    async def expiry_handler(cls, cog: "SentinelCog", moderation: "Moderation") -> None:
        """This method should be overridden by any expirable child classes, but should retain the same keyword arguments.
            If your moderation type should not expire, do not override this.

        Args:
            cog: A cog instance of a Sentinel cog.
            moderation: The moderation that is expiring.
        """
        raise NotImplementedError

    @classmethod
    async def duration_edit_handler(cls, ctx: commands.Context, old_moderation: "Moderation", new_moderation: "Moderation") -> None:
        """This method should be overridden by any child classes with editable durations, but should retain the same keyword arguments.
            If your moderation type's duration should not be editable, do not override this.

        Args:
            ctx: The context that triggered the duration edit.
            old_moderation: The old moderation, from before the `/edit` command was invoked.
            new_moderation: The current state of the moderation.
        """
        raise NotImplementedError


moderation_type_registry: ClassRegistry[ModerationType] = ClassRegistry(attr_name="key", unique=True)
""""""
