import threading
import os
from multiprocessing import Process

# 문자열 메서드
text = 'Master kim'
count = text.count('m') #문자열에서 m의 갯수를 센다
print(count)
find = text.find('kim') #문자열에서 kim의 위치를 찾는다 가장 먼저 나오는 위치를 찾는다
print(find)
try:
    index = text.index('kim') #문자열에서 kim의 위치를 찾는다 가장 먼저 나오는 위치를 찾는다
    print(index)
except ValueError:
    print('스승님을 찾을수 없습니다') 

team = ['master kim','seung','so','jin','min']
join_team = ",".join(team)
print(join_team)

upper_text = text.upper()
lower_text = text.lower()
print(upper_text)
print(lower_text)

replace_text = text.replace('Master','Captain')
print(replace_text)

team2 = "masterkim,seung,so,jin,min"
teams = team2.split(",")
print(teams)

#리스트 메서드
numbers = [1,2,3,4,5]
print(len(numbers))

del numbers[2]
print(numbers)

numbers = [1,2,3,4,5]
numbers.append(6)
print(numbers)

numbers = [5,4,2,1,3]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

team = ['master kim','seung','so','jin','min']
print(team.index('seung'))

numbers = [1,2,3,4,5]
numbers.insert(2,100)
print(numbers)

numbers.remove(100)
print(numbers)

numbers.pop(3)
print(numbers)

numbers = [1,2,3,3,4,5]
print(numbers.count(3))

numbers = [1,2,3]
numbers.extend([4,5,6])
print(numbers)

numbers = [1,2,3]
numbers += [4,5,6]
print(numbers)

#딕셔너리 메서드
empty_dict = {}

my_dict = {'apple':1 , 'banana':2 , 'orange':3}
print(my_dict)

my_dict['grage'] = 4
print(my_dict)

del my_dict['apple']
print(my_dict)

my_dict = {'apple':1 , 'banana':2 , 'orange':3}
print(my_dict['banana'])

key_list = list(my_dict.keys())
print(key_list)
value_list = list(my_dict.values())
print(value_list)

person = {'name': 'John', 'age':30, 'gender': 'male'}

items = person.items()
print(items)

person.clear()
print(person)

person = {'name': 'John', 'age':30, 'gender': 'male'}

name = person.get('name')
print(name)

email = person.get('email')
print(email)

email = person.get('email','이메일엄서요')
print(email)

print('name' in person)
print('email' in person)


def foo():
    print('This is foo')
    print('process id', os.getpid())
 
def bar():
    print('This is bar')
    print('process id', os.getpid())
 
def baz():
    print('This is baz')
    print('process id', os.getpid())

if __name__ == '__main__':
    print('process id', os.getpid())
    thread1 = threading.Thread(target=foo).start()
    thread2 = threading.Thread(target=bar).start()
    thread3 = threading.Thread(target=baz).start()


def foo():
    print('child process', os.getpid())
  
if __name__ == '__main__':
    print('parent process', os.getpid())

    child1 = Process(target=foo).start()
    child2 = Process(target=foo).start()
    child3 = Process(target=foo).start()