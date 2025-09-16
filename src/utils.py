import os
from dotenv import load_dotenv

load_dotenv()

YT_API_KEY = os.getenv("YT_API_KEY")
YT_CHANNEL_ID = os.getenv("YT_CHANNEL_ID")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_BUCKET = "my-youtube-bucket"