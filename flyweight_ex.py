class CarFamilies:

	car_family = {}

	def __new__(cls, car_family_id, car_name):
		try:
			id = cls.car_family[car_family_id]
		except KeyError:
			id = object.__new__(cls)
			cls.car_family[car_family_id] = id
		return id

	
car_data = (( 1, 'Audi'), (2, 'Ferrari'), (1, 'Audi'))

car_family_objects = []

for i in car_data:
        obj = CarFamilies(i[0], i[1])
        car_family_objects.append(obj)

for i in car_family_objects:
	print("id = " + str(id(i)))
	
