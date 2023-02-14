# (c) @AbirHasan2005

from pyrogram.types import Message


def get_media_file_name(message: Message):
    """
    Pass Message object of audio or document or sticker or video or animation to get file_name.
    """

    media = message.audio or \
            message.document or \
            message.sticker or \
            message.video or \
            message.animation

    return media.file_name if media and media.file_name else None


def get_media_file_size(message: Message):
    """
    Pass Message object of audio or document or photo or sticker or video or animation or voice or video_note to get file_size.
    """

    media = message.audio or \
            message.document or \
            message.photo or \
            message.sticker or \
            message.video or \
            message.animation or \
            message.voice or \
            message.video_note

    return media.file_size if media and media.file_size else None


def get_media_mime_type(message: Message):
    """
    Pass Message object of audio or document or video to get mime_type
    """

    media = message.audio or \
            message.document or \
            message.video

    return media.mime_type if media and media.mime_type else None


def get_media_file_id(message: Message):
    """
    Pass Message object of audio or document or photo or sticker or video or animation or voice or video_note to get file_id.
    """

    media = message.audio or \
            message.document or \
            message.photo or \
            message.sticker or \
            message.video or \
            message.animation or \
            message.voice or \
            message.video_note

    return media.file_id if media and media.file_id else None


def get_file_type(message: Message):
    if message.document:
        return "document"
    if message.video:
        return "video"
    if message.audio:
        return "audio"


def get_file_attr(message: Message):

    """
    Combine audio or video or document
    """

    return message.audio or message.video or message.document


def get_thumb_file_id(message: Message):
    media = message.audio or \
            message.video or \
            message.document
    return media.thumbs[0].file_id if media and media.thumbs else None
