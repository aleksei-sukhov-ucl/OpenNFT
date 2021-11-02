import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='config.env')
# enter your server IP address/domain name
HOST = os.getenv('HOST')  # or "domain.com"

# database name, if you want just to connect to MySQL server, leave it empty
DATABASE = os.getenv('DATABASE')

# this is the user you create
USERDB = os.getenv('USERDB')

# user password
PASSWORD = os.getenv('PASSWORD')
