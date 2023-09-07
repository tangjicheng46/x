import aiohttp
import asyncio
import json
import time
from multiprocessing import Process

async def fetch(session, url, data, request_id):
    async with session.post(url, json=data) as response:
        if response.status != 200:
            print(f"Request {request_id} returned with status {response.status}.")
            return
        result = await response.json()
        with open(f"timeout300_test/{request_id}.json", 'w') as f:
            json.dump(result, f, indent=4)

async def main(url, N, data):
    # 创建连接池
    conn = aiohttp.TCPConnector(limit=N)
    async with aiohttp.ClientSession(connector=conn) as session:
        tasks = [fetch(session, url, data, i) for i in range(N)]
        await asyncio.gather(*tasks)

def send_concurrent_requests(url, N):
    with open('timeout300.json', 'r') as f:
        data = json.load(f)
    start_time = time.time()
    asyncio.run(main(url, N, data))
    total_time = time.time() - start_time
    print(f"Cost: {total_time:.2f} seconds")

def execute_in_processes(url, concurrent_num, process_num):
    processes = []
    for _ in range(process_num):
        process = Process(target=send_concurrent_requests, args=(url, concurrent_num))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

if __name__ == "__main__":
    concurrent_num = 200
    process_num = 1  # 你想要使用的进程数量
    url_to_send = "http://gc3a.stg.g123.jp.private/v1/openai/i18n/chat/completions"

    execute_in_processes(url_to_send, concurrent_num, process_num)