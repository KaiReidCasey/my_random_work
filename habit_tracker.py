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
- get a timestamp working in Python (print out a time)
- programmatically create a new file and add timestamp to it
- append or prepend a timestamp to the existing file
- recall list of timestamps in human-readable form
- get a super basic UI going on Windows desktop/laptop
- add a button
- save a timestamp to file any time you press button
'''

def greet_user():
	print('Hello! We\'re under construction.')

greet_user()
exit()
