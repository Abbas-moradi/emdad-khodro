import os
import yagmail


dotenv_path = ".env"
try:
    with open(dotenv_path, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            os.environ[key] = value
except FileNotFoundError:
    print(f"File {dotenv_path} not found.")

yag = yagmail.SMTP(os.getenv("EMAIL"), os.getenv("PASSWORD"))


def send_mail(subject, body, to):
    try:
        yag.send(to=to, subject=subject, contents=body)
        yag.close()
        return True
    except:
        return False

