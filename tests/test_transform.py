import pytest
from pyspark.sql import SparkSession
from pyspark.sql import Row

spark = SparkSession.builder.master("local[1]").appName("Test").getOrCreate()

def test_transformation():
    data = [Row(video_id="abc123", title="Test", published_at="2024-01-01", channel_title="Demo")]
    df = spark.createDataFrame(data)
    assert df.count() == 1
