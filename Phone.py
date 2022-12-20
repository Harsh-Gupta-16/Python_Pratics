import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
number = "+918527637364"

ch_number = phonenumbers.parse(number,"CH")
print('Country Name of the number: ',geocoder.description_for_number(ch_number,"en"))
service_numner = phonenumbers.parse(number,'RO')
print('Service Provider of the number: ',carrier.name_for_number(service_numner,'en'))
