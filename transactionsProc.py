from itertools import islice

path = '/usr/local/data/transactions.txt'


def get_chunk_of_lines(file, n_lines):
	return [i.split(',') for i in islice(file, n_lines)]


def count_seg_clients(chunk):
	R_amount = 0
	AF_amount = 0
	for line in chunk:
		if line[3][0] == 'R':
			R_amount += 1
		else:
			AF_amount += 1
	return (R_amount, AF_amount)




with open(path) as f:
	chunk_cnt = 0
	R_amount = 0
	AF_amount = 0
	while True:
		chunk = get_chunk_of_lines(f, 2)
		#print(count_seg_clients(chunk)[0])
		#print(count_seg_clients(chunk)[1])

		R_amount += count_seg_clients(chunk)[0]
		AF_amount += count_seg_clients(chunk)[1]
		if not chunk:
			break
	print('clients in R segment:\t', R_amount, '\nclients in AF segment:\t', AF_amount)