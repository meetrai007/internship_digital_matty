import xlwt
import xlrd

workbook1=xlwt.Workbook()
sheet1=workbook1.add_sheet("sheet1")
sheet1.write(0,0,"meet")
sheet1.write(0,1,"akash")
sheet1.write(0,2,"amit")
workbook1.save("1st_workbook.xls")

wb = xlrd.open_workbook("1st_workbook.xls")
sheet = wb.sheet_by_index(0)
print (sheet.cell(0,0).value)
