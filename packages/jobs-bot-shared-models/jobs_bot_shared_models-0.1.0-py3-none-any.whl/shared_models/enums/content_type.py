from enum import StrEnum


class ContentType(StrEnum):
    TEXT = "text"
    AUDIO_MESSAGE = "audio_message"
    VIDEO_NOTE = "video_note"
    DOCUMENT = "document"
    ANY = "any"
