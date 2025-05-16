"""Pydantic schemas for data validation and serialization."""

from uuid import UUID
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field


# User schemas
class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: UUID
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


# Message schemas
class MessageBase(BaseModel):
    role: str
    content: str


class MessageCreate(MessageBase):
    conversation_id: UUID


class MessageResponse(MessageBase):
    id: UUID
    conversation_id: UUID
    created_at: datetime
    
    class Config:
        from_attributes = True


# Conversation schemas
class ConversationBase(BaseModel):
    title: Optional[str] = "New Conversation"


class ConversationCreate(ConversationBase):
    user_id: UUID


class ConversationResponse(ConversationBase):
    id: UUID
    user_id: UUID
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class ConversationWithMessages(ConversationResponse):
    messages: List[MessageResponse] = []
    
    class Config:
        from_attributes = True


# Health check schema
class HealthCheck(BaseModel):
    status: str
    timestamp: datetime = Field(default_factory=datetime.now)
    version: str = "0.1.0"
    database_connected: bool
