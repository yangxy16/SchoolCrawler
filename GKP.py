import requests as rq
from bs4 import BeautifulSoup
import random
import re
import json
import time

def getUA():
    return random.choice( [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
    ])
    
def downFile( url, savePath ):
    headers = { "User-Agent": getUA() }
    for i in range( 10 ):
        try:
            r = rq.get( url, headers = headers, stream = True )
            content_size = int( r.headers['content-length'] )
            with open( savePath, "wb") as f:
               for data in r.iter_content( chunk_size = 4096 ):
                   f.write(data)
            r.close()
            break
        except:
            continue
        finally:
            r.close()
        
f = open( './sch.txt', 'w', encoding = 'utf-8' )

for schId in range( 4000 ):
    schoolInfo = {}
    
    for i in range( 10 ):  
        print( "正在抓取：" + str( schId + 1 ), i )
        try:
            time.sleep( random.randint( 1, 3 ) )
            headers = { "User-Agent": getUA() }
            r = rq.get( 'http://www.gaokaopai.com/daxue-jianjie-{}.html'.format( schId + 1 ), headers = headers, proxies = None )
            
            if r.status_code == 200:
    
                schoolInfo['schoolId'] = schId + 1
            
                html = r.content.decode( 'utf-8' )
                html = html.replace( u'\u3000', u'' ).replace( u'\xa0', u'' ).replace( '\xa0', '' )

                #获取导航栏内容
                navList = []
                bsObj = BeautifulSoup( html, 'lxml' )
                for div in bsObj.find_all( 'div', { 'id' : 'locationNav' } ):
                    for subDiv in div.findAll( 'div', class_ = 'inner' ):
                        for href in subDiv.findAll( 'a' ):
                            navList.append( str( href ) )
                navList = navList[ 2 : 4 ]
                try:
                    navList[0] = re.findall( r'>(.*?)的大学</a>', navList[0], re.I | re.M | re.S )[0]      #地区
                    navList[1] = re.findall( r'>(.*?)</a>', navList[1], re.I | re.M | re.S )[0]            #大学名称
                    
                    schoolInfo['area'] = navList[0]
                    schoolInfo['name'] = navList[1]
                except:
                    #raise SystemExit( "错误的页面" )
                    continue    #错误的页面

                schImg = ''
                schoolInfo['logo'] = ''
                schoolInfo['logoUrl'] = ''
                #获取学校ICON
                for div in bsObj.find_all( 'div', class_ = 'schoolLogo' ):
                    for img in div.findAll( 'img' ):
                        schImg = img.attrs['src']
                        schoolInfo['logoUrl'] = schImg
                        break
                if len( schImg ) > 1:
                    saveName = schImg.replace( 'http://cdn.stc.gaokaopai.com/Public/Uploads/', '' )
                    downFile( schImg, './logo/' + saveName )
                    schoolInfo['logo'] = saveName

                #专业URL
                urlZY = 'http://www.gaokaopai.com/daxue-zhuanye-{}.html'.format( schId + 1 )
                
                #简介
                schIntro = ''
                try:
                    for div in bsObj.find_all( 'div', class_ = 'intro' ):
                        schIntro = re.findall( r'>(.*)</div>', str( div ), re.I | re.M | re.S )[0].replace( '\r\n', '' ).replace( '\n', '' ).replace( '<br/>', '\r\n' )
                except:
                    pass
                schoolInfo['intro'] = schIntro
                
                #创建时间、隶属于、学生人数、院士人数、重点学科、学校类型、博士点个数、硕士点个数
                itemAttrList = []
                for div in bsObj.find_all( 'div', class_ = 'baseInfo clearfix' ):
                    for ul in div.findAll( 'ul', class_ = 'baseInfo_left' ):
                        for li in ul.findAll( 'li', class_ = 'biItem' ):
                            title = re.findall( r'<span class="t">(.*?)</span>', str( li ), re.I | re.M | re.S )[0]
                            desp = re.findall( r'<div class="c">(.*?)</div>', str( li ), re.I | re.M | re.S )[0]
                            itemAttrList.append( ( title, desp ) )
                    for ul in div.findAll( 'ul', class_ = 'baseInfo_right' ):
                        for li in ul.findAll( 'li', class_ = 'biItem' ):
                            title = re.findall( r'<span class="t">(.*?)</span>', str( li ), re.I | re.M | re.S )[0]
                            desp = re.findall( r'<div class="c">(.*?)</div>', str( li ), re.I | re.M | re.S )[0]
                            itemAttrList.append( ( title, desp ) )
                
                schoolInfo['createtime'] = ''
                schoolInfo['belongs'] = ''
                schoolInfo['studentCount'] = ''
                schoolInfo['academicianCount'] = ''
                schoolInfo['keySubjectsCount'] = ''
                schoolInfo['schoolType'] = ''
                schoolInfo['doctorStationCount'] = ''
                schoolInfo['masterStationCount'] = ''
                    
                try:            
                    schoolInfo['createtime'] = itemAttrList[0][1]
                    schoolInfo['belongs'] = itemAttrList[1][1]
                    schoolInfo['studentCount'] = itemAttrList[2][1]
                    schoolInfo['academicianCount'] = itemAttrList[3][1]
                    schoolInfo['keySubjectsCount'] = itemAttrList[4][1]
                    schoolInfo['schoolType'] = itemAttrList[5][1]
                    schoolInfo['doctorStationCount'] = itemAttrList[6][1]
                    schoolInfo['masterStationCount'] = itemAttrList[7][1]
                except:
                    pass
                    
                #就业情况、
                schJobState = ''
                strFlag = '<div class="catTitle">'
                flagLength = len( strFlag )
                strFlagEnd = '</div>'
                nPos = 0
                
                schoolInfo['jobState'] = ''
                nPos = html.find( strFlag, nPos )
                if nPos != -1:
                    nEndPos = html.find( strFlagEnd, nPos + flagLength )
                    if nEndPos != -1:
                        doc = html[ nPos + flagLength : nEndPos + 1 ]
                        if doc.find( '就业情况' ) != -1:
                            nSubPos = html.find( '<div class="txt"', nEndPos + 1 )
                            if nSubPos != -1:
                                nEndSubPos = html.find( strFlagEnd, nSubPos + 1 )
                                if nEndSubPos != -1:
                                    doc = html[ nSubPos : nEndSubPos + len( strFlagEnd ) + 1 ]
                                    if doc and len( doc ) > 1:
                                        schJobState = re.findall( r'>(.*)</div>', doc, re.I | re.M | re.S )[0].replace('\r\n', '').replace('\n', '').strip()
                                        schoolInfo['jobState'] = schJobState
                #学生来源
                schStuArea = {}
                if nPos != -1:
                    nPos = html.find( strFlag, nPos + flagLength + 1 )
                    if nPos != -1:
                        nEndPos = html.find( strFlagEnd, nPos + flagLength )
                        if nEndPos != -1:
                            doc = html[ nPos + flagLength : nEndPos + 1 ]
                            if doc.find( '来源' ) != -1:
                                nSubPos = html.find( 'series:', nEndPos + 1 )
                                if nSubPos != -1:
                                    nEndSubPos = html.find( '}]', nSubPos + 1 )
                                    if nEndSubPos != -1:
                                        nSubSubPos = html.find( 'data:', nSubPos + 1 )
                                        if nSubSubPos != -1:
                                            doc = html[ nSubSubPos : nEndSubPos + 3 ]
                                            p = re.findall( '\[(.*?),(.*?)\]', doc, re.I | re.M | re.S )
                                            for s in p:
                                                schStuArea[ s[0].replace( '[', '' ).replace( ']', '' ).replace( '\"', '' ) ] = s[1]
                                                
                schoolInfo['studentFrom'] = schStuArea
                                                
                #男女比例
                try:
                    schStuBoys = re.findall( r'<div class="m"><div class="tip">男生<br />(.*?)</div></div>', html, re.I | re.M | re.S )[0]
                    schStuGirls = re.findall( r'<div class="f"><div class="tip">女生<br />(.*?)</div></div>', html, re.I | re.M | re.S )[0]
                except:
                    schStuBoys = '50'
                    schStuGirls = '50'
                
                schoolInfo['studentSex'] = { 'boys' : schStuBoys.replace('%', ''), 'girls' : schStuGirls.replace('%', '') }

                #特色专业、重点专业（国家重点、校级优势）
                schSpecialty = []
                schSpecialCounty = []
                schSpecialSelf = []
                
                for div in bsObj.find_all( 'div', class_ = 'modContent' ):
                    for subDiv in div.findAll( 'div', class_ = 'box txt' ):
                        strSubDiv = str( subDiv ).replace( '\t', '' ).replace( '\r\n' ,'' ).replace( '\n', '' ).strip()
                        if strSubDiv.find( 'style="display:block"' ) != -1:
                            p = re.findall( '<h3>(.*?)</h3>', strSubDiv, re.I | re.M | re.S )
                            for s in p:
                                schSpecialty.append( s )
                        else:
                            index = 0
                            for ul in subDiv.findAll( 'ul', class_ = 'list clearfix' ):
                                if index == 0:
                                    for li in ul.findAll( 'li' ):
                                        p = re.findall( '>(.*?)</a>', str( li )[5:], re.I | re.M | re.S )[0]
                                        schSpecialCounty.append( p )
                                    index = 1
                                else:
                                    for li in ul.findAll( 'li' ):
                                        p = re.findall( '>(.*?)</a>', str( li )[5:], re.I | re.M | re.S )[0]
                                        schSpecialSelf.append( p )
                                        
                schoolInfo['schoolSpecialty'] = schSpecialty
                schoolInfo['schoolSpecialCounty'] = schSpecialCounty
                schoolInfo['schoolSpecialSelf'] = schSpecialSelf

                #学费信息
                schMoney = ''
                if nPos != -1:
                    nPos = html.find( strFlag, nPos + flagLength + 1 )
                    if nPos != -1:
                        nEndPos = html.find( strFlagEnd, nPos + flagLength )
                        if nEndPos != -1:
                            doc = html[ nPos + flagLength : nEndPos + 1 ]
                            if doc.find( '学费信息' ) != -1:
                                nSubPos = html.find( '<div class="txt"', nEndPos + 1 )
                                if nSubPos != -1:
                                    nEndSubPos = html.find( strFlagEnd, nSubPos + 1 )
                                    if nEndSubPos != -1:
                                        doc = html[ nSubPos : nEndSubPos + len( strFlagEnd ) + 1 ]
                                        if doc and len( doc ) > 1:
                                            schMoney = re.findall( r'>(.*)</div>', doc, re.I | re.M | re.S )[0].replace('\r\n', '').replace('\n', '').replace('<br>', '').replace('<br />', '').replace('<br/>', '').strip()
                                            
                schoolInfo['schoolCoast'] = schMoney
                
                #学校地址、电话信息
                schLinkInfo = []
                for div in bsObj.find_all( 'div', class_ = 'infos' ):
                    for ul in div.findAll( 'ul' ):
                        for li in ul.findAll( 'li' ):
                            li = str( li ).replace( '\t', '' ).replace( '\r\n', '' ).replace( '\n', '' ).strip()
                            p = re.findall( r'<li><label>(.*?)</label>(.*?)</li>', li, re.I | re.M | re.S )
                            schLinkInfo.append( ( p[0][0].strip().replace( '：', '' ), p[0][1].strip() ) )
                            
                schoolInfo['schoolCity'] = ''
                schoolInfo['schoolAddr'] = ''
                schoolInfo['schoolTelphone'] = ''
                schoolInfo['schoolEmail'] = ''
                
                try:
                    schoolInfo['schoolCity'] = schLinkInfo[0][1]
                    schoolInfo['schoolAddr'] = schLinkInfo[1][1]
                    schoolInfo['schoolTelphone'] = schLinkInfo[2][1]
                    schoolInfo['schoolEmail'] = schLinkInfo[3][1]
                except:
                    pass
                
                #网址信息
                schHref = []
                for div in bsObj.find_all( 'div', class_ = 'website' ):
                    for a in div.findAll( 'a' ):
                        schHref.append( a.attrs['href'].strip() )
                        
                schoolInfo['schoolHomeUrl'] = ''
                schoolInfo['schoolEnrolUrl'] = ''
                
                try:
                    schoolInfo['schoolHomeUrl'] = schHref[0]
                    schoolInfo['schoolEnrolUrl'] = schHref[1]
                except:
                    pass
                
                print( schoolInfo )
                f.write( json.dumps( schoolInfo, ensure_ascii = False ) + '\r\n' )
                break
        except:
            continue

f.close()