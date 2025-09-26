import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from dotenv import load_dotenv

load_dotenv()

sender=''
pw=''
def login(yourID=None,password=None):
    """
    check id,pw are correct
    store id,pw
    """
    global sender
    global pw

    if yourID is None:
        yourID = os.getenv("KAKAO_ID")
    if password is None:
        password = os.getenv("KAKAO_PASSWORD")

    if yourID is None or password is None:
        print("KakaoMail: ID or Password not provided. Please provide them as arguments or set KAKAO_ID and KAKAO_PASSWORD environment variables.")
        return False
    
    sender=yourID+'@kakao.com'
    pw=password
    
    s=smtplib.SMTP_SSL("smtp.kakao.com",465)
    try:
        s.login( sender , pw ) 
        s.quit()
        return True
    except:
        print('KakaoMail: Failed to login')
        s.quit()
        return False
    
    
def send(recipient,subject,text, subtype='plain', attachments=None):
    print('KakaoMail:\n\t'+'From: '+sender+
        '\tTo: '+recipient+
        '\tSubject: '+subject+
        '\tText:'+text)
    
    if attachments:
        msg = MIMEMultipart()
        msg.attach(MIMEText(text.encode('utf-8'), _subtype=subtype, _charset='utf-8'))

        for file_path in attachments:
            try:
                with open(file_path, 'rb') as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(file_path)}"')
                msg.attach(part)
            except FileNotFoundError:
                print(f"KakaoMail: Attachment file not found: {file_path}")
                return
            except Exception as e:
                print(f"KakaoMail: Error attaching file {file_path}: {e}")
                return
    else:
        msg = MIMEText(text.encode('utf-8'), _subtype=subtype, _charset='utf-8')

    msg['Subject'] =subject
    msg['From'] = sender
    msg['To'] = recipient

    s=smtplib.SMTP_SSL("smtp.kakao.com",465)
    s.login( sender , pw ) 
    s.sendmail( sender, recipient, msg.as_string() ) 
    s.quit()
    print('KakaoMail: sent mail')
