# Task №1


# class Patient:
#
# 	def __init__(self, full_name: str, age: int, ill: str):
# 		self.full_name = full_name
# 		self.age = age
# 		self.ill = ill
#
# 	def date_appointment(self, date: str, time: str):
# 		self.date = date
# 		self.time = time
# 		print(f'{self.full_name} вы успешно записаны на прием {self.date}')
#
# 	def __str__(self):
# 		return (f'ФИО: {self.full_name}\n'
# 				f'Возраст: {self.age}\n'
# 				f'Заболевание: {self.ill}\n'
# 				f'Дата Записаи на прием: {self.date} в {self.time}')
#
#
# class Program:
# 	@staticmethod
# 	def main():
# 		patient_1 = Patient('Иванов Петр Петрович', 43, 'ОРВИ')
# 		patient_1.date_appointment('28 Декабря', '13:45')
# 		print(patient_1)
#
#
# Program.main()

# TASK №2


#
# class TouristSpot:
# 	def __init__(self, place_name: str, country: str, type_place: str):
# 		self.place_name = place_name
# 		self.country = country
# 		self.type_place = type_place
#
# 	def place_visit(self, name_turist):
# 		self.name_turist = name_turist
# 		print(f'{self.name_turist} ! - это то самое чудесно место {self.place_name}')
# 	def __str__(self):
# 		return (f'\nТуристическая достопримечательность: {self.place_name}\n'
# 				f'Страна: {self.country}\n'
# 				f'Тип достопримечательности: {self.type_place}\n'
# 				f'Посетители: {self.name_turist}')
#
# class Program:
# 	def main():
# 		turist_1 = TouristSpot('Чарские пески', 'Россия', 'Природа')
# 		turist_1.place_visit('Евгений')
# 		print(turist_1)
# Program.main()

# TASK № 3

# class ModelWindow:
#
# 	def __init__(self, title_window: str, dot_left_up_coordinates_X: int, dot_left_up_coordinates_Y,
# 				 horizontal_size: int, vertical_size, color_window: str, visibility_window: bool,
# 				 visibility_frame_window: bool):
#
# 		self.title_window = title_window
# 		self.dot_left_up_coordinates_X = dot_left_up_coordinates_X
# 		self.dot_left_up_coordinates_Y = dot_left_up_coordinates_Y
# 		self.horizontal_size = horizontal_size
# 		self.vertical_size = vertical_size
# 		self.color_window = color_window
# 		self.visibility_window = visibility_window
# 		self.visibility_frame_window = visibility_frame_window
#
# 	def set_horizontal_movement(self, new_set_horizontal_movement: int):
#
# 		if not isinstance(new_set_horizontal_movement, int):
# 			raise Exception('Error')
#
# 		if self.horizontal_size + new_set_horizontal_movement > 0 and \
# 				self.horizontal_size + new_set_horizontal_movement < 1921:
# 			self.horizontal_size += new_set_horizontal_movement
#
# 	def set_vertical_movement(self, new_set_vertical_movement: int):
# 		if not isinstance(new_set_vertical_movement, int):
# 			raise Exception('Error')
#
# 		if self.vertical_size + new_set_vertical_movement > 0 and \
# 				self.horizontal_size + new_set_vertical_movement < 1081:
# 			self.horizontal_size += new_set_vertical_movement
#
# 	def set_color_window(self, new_color: str):
# 		self.color_window = new_color
#
# 	def set_size_window(self, new_size_horizontal=0, new_size_vertical=0):
#
# 		if not isinstance(new_size_horizontal, int) or not isinstance(new_size_vertical, int):
# 			raise Exception('Error')
# 		if self.horizontal_size + new_size_horizontal > 10 and self.horizontal_size + new_size_horizontal < 1920:
# 			self.horizontal_size += new_size_horizontal
# 		if self.vertical_size + new_size_vertical > 5 and self.vertical_size + new_size_vertical < 1080:
# 			self.vertical_size += new_size_vertical
#
# 	def set_new_color(self, new_color):
# 		self.color_window = new_color
#
# 	def is_visibiliti_window(self):
# 		return self.visibility_window
#
# 	def is_visibility_frame_window(self):
# 		return self.visibility_frame_window
#
# 	def set_visibility_window(self, value: bool):
# 		if isinstance(value, bool):
# 			self.visibility_window = value
#
# 	def set_visibility_frame_window(self, value: bool):
# 		if isinstance(value, bool):
# 			self.visibility_frame_window = value
#
# 	def __str__(self) -> str:
# 		return f'Заголовок окна: {self.title_window}\
#              координаты левого верхнего угла: {self.dot_left_up_coordinates_X}'
#
#
# class Program:
# 	@staticmethod
# 	def main():
# 		window_1 = ModelWindow('Главное окно', 0, 0, 920, 180, 'Синий', True, True)
# 		window_1.move_horizonral_vertikal
# Program.main()

