import requests
num=requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&lang="+"en"+"&format=json")
print(num.status_code)
print(num.content)