# import smtplib
# from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
import io

from .get_smtp_server import get_smtp_server

def send_email(send_from, send_to, subject, message, signature=None, cc=None, bcc=None, files={},
              server="localhost", port=587, username='', password='',
              use_tls=True):
    """Compose and send email with provided info and attachments.

    Args:
        send_from (str): from name
        send_to (list[str]): to name(s)
        subject (str): message title
        message (str): message body
        files (dict{str:str|obj}): list of file paths to be attached to email
        server (str): mail server host name
        port (int): port number
        username (str): server auth username
        password (str): server auth password
        use_tls (bool): use TLS mode
    """
    
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    
    if cc is not None:
        msg['Cc'] = COMMASPACE.join(cc)
        
    if bcc is not None:
        msg['Bcc'] = COMMASPACE.join(bcc)
        
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    html_msg = MIMEText(message, 'html')
    msg.attach(html_msg)

    if signature != None:
        sgn = MIMEText(signature, "html")
        msg.attach(sgn)

    for filename in files:
        part = MIMEBase('application', "octet-stream")

        file_path_obj = files[filename]

        if isinstance(file_path_obj, io.BytesIO):
            part.set_payload(file_path_obj.getvalue())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',
                            f'attachment; filename={filename}')
        else:
            with open(file_path_obj, 'rb') as file:
                part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',
                            f'attachment; filename={filename}')
        msg.attach(part)

    smtp = get_smtp_server(server, port)
    if use_tls:
        smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()
     
    print(f'[smtp]: email sent successfully to {str(send_to)}!')