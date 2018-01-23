
ft = open("tesaurus-per-antonim.txt")
data_antonim = ft.readlines();
ft.close()

antonim_process = False
antonim_kiri = []

file = open("hasil-pasangan-antonim-id.txt","w")
for data in data_antonim:
	clean_data = data.rstrip()
	if len(clean_data) == 0:
		continue
	if not antonim_process:
		antonim_kiri = clean_data.split(' ')
		antonim_process = True
		continue
	A = antonim_kiri
	B = clean_data.split(' ')
	for kata_a in A:
		if len(kata_a) < 3:
			continue
		for kata_b in B:
			if len(kata_b) < 3:
				continue
			file.write(kata_a + ' ' + kata_b + '\n')
	antonim_process = False

file.close()