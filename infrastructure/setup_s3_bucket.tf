provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "youtube" {
  bucket = "my-youtube-bucket"
  acl    = "private"
}
