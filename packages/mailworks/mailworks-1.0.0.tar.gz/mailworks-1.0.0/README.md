# MailWorks

A Python package for sending emails using Gmail's SMTP server. This package provides a simple, secure, and reliable way to send emails through Gmail with support for HTML content, attachments, and multiple recipients.

## Features

- ✅ Send emails via Gmail SMTP
- ✅ Support for plain text and HTML emails
- ✅ File attachments
- ✅ Multiple recipients
- ✅ Environment variable configuration
- ✅ Configuration file support
- ✅ Connection testing
- ✅ Comprehensive error handling
- ✅ No external dependencies (uses Python standard library only)

## Installation

### From source (development)

```bash
# Clone the repository
git clone https://github.com/antoniocostabr/mailworks.git
cd mailworks

# Install in development mode
pip install -e .

# Or install with development dependencies
pip install -e ".[dev]"
```

### From PyPI (when published)

```bash
pip install mailworks
```

## Gmail Setup

Before using this package, you need to set up Gmail App Passwords:

### Step 1: Enable 2-Factor Authentication

1. Go to [Google Account settings](https://myaccount.google.com/)
2. Navigate to "Security" > "2-Step Verification"
3. Enable 2-Step Verification if not already enabled

### Step 2: Generate App Password

1. Go to [Google Account settings](https://myaccount.google.com/)
2. Navigate to "Security" > "2-Step Verification" > "App passwords"
3. Select "Mail" and your device
4. Generate the app password
5. **Important**: Use this 16-character app password, not your regular Gmail password

## Quick Start

### Basic Usage

```python
from email_sender import GmailSender

# Method 1: Using environment variables
# Set environment variables:
# export GMAIL_EMAIL="your.email@gmail.com"
# export GMAIL_PASSWORD="your_app_password"

sender = GmailSender()

# Send a simple email
success = sender.send_simple_email(
    to_email="recipient@example.com",
    subject="Hello from Python!",
    message="This is a test email sent from Python."
)

if success:
    print("Email sent successfully!")
```

### Advanced Usage

```python
from email_sender import GmailSender

# Method 2: Direct credentials
sender = GmailSender(
    email="your.email@gmail.com",
    password="your_app_password"
)

# Send HTML email with attachments to multiple recipients
success = sender.send_email(
    to_emails=["recipient1@example.com", "recipient2@example.com"],
    subject="Advanced Email Example",
    message="Plain text version of the email.",
    html_message="""
    <html>
        <body>
            <h2>Hello!</h2>
            <p>This is an <b>HTML email</b> with formatting.</p>
        </body>
    </html>
    """,
    attachments=["document.pdf", "image.png"]
)
```

## Configuration Options

### 1. Environment Variables

Set these environment variables:

```bash
export GMAIL_EMAIL="your.email@gmail.com"
export GMAIL_PASSWORD="your_app_password"
export GMAIL_SMTP_SERVER="smtp.gmail.com"  # Optional
export GMAIL_SMTP_PORT="587"               # Optional
```

### 2. Configuration File

Create a config file (e.g., `gmail_config.txt`):

```
GMAIL_EMAIL=your.email@gmail.com
GMAIL_PASSWORD=your_app_password
GMAIL_SMTP_SERVER=smtp.gmail.com
GMAIL_SMTP_PORT=587
```

Use it in your code:

```python
from email_sender.config import ConfigManager

config_manager = ConfigManager.from_file("gmail_config.txt")
sender = GmailSender(
    email=config_manager.config.email,
    password=config_manager.config.password
)
```

### 3. Direct Parameters

```python
from email_sender import GmailSender

sender = GmailSender(
    email="your.email@gmail.com",
    password="your_app_password"
)
```

## API Reference

### GmailSender Class

#### Constructor

```python
GmailSender(email=None, password=None)
```

- `email` (str, optional): Gmail email address. If not provided, reads from `GMAIL_EMAIL` environment variable.
- `password` (str, optional): Gmail app password. If not provided, reads from `GMAIL_PASSWORD` environment variable.

#### Methods

##### `send_email(to_emails, subject, message, html_message=None, attachments=None)`

Send an email with advanced options.

**Parameters:**
- `to_emails` (str or list): Recipient email address(es)
- `subject` (str): Email subject
- `message` (str): Plain text message body
- `html_message` (str, optional): HTML message body
- `attachments` (list, optional): List of file paths to attach

**Returns:** `bool` - True if successful

##### `send_simple_email(to_email, subject, message)`

Send a simple text email to a single recipient.

**Parameters:**
- `to_email` (str): Recipient email address
- `subject` (str): Email subject
- `message` (str): Plain text message body

**Returns:** `bool` - True if successful

##### `test_connection()`

Test the connection to Gmail SMTP server.

**Returns:** `bool` - True if connection successful

### Exception Classes

- `EmailSenderError`: Base exception class
- `AuthenticationError`: Raised when Gmail authentication fails
- `SendError`: Raised when email sending fails
- `ConfigurationError`: Raised when configuration is invalid

## Examples

See the `examples/` directory for complete working examples:

- `basic_example.py`: Simple email sending using environment variables
- `advanced_example.py`: HTML emails with attachments and multiple recipients
- `config_example.py`: Different configuration methods

## Error Handling

```python
from email_sender import GmailSender, AuthenticationError, SendError

try:
    sender = GmailSender()
    sender.test_connection()
    
    success = sender.send_simple_email(
        to_email="recipient@example.com",
        subject="Test Email",
        message="Hello, World!"
    )
    
except AuthenticationError as e:
    print(f"Authentication failed: {e}")
    print("Check your email and app password")
    
except SendError as e:
    print(f"Failed to send email: {e}")
    
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Security Best Practices

1. **Use App Passwords**: Never use your regular Gmail password. Always use Gmail App Passwords.

2. **Environment Variables**: Store credentials in environment variables, not in your code.

3. **Config Files**: If using config files, add them to `.gitignore` to avoid committing credentials.

4. **Permissions**: Keep your app passwords secure and rotate them regularly.

## Common Issues & Solutions

### Authentication Error (535)

**Problem**: `smtplib.SMTPAuthenticationError: (535, '5.7.8 Username and Password not accepted')`

**Solutions**:
- Ensure you're using an App Password, not your regular Gmail password
- Check that 2-Factor Authentication is enabled on your Gmail account
- Verify the email address is correct
- Try generating a new App Password

### Connection Issues

**Problem**: Connection timeouts or failures

**Solutions**:
- Check your internet connection
- Ensure port 587 is not blocked by your firewall
- Try using a different network
- Verify Gmail SMTP settings

### File Attachment Issues

**Problem**: Attachments not working

**Solutions**:
- Check that file paths exist and are accessible
- Ensure files are not too large (Gmail has a 25MB limit)
- Verify file permissions

## Development

### Running Examples

```bash
# Set your credentials
export GMAIL_EMAIL="your.email@gmail.com"
export GMAIL_PASSWORD="your_app_password"

# Run examples
python examples/basic_example.py
python examples/advanced_example.py
python examples/config_example.py
```

### Testing

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests (when available)
pytest

# Code formatting
black email_sender/
black examples/

# Type checking
mypy email_sender/
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions:

1. Check the [Common Issues](#common-issues--solutions) section
2. Look at the [examples](examples/) for usage patterns
3. Open an issue on [GitHub](https://github.com/antoniocostabr/mailworks/issues)

## Changelog

### v1.0.0
- Initial release
- Gmail SMTP support
- HTML email support
- File attachments
- Multiple recipients
- Configuration management
- Comprehensive error handling