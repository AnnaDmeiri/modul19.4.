# base_url = "https://petfriends.skillfactory.ru/"
# data = {
#     'name': 'Мур-мурзик',
#     'animal_type': 'Проверка',
#     'age': '5',
#     'pet_photo': ('pet_photo', open('C:\Users\VTO24.01.22\PycharmProjects\pythonProject_modul19.4\tests\images\photo_2023-02-17_00-07-51.jpg', 'rb'), 'image/jpg')
# }

# headers = {'auth_key': api_key, 'accept': 'application/json'}
# response = requests.post(base_url + 'api/pets', headers=headers, data=data)
# print(response.status_code)

import requests
import os
import random



response = requests.get('')
print(response.headers)
# print(response.status_code, 'status_code')
# print(response.request,'request')
print (response.text,'text')


direcory = 'C:\\Users\VTO24.01.22\Desktop\Новая папка\\'
files = os.listdir(direcory)
print(files)