import json

with open('SuperHero.json') as file:
    data = json.load(file)

members = data['members']

sorted_members = sorted(members, key=lambda x: x['age'], reverse=True)

for member in sorted_members:
    print(member['name'], member['age'])
