import subprocess
import time

def download_and_delete_s3_file(s3_uri):
    """
    Download a file from S3 using 'aws s3 cp' command, measure download time, and delete the downloaded file.

    :param s3_uri: The S3 URI of the file to download.
    :return: The download time in seconds.
    """
    # 构建下载命令
    download_command = f"aws s3 cp {s3_uri} ."

    # 记录开始时间
    start_time = time.time()

    try:
        # 执行下载命令
        subprocess.run(download_command, shell=True, check=True)

        # 记录结束时间
        end_time = time.time()

        # 计算下载时间
        download_time = end_time - start_time

        # 打印下载时间
        print(f"[tangjicheng] Downloaded {s3_uri} in {download_time} seconds.")

        return download_time

    except subprocess.CalledProcessError as e:
        print(f"Error downloading {s3_uri}: {e}")

    finally:
        # 删除下载的文件
        subprocess.run(f"rm -f ./*.safetensors", shell=True)

# Example usage:
s3_uri_prefix = 's3://staging-g123-ai/sagemaker/model/diffusion_model/deploy/Stable-diffusion/'
model_list = ['artifex-g123-manga-local-translationtool-novelai.safetensors',
              'artifex--bluegirl-cardos.safetensors',
              'artifex-g123-manga-local-translationtool-novelai.safetensors',
              'artifex-isekaimaou-kyo04-novelai.safetensors',
              'artifex-isekaimaou-otomo_7-cardos.safetensors'
              ]

for model_name in model_list:
    s3_uri = s3_uri_prefix + model_name
    download_time = download_and_delete_s3_file(s3_uri)
