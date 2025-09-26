import tgram
from .type_ import Type_

from typing import Optional


class ForumTopic(Type_):
    """
    This object represents a forum topic.

    Telegram documentation: https://core.telegram.org/bots/api#forumtopic

    :param message_thread_id: Unique identifier of the forum topic
    :type message_thread_id: :obj:`int`

    :param name: Name of the topic
    :type name: :obj:`str`

    :param icon_color: Color of the topic icon in RGB format
    :type icon_color: :obj:`int`

    :param icon_custom_emoji_id: Optional. Unique identifier of the custom emoji shown as the topic icon
    :type icon_custom_emoji_id: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.ForumTopic`
    """

    def __init__(
        self,
        message_thread_id: "int" = None,
        name: "str" = None,
        icon_color: "int" = None,
        icon_custom_emoji_id: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.message_thread_id = message_thread_id
        self.name = name
        self.icon_color = icon_color
        self.icon_custom_emoji_id = icon_custom_emoji_id

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ForumTopic"]:
        return (
            ForumTopic(
                me=me,
                json=d,
                message_thread_id=d.get("message_thread_id"),
                name=d.get("name"),
                icon_color=d.get("icon_color"),
                icon_custom_emoji_id=d.get("icon_custom_emoji_id"),
            )
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
