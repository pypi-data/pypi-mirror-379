"""
Gmail Email Sender

A class for sending emails using Gmail's SMTP server.
"""

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from typing import List, Optional, Union
from pathlib import Path

from .exceptions import AuthenticationError, SendError, ConfigurationError


class GmailSender:
    """
    A class for sending emails using Gmail's SMTP server.

    This class provides a simple interface for sending emails through Gmail
    using SMTP with TLS encryption.
    """

    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587

    def __init__(self, email: Optional[str] = None, password: Optional[str] = None):
        """
        Initialize the Gmail sender.

        Args:
            email: Gmail email address. If not provided, will look for GMAIL_EMAIL env var
            password: Gmail app password. If not provided, will look for GMAIL_PASSWORD env var

        Raises:
            ConfigurationError: If email or password is not provided or found in environment
        """
        self.email = email or os.getenv('GMAIL_EMAIL')
        self.password = password or os.getenv('GMAIL_PASSWORD')

        if not self.email:
            raise ConfigurationError("Gmail email is required. Provide it as parameter or set GMAIL_EMAIL environment variable.")

        if not self.password:
            raise ConfigurationError("Gmail password is required. Provide it as parameter or set GMAIL_PASSWORD environment variable.")

    def send_email(self,
                   to_emails: Union[str, List[str]],
                   subject: str,
                   message: str,
                   html_message: Optional[str] = None,
                   attachments: Optional[List[Union[str, Path]]] = None) -> bool:
        """
        Send an email using Gmail SMTP.

        Args:
            to_emails: Recipient email address(es)
            subject: Email subject
            message: Plain text message body
            html_message: Optional HTML message body
            attachments: Optional list of file paths to attach

        Returns:
            bool: True if email was sent successfully

        Raises:
            AuthenticationError: If Gmail authentication fails
            SendError: If email sending fails
        """
        try:
            # Convert single email to list
            if isinstance(to_emails, str):
                to_emails = [to_emails]

            # Create message
            msg = MIMEMultipart('alternative')
            msg['From'] = self.email
            msg['To'] = ', '.join(to_emails)
            msg['Subject'] = subject

            # Add plain text part
            text_part = MIMEText(message, 'plain')
            msg.attach(text_part)

            # Add HTML part if provided
            if html_message:
                html_part = MIMEText(html_message, 'html')
                msg.attach(html_part)

            # Add attachments if provided
            if attachments:
                for attachment_path in attachments:
                    self._add_attachment(msg, attachment_path)

            # Create SMTP session
            with smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT) as server:
                server.starttls()  # Enable TLS encryption
                try:
                    server.login(self.email, self.password)
                except smtplib.SMTPAuthenticationError as e:
                    raise AuthenticationError(f"Failed to authenticate with Gmail: {str(e)}")

                # Send email
                text = msg.as_string()
                server.sendmail(self.email, to_emails, text)

            return True

        except AuthenticationError:
            raise
        except Exception as e:
            raise SendError(f"Failed to send email: {str(e)}")

    def _add_attachment(self, msg: MIMEMultipart, file_path: Union[str, Path]) -> None:
        """
        Add an attachment to the email message.

        Args:
            msg: The email message object
            file_path: Path to the file to attach

        Raises:
            SendError: If attachment cannot be added
        """
        try:
            file_path = Path(file_path)

            if not file_path.exists():
                raise SendError(f"Attachment file not found: {file_path}")

            with open(file_path, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())

            # Encode file in ASCII characters to send by email
            encoders.encode_base64(part)

            # Add header as key/value pair to attachment part
            part.add_header(
                'Content-Disposition',
                f'attachment; filename= {file_path.name}'
            )

            # Attach the part to message
            msg.attach(part)

        except Exception as e:
            raise SendError(f"Failed to add attachment {file_path}: {str(e)}")

    def send_simple_email(self, to_email: str, subject: str, message: str) -> bool:
        """
        Send a simple text email to a single recipient.

        Args:
            to_email: Recipient email address
            subject: Email subject
            message: Plain text message body

        Returns:
            bool: True if email was sent successfully
        """
        return self.send_email(to_email, subject, message)

    def test_connection(self) -> bool:
        """
        Test the connection to Gmail SMTP server.

        Returns:
            bool: True if connection and authentication successful

        Raises:
            AuthenticationError: If authentication fails
            SendError: If connection fails
        """
        try:
            with smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT) as server:
                server.starttls()
                server.login(self.email, self.password)
            return True
        except smtplib.SMTPAuthenticationError as e:
            raise AuthenticationError(f"Authentication failed: {str(e)}")
        except Exception as e:
            raise SendError(f"Connection test failed: {str(e)}")
