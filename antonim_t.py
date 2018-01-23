import re

# ft = open("clean-tesaurus-handcrafted.txt")
ft = open("clean-tesaurus.txt")
tesaurus = ft.readlines();
ft.close()

code = "[RIORIORIO]"
alpha_context = ''
last_word = ''
now_word = ''

antRegex = re.compile("ant\s");
file = open("tesaurus-per-antonim.txt","w")
for line in tesaurus:
	if line.rstrip() == code:
		alpha_context = ''
		continue
	if alpha_context == '':
		alpha_context = line.rstrip().strip().lower()
		continue

	if antRegex.match(line):
		now_word = ''.join(i for i in line if not i.isdigit())
		now_word = re.sub(r'(\s\w\s)|(\W)', ' ', now_word)
		now_word = re.sub(r'\s+', ' ', now_word)
		now_word = re.sub(r'^ant ', '', now_word)
		now_word = now_word.rstrip().strip()
		file.write(last_word + "\n")
		file.write(now_word + "\n")
		file.write("\n")
	else:
		#if line[0] == alpha_context:
		last_word = ''.join(i for i in line if not i.isdigit())
		last_word = re.sub(r'(\s\w\s)|(\W)', ' ', last_word)
		last_word = re.sub(r'\s+', ' ', last_word)
		last_word = last_word.rstrip().strip()

file.close()