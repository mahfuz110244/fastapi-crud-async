import os

from sqlalchemy import (Column, DateTime, Integer, MetaData, String, Table,
                        create_engine, ForeignKey, JSON)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from databases import Database

DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()
notes = Table(
    "notes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(50)),
    Column("description", String(50)),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)

clients = Table(
    "clients",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(100)),
    Column("token", String(255)),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)

ocr_logs = Table(
    "ocr_logs",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("client_id", ForeignKey('clients.id'), index=True),
    # relationship("Client", back_populates="ocr"),
    Column("created_date", DateTime, default=func.now(), nullable=False),
    Column("request_data", JSON),
    Column("response_data", JSON),
    Column("gaze_request_data", JSON),
    Column("gaze_response_data", JSON),
    Column("huawei_request_data", JSON),
    Column("huawei_response_data", JSON),
)
# databases query builder
database = Database(DATABASE_URL)
