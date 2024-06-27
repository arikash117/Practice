import requests


response = requests.get('https://api.hh.ru/vacancies')

# vacancy list
vacancy_list = []
vacancies = response.json()['items']
for vacancy in vacancies:
    name = vacancy['name']
    vacancy_list.append(name)


# area list
area_list = []
areas = response.json()['items']
for area in areas:
    name = area['area']['name']
    area_list.append(name)
