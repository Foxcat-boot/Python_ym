import xlwt
workbook = xlwt.Workbook(encoding='utf-8')
sheet = workbook.add_sheet('pvuv_sheet')

# д�����
for col,column in enumerate(columns):
    sheet.write(0, col, column)
# д��ÿһ��
for row, data in enumerate(datas):
    for col, column_data in enumerate(data):
        sheet.write(row+1, col, column_data)

workbook.save('./output/pvuv_xlwt.xls')