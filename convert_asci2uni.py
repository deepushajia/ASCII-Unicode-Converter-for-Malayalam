def convert(text,font_name):
	try:
		get_v = font_name
		mapping = get_v.split("-")[-1]
		page_content = text
		map =  open('mapfile/'+mapping+'.map','r')
		mapread = map.read().split("\n")
		char = ''
		l = 0
		characters = ['\u0D46','\u0D47','\u0D48','\u0D4D\u0D30',]
		h = ''
		for x in range(len(page_content)):
			check =ord(str(page_content[x]))
			for y in range(len(mapread)-1):
				line = mapread[y]
				chars = line.split('=')
				if chars[0] == '':
					str_val = '='
				else:				
					str_val = chars[0]
				if int(str_val) == check:
					if check == 10:
						char = char + '\n'
					else:
						if chars[1] in characters:
							h = chars[1]
						else:
							char = char+ chars[1]
							if h != '':
								char = char+ h
								h=''
		return char, mapping
	except:
		return "Error Occured. Please report this.","Anja"
