def process(file_in, file_out):
	csv_rows = []
	with open(file_in) as f:
		for line in f:
			if line == '\n':
				continue
			line = line.strip() + '\n'
			csv_rows.append(line)

	with open(file_out, 'w') as f:
		for line in csv_rows:
			f.write(line)

process('data/raw/DIC_2005-2018_20190612_data.csv', 'data/cleaned/DIC_2005-2018_20190612_data.csv')
process('data/raw/DIC_2005-2018_20190612_codes.csv', 'data/cleaned/DIC_2005-2018_20190612_codes.csv')