# Task №4

#
# class ArrayUtils:
# 	@staticmethod
# 	def sum_elem(lst: list):
# 		"""
#         		Сложение элементов массива
#         		:param lst: Пренимает массив
#         		:return: Возвращает результат сложения элементов массива
#         """
# 		sum = 0
# 		for i in range(0, len(lst), 1):
# 			sum += lst[i]
# 		return sum
#
# 	@staticmethod
# 	def milt_elem(lst: list):
# 		"""
# 		        Умножение элементов массива
# 		        :param lst: Пренимает массив
# 		        :return: Возвращает результат умнижения элементов массива
# 		"""
# 		mult = 1
# 		for i in range(0, len(lst), 1):
# 			mult *= lst[i]
# 		return mult
#
# 	@staticmethod
# 	def find_max_elem_arr(lst: list):
# 		"""
# 				    Поиск максимального элемента массива
# 				    :param lst: Пренимает массив
# 				    :return: Возвращает результат максимальный элемент массива
# 		"""
# 		max_value = lst[0]
# 		for i in range(1, len(lst), 1):
# 			if max_value < lst[i]:
# 				max_value = lst[i]
# 		return max_value
#
# 	@staticmethod
# 	def find_min_elem_arr(lst: list):
# 		"""
# 					Поиск минимального элемента массива
# 					:param lst: Пренимает массив
# 					:return: Возвращает результат минимальный элемент массива
# 		"""
# 		min_value = lst[0]
# 		for i in range(1, len(lst), 1):
# 			if min_value > lst[i]:
# 				min_value = lst[i]
# 		return min_value
#
# 	@staticmethod
# 	def reverse_arr(lst: list):
# 		"""
# 					Поиск максимального элемента массива
# 					:param lst: Пренимает массив
# 					:return: Возвращает результат максимальный элемент массива
# 		"""
# 		return lst[::-1]
#
#
# class Program:
# 	@staticmethod
# 	def main():
# 		lst = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9]
# 		print(f'Сумма элементов массива: {ArrayUtils.sum_elem(lst)}')
# 		print(f'Произведение элементов массива: {ArrayUtils.milt_elem(lst)}')
# 		print(f'Максимальный элемент массива: {ArrayUtils.find_max_elem_arr(lst)}')
# 		print(f'Минимальный элемент массива: {ArrayUtils.find_min_elem_arr(lst)}')
# 		print(f'Массив с элементами в обратном порядке: {ArrayUtils.reverse_arr(lst)}')
#
#
# Program.main()

# Task №5

