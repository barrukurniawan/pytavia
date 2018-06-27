import pystmark
import json
import time 
import email_message

from core import config
from core import templating

"""
    This is our email library. Currently we use 
        Postmark as our email delivery system
"""
class email:

    def __init__(self):
        pass

    """
        message_key : value of the messages 
        email_data = {
            "name"  : sendee_name,
            "text"  : additional_text
        }
    """
    def send(self, params):
        message_key   = params["message_key"  ]
        email_data    = params["email_data"   ]
        to_email      = params["email_to"     ]
        subject_email = params["email_subject"]
        message_tag   = params["message_tag"  ]

        email_text    = email_message.message[message_key]
        email_return  = templating.Templating.render(
            email_text, email_data
        )

        message = pystmark.Message(
                sender=config.G_POSTMARK_API_SENDER_EMAIL,
                to=to_email,
                subject=subject_email,
                tag=message_tag,
                html=email_return
        )

        message.track_opens = True
        response = pystmark.send(
                message,
                api_key=config.G_POSTMARK_API_SERVER_TOKEN
        )
        # we have to check for failed to send emails and log them 
        json_response = response._data
        print json_response

        
