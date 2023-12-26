import requests
import json
from bs4 import BeautifulSoup as Bs
from fake_headers import Headers

URL = "https://spb.hh.ru/search/vacancy?area=1&area=2"
SEARCH_KEY = "python"
KEYWORDS = ["Django", "Flask"]
PERIOD = 7
CURRENCY = {"rub": '₽', "dol": "$", "eur": "€"}
headers = Headers(os="win", browser="chrome")


def get_soup():
    params = {
             "text": SEARCH_KEY,
             "search_period": PERIOD,
             "only_with_salary": "true"
             }
    response = requests.get(URL, headers=headers.generate(), params=params)
    response.encoding = "utf-8"
    return Bs(response.text, "lxml")


def filter_soup(soup, goal):
    result = []
    cur = CURRENCY[goal]
    vacancy_list = soup.find_all('div', class_='vacancy-serp-item-body__main-info')
    for item in vacancy_list:
        url_vacancy = item.find("a", class_='serp-item__title').get("href")
        title = item.find("a", class_='serp-item__title').text
        salary = item.find("span", class_="bloko-header-section-2").text
        company = item.find("a", class_="bloko-link bloko-link_kind-tertiary").text
        city = item.find("div", class_="vacancy-serp-item__info").find_all("div", class_="bloko-text")[1].text
        response = requests.get(url_vacancy, headers=headers.generate())
        vacancy = Bs(response.text, "lxml")
        description = vacancy.find("div", class_="vacancy-description")
        description = description.text if description else "not found"
        if all(word in description for word in KEYWORDS) and salary.endswith(cur):
            result.append({
                          "title": title,
                          "url": url_vacancy,
                          "salary": (salary := salary.replace(' ', ' ')),
                          "company": (company := company.replace('\xa0', ' ')),
                          "city": city.split(",")[0]
                          })
    print(f"Найдено : {len(result)} вакансий")
    return result


def dump_json(vacancies):
    with open("vacancies.json", "w", encoding="utf-8")as f:
        json.dump(vacancies, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    jobs = get_soup()
    wish = filter_soup(jobs, 'rub')
    dump_json(wish)


