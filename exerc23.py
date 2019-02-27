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
            word = word.replace('.', '')
            word = word.replace(':', '')
            word = word.lower()
            if (word in allStopWords):
				titulo = titulo.replace(word, "")
        for autor in autores.split('::'):
            for word in titulo.split():
                word = word.replace('.', '')
                word = word.replace(':', '')
                word = word.lower()
                yield autor + '-' + word, 1
					
def reducefn(k, v):
    print 'reduce ' + k
    return sum(v)

source = dict((file_name, file_contents(file_name))for file_name in text_files)

s = mincemeat.Server()

s.datasource = source
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

w = csv.writer(open(".\\results\\RESULT-2-3.csv", "w"))
for k, v in results.items():
	w.writerow([k.split('-')[0], k.split('-')[1], str(v).replace("[","").replace("]","")])
