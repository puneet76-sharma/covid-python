# pip install covid

from covid import Covid

covid= Covid()

get_all_data=covid.get_data()


country=input("enter the country name to check the Covid data: ")
cases= covid.get_status_by_country_name(country)

# print("All Data", get_all_data)

for i in cases:
	print(i, ":", cases[i])

input()
