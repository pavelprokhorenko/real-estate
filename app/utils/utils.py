import smtplib
import ssl

from app.core.config import settings


def send_email(receiver_email: str, sub: str, msg: str):
    """
    Send email to "receiver_email" with message_text.
    """
    message = f"""\
    From: {settings.EMAILS_FROM_NAME}
    Subject: {sub}
    Message: {msg}
    """
    context = ssl.create_default_context()
    with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.starttls(context=context)
        server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
        server.sendmail(settings.SMTP_USER, receiver_email, message)
