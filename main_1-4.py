class MusicAlbum:
	def __init__(self, artist: str, name_album: str, track_list: list):
		self.artist = artist
		self.name_album = name_album
		self.track_list = track_list


	def add_track(self, track: str):
		self.track_list.append(track)

	def delete_track(self, track: str):
		if track in self.track_list:
			self.track_list.remove(track)
			print(f'{track} был удален из списка проигрываемых')
		else:
			print(f'{track} не найден возможно вы его удалили или не добавили ранее')

	def play_track(self, track: str):
		if track in self.track_list:
			print(f'Сейчас играет {track}')
		else:
			print('Трэк не найден')

	def get_info_album(self):
		print(f'Альбом {self.name_album}, был выпушен группой {self.name_album}, на момент выпуска в нем было {len(self.track_list)}')
class Program:
	@staticmethod
	def main():
		track1 = MusicAlbum(f'Наутилус помпилиус', 'яблокитай', ['люди на холме', 'во время дождя', 'три царя'])
		track1.add_track('Атлантида')
		track1.delete_track('во время дождя')
		track1.play_track('три царя')
		track1.get_info_album()
