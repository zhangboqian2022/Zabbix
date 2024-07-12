'''
Descripttion: THIS FILE IS PART OF Digital China PROJECT
version: 1.0
Author: Daniel 张大牛
Date: 2024-07-11 10:00:00
LastEditors: Daniel zhangbqd@dcits.com
LastEditTime: 2024-07-12 10:00:00
# v1.0 版本说明
# 脚本功能：查询 Zabbix 主机组内存利用率
# 连接到 Zabbix 数据库，获取指定主机组的内存利用率信息
# 支持按天数查询历史内存利用率数据
# 支持按主机组筛选内存利用率数据
# 支持设置内存利用率阈值
# 输出内存利用率低于阈值的主机列表，并显示每个主机的平均和最大内存利用率

Descripttion: Zabbix Project
version: 1.0
Author: Daniel 张大牛
Date: 2024-07-11 10:00:00
LastEditors: Daniel zhangbqd@dcits.com
LastEditTime: 2024-07-12 10:00:00
# v1.0 Version Description
# Script Function: Query Zabbix Host Group Memory Utilization
# Connect to Zabbix database and retrieve memory utilization information for specified host group
# Support querying historical memory utilization data by days
# Support filtering memory utilization data by host group
# Support setting memory utilization threshold
# Output the list of hosts with memory utilization below the threshold, showing each host's average and maximum memory utilization
'''

import mysql.connector
from datetime import datetime, timedelta
import argparse

# 设置命令行参数
parser = argparse.ArgumentParser(description='查询Zabbix主机组的内存利用率')
parser.add_argument('days', type=int, help='查询的天数')
parser.add_argument('hostgroup', type=str, help='主机组名称')
parser.add_argument('threshold', type=float, help='内存平均利用率阈值')
args = parser.parse_args()

# 连接到数据库
conn = mysql.connector.connect(
    host='hostIP',        # 替换为你的数据库主机名或IP地址
    user='username',           # 替换为你的数据库用户名
    password='password',       # 替换为你的数据库密码
    database='zabbix'
)

cursor = conn.cursor()

# 获取当前时间和指定天数前的时间戳
now = datetime.now()
time_from = int((now - timedelta(days=args.days)).timestamp())

# 获取主机群组中的主机ID和itemid
query_itemid = """
SELECT h.host, i.itemid, i.name, i.key_
FROM items i
JOIN hosts h ON i.hostid = h.hostid
WHERE h.hostid IN (
    SELECT h.hostid
    FROM hosts h
    JOIN hosts_groups hg ON h.hostid = hg.hostid
    JOIN hstgrp g ON hg.groupid = g.groupid
    WHERE g.name = %s
) AND i.name LIKE %s;
"""

cursor.execute(query_itemid, (args.hostgroup, '%Memory utilization%'))
results = cursor.fetchall()

# 打印主机和itemid信息
print("主机和内存利用率itemid:")
for row in results:
    print(f"主机：{row[0]}, ItemID：{row[1]}, 监控项名称：{row[2]}, Key：{row[3]}")

# 提取所有itemid
itemids = [row[1] for row in results]

# 检查每个itemid在history表中的数据
query_avg_memory = """
WITH HostGroup AS (
    SELECT 
        h.hostid, h.host, i.itemid
    FROM 
        hosts h
    JOIN 
        hosts_groups hg ON h.hostid = hg.hostid
    JOIN 
        hstgrp g ON hg.groupid = g.groupid
    JOIN 
        items i ON h.hostid = i.hostid
    WHERE 
        g.name = %s
        AND i.name LIKE %s
)
SELECT 
    hg.host,
    AVG(his.value) AS avg_memory_utilization,
    MAX(his.value) AS max_memory_utilization
FROM 
    history AS his
JOIN 
    HostGroup AS hg ON his.itemid = hg.itemid
WHERE 
    his.itemid IN ({})
    AND his.clock >= %s
GROUP BY 
    hg.host
HAVING 
    avg_memory_utilization < %s;
""".format(','.join(map(str, itemids)))

cursor.execute(query_avg_memory, (args.hostgroup, '%Memory utilization%', time_from, args.threshold))

# 获取结果并输出平均和最大内存利用率
results = cursor.fetchall()
print(f"{args.days}天内内存平均利用率小于{args.threshold}%的主机列表（主机组：{args.hostgroup}）:")
for row in results:
    print(f"主机：{row[0]}， 平均内存利用率：{row[1]:.2f}%， 最大内存利用率：{row[2]:.2f}%")

# 关闭数据库连接
cursor.close()
conn.close()
