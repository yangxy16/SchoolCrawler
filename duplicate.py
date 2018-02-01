import json

tblGF = {}
f = open( 'gflist.txt', 'r', encoding = 'utf-8' )
while True:
    line = f.readline()
    if not line:
        break
        
    tbl = json.loads( line )
    if tbl['name'] and len( tbl['name'] ) > 0:
        tblGF[tbl['name']] = tbl
f.close()
    
tblCralwer = {}
f = open( 'sch.txt', 'r', encoding = 'utf-8' )
while True:
    line = f.readline()
    if not line:
        break
    
    if len( line ) > 2:
        tbl = json.loads( line )
        if tbl['name'] and len( tbl['name'] ) > 0:
            tblCralwer[tbl['name']] = tbl
f.close()

# tblCralwerAttr = {}
# f = open( 'schAttr.txt', 'r', encoding = 'utf-8' )
# while True:
    # line = f.readline()
    # if not line:
        # break
    
    # if len( line ) > 2:
        # tbl = json.loads( line )
        # if tbl['name'] and len( tbl['name'] ) > 0:
            # tblCralwerAttr[tbl['name']] = tbl
# f.close()

f = open( 'duplicatesch.txt', 'w', encoding = 'utf-8' )
for k, v in tblGF.items():
    tbl1 = tblCralwer.get( k, None )
    tbl2 = tblCralwer.get( v['name'] + '（' + v['area'].replace( '市', '' ) + '）', None )
    if not tbl1:
        if not tbl2:
            f.write( json.dumps( v, ensure_ascii = False ) + '\n' )
f.close()