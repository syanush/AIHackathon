"""
Main Chainlit application for AIHackathon conversational interface.
"""
import os
from typing import Dict, List
import chainlit as cl
from chainlit.types import AskFileResponse
from dotenv import load_dotenv
from sqlalchemy.orm import Session

# Load environment variables
load_dotenv()

# Import database models
from app.models.models import User, Conversation, Message
from app.database.connection import get_db

# Get database session
db_generator = get_db()
db: Session = next(db_generator)


@cl.on_chat_start
async def on_chat_start():
    """Initialize the chat session when a user starts a conversation."""
    # Send initial message
    await cl.Message(
        content="Welcome to AIHackathon! How can I help you today?",
        author="AIHackathon Bot"
    ).send()
    
    # Initialize conversation in database
    try:
        # In a real app, you'd get the user from auth context
        user = db.query(User).filter(User.username == 'demo_user').first()
        if not user:
            user = User(username='demo_user', email='demo@example.com')
            db.add(user)
            db.commit()
            db.refresh(user)
        
        conversation = Conversation(user_id=user.id, title="New Conversation")
        db.add(conversation)
        db.commit()
        
        # Store conversation ID in session
        cl.user_session.set("conversation_id", str(conversation.id))
        cl.user_session.set("user_id", str(user.id))
        
    except Exception as e:
        print(f"Error initializing conversation: {e}")
        # Log error but continue with chat


@cl.on_message
async def on_message(message: cl.Message):
    """Handle incoming user messages."""
    # Get conversation ID from session
    conversation_id = cl.user_session.get("conversation_id")
    
    # Store message in database
    try:
        db_message = Message(
            conversation_id=conversation_id,
            role="user",
            content=message.content
        )
        db.add(db_message)
        db.commit()
    except Exception as e:
        print(f"Error storing message: {e}")
    
    # Process the message (in a real app, you'd call your AI model here)
    response_content = f"You said: {message.content}\n\nThis is a demo response. In a real application, this would be processed by an AI model."
    
    # Send response
    response = cl.Message(content=response_content)
    await response.send()
    
    # Store response in database
    try:
        db_response = Message(
            conversation_id=conversation_id,
            role="assistant",
            content=response_content
        )
        db.add(db_response)
        db.commit()
    except Exception as e:
        print(f"Error storing response: {e}")


@cl.on_chat_end
async def on_chat_end():
    """Clean up when the chat session ends."""
    # Close the database session
    # This is a bit simplistic - in production you'd want proper session management
    try:
        db.close()
    except Exception as e:
        print(f"Error closing database session: {e}")
