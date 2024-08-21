import requests
from EmployeeApi import Employee

api = Employee("https://x-clients-be.onrender.com")

def test_add_new_employee():
    #Создать новую компанию
    name = "Тру-ля-ля"
    descr = "Музыкальная студия звукозаписи"
    result = api.create_company(name, descr)
    new_id = result["id"]

    #Поиск компании по ID
    new_company = api.get_company(new_id)
    companyId = new_company["id"]

    #Получить список сотрудников 
    body = api.get_employees_list(companyId)
    len_before = len(body)

    #Добавить нового сотрудника
    firstName = "Роза"
    lastName = "Барбоскина"
    middleName = "Мухтаровна"
    company = companyId
    email = "supersinger@gmail.com"
    url = "string"
    phone = "string"
    birthdate = "1991-09-11"
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = new_employee["id"]

    assert new_employee is not None

    #Получить список сотрудников
    body = api.get_employees_list(companyId)
    len_after = len(body)

    #Получить сотрудника по ID
    new_employee = api.get_employee(emp_id)
    employee_id = new_employee["id"]
    assert len_after - len_before == 1
    assert body[-1]["firstName"] == "Роза"
    assert body[-1]["lastName"] == "Барбоскина"
    assert body[-1]["middleName"] == "Мухтаровна"
    assert body[-1]["companyId"] == companyId
    assert body[-1]["phone"] == "string"
    assert body[-1]["birthdate"] == "1991-09-11"
    assert body[-1]["isActive"] == True
    assert body[-1]["id"] == emp_id

def test_get_an_employee_by_id():
    #Создать новую компанию
    name = "Супер FooT"
    descr = "Мастерская обуви"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]

    #Поиск компании по ID
    new_company = api.get_company(new_id)
    companyId = new_company['id']

    # получить список сотрудников 
    body = api.get_employees_list(companyId)
    begin_list = len(body)

    # добавить нового сотрудника
    firstName = "Иван"
    lastName = "Тапкин"
    middleName = "Шпилькович"
    company = companyId
    email = "crocs@mail.ru"
    url = "string"
    phone = "string"
    birthdate = "2000-02-20"
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate,isActive=1)
    emp_id = new_employee["id"]

    assert new_employee is not None

    #Получить список сотрудников 
    body = api.get_employees_list(companyId)
    after_list = len(body)
    assert after_list - begin_list == 1

    #Получить сотрудника по ID
    new_employee = api.get_employee(emp_id)
    employee_id = new_employee["id"]
    assert body[-1]["firstName"] == "Иван"
    assert body[-1]["lastName"] ==  "Тапкин"
    assert body[-1]["middleName"] == "Шпилькович"
    assert body[-1]["companyId"] == companyId
    assert body[-1]["phone"] ==  "string"
    assert body[-1]["birthdate"] == "2000-02-20"
    assert body[-1]["isActive"] == True
    assert body[-1]["id"] == emp_id

def test_change_employee_information():
    #Создать новую компанию
    name = "Тик-так"
    descr = "Ремонт часов"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]

    #Поиск компании по ID
    new_company = api.get_company(new_id)
    companyId = new_company["id"]

    #Добавить нового сотрудника
    firstName = "Василий"
    lastName = "Стерлков"
    middleName = "Циферблатович"
    company = companyId
    email = "clock123@yandex.ru"
    url = "string"
    phone = "string"
    birthdate = "1989-08-09"
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = new_employee["id"]

    #Получить список сотрудников
    body = api.get_employees_list(companyId)

    #Получить сотрудника по ID
    new_employee = api.get_employee(emp_id)
    employee_id = new_employee["id"]
    assert body[-1]["firstName"] == "Василий"
    assert body[-1]["lastName"] ==  "Стерлков"
    assert body[-1]["middleName"] == "Циферблатович"
    assert body[-1]["companyId"] == companyId
    assert body[-1]["phone"] ==  "string"
    assert body[-1]["birthdate"] == "1989-08-09"
    assert body[-1]["isActive"] == True
    assert body[-1]["id"] == emp_id

    # Изменить информацию о сотруднике
    new_lastName = "Шестерёнков"
    new_email = "clock_the_best@yandex.ru"
    new_url = "_Updated_"
    new_phone = "Updated"
    new_isActive = False
    edited = api.change_employee(employee_id, new_lastName, new_email, new_url, new_phone, new_isActive)
    assert edited["email"] == "clock_the_best@yandex.ru"
    assert edited["url"] == "_Updated_"
    assert edited["isActive"] == False