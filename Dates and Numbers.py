#القيمة المطلقة 
number = 3
print(pow(number,2 ))

#القيمة الاكبر 
tal  = 150, 160,170,180,200
print(max(tal))
print(min(tal))
print(sum(tal))

#الجذر التربيعي 
import math 
number = 144
print (math.sqrt(number))

#باقي القسمة
import math
print( math.remainder(9,3))

#الرقم عشوائي
import random
print(random.randint(1,5))

#انشاء التاريخ 
# date الدالة
# datetimeالمكتبة 
import datetime
date = datetime.date(2022, 1,1)
print(date.year)

#انشاء وقت 
import datetime
time= datetime.time (13,15,14)
print(time .second)

#الوقت الحالي
import datetime
now= datetime.datetime .today()
print(now.month)

#تحويل التاريخ الي نص 
import datetime
date = datetime.date (2022,2,1)
time = datetime.time (21,2,3)

print(date )
print(time)
print ( date. strftime('%A %B %Y'))
print( time.strftime('%I %M %S' ))







