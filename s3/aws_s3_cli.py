import subprocess
import os
import time

def get_bucket_name():
    env = os.environ.get('env')
    if env == 'staging':
        return 'staging-g123-ai'
    elif env == 'production':
        return 'production-g123-ai'
    else:
        raise ValueError("Invalid 'env' value. 'env' must be 'staging' or 'production'.")

def get_uri(filename, bucket_name):
    if filename.startswith("/s3/mount"):
        uri = filename.replace("/s3/mount", f"s3://{bucket_name}", 1)
        return uri
    else:
        print("Error: File name does not start with '/s3/mount'.")

def download_s3_file_to_bytes(s3_uri):
    try:
        temp_file = "/tmp/temporary_s3_download_file"
        subprocess.run(["aws", "s3", "cp", s3_uri, temp_file, "--no-progress"], check=True)
        with open(temp_file, 'rb') as file:
            file_bytes = file.read()
        os.remove(temp_file)
        return file_bytes
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error downloading file from S3: {str(e)}")


if __name__ == "__main__":
    file_name = "/s3/mount/sagemaker/model/diffusion_model/deploy/Stable-diffusion/artifex-qb-qb_all-Meina.safetensors"
    start_time = time.time()
    bucket_name = get_bucket_name()
    uri = get_uri(file_name, bucket_name)
    print(uri)
    download_s3_file_to_bytes(uri)
    end_time = time.time()
    print(f"cost: {end_time - start_time}")
