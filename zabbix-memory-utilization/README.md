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
python check-server-v1.py <days> <hostgroup> <threshold>
days: 查询的天数
hostgroup: 主机组名称
threshold: 内存平均利用率阈值（百分比）
示例：


python check-server-v1.py 7 "Web Servers" 80
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
python check-server-v1.py <days> <hostgroup> <threshold>
days: 查询的天数
hostgroup: 主机组名称
threshold: 内存平均利用率阈值（百分比）
示例：


python check-server-v1.py 7 "Web Servers" 80
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


### 更新后的 README.md 内容（ v1.1 版本说明）


版本更新 v1.1 版本说明

在 v1.1 版本中，增加了一个新功能，用于统计内存利用率超过指定阈值的次数。具体更新如下：

增加了一个命令行参数 max_exceed_count，用于指定内存利用率超过阈值的最大次数。

脚本现在可以输出在指定天数内，内存平均利用率低于指定阈值且超过阈值次数小于指定次数的主机列表。

更新后的使用示例：


python3 check-server-v1.1.py <days> <hostgroup> <threshold> <max_exceed_count>
days: 查询的天数
hostgroup: 主机组名称
threshold: 内存平均利用率阈值（百分比）
max_exceed_count: 超过阈值的最大次数
示例：


python3 check-server-v1.1.py 30 'Zabbix servers' 40 10
这个命令将查询过去 30 天内内存平均利用率低于 40% 且超过 40% 的次数少于 10 次的主机列表。






