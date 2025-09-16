from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("YouTubeTransform").getOrCreate()

# Load raw JSON
df = spark.read.json("s3a://my-youtube-bucket/raw/youtube.json")

# Transform
cleaned = df.select(
    col("id.videoId").alias("video_id"),
    col("snippet.title").alias("title"),
    col("snippet.publishedAt").alias("published_at"),
    col("snippet.channelTitle").alias("channel_title")
).dropna()

# Save as Parquet
cleaned.write.mode("overwrite").parquet("s3a://my-youtube-bucket/clean/youtube_videos")

print("✅ Transformation complete and saved to S3")
