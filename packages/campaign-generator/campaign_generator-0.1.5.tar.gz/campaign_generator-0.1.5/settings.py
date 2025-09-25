import os
from pydantic_settings import BaseSettings

class ClickUpSettings(BaseSettings):
    clickup_api_key: str
    clickup_team_id: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class LocalSettings(BaseSettings):
    research_output_dir: str = "research output"
    question_output_dir: str = "question output"
    audio_output_dir: str = "audio output"
    transcripts_output_dir: str = "transcripts output"
    content_generation_dir: str = "content generation"