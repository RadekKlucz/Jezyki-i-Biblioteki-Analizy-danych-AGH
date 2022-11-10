#!/usr/bin/python
import getpass # taki input ale do hasel czyli nie widac 
import imaplib


imap_port = 993
imap_server = "poczta.agh.edu.pl"
imap_login = "mag@agh.edu.pl"

m = imaplib.IMAP4_SSL(imap_server, imap_port)
m.login(imap_login, getpass.getpass() ) 

status, counts = m.status("Inbox", "(MESSAGES UNSEEN)")

unread = counts[0].split()[4][:-1]
print( "Number of unreaded emails: %s" % int(unread) )
input()


m.select()
typ, data = m.search(None, 'ALL')
for num in data[0].split():
    typ, data = m.fetch(num, '(RFC822)')
    print()
    print('Message %s\n%s\n' % (num, data[0][1]))
    input()
m.close()

m.logout()