import json
import requests
import time

from fake_headers import Headers
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tqdm import tqdm


class Scraper:
    """класс для сбора данных о вакансиях с hh

    атрибуты:
     __driver, __ref только для использования внутри функций класса
    vacancies хранит данные после получения, можно посмотреть, передав объект в print

    методы:
    set_params - настройка строки запроса к hh
    fetch_vacancies - получение данных

    """
    def __init__(self):
        options = Options()
        options.add_argument("--headless")
        self.__driver = webdriver.Chrome(options=options)
        self.__ref = "https://spb.hh.ru/search/vacancy?area=1&area=2&only_with_salary=true"
        self.vacancies = []

    def __str__(self):
        res = f"{'job_title':80}|{'company':50}|{'salary':20}|{'url'}\n"
        for el in self.vacancies:
            res += f"{el['job_title']:80}|{el['company']:50}|{el['salary']:20}|{el['url']}\n"
        return res

    @staticmethod
    def is_connect(ref):
        """проверка корректности адреса"""
        headers = Headers(os="win", browser="chrome")
        return requests.get(ref, headers=headers.generate()).status_code == 200

    def set_params(self, *, keywords: list=["python"], period=3):
         """добавляет параметры в url-адрес, если получается корректным"""
         new_ref = self.__ref + f"&text={'+'.join(keywords)}&search_period={period}"
         if self.is_connect(new_ref):
             self.__ref = new_ref
         else:
             print("Invalid parameters")

    def fetch_vacancies(self) -> None:
        """ использует вебдрайвер объекта(self.__driver) и его ссылку(self.__ref),
        чтобы получить данные и сохранить их в виде списка словарей в self.vacancies"""
        browser = self.__driver
        browser.get(self.__ref)
        counter = int(browser.find_element(By.CSS_SELECTOR, "h1[class='bloko-header-section-3']").text.split()[0])
        scale = tqdm(range(counter), postfix="scraped", position=0)
        jobs = set()
        page = 1
        while counter >= 0:
            WebDriverWait(browser, 1).until(
                EC.presence_of_element_located((By.CLASS_NAME, "vacancy-serp-item-body__main-info"))
            )
            url_vacancy = browser.find_elements(By.CLASS_NAME, 'serp-item__title')
            urls = [i.get_attribute("href") for i in url_vacancy]
            titles = browser.find_elements(By.CLASS_NAME, 'serp-item__title')
            counter -= len(titles)
            titles = [i.text for i in titles]
            salaries = [i.text.replace("\u202f", " ") for i in
                        browser.find_elements(By.CLASS_NAME, 'bloko-header-section-2')]
            companies = [el.text for el in
                         browser.find_elements(By.CSS_SELECTOR, "a[class='bloko-link bloko-link_kind-tertiary']")]
            for title, url, salary, company in zip(titles, urls, salaries, companies):
                if url not in jobs:
                    jobs.add(url)
                    item = {"job_title": title,
                            "salary": salary,
                            "company": company,
                            "url": url
                            }
                    self.vacancies.append(item)
                scale.update(1)
                # sleep просто для вида, до 50 вакансий со страницы в один момент получаются
                time.sleep(0.2 if counter <= 50 else 0)
            if counter > 0:
                page += 1
                url = self.__ref + f"page={page}"
                browser.get(url)


def filter_jobs(vacancies: list, cond):
    """принимает список словарей, возвращает отфильтрованный
    параметром должен быть указан один из реализованных(пока это "rub" или "dol")
    """
    conditions = {"rub": lambda x: x["salary"].endswith("₽"),
                  "dol": lambda x: x["salary"].endswith("$")
                  }
    if cond not in conditions:
        print("Unknown filter")
        return vacancies
    return list(filter(conditions[cond], vacancies))


def save_jobs(jobs: list, filename, *, add: bool=False):
    """сохраняет список словарей в файл, если передать параметр add=True, то данные не перезапишут старые"""
    with open(filename+".json", "a" if add else "w", encoding="utf-8") as output:
        json.dump(jobs, output, ensure_ascii=False, indent=4)
    print(f"\n{len(jobs)} vacancies with unique url saved in {filename}.json")


if __name__ == "__main__":
    scraper = Scraper()
    scraper.set_params(keywords=["python", "flask"], period=3)
    scraper.fetch_vacancies()
    print(scraper)
    save_jobs(filter_jobs(scraper.vacancies, "rub"), "jobs")










