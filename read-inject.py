import sys

arglen = len(sys.argv)

if(arglen <= 1):

	doc = '''
Argument not found
missing - [source.jpeg]

TRY : 
	python3 read-inject.py [source.jpeg]

	'''

	print(doc)


else:
	
	inject_data = None

	with open(str(sys.argv[1]), "rb") as file:

		content = file.read()
		offset = content.index(bytes.fromhex('FFD9'))
		file.seek(offset + 2)
		data = file.read()
		data = (data.decode('utf-8')).split(" ")
		del data[len(data) - 1]
		
		
	
	for d in data:

		print("inject ", data.index(d), " - " + d)