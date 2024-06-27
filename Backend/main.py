import requests


# список вакансии
response = requests.get('https://api.hh.ru/vacancies')

vacancy_list = []
vacancies = response.json()['items']
for vacancy in vacancies:
    name = vacancy['name']
    vacancy_list.append(name)
print(vacancy_list)
