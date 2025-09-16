# YouTube Data Engineering Project

This project builds a simple **ETL pipeline** for analyzing YouTube channel data using:
- **YouTube Data API** (extract video metadata)
- **AWS S3** (store raw and processed data)
- **PySpark on Databricks** (clean & transform data)
- **Delta Lake / Parquet** (structured storage)

## Architecture
1. Extract → Fetch video metadata from YouTube Data API
2. Load Raw → Store JSON files in S3 (`raw/`)
3. Transform → Clean and enrich with PySpark
4. Load Curated → Save Parquet/Delta tables in S3 (`clean/`)

## Setup
1. Create `.env` file with:
YT_API_KEY=your_api_key
YT_CHANNEL_ID=channel_id_here
AWS_ACCESS_KEY_ID=xxx
AWS_SECRET_ACCESS_KEY=xxx


2. Install dependencies:
```bash
pip install -r requirements.txt
Run ingestion:


python src/ingest.py
Run transformation:

python src/transform.py