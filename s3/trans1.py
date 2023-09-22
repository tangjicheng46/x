import os
import sys
import time
import threading
import boto3
from botocore.exceptions import NoCredentialsError
from boto3.s3.transfer import TransferConfig

def download_file_from_s3(s3_uri):
    # 解析S3 URI
    parts = s3_uri.split('/')
    if len(parts) < 4 or parts[0] != 's3:':
        raise ValueError("Invalid S3 URI format. Please use 's3://bucket/key'.")

    bucket_name = parts[2]
    file_key = '/'.join(parts[3:])

    # 创建S3客户端
    client = boto3.client('s3')

    # 配置TransferConfig以优化下载
    config = TransferConfig(
        multipart_threshold=8 * 1024 * 1024,  # 分块传输阈值大小
        max_concurrency=10,  # 最大并发下载数
        num_download_attempts=10,  # 下载重试次数
    )

    # 创建S3Transfer对象
    transfer = boto3.s3.transfer.S3Transfer(client, config)

    # 记录开始时间
    start_time = time.time()

    try:
        # 使用S3Transfer下载文件
        file_path = '/tmp/temporary_download_file'  # 临时文件路径
        transfer.download_file(bucket_name, file_key, file_path)

        # 读取文件内容到字节对象
        with open(file_path, 'rb') as file:
            file_bytes = file.read()

        # 删除临时文件
        os.remove(file_path)

        # 计算下载耗时
        end_time = time.time()
        download_time = end_time - start_time

        return file_bytes, download_time
    except NoCredentialsError:
        raise Exception("AWS credentials not found. Make sure you have configured your AWS credentials.")
    except Exception as e:
        raise Exception(f"Error downloading file from S3: {str(e)}")


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

# 示例用法
if __name__ == "__main__":
    s3_uri = 's3://your-bucket-name/path/to/your/file.txt'
    try:
        file_bytes, download_time = download_file_from_s3(s3_uri)
        print(f"File downloaded successfully in {download_time:.2f} seconds.")
        # 现在，file_bytes 变量包含了文件的内容
    except Exception as e:
        print(f"Error: {str(e)}")
