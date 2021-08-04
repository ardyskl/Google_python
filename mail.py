#!/usr/bin/env python3

import os
import os.path
from email.message import EmailMessage
import mimetypes

message = EmailMessage()

attachment_path = "flipped_&_resized.png"
attachment_filename = os.path.basename(attachment_path)
mime_type, _ = mimetypes.guess_type(attachment_path)
mime_type, mime_subtype = mime_type.split('/', 1)

# testing
# print(message)

sender = "me@lovegoogle.com"
recipient = "you@lovegoogletoo.com"

message['From'] = sender
message['To'] = recipient

# testing
# print(message)

message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)
# testing
# print(message)

body = """oi oi, mate! You mighty Aussie cunt!


I'm learing to send emails using python mate!"""

message.set_content(body)

with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype, filename=os.path.basename(attachment_path))

print(message)
