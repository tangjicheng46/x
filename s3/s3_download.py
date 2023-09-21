import boto3
import io
import os
import time

def origin_download(s3_uri):
    """
    Read a file from an S3 URI and return its content as bytes.

    :param s3_uri: The S3 URI of the file to read (e.g., 's3://bucket-name/path/to/file.txt').
    :return: A tuple containing the file content as bytes and the download time in seconds.
    """
    # Parse the S3 URI to extract bucket name and object key
    s3_uri_parts = s3_uri.split('/')
    if len(s3_uri_parts) < 4 or s3_uri_parts[0] != 's3:' or s3_uri_parts[1] != '' or s3_uri_parts[3] == '':
        raise ValueError("Invalid S3 URI format")

    bucket_name = s3_uri_parts[2]
    object_key = '/'.join(s3_uri_parts[3:])

    # Initialize the S3 client
    s3_client = boto3.client('s3')

    start_time = time.time()  # 记录开始时间

    # Download the object from S3
    try:
        response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
        s3_object = response['Body'].read()

        # Convert the S3 object to bytes
        bytes_data = io.BytesIO(s3_object).read()

        end_time = time.time()  # 记录结束时间
        download_time = end_time - start_time  # 计算下载时间

        return bytes_data, download_time

    except Exception as e:
        raise Exception(f"Error downloading {s3_uri}: {e}")

def bench(func):
    s3_uri_prefix = 's3://staging-g123-ai/sagemaker/model/diffusion_model/deploy/Stable-diffusion/'
    model_list = ['artifex-g123-manga-local-translationtool-novelai.safetensors',
                  'artifex--bluegirl-cardos.safetensors',
                  'artifex-g123-manga-local-translationtool-novelai.safetensors',
                  'artifex-isekaimaou-kyo04-novelai.safetensors',
                  'artifex-isekaimaou-otomo_7-cardos.safetensors'
                  ]
    
    for model_name in model_list:
        s3_uri = s3_uri_prefix + model_name
        file_bytes, download_time = func(s3_uri)
        print(f"download {len(file_bytes)} bytes in {download_time} seconds.")

if __name__ == "__main__":
    bench(origin_download)
