# -*- coding: utf-8 -*-
import os

BASE_DIR =os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) )
SYS_DIR = os.path.join(os.path.join(BASE_DIR,'Conf'),'sys.conf')
SQLDB_DIR = os.path.join(os.path.join(BASE_DIR,'Conf'), 'mysqldb.conf')
MONGO_DIR = os.path.join(os.path.join(BASE_DIR,'Conf'),'mongodb.conf')