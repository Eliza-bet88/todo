import random
import string
from datetime import datetime, timedelta

def generate_token():
    letters = string.ascii_letters + string.digits
    token = ''.join(random.choice(letters) for i in range(40))
    return token

def get_expiry_time(hours=24):
    return datetime.now() + timedelta(hours=hours)
