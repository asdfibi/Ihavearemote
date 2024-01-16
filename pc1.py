import imaplib

user = 'htn45565'
passw = 'dytbb138186'
imap_server = "imap.163.com"
imap_port = 993
imap_connection = imaplib.IMAP4_SSL(imap_server, imap_port)
imap_connection.login(user, passw)
folder = 'INBOX'
imap_connection.select(folder)
response,messages=imap_connection.search(None,'ALL')
for num in messages[0].split():
    response,data=imap_connection.fetch(num,'(RFC822)')
    raw_email=data[0][1].decode('utf-8')
    print(raw_email)
imap_connection.close()
imap_connection.logout()
