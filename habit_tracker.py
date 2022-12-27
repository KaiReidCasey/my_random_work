'''
Brainstorming:

Need a GUI pretty early on.

- user opens app and gets asked
    ~ which pre-existing habit to tick off
    ~ whether to add/delete habits
    ~ whether to view a visualization of habit frequency over time
    ~ whether to change the current date/time
    ~ whether to un-tick a previously ticked habit

- when user ticks off a habit, log the:
    ~ timestamp
    ~ habit ID
    ~ name of habit
    ~ class of habit, if it has one (career, physical health, etc)
    ~ username

- when user wants to visualize a habit, create these options:
    ~ view which days in the past 28-35 days they have done the habit
        * allow scrolling back to previous months
    ~ view number of time per day habit was done in past 7 days
    ~ view number of time per day habit was done in past 28-35 days
    ~ Calendar view
    ~ compare calander months
    ~ compare weeks
    ~ compare last X "Mon"days
    ~ compare last X "5th" of the months
Basically, users should be able to determine whether they are doing more, less, or the same amount of the habit

TODO:
+ get a datetimes working in Python (print out a time)
+ programmatically create a new file and add datetimes to it
+ append or prepend a datetimes to the existing file
+ Clean up user selection options
- recall list of datetimes in human-readable form
- add a label when saving datetimes
- create a list of valid labels in their own text file
- validate labels before adding to datetimes
- add ability for user to add to the list of valid labels
- add ability for user to subtract from the list of valid labels
- get a super basic UI going on Windows desktop/laptop
- add a button
- save a datetimes to file any time you press button
'''

# To allow tracking when events happened
# Used in get_current_time()
from datetime import datetime, timezone

'''
From
https://docs.python.org/3/library/datetime.html#datetime.datetime.now

"Warning: Because naive datetime objects are treated by many datetime 
methods as local times, it is preferred to use aware datetimes to 
represent times in UTC. As such, the recommended way to create an 
object representing the current time in UTC is by calling 
datetime.now(timezone.utc)."
'''

SAVED_TIME_ENTRIES_PATH = 'habit_tracker_time_entries.txt'

'''
Returns current time
TODO: verify works for user's time zone, even when they travel 
'''
def get_current_time():
	return datetime.now()# Attributes: year, month, day, hour, minute, second, microsecond, and tzinfo.

# Expects file path to .txt file, existing or not
def save_current_time(file_path):
	time_entry_file = open(file_path,'a')
	time_entry_file.write(str(get_current_time()))
	time_entry_file.write('\n')
	print('Time successfully saved!')
	time_entry_file.close()

# Expects file path to .txt file, existing or not
def read_saved_times(file_path):
	print('Saved times include:')
	time_entry_file = open(file_path,'r')
	print(time_entry_file.read())
	time_entry_file.close()

def greet_user():
	print('Hello! Welcome to my habit tracker.')

def display_time_for_user():
	print(' The current time is: ')
	print(get_current_time())

def get_and_respond_to_user_selection():
	display_time_for_user()
	print('What would you like to do?')
	# get user input with error handling
	option_selected = -1
	while option_selected != 0:
		print('\nPlease select an option from the following:')
		print('1 - Save the current time')
		print('2 - Read the current time')
		print('3 - Read saved times')
		print('0 - Exit the program')
		try:
			option_selected = int(input('> '))
			# react to user input
			if(option_selected == 1):
				save_current_time(SAVED_TIME_ENTRIES_PATH)
			elif(option_selected == 2):
				display_time_for_user()
			elif(option_selected == 3):
				read_saved_times(SAVED_TIME_ENTRIES_PATH)
			elif(option_selected == 0):
				close_habit_tracker()
			else:
				print('Incorrect selection. Please enter 1, 2, 3, or 0.')
		except ValueError:
			print('Incorrect selection. Please enter a valid number.')

def close_habit_tracker():
	print('Thanks for using my habit tracker! Bye!')
	exit()

greet_user()
get_and_respond_to_user_selection()
close_habit_tracker()
