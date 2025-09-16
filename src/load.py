from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("YouTubeLoad").getOrCreate()

df = spark.read.parquet("s3a://my-youtube-bucket/clean/youtube_videos")
df.show(5)

print("✅ Data loaded successfully")
