from smartphone import Smartphone

catalog = []
catalog.append(Smartphone("Samsung", "Galaxy S23", "+79012345678"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 13Pro", "+79789012345"))
catalog.append(Smartphone("Asus", "Zenfone 10", "+79874442356"))
catalog.append(Smartphone("Huawei", "P60 Pro", "+79772890023"))
catalog.append(Smartphone("Apple", "iPhone 13pro", "+79378612378"))

for phone in catalog:
   print(f"{phone.brand}, {phone.model}, {phone.phone_number}")