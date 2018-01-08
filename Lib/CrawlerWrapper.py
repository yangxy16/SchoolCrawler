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

class Crawler:
    
    @staticmethod
    def getSchool():
        schlist = []
        for url in WebConf.DATA5U:
            headers = { "User-Agent": UserAgent.getUA() }
            try:
                r = rq.get( url, headers = headers )
                if r.status_code == 200:
                    html = r.content.decode( 'utf-8' )
                    schlist.extend( GKCHSIParser.parseDocument( html ) )
            except:
                pass
            time.sleep( 0.6 )