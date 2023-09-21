import boto3
import io
import os
import time

def read_s3_file_to_bytes(s3_uri):
    """
    Read a file from an S3 URI and return its content as bytes using multipart download for optimization.

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

    # 获取文件大小
    response = s3_client.head_object(Bucket=bucket_name, Key=object_key)
    file_size = response['ContentLength']

    # 分段下载
    chunk_size = 1024 * 1024  # 1MB
    num_parts = int(file_size / chunk_size) + 1

    s3_object = b''  # 用于存储下载的文件内容

    for part_number in range(1, num_parts + 1):
        start_byte = (part_number - 1) * chunk_size
        end_byte = min(part_number * chunk_size - 1, file_size - 1)
        response = s3_client.get_object(
            Bucket=bucket_name,
            Key=object_key,
            Range=f'bytes={start_byte}-{end_byte}'
        )
        s3_object += response['Body'].read()

    end_time = time.time()  # 记录结束时间
    download_time = end_time - start_time  # 计算下载时间

    return s3_object, download_time

# Example usage:
s3_uri = 's3://staging-g123-ai/sagemaker/model/diffusion_model/deploy/Stable-diffusion/artifex-g123-manga-local-translationtool-novelai.safetensors'
file_bytes, download_time = read_s3_file_to_bytes(s3_uri)
print(f"Downloaded {len(file_bytes)} bytes in {download_time} seconds.")
