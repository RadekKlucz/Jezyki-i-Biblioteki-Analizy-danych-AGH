#!/usr/bin/env python3
"""
Prototype client for simple monitoring purposes.
"""
import os
import time
import traceback
import xmpp
import getpass


def handle_messages(client, stanza):
    """
    Handler which executes given commands from authorized jids.
    """
    sender = stanza.getFrom()
    print('sender :',sender)
    message_type = stanza.getType()
    if any([sender.bareMatch(x) for x in AUTHORIZED_JIDS]):
        command = stanza.getBody()
        if command:
          print('cmd :',command)
          message = "odp na "+command
          client.send(xmpp.Message(sender, message, typ=message_type))


def handle_presences(client, stanza):
    """
    Handler which automatically authorizes subscription requests
    from authorized jids.
    """
    sender = stanza.getFrom()
    presence_type = stanza.getType()
    if presence_type == "subscribe":
        if any([sender.bareMatch(x) for x in AUTHORIZED_JIDS]):
            client.send(xmpp.Presence(to=sender, typ="subscribed"))


def run_client(client_jid, client_password):
    """
    Initializes and runs a fresh xmpp client (blocking).
    """
    # Initialize and connect the client.
    jid = xmpp.JID(client_jid)
    client = xmpp.Client(jid.domain,debug=[])
    if not client.connect():
        return

    # Authenticate.
    if not client.auth(jid.node, client_password, jid.resource):
        return

    # Register the message handler which is used to respond
    # to messages from the authorized contacts.
    client.RegisterHandler("message", handle_messages)

    # Register the presence handler which is used to automatically
    # authorize presence-subscription requests from authorized contacts.
    client.RegisterHandler("presence", handle_presences)

    # Go "online".
    client.sendInitPresence()
    client.Process()

    client.send(xmpp.Message("mag@jabbim.pl", 'Hello mag', typ='chat'))

    while client.isConnected():
        # Handle stanzas and sleep.
        client.Process()
        time.sleep(1)


if __name__ == "__main__":
    CLIENT_JID = "home@jabbim.pl"
    CLIENT_PASSWORD = getpass.getpass() 
    AUTHORIZED_JIDS = ["mag@jabbim.pl"]

    # Loop until the program is terminated.
    # In case of connection problems and/or exceptions, the client is
    # run again after a delay.
    while True:
        print( "Trying to connect ...")
        try:
          run_client(CLIENT_JID, CLIENT_PASSWORD)
        except Exception:
          print ("Caught exception!")
          traceback.print_exc()
        print( "Not connected - attempting reconnect in a moment.")
        time.sleep(10)
