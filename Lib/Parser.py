# /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    页面内容解析器封装
'''

from bs4 import BeautifulSoup
import re
import hashlib

class GKCHSIParser:

    @staticmethod
    def parseDocument( html ):
        tableFlag = '<table width="100%" border="0" align="center" cellpadding="3" cellspacing="1" bgcolor="#E1E1E1" style="margin:0px auto;">'
        nTableFlag = len( tableFlag )
        
        nPos = 1
        while True:
            nPos = html.find( tableFlag, nPos )
            if nPos != -1:
                nPosEnd = html.find( '</tr>', nPos + nTableFlag )
                if nPosEnd != -1:
                    doc = html[ nPos + nTableFlag : nPosEnd ]
                    nPos = nPosEnd
                else:
                    pass
            else:
                break