import requests


response = requests.get('https://api.hh.ru/vacancies')

# vacancy list
vacancy_list = []
vacancies = response.json()['items']
for vacancy in vacancies:
    name = vacancy['name']
    vacancy_list.append(name)

# vacancy id list
vacancy_id_list = []
for vacancy_id in vacancies:
    name = vacancy_id['id']
    vacancy_id_list.append(name)


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


# experience list
experience_list = []
for experience in vacancies:
    name = experience['experience']['name']
    experience_list.append(name)


# employer list
employer_list = []
for employer in vacancies:
    name = employer['employer']['name']
    employer_list.append(name)

