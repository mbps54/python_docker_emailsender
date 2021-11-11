#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Script send an email using MS Exchange server to a defined address list.
# There are 8 system environments needed for this script.

import os
import time
from sys import argv
from exchangelib import DELEGATE, Account, Credentials, Message, Mailbox, Configuration
from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter

BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter

POSTSERVER = str(os.environ.get("POST_SERVER"))  # Ex: 'mail.hogwarts.com'
POSTDOMAIN = str(os.environ.get("POST_DOMAIN"))  # Ex: 'GRYFFINDOR'
POSTUSERNAME = str(os.environ.get("POST_USERNAME"))  # Ex: 'harry.potter'
POSTPASSWORD = str(os.environ.get("POST_PASSWORD"))  # Ex: 'Caput.Draconis'
POSTFROMADDRESS = str(os.environ.get("POST_FROM_ADDRESS"))  # Ex: 'harry.potter@hogwarts.com'
POSTTOADDRESS = str(os.environ.get("POST_TO_ADDRESS_LIST"))  # Ex: 'hermione.granger@hogwarts.com'
POSTSUBJECT = str(os.environ.get("POST_SUBJECT"))  # Ex: 'Philosopher's Stone'
POSTMESSAGE = str(os.environ.get("POST_MESSAGE"))  # Ex: 'Dear Hermione, Thank you for ...'


def send_mail(receiver_address: str, subject: str, mail_content: str) -> None:
    # function send email, using exchangelib module and input parameters
    credentials = Credentials(
        username=POSTDOMAIN + "\\" + POSTUSERNAME, password=POSTPASSWORD
    )
    config = Configuration(server=POSTSERVER, credentials=credentials)

    a = Account(
        primary_smtp_address=POSTFROMADDRESS,
        autodiscover=False,
        config=config,
        access_type=DELEGATE,
    )

    m = Message(
        account=a,
        subject=subject,
        body=mail_content,
        to_recipients=[Mailbox(email_address=receiver_address)],
    )
    m.send_and_save()
    print('E-mail have been sent to {}'.format(POSTTOADDRESS))


if __name__ == "__main__":
    receiver_addresses = list(POSTTOADDRESS.split(","))
    for receiver_address in receiver_addresses:
        send_mail(receiver_address, POSTSUBJECT, POSTMESSAGE)
