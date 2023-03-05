"""Database connection"""
from sqlmodel import create_engine
from .config import settings


engine = create_engine(
    settings.db.uri, # pyright: ignore
    echo=settings.db.echo,  # pytight: ignore
    connect_args=settings.db.connect_args, # pytight: ignore

)
