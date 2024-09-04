import datetime
import logging
import traceback
from datetime import datetime
from typing import Text

import uuid
# from flask_validator import ValidateEmail, ValidateString, ValidateCountry
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Text, Float, TIMESTAMP, JSON, Table
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.dialects.postgresql import UUID, JSON
from sqlalchemy.orm import relationship, validates
from sqlalchemy.sql import func

from wiz_server import db

# Association Table for Paper and Tag (Many-to-Many Relationship)
paper_tags = Table(
    'paper_tags',
    db.metadata,
    Column('paper_id', UUID(as_uuid=True),
           ForeignKey('papers.id'), primary_key=True),
    Column('tag_id', UUID(as_uuid=True),
           ForeignKey('tags.id'), primary_key=True),
    Column('created_at', TIMESTAMP, server_default=func.now())
)


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    username = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(
        TIMESTAMP, server_default=func.now(), onupdate=func.now())

    # @classmethod
    # def __declare_last__(cls):
    #     ValidateEmail(User.email, True, True, "The email is not valid. Please check it")
    #     ValidateString(User.username, True, True, "The username type must be string")

    @validates('username')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value

    visualizations = relationship("Visualization", back_populates="user")


class Paper(db.Model, SerializerMixin):
    __tablename__ = 'papers'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(500), nullable=False)
    abstract = Column(Text)
    publication_year = Column(Integer, nullable=False)
    journal_id = Column(UUID(as_uuid=True), ForeignKey(
        'journals.id'), nullable=False)
    category_id = Column(UUID(as_uuid=True), ForeignKey(
        'categories.id'), nullable=False)
    doi = Column(String(255), unique=True, nullable=False)
    authors = Column(String(500))
    citation_count = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(
        TIMESTAMP, server_default=func.now(), onupdate=func.now())

    journal = relationship("Journal", back_populates="papers")
    category = relationship("Category", back_populates="papers")
    tags = relationship("Tag", secondary=paper_tags, back_populates="papers")


class Journal(db.Model, SerializerMixin):
    __tablename__ = 'journals'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    impact_factor = Column(Float)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(
        TIMESTAMP, server_default=func.now(), onupdate=func.now())

    papers = relationship("Paper", back_populates="journal")


class Category(db.Model, SerializerMixin):
    __tablename__ = 'categories'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(
        TIMESTAMP, server_default=func.now(), onupdate=func.now())

    papers = relationship("Paper", back_populates="category")


class Visualization(db.Model, SerializerMixin):
    __tablename__ = 'visualizations'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey(
        'users.id'), nullable=False)
    type = Column(String(50), nullable=False)
    config = Column(JSON)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(
        TIMESTAMP, server_default=func.now(), onupdate=func.now())

    user = relationship("User", back_populates="visualizations")


class Tag(db.Model, SerializerMixin):
    __tablename__ = 'tags'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(
        TIMESTAMP, server_default=func.now(), onupdate=func.now())

    papers = relationship("Paper", secondary=paper_tags, back_populates="tags")
