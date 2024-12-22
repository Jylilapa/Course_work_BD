import psycopg2
from src.config import config


class DBManager:
    """класс для подключения к БД PostgreSQL"""

    def __init__(self, db_name):
        self.__db_name = db_name

    def __execute_query(self, query):
        con = psycopg2.connect(dbname=self.__db_name, **config())
        with con:
            with con.cursor() as cur:
                cur.execute(query)
                result = cur.fetchall()
        con.close()
        return result

    def get_companies_and_vacancies_count(self):
        """получает список всех компаний и количество вакансий у каждой компании"""
        query = (
            "SELECT e.name, COUNT(v.id) AS vacancy_count FROM employers e "
            "JOIN vacancies v ON e.id = v.employer GROUP BY e.name"
        )
        return self.__execute_query(query)

    def get_all_vacancies(self):
        """получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты
        и ссылки на вакансию"""
        query = (
            "SELECT vacancies.name, salary_from, salary_to, employer FROM vacancies "
            "JOIN employers ON vacancies.employer = employers.id"
        )
        return self.__execute_query(query)

    def get_avg_salary(self):
        """получает среднюю зарплату по вакансиям"""
        query = "SELECT AVG(salary_from) FROM vacancies"
        return self.__execute_query(query)

    def get_vacancies_with_higher_salary(self):
        """получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        query = "SELECT * FROM vacancies WHERE salary_from > (SELECT AVG(salary_from) FROM vacancies)"
        return self.__execute_query(query)

    def get_vacancies_with_keyword(self, user_query):
        """получает список всех вакансий, в названии которых содержатся переданные в метод слова"""
        query = f"SELECT * FROM vacancies WHERE name LIKE '%{user_query}%'"
        return self.__execute_query(query)
