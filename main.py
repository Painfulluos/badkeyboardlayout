import keyboard
import pyperclip
import time
import pprint


def get_layout(first_layout: str, second_layout: str) -> dict:

	lower_layout = {}
	upper_layout = {}

	for i in range(len(first_layout)):
		lower_layout[first_layout[i]] = second_layout[i]
		upper_layout[first_layout[i].upper()] = second_layout[i].upper()


	return {'lower_layout': lower_layout, 'upper_layout': upper_layout}

def get_buff_text():
	return pyperclip.paste()


class Keyboard:
	RUS_LAYOUT = 'йцукенгшщзхъфывапролджэячсмитьбю.'
	ENG_LAYOUT = "qwertyuiop[]asdfghjkl;'zxcvbnm,./"

	engru_lower = get_layout(ENG_LAYOUT, RUS_LAYOUT)['lower_layout']
	engru_upper = get_layout(ENG_LAYOUT, RUS_LAYOUT)['upper_layout']

	def reverse(self):
		buff_text = get_buff_text()
		translate_text = ''
		
		for i in buff_text:
			try:
				translate_text += Keyboard.engru_lower[i]
			except:
				try:
					translate_text += Keyboard.engru_upper[i]
				except:
					translate_text += i
		return translate_text

	def reverse_to_buff(self):
		pyperclip.copy(self.reverse())


if __name__ == '__main__':
	kb = Keyboard()
	kb.reverse_to_buff()