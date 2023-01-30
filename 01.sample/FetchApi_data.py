import requests
import csv

url = 'https://raw.githubusercontent.com/akatsukioshiro/test_01/main/task02.json'

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}
response = requests.request("GET", url, headers=headers, data={})
myjson = response.json()
ourdata=[]
csvheader=['Name','Age']

for x in myjson['data']:
    listing =[x['name'],x['age']]
    ourdata.append(listing)

with open('FetchApi_data.csv','w',encoding='UTF8',newline='') as file:
    writer= csv.writer(file)

    writer.writerow(csvheader)
    writer.writerows(ourdata)

print(ourdata)
