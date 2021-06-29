import requests
import os

token = '28281f307e22ef0b1c8e93e1552b596481baa3be59aea1019b4765241f8ce47eaaa613d30a15940ec1203'

# links = ['my_suicide_in_the_dark', 'mandsm', 'vanna_ana', '2walls2', 'yavbzh']

ID = input()

data_collection = os.listdir("data")
if not data_collection:
    f = open('data/data1.txt', 'w', encoding='utf-8')
else:
    f = open('data/data' + str(int(data_collection[-1][4:-4]) + 1) + '.txt', 'w', encoding='utf-8')

json_response = requests.get(('https://api.vk.com/method/wall.get?domain={}&count=100&v=5.103&access_token=' + token).\
                                format(ID)).json()
if json_response.get('error'):
    print(json_response.get('error'))
else:
    for item in json_response['response']['items']:
        f.write(item['text'] + '\n')
offset = 0
for hundred in range(json_response['response']['count']//100):
    offset += 100
    json_response = requests.get(('https://api.vk.com/method/wall.get?domain={}&offset='+ str(offset) +'&count=100&v=5.103&access_token=' + token).\
                                format(ID)).json()
    if json_response.get('error'):
        print(json_response.get('error'))
    else:
        for item in json_response['response']['items']:
            f.write(item['text'] + '\n')

f.close();

