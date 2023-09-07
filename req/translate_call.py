import requests
import json
import time

URL_gateway = "http://gc3a.stg.g123.jp.private/v1/translation/translate-text-batch"  # 请替换为您的URL
URL = "http://127.0.0.1:8080/translate-text-batch"

# 定义一个函数发送请求
def send_request(records):
    data = {
        "metadata": {
            "labels": "string",
            "name": "i18n-service"
        },
        "payload": {
            "appid": "auo",
            "fromLang": "zh",
            "records": records,
            "toLang": "ja"
        }
    }

    json_string = json.dumps(data, ensure_ascii=False)
    file = open("data.json", "w")
    file.write(json_string)

    try:
        response = requests.post(URL, json=data)
        response.raise_for_status()  # 如果响应不是200，它会引发一个HTTPError
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except Exception as err:
        print(f"An error occurred: {err}")
        return None

    return response.text

# 从文件读取数据并构建请求的数据结构
def process_file(file_path):
    records = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for index, line in enumerate(f.readlines(), 1):  # 从1开始计数
            record = {
                "id": str(index),
                "text": line.strip()  # 去除两端的空白字符，例如换行符
            }
            records.append(record)

    response = send_request(records)
    if response:
        print(response)

if __name__ == "__main__":
    start_time = time.time()
    process_file('text_batch.txt')
    end_time = time.time()
    cost_time = end_time - start_time
    print(f"cost: {cost_time}")
