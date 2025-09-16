import requests
import json
import boto3
from utils import YT_API_KEY, YT_CHANNEL_ID, AWS_BUCKET

def fetch_youtube_data(api_key, channel_id):
    url = f"https://www.googleapis.com/youtube/v3/search?key={api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults=10"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def save_raw_to_s3(data, bucket, key):
    s3 = boto3.client("s3")
    s3.put_object(Bucket=bucket, Key=key, Body=json.dumps(data))

if __name__ == "__main__":
    data = fetch_youtube_data(YT_API_KEY, YT_CHANNEL_ID)
    save_raw_to_s3(data, AWS_BUCKET, "raw/youtube.json")
    print("✅ Data ingested and saved to S3")
