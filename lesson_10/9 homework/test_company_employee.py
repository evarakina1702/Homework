import allure
from EmployeeAPI import EmployeeApi
from CompanyID import CompanyID
from EmployeeTable import EmployeeTable


base_url = 'https://x-clients-be.onrender.com'
employee_api = EmployeeApi(base_url)

db_connection_string = ('postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0')
company_id = CompanyID(db_connection_string)
employee_table = EmployeeTable(db_connection_string)

# Новая компания
name = "Тик-так"
description = "Ремонт часов"

# Новый сотрудник
id = 1
first_name = "Василий"
last_name = "Стерлков"
middle_name = "Циферблатович"
email = "clock123@yandex.ru"
url = "string"
phone = "+string"
birthdate = "1989-08-09"
is_active = True


@allure.title('Получить список сотрудников')
@allure.description('Тест получения списка сотрудников с помощью API')
@allure.feature('Сотрудник')
@allure.severity(allure.severity_level.NORMAL)
def test_get_employee_list():
    #Создать новую компанию в базе данных
    company_id.create(name, description)
    new_company_id = company_id.get_max_id()

    #Создать нового сотрудника в базе данных
    employee_table.create(first_name, last_name, phone, new_company_id, is_active)
    new_employee_id = employee_table.get_max_id()

    #Получить список сотрудников с помощью API
    employee_list_api = employee_api.get_employee_list(new_company_id)

    #Получить список сотрудников в базе данных
    employee_list_db = employee_table.get_company_employees(new_company_id)

    #Удалить нового сотрудника и новую компанию из базы данных
    employee_table.delete(new_employee_id)
    company_id.delete(new_company_id)

    with allure.step('Check new id is in the list'):
        assert employee_list_api[0]["id"] == new_employee_id, \
            "Employee's ID is not equal"
    with allure.step('Check that API list is equal DB list'):
        assert len(employee_list_api) == len(employee_list_db)


@allure.title('Создать сотрудника')
@allure.description('Тест создания сотрудника с помощью API')
@allure.feature('Сотрудник')
@allure.severity(allure.severity_level.CRITICAL)
def test_create_employee():
    #Создать новую уомпанию в базе данных
    company_id.create(name, description)
    new_company_id = company_id.get_max_id()

    #Создать нового сотрудника с помощью API
    new_employee = employee_api.add_employee(id, first_name, last_name, middle_name, new_company_id, email, url, phone, birthdate, is_active)
    new_employee_id = new_employee["id"]

    #Получить сотрудника из базе данных
    employee = employee_table.get_employee_by_id(new_employee_id)

    #Удалить нового сотрудника и новую компанию из базы данных
    employee_table.delete(new_employee_id)
    company_id.delete(new_company_id)

    with allure.step('Проверьте, был ли создан новый сотрудник в DB'):
        assert len(employee) == 1, "Сотрудник не был создан"


@allure.title('Получить сотрудника')
@allure.description('Протестируйте сотрудника с помощью API')
@allure.feature('Сотрудник')
@allure.severity(allure.severity_level.NORMAL)
def test_get_employee():
    #Создать новую компанию в базе данных
    company_id.create(name, description)
    new_company_id = company_id.get_max_id()

    #Создать нового сотрудника в базе данных
    employee_table.create(first_name, last_name, phone, new_company_id, is_active)
    new_employee_id = employee_table.get_max_id()

    #Получите информацию о сотруднике с помощью API
    employee = employee_api.get_employee(new_employee_id)

    #Удалить нового сотрудника и новую компанию из базы данных
    employee_table.delete(new_employee_id)
    company_id.delete(new_company_id)

    with allure.step('Проверьте, возвращается ли новый идентификатор из API'):
        assert employee["id"] == new_employee_id
    with allure.step('Проверьте, чтобы имя нового сотрудника возвращалось из API'):
        assert employee["firstName"] == first_name
    with allure.step('Проверьте длину тела срабатывания'):
        assert len(employee) == 12


@allure.title('Сменить сотрудника с помощью API')
@allure.description('Протестируйте смену сотрудника с помощью API')
@allure.feature('Сотрудник')
@allure.severity(allure.severity_level.NORMAL)
def test_change_employee_by_api():
    #Создать новую компанию в базе данных
    company_id.create(name, description)
    new_company_id = company_id.get_max_id()

    #Создать нового сотрудника в базе данных
    employee_table.create(first_name, last_name, phone, new_company_id, is_active)
    new_employee_id = employee_table.get_max_id()

    #Исправьте ошибку сотрудника с помощью API
    new_email = "new_new@gmail.com"
    new_url = "_Updated_"
    new_is_active = False
    patched_employee = employee_api.change_employee(new_employee_id, new_email, new_url, new_is_active )
    with allure.step('Проверьте исправленную информацию о сотруднике из API'):
        assert patched_employee["id"] == new_employee_id
        assert patched_employee["email"] == new_email
        assert patched_employee["url"] == new_url
        assert patched_employee["isActive"] == new_is_active

    #Получите исправленную информацию о сотруднике из базы данных
    employee = employee_table.get_employee_by_id(new_employee_id)

    #Удалить нового сотрудника и новую компанию из базы данных
    employee_table.delete(new_employee_id)
    company_id.delete(new_company_id)

    with allure.step('Проверьте исправленную информацию о сотруднике из базы данных'):
        assert employee[0][0] == new_employee_id
        assert employee[0][8] == new_email
        assert employee[0][10] == new_url
        assert employee[0][1] == new_is_active


@allure.title('Изменить сотрудника по базе данных')
@allure.description('Тестовое изменение сотрудника по базе данных')
@allure.feature('Сотрудник')
@allure.severity(allure.severity_level.NORMAL)
def test_change_employee_by_db():
    #Создать новую компанию в базе данных
    company_id.create(name, description)
    new_company_id = company_id.get_max_id()

    #Создать нового сотрудника в базе данных
    employee_table.create(first_name, last_name, phone, new_company_id, is_active)
    new_employee_id = employee_table.get_max_id()

    #Исправьте ошибку сотрудника с помощью API
    new_email = "clock_the_best@yandex.ru"
    new_url = "_Updated_"
    new_is_active = False
    employee_table.update(new_employee_id, new_email, new_url, new_is_active)

    #Получить информацию сотрудников с помощью API
    employee = employee_api.get_employee(new_employee_id)

    with allure.step('Проверьте исправленную информацию о сотруднике из API'):
        assert employee["id"] == new_employee_id
        assert employee["email"] == new_email
        assert employee["avatar_url"] == new_url
        assert employee["isActive"] == new_is_active