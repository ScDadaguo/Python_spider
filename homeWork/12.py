import xlrd
import xlwt
from xlutils.copy import copy

workbook = xlrd.open_workbook('中科启信通讯录.xls')
worksheet =workbook.sheet_by_name(u"员工工资表")
datalist=[]
for i in range(1,38):
    for j in range(4):
        if worksheet.row_values(i)[6*j]!='' :
            datalist.append(worksheet.row_values(i)[6*j:6*j+6])
for i in datalist:
    s=str(i[5])
    tmp=s[0:11]
    i[5]=tmp;

print (datalist)
# +++++++++++++++++++++++++++++++++
sexlist=[]
for i in datalist:
    sexlist.append(i[3])
sexset=set(sexlist)
sexlist=list(sexset)

sexdic={}
for i in sexlist:
    sexdic[i]=0;

for i in datalist:
    for key in sexdic:
        if i[3]==key:
            sexdic[key]+=1
print(sexdic)

# ++++++++++++++++++++++++++++++
count_5000=0
count_5000_10000=0
count_10000_15000=0
count_15000=0
for i in datalist:

    if int(i[4])<5000:
        count_5000+=1
    if int(i[4])>=5000 and int(i[4])<10000:
        count_5000_10000+=1
    if int(i[4])>=10000 and int(i[4])<15000:
        count_10000_15000+=1
    if int(i[4])>=15000 :
        count_15000+=1

print(count_5000)
print(count_5000_10000)
print(count_10000_15000)
print(count_15000)
gongzilist=[count_5000,count_5000_10000,count_10000_15000,count_15000]
print(gongzilist)


# +++++++++++++++++++++++++++++++++++
writebook=copy(workbook)
writesheet=writebook.get_sheet(4)

writesheet.write(0,0,"工资档次")
writesheet.write(0,1,"人数")
writesheet.write(0,2,"比例")
writesheet.write(0,3,"平均工资")
writesheet.write(1,0,"<5000")
writesheet.write(2,0,"5000—10000")
writesheet.write(3,0,"10000—15000")
writesheet.write(4,0,"10000—15000")
sum=0;
for i in datalist:
    sum+=i[4]
avg=sum/len(datalist)
writesheet.write(1,3,avg)
insertRow=0
for i in gongzilist:
    print(i)
    insertRow+=1
    writesheet.write(insertRow,1,i)
writebook.save("中科启信通讯录.xls")




font  =  xlwt.Font()
font.name = u"隶书"
#1-白，2-红，3-绿，4-蓝，5-黄，6-玫红，7-天蓝，8-黑
font.colour_index = 4
font.height = 20*16
borders = xlwt.Borders()
borders.left = xlwt.Borders.THIN
alignment = xlwt.Alignment()
alignment.horz = xlwt.Alignment.HORZ_CENTER
style = xlwt.XFStyle()
style.font = font
style.borders = borders
style.alignment = alignment















