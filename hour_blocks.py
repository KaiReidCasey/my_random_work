# used for Regex that grabs hour block info from .txt
import re

HOUR_BLOCKS_PATH = 'hour_blocks.txt'
HOUR_BLOCKS_REGEX = r'(.*): (.*)'

def get_file_contents(file_path):
	# TODO: Validate string
	f_open = open(file_path,'r')
	data = f_open.read()
	f_open.close()
	return data

def interpolate_file_contents(file_contents):
	data = re.findall(HOUR_BLOCKS_REGEX, file_contents)
	return data

def convertIntoSchedule(hour_blocks):
	print(f'{hour_blocks}')

raw_hours_content = get_file_contents(HOUR_BLOCKS_PATH)
hours_data = interpolate_file_contents(raw_hours_content)
convertIntoSchedule(hours_data)
