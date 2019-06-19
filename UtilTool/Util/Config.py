# -*- coding: utf-8 -*-
import configparser
import os
from UtilTool.Util.BasePath import *

#重写configparser 避免转化为小写
class MyConfigParser(configparser.ConfigParser):
    def __init__(self, defaults=None):
        configparser.ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr

"""
配置文件读写
"""
class Conf:
	#系统配置文件
	@staticmethod
	def getSysValue(key):
		try:
			cf = configparser.ConfigParser()
			cf.read(SYS_DIR , encoding='UTF-8')
			return cf.get("sys", key)
		except Exception as e:
			raise e

	@staticmethod
	def setSysValue(key ,value):
		try:
			cf = MyConfigParser()
			cf.read(SYS_DIR , encoding='UTF-8')
			cf.set("sys", key ,value)
			with open(SYS_DIR, "w") as fw:
				cf.write(fw) # 使用write将修改内容写到文件中，替换原来config文件中内容
		except Exception as e:
			raise e

	#mysql配置文件
	@staticmethod
	def getDbValue(key):
		try:
			cf = configparser.ConfigParser()
			cf.read(SQLDB_DIR , encoding='UTF-8')
			return cf.get("mysqldb", key)
		except Exception as e:
			raise e

	#mongodb配置文件
	@staticmethod
	def getMongoDbValue(key):
		try:
			cf = configparser.ConfigParser()
			cf.read(MONGO_DIR , encoding='UTF-8')
			return cf.get("mongodb", key)
		except Exception as e:
			raise e

if __name__ == "__main__":
	try:
		print ( Conf.setSysValue("SystemToMail" , "false") )
	except Exception as e:
		print (e)