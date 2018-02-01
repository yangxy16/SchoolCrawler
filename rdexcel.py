import xlrd
import json

def read_excel_xlrd():
    TC_workbook=xlrd.open_workbook(r"W020170616379651135432.xls")

    first_sheet=TC_workbook.sheet_by_index(0)
    
    sch_list = []
    index = 3
    
    while True:
        try:
            tmp = first_sheet.cell( index, 0 ).value
        except:
            tmp = None
        
        if tmp:
            v = []
            try:
                for i in range( 6 ):
                    v.append( first_sheet.cell( index, i ).value )
                tmp = first_sheet.cell( index, 6 ).value
                if tmp:
                    v.append( tmp )
                else:
                    v.append( '公办' )
                sch_list.append( v )
            except:
                pass
        else:
            break
        index += 1
    
    f = open( 'gflist.txt', 'w', encoding = 'utf-8' )
    for sch in sch_list:
        v = { 'name' : sch[1].replace('\n', ''),'belongs' : sch[3].replace('\n', ''), 'code' : sch[2], 'area' : sch[4].replace('\n', ''), 'level' : sch[5], 'public': sch[6] }
        f.write( json.dumps( v, ensure_ascii = False ) + '\n' )
    f.close()
    
if __name__=="__main__":
    read_excel_xlrd()