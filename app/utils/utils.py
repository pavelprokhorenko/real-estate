import smtplib
import ssl

from app.core.config import settings


def send_email(email_to: str, email_subject: str, email_message: str) -> None:
    """
    Send email to "receiver_email" with message_text.
    """
    message = (
        f"From: {settings.EMAILS_FROM_NAME}\n"
        f"Subject: {email_subject}\n"
        f"{email_message}"
    )
    context = ssl.create_default_context()
    with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.starttls(context=context)
        server.login(user=settings.SMTP_USER, password=settings.SMTP_PASSWORD)
        server.sendmail(from_addr=settings.SMTP_USER, to_addrs=email_to, msg=message)


def send_new_account_email(email_to: str, username: str) -> None:
    """
    Send email to new user.
    """
    subject = f"{settings.PROJECT_NAME} - new account"
    message = (
        f"You have successfully registered. Congratulations, {username}!\n"
        f"Go to dashboard - {settings.SERVER_HOST}"
    )
    send_email(email_to=email_to, email_subject=subject, email_message=message)
