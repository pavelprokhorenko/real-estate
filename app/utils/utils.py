import smtplib
import ssl

from app.core.config import settings


def send_email(email_to: str, sub: str, msg: str):
    """
    Send email to "receiver_email" with message_text.
    """
    message = f"""\
From: {settings.EMAILS_FROM_NAME}
Subject: {sub}

{msg}
"""
    context = ssl.create_default_context()
    with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.starttls(context=context)
        server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
        server.sendmail(settings.SMTP_USER, email_to, message)


def send_new_account_email(email_to: str, username: str):
    subject = f"{settings.PROJECT_NAME} - new account"
    message = f"""
    You have successfully registered. Congratulations, {username}!
    Go to dashboard - {settings.SERVER_HOST}
    """
    send_email(email_to=email_to, sub=subject, msg=message)
