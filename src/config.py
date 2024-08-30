import os
from dotenv import load_dotenv

load_dotenv()

MailAddress = os.getenv('Mailaddress')
Password = os.getenv('Password')
SQUARE_ID = os.getenv('SQUARE_ID')