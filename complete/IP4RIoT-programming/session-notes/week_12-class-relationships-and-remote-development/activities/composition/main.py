from house import House

house = House("17, Street St, Applecross, WA 6000")
room1 = house.add_room("bedroom", 30.0)
room2 = house.add_room("bathroom", 25.0)

print(house.address)