# class Vector:
# 	def __init__(self, x: float, y: float, z: float):
# 		self.x = x
# 		self.y = y
# 		self.z = z
#
# 	def __add__(self, other):
# 		"""
# 		Сложение векторов
# 		@param other:
# 		@return: В результате сложения векторов возвращает новый вектор
# 		"""
# 		new_x = self.x + other.x
# 		new_y = self.y + other.y
# 		new_z = self.z + other.z
# 		return Vector(new_x, new_y, new_z)
#
# 	def __sub__(self, other):
# 		"""
# 		Вычитание векторов
# 		@param other:
# 		@return: В результате вычитания векторов возвращает новый вектор
# 		"""
# 		new_x = self.x + other.x
# 		new_y = self.y + other.y
# 		new_z = self.z + other.z
# 		return Vector(new_x, new_y, new_z)
#
# 	def __mul__(self, other):
# 		"""
# 		Может использоваться как для векторного произведения так и умножения на число
# 		в зависимости от типа аргумента (вектор или число)
# 		@param other:
# 		@return: В результате выислений возвращает новый вектор
# 		"""
# 		if isinstance(self, Vector) and isinstance(other, Vector):
# 			new_x = self.y * other.z - self.z * other.y
# 			new_y = self.z * other.x - self.x * other.z
# 			new_z = self.x * other.y - self.y * other.x
#
# 		elif isinstance(other, int) or isinstance(other, float):
# 			new_x = self.x * other
# 			new_y = self.y * other
# 			new_z = self.z * other
# 		return Vector(new_x, new_y, new_z)
#
# 	@staticmethod
# 	def scalar_mult(v1, v2):
# 		"""
# 		Скалярное произведение
# 		@param v1:
# 		@param v2:
# 		@return: значение скалярного произведения
# 		"""
# 		new_x = v1.x * v2.x
# 		new_y = v1.y * v2.y
# 		new_z = v1.z * v2.z
# 		return new_x + new_y + new_z
#
# 	@staticmethod
# 	def calculating_norm_vector(value):
# 		"""
# 		Расчет нормы вектора (длины)
# 		@param self:
# 		@return: Значение нормы (длины) вектора
# 		"""
# 		return (value.x ** 2 + value.y ** 2 + value.z ** 2) ** 0.5
#
#
# 	def __str__(self):
# 		return f'вектор: {self.x, self.y, self.z}'
#
#
# class Programm:
# 	@staticmethod
# 	def main():
# 		v1 = Vector(1, 2, 3)
# 		v2 = Vector(3, 2, 1)
# 		print(f'Первый вектор: {v1}')
# 		print(f'Второй вектор: {v2}')
# 		print(f'Сложение векторов: {v1 + v2}')
# 		print(f'Разница векторов: {v1 - v2}')
# 		print(f'Разница векторов: {v2 - v1}')
# 		print(f'Скалярное произведение: {v1 * 123}')
# 		print(f'Скалярное произведение: {v2 * 3.14}')
# 		print(f'Векторное произведение векторов: {v1 * v2}')
# 		print(f'Векторное произведение векторов: {v2 * v1}')
# 		print(f'Скалярное произведение двух векторов равно: {Vector.scalar_mult(v1, v2)}')
# 		print(f'Длина вектора {v1} равна: {Vector.calculating_norm_vector(v1)}')
# 		print(f'Длина вектора {v2} равна: {Vector.calculating_norm_vector(v2)}')
#
#
# Programm.main()

#Task №6 (Не докнца решил)

