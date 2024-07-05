from smartphone import Smartphone

catalog = []
phone1 = Smartphone ("Samsung","Galaxy S23", "+79123456789")
phone2 = Smartphone ( "Apple", "iPhone 12", "+79098765432")
phone3 = Smartphone ("Xiaomi","Mi 11", "+79876543210")
phone4 = Smartphone ("Google","Pixel 5", "+79765432109")
phone5 = Smartphone ("OnePlus","g Pro", "+79654321098")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
        print (f" {phone.brand} - {phone.model}. {phone.phone_number}")