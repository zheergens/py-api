# -*- coding: utf-8 -*-
from app.v1.common import singleton

from flask import g
import time
import pymongo
import pymysql
import redis

@singleton
class DB(object):
    def __init__(self):
        self.mysql = None
        self.redis = None
        self.dot_redis = None
        self.mongo = None
        self.mongo_conn = None

        self.init_connect()

    def __del__(self):
        pass

    def init_connect(self):
        # 连接 mongodb
        self.mongo_conn = pymongo.MongoClient(g.config.get('HOST'), g.config.get('PORT'))
        self.mongo = self.mongo_conn[g.config.get('DB')]
        # self.mongo.authenticate(name=g.config('user', 'Mongo'),
        #                         password=g.config('password', 'Mongo'))