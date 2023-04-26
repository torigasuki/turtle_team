phone_book = {"john": "1234-5678", "jane":"2345-6789", "jack":"3456-7890"}

def search():
    name = yield
    while True:
        if name in phone_book:
            phone_number = phone_book[name]
        else:
            phone_number = "Not found"
        name = yield phone_number
        print(name)

search_coroutine = search()
next(search_coroutine)

result = search_coroutine.send("john")
print(result)

result = search_coroutine.send("jane")
print(result)

result = search_coroutine.send("jack")
print(result)

