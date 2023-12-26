import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart


class Postman:
    GMAIL_SMTP_SERVER = "smtp.gmail.com"
    GMAIL_IMAP_SERVER = "imap.gmail.com"

    def __init__(self, address, password):
        self.address = address
        self.password = password
        self.header = None

    def send_mail(self, recipients: list, subject='Subject', message='Message'):
        msg = MIMEMultipart()
        msg['From'] = self.address
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        send_server = smtplib.SMTP(GMAIL_SMTP_SERVER, 587)
        # identify ourselves to smtp gmail client
        send_server.ehlo()
        # secure our email with tls encryption
        send_server.starttls()
        # re-identify ourselves as an encrypted connection
        send_server.ehlo()
        send_server.login(self.address, self.password)
        send_server.sendmail(self.address, recipients, msg.as_string())
        send_server.quit()

    def receive_mail(self, subject=None):
        rec_server = imaplib.IMAP4_SSL(GMAIL_IMAP_SERVER)
        rec_server.login(self.address, self.password)
        rec_server.list()
        rec_server.select("INBOX")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = rec_server.uid('search', subject, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = rec_server.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        rec_server.logout()
        return email_message


if __name__ == "__main__":
    recipients = ['vasya@email.com', 'petya@email.com']
    postman = Postman('login@gmail.com', 'qwerty')
    postman.send_mail(recipients)
    print(postman.receive_mail())
