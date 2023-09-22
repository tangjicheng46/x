import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from botocore.config import Config
from s3transfer import S3Transfer
import io

def download_s3_file_to_bytes(s3_uri):
    """
    Download a file from an S3 URI and return its content as bytes.

    :param s3_uri: The S3 URI of the file to download (e.g., 's3://bucket-name/path/to/file.txt').
    :return: The file content as bytes.
    """
    try:
        # 解析 S3 URI 获取 bucket 名和 object key
        s3_uri_parts = s3_uri.split('/')
        if len(s3_uri_parts) < 4 or s3_uri_parts[0] != 's3:' or s3_uri_parts[1] != '' or s3_uri_parts[3] == '':
            raise ValueError("Invalid S3 URI format")

        bucket_name = s3_uri_parts[2]
        object_key = '/'.join(s3_uri_parts[3:])

        # 配置 AWS 客户端
        aws_config = Config(signature_version='s3v4')
        s3_client = boto3.client('s3', config=aws_config)

        # 创建 S3Transfer 实例
        transfer = S3Transfer(s3_client)

        # 创建一个 BytesIO 缓冲区来保存下载的文件内容
        file_data = io.BytesIO()

        # 使用 S3Transfer 下载文件到缓冲区
        transfer.download_fileobj(bucket_name, object_key, file_data)

        # 将文件内容作为 bytes 返回
        return file_data.getvalue()

    except (NoCredentialsError, PartialCredentialsError) as e:
        raise Exception("AWS credentials are missing or invalid. Please configure your AWS credentials.")

    except Exception as e:
        raise Exception(f"Error downloading {s3_uri}: {e}")

# 示例用法：
s3_uri = 's3://your-bucket-name/path/to/your/file.txt'
file_bytes = download_s3_file_to_bytes(s3_uri)
print(file_bytes)
