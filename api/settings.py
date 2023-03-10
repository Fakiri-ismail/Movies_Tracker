from functools import lru_cache

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    # General Settings
    enable_metrics: bool = Field(
        True,
        title="Enable Metrics",
        description="Expose prometheus metrics if set to True (Default: True)",
        env="ENABLE_METRICS",
    )

    # MongoDB Settings
    mongo_connection_string: str = Field(
        "mongodb://localhost:27017",
        title="MongoDB connection String",
        env="MONGODB_CONNECTION_STRING",
    )
    mongo_database_name: str = Field(
        "movie_track_db",
        title="MongoDB Movies Database Name",
        env="MONGODB_DATABASE_NAME",
    )


@lru_cache()
def settings_instance():
    """
    Settings instance to used as a FastAPI dependency.
    """
    return Settings()
