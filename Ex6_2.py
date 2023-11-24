from datetime import datetime 
import calendar 
day=int(input("Nhập ngày:"))
month=int(input("Nhập tháng:"))
year=int(input("Nhập năm:"))
date= datetime(year,month,day)
print ((calendar.monthrange(year,month)))