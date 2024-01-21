import os
from dotenv import load_dotenv
import yagmail



dotenv_path = ".env"
load_dotenv(dotenv_path)
yag = yagmail.SMTP(os.getenv("EMAIL"), os.getenv("PASSWORD"))


def send_mail(subject, body, to):
    try:
        yag.send(to=to, subject=subject, contents=body)
        yag.close()
        return True
    except:
        return False

