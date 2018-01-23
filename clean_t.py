import re

ft = open("tesaurus-id.txt")
tx = ft.readlines();
ft.close()

def clean_text(tesaurus):
	out_text = ''
	for line in tesaurus:
		clean_line = line.rstrip()
		if clean_line.strip()[-1:] == '-':
			out_text += clean_line[:-1].replace("- ", "")
		else:
			if clean_line.strip()[-1:] == ',':
				out_text += clean_line.replace("- ", "")	
			else:
				if len(re.findall("[;]\s*\w", clean_line)) > 0 and not len(re.findall("\d", clean_line)) > 0:
					lines = clean_line.split(";")
					for xline in lines:
						if len(xline.strip()) > 0:
							out_text += xline.replace("- ", "") + ';' + '\n'
				else:
					out_text += clean_line.replace("- ", "") + '\n'
	return out_text

out = clean_text(tx);
file = open("clean-tesaurus.txt","w")
file.write(out)
file.close()