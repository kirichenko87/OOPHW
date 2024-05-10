class Animal:
	def __init__(self, name_animal, type_animal, age_animal):
		self.name_animal = name_animal
		self.type_animal = type_animal
		self.age_animal = age_animal

	def sound_animal(self):
		print('Какого ... , кто это... сюда поставил ?!?!')
	def getinfo(self):
		print(f'Вы выбрали {self.name_animal}, это очень редкий вид {self.type_animal}, сейчас ему {self.age_animal} '
			  f'издает он прекрасный звук в несвойственной манере {self.sound_animal()}')



