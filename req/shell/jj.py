import json

# 读取文件内容
with open('text_batch.txt', 'r') as f:
    lines = f.readlines()

# 为每一行生成一个JSON对象
records = []
for idx, line in enumerate(lines, 1):  # 从1开始计数
    record = {
        "id": str(idx),
        "text": line.strip()  # 移除行尾的换行符
    }
    records.append(record)

# 构建总的JSON结构
data = {"records": records}

# 保存JSON到文件
with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("JSON saved to output.json")
