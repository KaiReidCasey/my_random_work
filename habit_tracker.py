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
+ get a timestamp working in Python (print out a time)
- programmatically create a new file and add timestamp to it
- append or prepend a timestamp to the existing file
- recall list of timestamps in human-readable form
- get a super basic UI going on Windows desktop/laptop
- add a button
- save a timestamp to file any time you press button
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

'''
Returns current time
TODO: verify works for user's time zone, even when they travel 
'''
def get_current_time():
	return datetime.now()# Attributes: year, month, day, hour, minute, second, microsecond, and tzinfo.

def greet_user():
	print('Hello! Welcome to my habit tracker.')

def ask_user_if_save_current_time():
	print(' The current time is: ')
	print(get_current_time())
	print('Would you like to save it?')
	print('Sorry, we\'re under construction.')

def close_habit_tracker():
	print('Bye!')
	exit()

greet_user()
ask_user_if_save_current_time()
close_habit_tracker()
