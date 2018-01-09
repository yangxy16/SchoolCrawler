# /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    页面内容解析器封装
'''
import re
from bs4 import BeautifulSoup

class GKCHSIParser:

    @staticmethod
    def parseDocument( htmlDoc ):
        html = htmlDoc
        tblFlag = '<table width="100%" border="0" align="center" cellpadding="3" cellspacing="1" bgcolor="#E1E1E1" style="margin:0px auto;">'
        nPos = html.find( tblFlag )
        if nPos != -1:
            nEndPos = html.find( '</table>', nPos + len( tblFlag ) )
            if nEndPos != -1:
                html = html[ nPos : nEndPos + 9 ]

        trFlag = '<tr bgcolor="#FFFFFF" onMouseOver="this.style.background='
        nPos = html.find( trFlag, 1 )  
        dataList = []
        
        while nPos != -1:
            nEndPos = html.find( '</tr>', nPos + len( trFlag ) )
            if nEndPos != -1:
                doc = html[ nPos : nEndPos + 6 ].strip()
                nPos = html.find( trFlag, nEndPos )
                bsObj = BeautifulSoup( doc, 'lxml' )
                for tr in bsObj.find_all( 'tr' ):
                    tdList = []
                    for td in tr.findAll( 'td' ):
                        tdList.append( str( td ) )
                    item = {}
                    if tdList and len( tdList ) > 0:
                        td = str( tdList[0] )
                        itemSchool = re.findall( r'<a href="(.*?)" target=(.*?)>(.*?)</a>', td, re.I | re.M | re.S )
                        if itemSchool:
                            item['url'] = 'http://gaokao.chsi.com.cn' + itemSchool[0][0]
                            item['name'] = itemSchool[0][2]
                        else:
                            item['url'] = ''
                            item['name'] = re.findall( r'<td align="left">(.*?)</td>', td, re.I | re.M | re.S )[0].replace('\r','').replace('\t','').strip()
                        
                        item985 = '<span class="a211985 span985">985</span>'
                        item211 = '<span class="a211985 span211">211</span>'
                        itemYan = '<span class="a211985 spanyan">研</span>'
                        
                        if td.find( item985 ) != -1:
                            item['985'] = True
                        else:
                            item['985'] = False
                            
                        if td.find( item211 ) != -1:
                            item['211'] = True
                        else:
                            item['211'] = False
                            
                        if td.find( itemYan ) != -1:
                            item['yan'] = True
                        else:
                            item['yan'] = False
                            
                        td = str( tdList[1] )
                        item['area'] = td[ 4: -5 ].strip()
                        
                        td = str( tdList[2] )
                        item['area'] = td[ 17: -5 ].strip()
                        
                        td = str( tdList[3] )
                        item['xueli'] = td[ 4: -5 ].replace( '\r\t', '' ).strip()
                        
                        td = str( tdList[4] )
                        item['banxue'] = td[ 4: -5 ].strip()
                        
                        td = str( tdList[5] )
                        item['yuanxiao'] = td[ 4: -5 ].strip()
                        
                        dataList.append( item )
            else:
                break
 
        #查找下一页
        itemUrl = None
        bsObj = BeautifulSoup( htmlDoc, 'lxml' )
        for ul in bsObj.find_all( 'ul', class_ = 'ulPage' ):
            for li in ul.findAll( 'li' ):
                li = str( li )
                itemUrl = re.findall( r'<a href="(.*)">下一页</a>', li, re.I | re.M | re.S )
                if itemUrl and len( itemUrl ) > 0:
                    itemUrl = itemUrl[0]
                    break
            if itemUrl:
                break
        
        return itemUrl, dataList