import zipfile

wordList = ['data', 'youch', 'yoight', 'yeet', 'youcher', 'yeeter', 'yoighter',
	    'yum', 'yummy', 'tasty', 'delicious', 'tastylicious', 'scrummy', 
	    'scrumptious', 'Alfie', 'Graeme', 'Graham', 'Ollie', 'Bolly',
	    'Sorry', 'about', 'how', 'my', 'code', 'looks']

file = zipfile.ZipFile("protectedZip.zip")
correctPassword = ''
for password in wordList:
	try:
		print(password)
		password = password.encode()
		data = file.extractall(pwd=password)
		print(data)
		correctPassword = str(password, 'utf-8')
		break
	except:
		pass
if(correctPassword == ''):
	print("No password found.")
else:
	print("The password is: ", correctPassword)
