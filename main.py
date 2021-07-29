import keyboard
import pyperclip
import time


def get_layout(first_layout: str, second_layout: str) -> dict:

	lower_layout = {}
	upper_layout = {}

	for i in range(len(first_layout)):
		lower_layout[first_layout[i]] = second_layout[i]
		upper_layout[first_layout[i].upper()] = second_layout[i].upper()


	return {'lower_layout': lower_layout, 'upper_layout': upper_layout}

def get_buff_text():
	text = pyperclip.paste()
	print('program get buff text')
	time.sleep(.01)
	print(f'text save in buff: {text}')
	return text

class Changer:
	RUS_LAYOUT = 'йцукенгшщзхъфывапролджэячсмитьбю.'
	ENG_LAYOUT = "qwertyuiop[]asdfghjkl;'zxcvbnm,./"

	engru_lower = get_layout(ENG_LAYOUT, RUS_LAYOUT)['lower_layout']
	engru_upper = get_layout(ENG_LAYOUT, RUS_LAYOUT)['upper_layout']

	def reverse(self):
		buff_text = get_buff_text()
		translate_text = ''
		
		for i in buff_text:
			try:
				translate_text += Changer.engru_lower[i]
			except:
				try:
					translate_text += Changer.engru_upper[i]
				except:
					print('except')
					translate_text += i
		print(translate_text)
		return translate_text

	def reverse_to_buff(self):
		pyperclip.copy(self.reverse())
		print('copy reversed text in buff')

if __name__ == '__main__':
	kb = Changer()
	print('program start')
	while True:
		time.sleep(.01)
		try:
			if keyboard.is_pressed('ctrl') and keyboard.is_pressed('shift') and keyboard.is_pressed('b'):
				kb.reverse_to_buff()
				time.sleep(.15)

			if keyboard.is_pressed('ctrl') and keyboard.is_pressed('esc'):
				print('program stop')
				exit()
		except ImportError:
			print("You must be root to use this library on linux.")
			break