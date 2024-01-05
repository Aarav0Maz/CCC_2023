Chilis_values = {"Poblano": 1500, "Miralsol": 6000, "Serrano": 15500, "Cayenne": 40000, "Thai": 75000, "Habanero": 1500 }

NumberOfChili = int(input("enter the number of chili:"))

total_shu = 0

for _ in range(NumberOfChili):
    typeOfChilli = input("type of chili:").strip()

    total_shu += Chilis_values.get(typeOfChilli,0)

print("the SHU of the chili is", total_shu )





























