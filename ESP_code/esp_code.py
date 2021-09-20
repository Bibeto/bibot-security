import urequests as requests 
# import machine 

url = ""

headers = {'X-AIO-Key': 'xxxxxxxxxxxxxxxxxxx',
           'Content-Type': 'application/json'}

data = '{"value": "50"}'

r = requests.post(url, data=data, headers=headers)
results = r.json()
print(results)