"""
MailWorks - Universal Email Sender Package

A Python package for sending emails using any SMTP server with STARTTLS support.
Works with Gmail, Outlook, Yahoo, ProtonMail, and any custom SMTP provider.
Defaults to Gmail settings for convenience.
"""

from .mail_sender import MailSender
from .exceptions import EmailSenderError, AuthenticationError, SendError, ConfigurationError

# Backward compatibility
GmailSender = MailSender

__version__ = "2.1.0"
__author__ = "Antonio Costa"

__all__ = [
    "MailSender",
    "GmailSender",  # For backward compatibility
    "EmailSenderError",
    "AuthenticationError",
    "SendError",
    "ConfigurationError"
]
