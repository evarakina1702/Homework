from address import Address
from mailing import Mailing

to_address = Address ("12345", "Москва", "Брусилова", "21", "11" )
from_address = Address ("54321", "Саратов", "Астраханская", "10")
mailing = Mailing (to_address, from_address, 3500, "ABC123")

print(f"Отправление {mailing.trask} из {mailing.from_address.index}, {mailing.from_address.city}, "
      f" {mailing.from_address.street}, {mailing.from_address.house} - {mailing.to_address.apartment} "
      f"B {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
      f" {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")