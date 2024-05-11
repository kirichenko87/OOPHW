class PassengerPlane:

	def __init__(self, manufacturer: str, airplane: str, sit_place: int, flight_height: int, speed_airplane: int):
		self.manufacturer = manufacturer
		self.airplane = airplane
		self.sit_place = sit_place
		self.flight_height = flight_height
		self.speed_airplane = speed_airplane

	def airplane_down(self):
		if self.flight_height == 0 and self.speed_airplane == 0:
			print('Самолет приземлился')

	def airplane_up(self):
		if self.flight_height > 500:
			print('Самолет взлетел')

	def change_height(self, new_height: int):
		self.flight_height = new_height

	def change_speed(self, new_speed: int):
		self.speed_airplane = new_speed

	def get_info(self):
		if self.flight_height < 1:
			print(f'Уважаемые дамы и господа, мы рады вас приветствовать на борту самолеты {self.airplane},'
				  f' произведеный компание {self.manufacturer}, на борту полная посадка {self.sit_place} человек, скоро мы взлетим')
		else:
			print(f'Уважаемые дамы и господа, мы рады вас приветствовать на борту самолеты {self.airplane},'
				  f' произведеный компание {self.manufacturer}, на борту полная посадка {self.sit_place} человек, скоро находимся на высоте'
				  f'{self.flight_height} скорость полета {self.speed_airplane}')


class Program:


	@staticmethod
	def main():
		pass