# class Fraction:
# 	def __init__(self, numerator: int, denominator: int):
# 		self.numerator = numerator
# 		self.denominator = denominator
#
# 	def __add__(self, other):
# 		"""
# 		Сложение дробей
# 		@param other:
# 		@return: Возвращает новую дробь
# 		"""
# 		if not Fraction.division_zero(self.denominator, other.denominator):
# 			raise 'В знаменателе имеется ноль'
# 		else:
# 			if self.denominator == other.denominator:
# 				rez_plus_numerator = self.numerator + other.numerator
# 				return rez_plus_numerator
# 			elif self.denominator != other.denominator:
# 				noz = Fraction.nok(self.numerator, other.numerator)
# 				rez_plus_numerator = (noz / self.numerator) + (noz / other.numerator)
# 				return rez_plus_numerator, noz
#
# 	def __sub__(self, other):
# 		"""
# 		Вычитание дробей
# 		@param other:
# 		@return: возвращает новую дробь
# 		"""
# 		if not Fraction.division_zero(self.denominator, other.denominator):
# 			raise 'В знаменателе имеется ноль'
# 		else:
# 			if self.denominator == other.denominator:
# 				numerator_new = self.numerator - other.numerator
# 				return Fraction(numerator_new, self.denominator)
# 			elif self.denominator != other.denominator:
# 				noz = Fraction.nok(self.numerator, other.numerator)
# 				rez_plus_numerator = (noz / self.numerator) - (noz / other.numerator)
# 				return rez_plus_numerator, noz
#
# 	def __mul__(self, other):
# 		if not Fraction.division_zero(self.denominator, other.denominator):
# 			raise 'В знаменателе имеется ноль'
# 		else:
# 			numerator_new = self.numerator * other
# 			denominator_new = self.denominator * other
# 			if numerator_new % numerator_new == 0 and denominator_new % numerator_new == 0:
# 				return numerator_new / numerator_new, denominator_new / numerator_new
#
# 			return numerator_new, denominator_new
#
# 	@staticmethod
# 	def od(value1, value2):
# 		"""
# 		Формула для поиска наименьшего общего делителя
# 		@param value1:
# 		@param value2:
# 		@return:
# 		"""
# 		for i in range(value1, value1 * value2 + 1, 1):
# 			if value1 % i == 0 and value2 % i == 0:
# 				return i
#
# 	@staticmethod
# 	def nok(value1, value2):
# 		"""
# 		Поиск наименьшего общего делителя
# 		@param value1:
# 		@param value2:
# 		@return:
# 		"""
# 		if value1 > value2:
# 			rez = Fraction.od(value2, value1)
# 			return rez
# 		elif value1 < value2:
# 			rez = Fraction.od(value1, value2)
# 			return rez
#
# 	@staticmethod
# 	def division_zero(value1, value2):
# 		"""
# 		Провера деления на ноль
# 		@param value1:
# 		@param value2:
# 		@return: Возвращает логическоре значение
# 		"""
# 		if value1 == 0 or value2 == 0:
# 			return False
# 		return True


#Task №7


class GeometryUtils:
	PI = 3.1415

	@staticmethod
	def area_circle(value: int):
		if not isinstance(value, int):
			raise 'Type ERROR'
		else:
			s = GeometryUtils.PI * value
			return s

	@staticmethod
	def perimeter_circle(value: int):
		if not isinstance(value, int):
			raise 'Type ERROR'
		else:
			p = 2 * GeneratorExit.PI * value
			return p

	@staticmethod
	def area_rectangle(length: int, width: int):
		if not isinstance(length, int) and not isinstance(width, int):
			raise 'Type ERROR'
		else:
			s = length * width
			return s

	@staticmethod
	def perimeter_rectangle(length: int, width: int):
		if not isinstance(length, int) and not isinstance(width, int):
			raise 'Type ERROR'
		else:
			p = 2 * (length + width)
			return p
	@staticmethod
	def formula_Herona(a: int, b: int, c: int):
		if not isinstance((a, b, c), int):
			raise 'Type ERROR'
		else:
			p = (a + b + c) / 2
			s = p * (p - a) * (p - b) * (p - c)
			return s

class Program:
	@staticmethod
	def main():
		radius_circle = int(input("Введите радиус круга: "))
		print(f'Площадь круга: {GeometryUtils.area_circle(radius_circle)}')
		print(f'Периметр круга: {GeometryUtils.perimeter_circle(radius_circle)}')
		length_rectangle = int(input("Введите длину прямоугольника: "))
		width_rectangle = int(input("Введите ширину прямоугольника: "))
		print(f'Площадь прямоугольник: {GeometryUtils.area_rectangle(length_rectangle, width_rectangle)}')
		print(f'Периметр прямоугольника: {GeometryUtils.perimeter_rectangle(length_rectangle, width_rectangle)}')
		side_a = int(input("Введите первую сторону треугольника: "))
		side_b = int(input("Введите вторую сторону треугольника: "))
		side_c = int(input("Введите третью сторону треугольника: "))
		print(f'Площадь треугольника: {GeometryUtils.formula_Herona(side_a, side_b, side_c)}')
