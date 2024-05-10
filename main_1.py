class Animal:
	def __init__(self, name_animal: str, type_animal: str, age_animal: int, sound_txt : str):
		self.name_animal = name_animal
		self.type_animal = type_animal
		self.age_animal = age_animal
		self.sound_txt = sound_txt
	def sound_animal (self):
		print(f'Наша {self.name_animal}, когда видит незнакомца всегда издает этот тошный звук {self.sound_txt}')


	def get_info(self):
		print(f'Вы выбрали {self.name_animal}, это очень редкий вид {self.type_animal}, сейчас ему {self.age_animal} '
			  f' при виде соперника издает {self.sound_txt}, пытаясь привести к бегству подлеца!')


class Program:
	@staticmethod
	def main():
		animal_1 = Animal('Геннадич', 'Гусь', 6, 'Га-Га')
		animal_1.sound_animal()
		animal_1.get_info()
