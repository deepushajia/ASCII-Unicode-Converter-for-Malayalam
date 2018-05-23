import os

maplist = ["MLB-Ambili","ML-Anjali","ML-Aathira","MLB-Ambili","ML-Aswathi","MLW-TTMalavika","MLB-Ambili","MLB-Ambili","MLB-Ambili","MLB-Indulekha","MLW-TTKarthika","ML-TTRavivarma","MLB-TTRevathi","ML-TTSarada","ML-Aswathi","ML-TTJyotsna","ML-Surya","MLW-TTAshtamudi","ML-Mayoori","ML-TTMayoori","ML-Ravivarma","MLB-TTAmbili"]
mapfontlist = open('file.txt','r')
mapfontread = mapfontlist.read()
mapfontread = mapfontread[1:-1]
mapfontread = mapfontread.replace("'","")
sorted_list = mapfontread.split(',')
sorted_list = sorted(sorted_list)
######### FONT TO FONT_NAME MAPPING IN THE SYSTEM ########## will not work for PFB
'''global fonts
fonts_available = []

for x in ['ttf']:
	global fonts

fonts_available = set(fonts_available)
fonts_available = list(fonts_available)
global font_list
font_list = []
for y in fonts_available:


sorted_list = sorted(font_list) '''

################################################
mala_dict = ['\u0D00', '\u0D01', '\u0D02', '\u0D03', '\u0D04', '\u0D05', '\u0D06', '\u0D07', '\u0D08', '\u0D09', '\u0D0A', '\u0D0B', '\u0D0C', '\u0D0D', '\u0D0E', '\u0D0F', '\u0D10', '\u0D11', '\u0D12', '\u0D13', '\u0D14', '\u0D15', '\u0D16', '\u0D17', '\u0D18', '\u0D19', '\u0D1A', '\u0D1B', '\u0D1C', '\u0D1D', '\u0D1E', '\u0D1F', '\u0D20', '\u0D21', '\u0D22', '\u0D23', '\u0D24', '\u0D25', '\u0D26', '\u0D27', '\u0D28', '\u0D29', '\u0D2A', '\u0D2B', '\u0D2C', '\u0D2D', '\u0D2E', '\u0D2F', '\u0D30', '\u0D31', '\u0D32', '\u0D33', '\u0D34', '\u0D35', '\u0D36', '\u0D37', '\u0D38', '\u0D39', '\u0D3A', '\u0D3B', '\u0D3C', '\u0D3D', '\u0D3E', '\u0D3F', '\u0D40', '\u0D41', '\u0D42', '\u0D43', '\u0D44', '\u0D45', '\u0D46', '\u0D47', '\u0D48', '\u0D49', '\u0D4A', '\u0D4B', '\u0D4C', '\u0D4D', '\u0D4E', '\u0D4F', '\u0D50', '\u0D51', '\u0D52', '\u0D53', '\u0D54', '\u0D55', '\u0D56', '\u0D57', '\u0D58', '\u0D59', '\u0D5A', '\u0D5B', '\u0D5C', '\u0D5D', '\u0D5E', '\u0D5F', '\u0D60', '\u0D61', '\u0D62', '\u0D63', '\u0D64', '\u0D65', '\u0D66', '\u0D67', '\u0D68', '\u0D69', '\u0D6A', '\u0D6B', '\u0D6C', '\u0D6D', '\u0D6E', '\u0D6F', '\u0D70', '\u0D71', '\u0D72', '\u0D73', '\u0D74', '\u0D75', '\u0D76', '\u0D77', '\u0D78', '\u0D79', '\u0D7A', '\u0D7B', '\u0D7C', '\u0D7D', '\u0D7E', '\u0D7F']

def convert(text,font_name): #ML-TTAmbili Italic
	try:
		get_v = font_name
		mapping = get_v.split("-")[-1]
		length = len(text)
		map = open('mapfile/'+mapping+'.map','r')
		mapread = map.read().split('\n')
		mapcontents_0 = []
		two_in_one = ['ഈ','ഊ','ഐ','ഓ','ഔ','ൈ','ൊ','ോ','ൌ']
		for a in two_in_one:
			if not a in mapcontents_0:
				if a == 'ഈ':
					text = text.replace('ഈ','ഇൗ')
				elif a == 'ഊ':
					text = text.replace('ഊ','ഉൗ')
				elif a == 'ഐ':
					text = text.replace('ഐ','എെ')
				elif a == 'ഓ':
					text = text.replace('ഓ','ഒാ')
				elif a == 'ഔ':
					text = text.replace('ഔ','ഒൗ')
				elif a == 'ൈ':
					text = text.replace('ൈ','െെ')
				elif a == 'ൊ':
					text = text.replace('ൊ','ൊ')
				elif a == 'ോ':
					text = text.replace('ോ','ോ')
				elif a == 'ൌ':
					text = text.replace('ൌ','ൌ')

		#for i in range(length):
		list_text = list(text)
		array = []
		skip = False 
		for k in range(len(list_text)):
			if not skip: 
				if list_text[k] in ['െ','േ']:
					ind = 1
					place_true = True
					num = 2
					while place_true:
						if ((len(array)>2) and (array[-1* num] in ['്'])):
							ind = ind + 2
						elif array[-1* (num+1):-1* (num-1)] == [' ','്ര']:
							ind = ind + 1
						else:
							place_true = False
						num = num +2

					array.insert(-1*ind,list_text[k])
				elif list_text[k:k+2] in [['്','ര']]:
					ind = 1
					place_true = True
					num = 2
					while place_true:
						if ((len(array)>2) and (array[-1* num] in ['്'])):
							ind = ind + 2
						else:
							place_true = False
						num = num +1

					skip = True
					array.insert(-1*ind, ''.join(list_text[k:k+2]))
				else:
					array.append(list_text[k])
			else:
				skip = False

		text = ''.join(array)
		#text = text.replace('\\xad',chr(301))
		for j in range(len(mapread)-1):
			cha = mapread[j].split('=')
			mapcontents_0.append(cha[1])
			if len(cha[1]) >= 5:
				text = text.replace(cha[1],chr(int(cha[0])))


		for j in range(len(mapread)-1):
			cha = mapread[j].split('=')
			mapcontents_0.append(cha[1])
			if len(cha[1]) >= 4:
				text = text.replace(cha[1],chr(int(cha[0])))

		for j in range(len(mapread)-1):
			cha = mapread[j].split('=')
			mapcontents_0.append(cha[1])
			if len(cha[1]) >= 3:
				text = text.replace(cha[1],chr(int(cha[0])))

		for j in range(len(mapread)-1):
			cha = mapread[j].split('=')
			mapcontents_0.append(cha[1])
			if len(cha[1]) >= 2:
				text = text.replace(cha[1],chr(int(cha[0])))
				

		for j in range(len(mapread)-1):
			chars = mapread[j].split('=')
			if chars[1] != '':
				text = text.replace(chars[1],chr(int(chars[0])))
		return text, mapping
	except:
		return "Error Occured. Please report this.","Anja"
