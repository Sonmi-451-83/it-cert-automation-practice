#!/usr/bin/env python3

import email
import mimetypes
import smtplib
import os


def generate_email(sender, recipient, subject, body, attachment_path=None):
    """Creates an email with an attachment."""
    # Basic Email formatting
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    # Process the attachment and add it to the email
    if attachment_path:
      attachment_filename = os.path.basename(attachment_path)
      mime_type, _ = mimetypes.guess_type(attachment_path)
      mime_type, mime_subtype = mime_type.split('/', 1)

      with open(attachment_path, 'rb') as ap:
          message.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype,
                                  filename=attachment_filename)

    return message


def send_email(message):
    """Sends the message to the configured SMTP server."""
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()