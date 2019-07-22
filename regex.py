import re

def find_phone_num(phone_num):
	phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
	phone_num_object = phone_num_regex.findall(phone_num)
	return phone_num_object

phone_num = "My number is 415-555-4242 415-555-4234."
phone_num_object = find_phone_num(phone_num)

# if phone_num_object is not None:
if len(phone_num_object) != 0:
	# print(phone_num_object)

	for phone_n in phone_num_object:
		print(phone_n);
else:
	print("Phone Number not exist in the given string")