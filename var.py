import os
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv(".env")

def make_int(str_input):
    str_list = str_input.split(" ")
    int_list = []
    for x in str_list:
        int_list.append(int(x))
    return int_list

class Var:
    API_ID = int(os.getenv("API_ID", "22926746"))
    API_HASH = os.getenv("API_HASH", "ffd91926f59e55fb08b3e1a4f5b99b1d")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "6223660988:AAH_D49zGMjnwhJGzNnYdt2XAmqyJmTnNUg")
    sudo = os.getenv("SUDO", "7997412957")
    SUDO = []
    if sudo:
        SUDO = make_int(sudo)
