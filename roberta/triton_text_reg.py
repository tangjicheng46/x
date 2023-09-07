import numpy as np
from tritonclient.http import InferenceServerClient, InferenceServerException

# 创建一个连接到Triton服务器的客户端
client = InferenceServerClient(url="localhost:8000")

# 创建输入数据
# 假设input_data是你的输入数据，形状为(1, height, width, 3)。
input_data = np.random.random((1, 224, 224, 3)).astype(np.float32)

inputs = []
outputs = []

# 定义输入
inputs.append(client.InferInput('input_images:0', input_data.shape, 'FP32'))
inputs[0].set_data_from_numpy(input_data)

# 定义输出
outputs.append(client.InferRequestedOutput('feature_fusion/Conv_7/Sigmoid:0'))
outputs.append(client.InferRequestedOutput('feature_fusion/concat_3:0'))

# 发送推理请求
results = client.infer(model_name="text_detection", inputs=inputs, outputs=outputs)

# 获取输出结果
output1_data = results.as_numpy('feature_fusion/Conv_7/Sigmoid:0')
output2_data = results.as_numpy('feature_fusion/concat_3:0')

print(output1_data)
print(output2_data)
