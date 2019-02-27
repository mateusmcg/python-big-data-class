import csv
import glob

import mincemeat

text_files = glob.glob('.\\trab-2.3\\*')

def file_contents(file_name):
	f = open(file_name)
	try:
		return f.read()
	finally:
		f.close()
		
def mapfn(k, v):
    print 'map ' + k
    for line in v.splitlines():
        titulo = line.split(':::')[2]
        autores = line.split(':::')[1]
        from stopwords import allStopWords
        for word in titulo.split():
			if (word in allStopWords):
				titulo = titulo.replace(word, "")
        for autor in autores.split('::'):
            yield autor, titulo
					
def reducefn(k, v):
    print 'reduce ' + k
    print v
    totalPalavras = 0
    for autor, titulo in enumerate(v):
        totalPalavras = totalPalavras + len(titulo.split())
    L = list()
    L.append(totalPalavras)
    return L

source = dict((file_name, file_contents(file_name))for file_name in text_files)

s = mincemeat.Server()

s.datasource = source
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

w = csv.writer(open(".\\results\\RESULT-2-3.csv", "w"))
for k, v in results.items():
	w.writerow([k, str(v).replace("[","").replace("]","")])
