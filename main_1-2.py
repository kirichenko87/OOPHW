class Book:
	def __init__(self, title_book: str, autor_book: str, number_pages: int):
		self.title_book = title_book
		self.autor_book = autor_book
		self.number_pages = number_pages

	def open_book(self, page):
		if not page.is_integer():
			print('У вас проблемы вы ввели не число ')
		if page < self.number_pages and page < 0:
			print('Ожидайте ваша страница вот - вот откроется!')
		else:
			print('Такой страница нет в книге')

	def info_book(self):
		print(f'Эта книга {self.title_book} бюыл написана замечательным автором {self.autor_book}, '
			  f'и в ней {self.number_pages} чудесных страниц ')

class Program:
	"""
	Run file
	"""
	@staticmethod
	def main():
		book_1 = Book('Изучаем python', 'Марк Лутц', 830)
		book_1.open_book(501)
		book_1.info_book()
