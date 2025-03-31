import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from config import SMTP_SERVER, SMTP_PORT, YOUR_EMAIL, YOUR_APP_PASSWORD, MAIN_RECIPIENT, RECIPIENT_EMAILS

def send_html_email(subject, html_body, attachment_path):
    msg = MIMEMultipart("related")
    msg["Subject"] = subject
    msg["From"] = YOUR_EMAIL
    msg["To"] = MAIN_RECIPIENT
    msg["Bcc"] = ", ".join(RECIPIENT_EMAILS)

    msg_alt = MIMEMultipart("alternative")
    msg.attach(msg_alt)

    msg_alt.attach(MIMEText("Your email client doesn't support HTML.", "plain"))
    msg_alt.attach(MIMEText(html_body, "html"))

    with open(attachment_path, "rb") as img:
        img_data = img.read()
        img_mime = MIMEImage(img_data)
        img_mime.add_header("Content-ID", "<chart>")
        msg.attach(img_mime)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(YOUR_EMAIL, YOUR_APP_PASSWORD)
        server.send_message(msg)
        print("✅ Email sent successfully.")
