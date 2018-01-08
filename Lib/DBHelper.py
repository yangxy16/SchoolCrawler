# /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    数据库封装
'''

from Lib.Config import DBConf
import pymysql.cursors

class DBHelper:
    def __enter__( self ):
        try:
            self.connection = pymysql.connect( host = DBConf.IP, port = DBConf.PORT, 
                                                user = DBConf.User, password = DBConf.PassWord, 
                                                db = DBConf.DBName, charset = 'utf8mb4', 
                                                cursorclass = pymysql.cursors.DictCursor )
        except:
            self.connection = None
            raise RuntimeError( 'MySQL Connect Failed' )
            
        return self
                                            
    def __exit__( self, type, value, trace ):
        if self.connection:
            self.connection.close()
            
    def addSchool( self, *args, **kwargs ):
        try :
            with self.connection.cursor() as cursor :
                pass
                #cursor.execute( 'INSERT INTO tblIPPool ( `hash`, `ip`, `port` ) values( %s, %s, %s )', ( hash, ip, port ) )
            self.connection.commit()
        except:
            pass