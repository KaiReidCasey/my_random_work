'''
Possible TODOs:
- Clean this up, break into classes, etc
- Return max combined income possible on SSI
- Include SSDI
- Include state benefit
- Include unearned income
- List things that do not count as income
- Include students
'''

'''
Example:
Amy gets $841/mo in SSI
Amy works and earns $1,767.00
1767 - 20 - 65 = 1,682
1682/2 = 841

This means they have a total of $1682 that month.

'''

# Global variable declarations
total_ssi_amount = 841.00
earned_income = 0.00
initially_skipped_earned_income = 85.00
rate_earned_income_counted_after_skipped = 0.50

max_earned_income = 1767.00 # https://www.ssa.gov/pubs/EN-05-11015.pdf
max_unearned_income = 861.00
# max_uncounted_income_per_year is a thing for students
user_input = False


# Functions

def	is_allowable_amount(earned_income):
	if(earned_income > max_earned_income):
		return False
	else:
		return True

# this is the monthly earned income's impact on your total SSI benefit 
def get_ssi_reduction_from_earned_income(earned_income):
	if earned_income <= initially_skipped_earned_income:
		reduction = 0.0
	else:
		reduction = earned_income - initially_skipped_earned_income
		reduction = reduction * rate_earned_income_counted_after_skipped
	return reduction

# TODO: Consider building a class
def ssi_and_earned_income_calculator():
	print('\nHow much did you earn this month from employment?')
	user_input = False
	while user_input == False:
		try:
			earned_income = float(input('> '))
			user_input = True
		except ValueError:
			print('Incorrect amount. Please enter an amount such as:',\
			  total_ssi_amount)
			continue

	amount_allowable = is_allowable_amount(earned_income)
	if amount_allowable == True:
		ssi_reduction = get_ssi_reduction_from_earned_income(earned_income)
		total_months_profit = total_ssi_amount + earned_income - ssi_reduction
		print('\nThis month:')
		print(f'\nYour total profits would be ${"{:.2f}".format(total_months_profit)}')
		print('Ignoring changes to EBT benefits.')
		print(f'Your reduction would be ${"{:.2f}".format(ssi_reduction)}')
		print(f'Your SSI would be ${"{:.2f}".format(total_ssi_amount-ssi_reduction)}')
		print(f'Your earned income entered was ${"{:.2f}".format(earned_income)}')
	else:
		print(f'\nYour income exceeds the ${"{:.2f}".format(max_earned_income)} SSI income limit.')
		print(f'Your total income this month will be: ${"{:.2f}".format(earned_income)}.')
		print("Please report this to the SSA if this is not an estimate.")


# Starting user interaction:

print('Welcome to an unofficial SSI benefit calculator.')
print('Results may not reflect reality, so please verify the results\
   with the Social Security Administration.')
print('The information in this program is based upon information found here: \
   https://www.ssa.gov/ssi/text-income-ussi.htm')
print('It assumes that you do not have SSDI or a state suppliment.')
print('It also assumes that you are not a student.')
print(f'It also assumes that your SSI benefit is ${"{:.2f}".format(total_ssi_amount)}.')
print('Last updated: August 2022')

option_selected = -1
while option_selected != 0:
	print('\n\nPlease select an option from the following:')
	print('1 - Calculate total monthly earnings between SSI & earned income')
	print('0 - Exit the program')
	try:
		option_selected = int(input('> '))
		if(option_selected == 1):
			ssi_and_earned_income_calculator()
		elif(option_selected == 0):
			print('Goodbye!')
		else:
			print('Incorrect selection. Please enter either 1 or 0')
	except ValueError:
		print('Incorrect selection. Please enter a valid number.')
exit()
