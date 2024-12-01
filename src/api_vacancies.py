import requests
from abc import ABC, abstractmethod


class ApiVacancies(ABC):
    """Абстрактный класс получения вакансий по API"""

    @abstractmethod
    def load_vacancies(self, keyword):
        pass


class HeadHunter(ApiVacancies):
    """Класс получения вакансий с сайта HeadHunter"""

    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "page": 0, "per_page": 100}
        self.vacancies = []

    def load_vacancies(self, keyword):
        """Метод получения вакансий"""
        self.params["text"] = keyword
        while self.params.get("page") != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()["items"]
            self.vacancies.extend(vacancies)
            self.params["page"] += 1
            return vacancies