import requests
import json
import time

# 从文件中读取文本
with open('text_long.txt', 'r') as file:
    test_string = file.read().strip()

prompt = "请把下面的内容，从中文翻译为日语：" + test_string

# 构建POST请求的数据
data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
}

headers = {
    'Content-Type': 'application/json'
}

url = "http://gc3a.stg.g123.jp.private/v1/openai/i18n/chat/completions"

start_time = time.time()
response = requests.post(url, headers=headers, data=json.dumps(data))
end_time = time.time()
cost_time = end_time - start_time

# 处理响应
if response.status_code == 200:
    result = response.json()
    with open('single_long_resp.json', 'w') as json_file:
        json.dump(response.json(), json_file, indent=4, ensure_ascii=False)
    # print(result)
else:
    print(f"Error: {response.status_code}")
    print(response.text)

print(f"cost: {cost_time}")
