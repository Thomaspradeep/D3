resource "aws_s3_bucket" "log_bucket" {
    bucket = "log-${var.bucket_name}"
   versioning{
    enabled = true
}
    tags = {
        Env = "Dev"
    }
}

resource "aws_s3_bucket" "CDS_Infra_bucket" {
    bucket = var.bucket_name
    logging{
        target_bucket = aws_s3_bucket.log_bucket.id
        target_prefix = "Log/land_bucket"
    }

   versioning{
    enabled = true
}
    tags = {
        Env = "Dev"
    }
}

resource "aws_s3_bucket_object" "log_bucket"{
    bucket = aws_s3_bucket.log_bucket.id
    region = "us-east-1"
    key = "Log/land_bucket"
}

resource "aws_s3_bucket" "glue_bucket_matthew"{
    bucket = "bucket101matthew"
    
    versioning{
    enabled = true
}
}