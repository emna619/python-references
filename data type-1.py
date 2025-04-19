from types import MappingProxyType

name = "emna" 
age = 14  
is_student = True 
print(type(name)) 
print(type(age)) 
print(type(is_student)) 

# يعني انه ٢مع ٥ بعدها ضربها في ٥ كذا يساوي ٣٥
result = 2 + 5 
result *= 5 
print(result)

 #هاذي عملية تكتب و لا تحفظ كمتغير
print(2+3)

# هاذي معامل المساواة
result = 3 == 3
print(result)
# معامل عدم التساوي اذا مو متساوية يعني حقيقي

result = 4 != 4
print(result)

#معامل اصغر من او يساوي اذا صح يبقى حقيقي
result = 5 <=6 
print(result) 
 # معامل اصغر من او يساوي اذا صح يبقى حقيقي
result = 2 < 4  
print(result) 
 
name = "Miry" 
age = 12 
weight = 46.5 
# هنا بيحولها لعددعشري
float_number = float(age) 
print(float_number)

# هنا بيحولها لعدد صحيح
int_number = int(weight) 
print(int_number)


#lists القائمة  
names = ["emna", "miry", "lan"]# index begin 0

#في اخر السطر
names.append('dana') 
print(names) 
#اختيار الاسم  
names.insert(3, 'booo') 
print(names ) 
# لحذف  الاسم  
names.remove('dana') 
print(names) 
# دالة الحذف  
names.clear() 
print(names) 
#القائمة tuples ( لا يتغير) (من دون اقواس ) 
first_friend = ("miry", 'green', ' 12-10-2021') 
print(type(first_friend)) 
print(first_friend[0]) 
# dictionaries مفاتيح خاص ) 
first_friend = {'name':'miry', 'fav_color': 'green', 'birthdate': '12-10-2021' } 
print(type(first_friend)) 
print(first_friend['birthdate']) 
print(first_friend.values()) 
print(first_friend.keys())

