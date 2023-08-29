# 使用基础镜像
FROM --platform=linux/amd64 ubuntu:20.04

# 设置环境变量，避免交互式安装
ENV DEBIAN_FRONTEND=noninteractive

# 更新源并安装基本工具
RUN apt-get update && \
    apt-get install -y \
    wget \
    bzip2 \
    ca-certificates \
    libglib2.0-0 \
    libxext6 \
    libsm6 \
    libxrender1 \
    git \
    curl \
    vim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
COPY ./app.py /app/app.py

# 安装 Miniconda
ENV CONDA_HOME /opt/conda
ENV PATH $CONDA_HOME/bin:$PATH

RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-py310_23.3.1-0-Linux-x86_64.sh -O /tmp/miniconda.sh && \
    /bin/bash /tmp/miniconda.sh -b -p $CONDA_HOME && \
    rm /tmp/miniconda.sh && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN pip3 install --no-cache-dir -r requirements.txt

# 清理不需要的包和缓存
RUN conda clean -a -y

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
