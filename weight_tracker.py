
'''
Ask user what they want to do
 - add entry
 - display graph
 - display entries

First I'm going to focus on displaying the entries
It is built from a text file

'''

# line = input('> ')
# print(line)
ENTRIES_FILE_PATH = 'weight_entries.txt'

def display_options():
	print('What would you like to do?')
	print('1 - Display Entries')
	print('0 - Exit Program')

def get_user_selection():
	user_selection = int(input('> '))
	print('You selected ',user_selection)
	return user_selection

def get_file_contents():
	# TODO: Validate string
	f_open = open(ENTRIES_FILE_PATH,'r')
	data = f_open.read()
	f_open.close()
	# temporary to ensure I'm reaching the data
	print(data) # works! Now to make it pretty
	# return numbers

def interpret_user_selection(user_selection):
	if(user_selection == 0):
		print('Goodbye!')
		exit()
	elif(user_selection == 1):
		print('Entries placeholder')
		get_file_contents()
	else:
		print('Invalid entry. Please try again.')
		display_options()
		get_user_selection()

print('Hello and welcome to a very simple weight tracker!')
while True:
	display_options()
	user_selection = get_user_selection()
	interpret_user_selection(user_selection)


