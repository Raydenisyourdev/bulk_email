# Bulk_emails
A simple Python script for sending emails automatically through Gmail using SMTP.
I built this project to experiment with email automation in Python. It lets you configure the recipient, subject, message and number of emails to send without having to modify the actual sending logic.

What it does
- Sends emails through Gmail.
- Lets you set how many emails to send in one execution.
- Allows you to customize the subject and message.
- Stops automatically if an error occurs.


## Getting started

### 1. Clone the repository

```bash
git clone <https://github.com/Raydenisyourdev/bulk_email.git>
cd Bulk_emails
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

```powershell
# Windows
.\venv\Scripts\Activate.ps1
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the root directory:

```env
SENDER_EMAIL=your_email@gmail.com
APP_PASSWORD=your_app_password
RECEIVER_EMAIL=recipient@gmail.com
```


**Note:** Gmail SMTP authentication requires an App Password for eligible accounts. If your account doesn't support App Passwords, you'll need to use Gmail API with OAuth 2.0 instead.But first tebu check if 2fa is enabled. If disabled, Enable it 

## Customizing your emails

You can configure the email settings directly in `main.py`:

```python
EMAIL_LIMIT = 3

SUBJECT = "Your subject"

BODY = """
Your message goes here.
"""

```

- `EMAIL_LIMIT` determines how many emails the script sends.
- `SUBJECT` sets the email subject.
- `BODY` contains the actual message.
- `DELAY` sets the waiting time between emails, in seconds.

## Running the script

Once everything is configured, run:

```bash
python main.py
```

Built with Python.