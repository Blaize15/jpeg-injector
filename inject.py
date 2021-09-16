import sys

# variables defined

arglen = len(sys.argv)


# When no arguments
if(arglen <= 1):
	

	doc = '''
Argument not found
missing - [source.jpeg] AND [data]

TRY :
	python3 inject.py [source.jpeg] [data]

	'''
	print(doc)

# When arguments provided

else:

	if(arglen == 3):
		
		source_file = str(sys.argv[1])
		data = str(sys.argv[2])
		data = data + " "
		
		
		with open(source_file, "ab") as file:
			print("Injecting...")
			file.write(bytes(str(data), "utf-8"))
			print("Injection done...")
			print("Injected > {}".format(sys.argv[2]))

	elif(arglen == 2):

		doc = '''
Argument not found
missing - [data]

TRY :
	python3 inject.py [source.jpeg] [data]

	'''
		print(doc)




