# myproject/Dockerfile
 # 建立 python3.7 环境
 FROM python:3.7
 
 # 镜像作者Lucas
 MAINTAINER Lucas
 
 # 设置 python 环境变量
 ENV PYTHONUNBUFFERED 1
 
 COPY pip.conf /root/.pip/pip.conf
 
 # 创建 myproject 文件夹
 RUN mkdir -p /var/www/html/myproject
 
 # 将 myproject 文件夹为工作目录
 WORKDIR /var/www/html/myproject
 
 # 将当前目录加入到工作目录中（. 表示当前目录）
 ADD . /var/www/html/myproject
 
 # 更新pip版本
 RUN /usr/local/bin/python -m pip install --upgrade pip
 
 # 利用 pip 安装依赖
 RUN pip install -r requirements.txt
 
 # 去除windows系统编辑文件中多余的\r回车空格
 RUN sed -i 's/\r//' ./start.sh
 
 # 给start.sh可执行权限
 RUN chmod +x ./start.sh
