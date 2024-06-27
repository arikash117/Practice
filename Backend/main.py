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
for area in vacancies:
    name = area['area']['name']
    area_list.append(name)


# schedule list
schedule_list = []
for schedule in vacancies:
    name = schedule['schedule']['name']
    schedule_list.append(name)


# employment list
employment_list = []
for employment in vacancies:
    name = employment['employment']['name']
    employment_list.append(name)
print(employment_list)
