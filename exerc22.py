import mincemeat
import glob
import csv

text_files = glob.glob('.\\join\\*')

def file_contents(file_name):
	f = open(file_name)
	try:
		return f.read()
	finally:
		f.close()

def mapfn(k, v):
			print 'map ' + k
			for line in v.splitlines():
				if k == '.\\join\\2.2-vendas.csv':
					yield line.split(':')[0], 'Vendas' + ':' + line.split(';')[5]
				if k == '.\\join\\2.2-filiais.csv':
					yield line.split(':')[0], 'Filial' + ':' + line.split(';')[1]
					
def reducefn(k, v):
	print 'reduce ' + k
	total = 0
	NomeFilial = ''
	for index, item in enumerate(v):
		if item.split(":")[0] == 'Vendas':
			total = int(item.split(":")[1]) + total
		if item.split(":")[0] == 'Filial':
			NomeFilial = item.split(":")[1]
	L = list()
	L.append(NomeFilial + " , " + str(total))
	return L

source = dict((file_name, file_contents(file_name))for file_name in text_files)

s = mincemeat.Server()

s.datasource = source
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

w = csv.writer(open(".\\results\\RESULT-2-2.csv", "w"))
for k, v in results.items():
	w.writerow([k, str(v).replace("[","").replace("]","").replace("'","").replace(' ','')])