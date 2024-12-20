from src.bd_manager import DBManager
from src.bd_vacancies import create_database, create_tables, insert_data_in_tables


db_name = "cw5"
create_database(db_name)
create_tables(db_name)
insert_data_in_tables(db_name)

db = DBManager("cw5")

while True:
    print(
        "Здраствуй! Эта функция работает с данными о работодателях и вакансиях"
        " Для этого напишите цифру и получите результат от определенной функции"
        "1 - список всех компаний и количество вакансий у каждой компании."
        "2 - список всех вакансий с указанием названия компании, названия вакансии и зарплаты"
        "3 - выведет среднюю зарплату по вакансиям"
        "4 - список всех вакансий, у которых зарплата выше средней по всем вакансиям"
        "5 - список всех вакансий, в названии которых содержатся введенное Вами слово, например, python"
    )
    user_input = input("Какую функцию хотите вывести? Напишите номер: ")
    if user_input == "1":
        print(db.get_companies_and_vacancies_count())
    elif user_input == "2":
        (print(db.get_all_vacancies()))
    elif user_input == "3":
        print(db.get_avg_salary())
    elif user_input == "4":
        print(db.get_vacancies_with_higher_salary())
    elif user_input == "5":
        user_query = input("Введите слово для поиска по вакансиям: ")
        print(db.get_vacancies_with_keyword(user_query))
