#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb

db = MySQLdb.connect("192.168.204.240", "sports_rw", "Q41IrJPg7S#1")

cursor = db.cursor()

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 更新语句
sql = "UPDATE `sports`.`match_live_stream` \
       SET `has_replay`='1', `replay_args`='&playback=1&startoffset=0&endoffset=0' \
       WHERE `id`='1372'"
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()

# 关闭数据库连接
db.close()