import aiohttp
import asyncio
import json
import time

async def send_request(session, test_string):
    prompt = "请把下面的内容，从中文翻译为日语：" + test_string
    url = "http://gc3a.stg.g123.jp.private/v1/openai/i18n/chat/completions"
    headers = {
        'Content-Type': 'application/json'
    }
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
    async with session.post(url, headers=headers, json=data) as response:
        return await response.json()

async def main():
    # 从文件中读取每一行
    with open('text_batch.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]

    async with aiohttp.ClientSession() as session:
        tasks = [send_request(session, line) for line in lines]
        responses = await asyncio.gather(*tasks)

    # Save each response to a separate JSON file
    for idx, response in enumerate(responses, 1):
        with open(f"origin_resp/{idx}.json", 'w') as json_file:
            json.dump(response, json_file, indent=4, ensure_ascii=False)

start_time = time.time()
asyncio.run(main())
end_time = time.time()
cost_time = end_time - start_time

print(f"cost: {cost_time}")
