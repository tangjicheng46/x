from awscliv2.api import AWSAPI
from awscliv2.exceptions import AWSCLIError

aws_api = AWSAPI()

try:
    output = aws_api.execute(["s3", "ls"])
except AWSCLIError as e:
    print(f"Something went wrong: {e}")
else:
    print(output)