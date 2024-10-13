## 安装配置

**Debian系安装3.6**
1. sudo add-apt-repository ppa:jonathonf/python-3.6
1. sudo apt update 
1. sudo apt install python3.6

**Centos7安装3.11**

[在 CentOS 7 / RHEL 7 上安装 Python 3.11](https://blog.csdn.net/zhezhebie/article/details/132499755)  
[pip install报错"Can't connect to HTTPS URL because the SSL module is not available"](https://www.cnblogs.com/world-of-yuan/p/17855748.html)  

编译安装 libssl
1. ./config--prefix=/opt/openssl
1. make -j && make install

编译安装 python
1. make  clean
1. /configure --prefix=/opt/python3.11 --with-openssl=/opt/openssl --with-openssl-rpath=auto
1. make -j && make altinstall

### Docker安装
> [docker hub](https://hub.docker.com/_/python/)

### Conda
> [Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)`简单理解为 venv + pip`  
> [Miniconda 安装](https://docs.anaconda.com/miniconda/)  

- 安装 conda create -n py39  python=3.9 
    - conda create -n py311 python=3.11
- 激活指定环境 conda activate py39
- 退出环境 conda deactivate

### sys.path
> [Doc: Python path](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH)

- sys.path 是 指定模块的搜索路径的字符串列表。`类似于Java的 ClassPath, Go的 GOPATH, 让解释器知道去哪找包`
    - 查看系统的 sys.path 进入交互解释器
    ```python
        import sys
        print("\n".join(sys.path))
    ```

**修改sys.path**
1. 代码中直接添加, 执行就生效, 程序结束就失效
    ```python
        #  假如有如下两个文件 在不同的包下
        # /src/configs/config.py
        # /src/common/Database.py

        parent_path = os.path.dirname(sys.path[0])
        # 避免重复添加
        if parent_path not in sys.path:
            sys.path.append(parent_path)
        import configs.config
    ```

1. 添加 *.pth 文件
    - 在 `/usr/local/lib/` 目录下有多个 Python 版本,配置自己需要的版本
    - 例如在 `python2.7/site-packages` 中添加 test.pth 文件,文件内容为项目的绝对路径
        - python3.x 则是在 `dist-packages` 目录下

1. 修改环境变量
    - 修改或添加 环境变量 PYTHONPATH 路径用分号分隔
