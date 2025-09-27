"""
Email Sender Package

A Python package for sending emails using Gmail SMTP.
"""

from .gmail_sender import GmailSender
from .exceptions import EmailSenderError, AuthenticationError, SendError, ConfigurationError

__version__ = "1.0.0"
__author__ = "Antonio Costa"

__all__ = [
    "GmailSender",
    "EmailSenderError",
    "AuthenticationError",
    "SendError",
    "ConfigurationError"
]
