NumPeople = int(input("Number of people attending"))
availibility = [input().strip() for _ in range(nun_people)]

day_count = [0, 0, 0, 0, 0]

for person_availibility in availibility: 
    for day in range(5):
        if person_availibility[day] == 'Y':
            day_count[day]

max_attendence