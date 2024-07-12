# Zabbix 主机组内存利用率查询程序

这是一个用于查询 Zabbix 主机组内存利用率的 Python 脚本。脚本通过连接 Zabbix 数据库，获取指定主机组的内存利用率信息，并筛选出平均内存利用率低于指定阈值的主机。

## 特性

- 支持按天数查询历史内存利用率数据
- 支持按主机组筛选内存利用率数据
- 支持设置内存利用率阈值

## 依赖

- Python 3.x
- mysql-connector-python

## 安装

1. 克隆仓库
    ```bash
    git clone https://github.com/yourusername/zabbix-memory-utilization.git
    ```
2. 安装依赖
    ```bash
    pip install mysql-connector-python
    ```

## 使用

运行脚本前，请确保已正确配置数据库连接信息。

```bash
python zabbix_memory_utilization.py <days> <hostgroup> <threshold>
days: 查询的天数
hostgroup: 主机组名称
threshold: 内存平均利用率阈值（百分比）
示例：


python zabbix_memory_utilization.py 7 "Web Servers" 80.0
配置
在脚本中设置数据库连接信息：

python

conn = mysql.connector.connect(
    host='地址',        # 替换为你的数据库主机名或IP地址
    user='用户名',           # 替换为你的数据库用户名
    password='密码',       # 替换为你的数据库密码
    database='zabbix'
)
输出
脚本将输出指定天数内，内存平均利用率小于指定阈值的主机列表，并显示每个主机的平均内存利用率和最大内存利用率。


中文版 README.md
markdown
复制代码
# Zabbix 主机组内存利用率查询程序

这是一个用于查询 Zabbix 主机组内存利用率的 Python 脚本。脚本通过连接 Zabbix 数据库，获取指定主机组的内存利用率信息，并筛选出平均内存利用率低于指定阈值的主机。

## 特性

- 支持按天数查询历史内存利用率数据
- 支持按主机组筛选内存利用率数据
- 支持设置内存利用率阈值

## 依赖

- Python 3.x
- mysql-connector-python

## 安装

1. 克隆仓库
    ```bash
    git clone https://github.com/yourusername/zabbix-memory-utilization.git
    ```
2. 安装依赖
    ```bash
    pip install mysql-connector-python
    ```

## 使用

运行脚本前，请确保已正确配置数据库连接信息。

```bash
python zabbix_memory_utilization.py <days> <hostgroup> <threshold>
days: 查询的天数
hostgroup: 主机组名称
threshold: 内存平均利用率阈值（百分比）
示例：


python zabbix_memory_utilization.py 7 "Web Servers" 80.0
配置
在脚本中设置数据库连接信息：

python

conn = mysql.connector.connect(
    host='地址',        # 替换为你的数据库主机名或IP地址
    user='用户名',           # 替换为你的数据库用户名
    password='密码',       # 替换为你的数据库密码
    database='zabbix'
)
输出
脚本将输出指定天数内，内存平均利用率小于指定阈值的主机列表，并显示每个主机的平均内存利用率和最大内存利用率。

许可证
该项目遵循 MIT 许可证。



# Zabbix Host Group Memory Utilization Query Script

This is a Python script for querying the memory utilization of Zabbix host groups. The script connects to the Zabbix database, retrieves memory utilization data for the specified host group, and filters out hosts with an average memory utilization below the specified threshold.

## Features

- Query historical memory utilization data by days
- Filter memory utilization data by host group
- Set memory utilization threshold

## Dependencies

- Python 3.x
- mysql-connector-python

## Installation

1. Clone the repository
    ```bash
    git clone https://github.com/yourusername/zabbix-memory-utilization.git
    ```
2. Install dependencies
    ```bash
    pip install mysql-connector-python
    ```

## Usage

Before running the script, ensure the database connection information is correctly configured.

```bash
python zabbix_memory_utilization.py <days> <hostgroup> <threshold>
days: Number of days to query
hostgroup: Host group name
threshold: Average memory utilization threshold (percentage)
Example:


python zabbix_memory_utilization.py 7 "Web Servers" 80.0
Configuration
Set the database connection information in the script:

python

conn = mysql.connector.connect(
    host='your_host',        # Replace with your database host or IP address
    user='your_username',           # Replace with your database username
    password='your_password',       # Replace with your database password
    database='zabbix'
)
Output
The script will output a list of hosts with an average memory utilization below the specified threshold within the specified number of days, showing each host's average and maximum memory utilization.


