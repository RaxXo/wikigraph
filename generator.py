import pickle
data = pickle.load(open("data.p","rb"))

f = open("test.csv", "w+")
for key in data.keys():
	f.write(key)
	for s in data[key]:
		f.write(";" + s)
	f.write("\n")
f.close()
