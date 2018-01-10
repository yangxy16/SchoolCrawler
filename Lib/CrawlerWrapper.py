# /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    代理IP抓取Worker
'''

from Lib.Config import WebConf, UserAgent
from Lib.Parser import GKCHSIParser
from Lib.DBHelper import DBHelper

import requests as rq
import time
import json

class Crawler:
    
    @staticmethod
    def getSchool( filepath ):
        schlist = []
        def getPage( schlist, url, proxies ):
            headers = { "User-Agent": UserAgent.getUA() }
            try:
                r = rq.get( url, headers = headers, proxies = proxies )
                if r.status_code == 200:
                    html = r.content.decode( 'utf-8' )
                    url, schs = GKCHSIParser.parseSchool( html )
                    schlist.extend( schs )
                    return True, url
            except:
                pass
            return False, url
        
        url = WebConf.GKCHSI
        while True:
            proxies = None
            ret, url = getPage( schlist, url, proxies )
            if ret:
                time.sleep( 1 )
            if not url:
                break
                
        with open( filepath, 'wb' ) as f:
            for item in schlist:
                f.write( json.dumps( item, ensure_ascii = False ).encode( 'utf-8' ) )
                f.write( '\r\n'.encode( 'utf-8' ) )
                
    @staticmethod
    def getMajor( filepath, savepath ):
        def getPage( url, proxies ):
            headers = { "User-Agent": UserAgent.getUA() }
            try:
                r = rq.get( url, headers = headers, proxies = proxies )
                if r.status_code == 200:
                    html = r.content.decode( 'utf-8' )
                    return GKCHSIParser.parseMajor( html )
            except:
                pass
            return None
    
        schlist = []
        with open( filepath, 'rb' ) as f:
            while True:
                line = f.readline()
                if not line:
                    break
                else:
                    schlist.append( json.loads( line ) )
                    
        with open( savepath, 'wb' ) as f:
            for sch in schlist:
                if sch['url'] and len( sch['url'] ) > 1:
                    data = getPage( sch['url'], None )
                    print( data )
                    
                break
                    #sch['extra_1'] = data
                    #f.write( json.dumps( sch, ensure_ascii = False ).encode( 'utf-8' ) )
                    #f.write( '\r\n'.encode( 'utf-8' ) )