import re

names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()

last_name = r'Love'
first_name = r'Kenneth'
#print(re.match(last_name, data))
#print(re.search(first_name, data))
#print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data))
#print(re.findall(r'\w*, \w+', data))
#print(re.findall(r'\b[trehous]{9}\b', data, re.I))
line = re.compile(r'''
	^(?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]+))\t  		# Last and first names
	(?P<email>[-\w\d.+]+@[-\w\d.]+)\t   	# Email
	(?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t  # Phone
	(?P<job>[\w\s]+,\s[\w\s.]+)\t?       # Job and companay
	(?P<twitter>@[\w\d]+)?$ 					# Twitter
	''', re.X|re.MULTILINE)
#print(line)
#print(line.groupdict())


#print(line.search(data).groupdict())
#for match in line.finditer(data):
#	print('{first} {last} <{email}>'.format(**match.groupdict()))

string = '''Love, Kenneth: 20
Chalkley, Andrew: 25
McFarland, Dave: 10
Kesten, Joy: 22
Stewart Pinchback, Pinckney Benton: 18'''


players = re.search('''
    (?P<last_name>[-\w ]+),\s   # last name
    (?P<first_name>[-\w ]+):\s  # first name
    (?P<score>[\d]+)          # score
''', string, re.X|re.M|re.I)



class Player():
	last_name = ''
	first_name = ''
	score = 0

	def __init__(self, last_name, first_name, score):
		self.last_name = last_name
		self.first_name = first_name
		self.score = score


print(string)
print(players.group('first_name'))