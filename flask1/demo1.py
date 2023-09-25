from flask import Flask

# 创建一个 Flask 应用实例
app = Flask(__name__)

# 定义路由，用于处理根路径的请求
@app.route('/')
def hello_world():
    return 'Hello, World!'

# 运行应用
if __name__ == '__main__':
    app.run()

