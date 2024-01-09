resource "aws_s3_bucket_object" "ddm_client" {
    bucket = var.bucket_id
    acl = "private"
    key = "ddm_client/${var.client_name}/" 
    content_type = "application/x-directory"
}

resource "aws_s3_bucket_object" "ddm_client_process" {
    bucket = var.bucket_id
    acl = "private"
    key = "ddm_client/${var.client_name}/Process/" 
    content_type = "application/x-directory"
}