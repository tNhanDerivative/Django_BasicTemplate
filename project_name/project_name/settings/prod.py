
import os
from dotenv import load_dotenv
load_dotenv()


ALLOWED_HOSTS = ['127.0.0.1',os.getenv('SERVER_IP'),  os.getenv('DOMAIN_NAME')]