import requests

url='https://jsonplaceholder.typicode.com/posts/'
data={
    'userId':1,
    'title':'homework',
    'body':'JeongSeungHo'
}
response = requests.post(url,json=data)
response = response.json()
title = response['title']
body = response['body']
userid = response['userId']
id = response['id']

file = open('result.txt','w')

file.write(f'title : {title}\n')
file.write(f'body :{body}\n')
file.write(f'userId :{userid}\n')
file.write(f'id : {id}\n')

file.close()
