# TO-DO LIST
# MAKE SYSTEM THAT CHECKS IF EACH MESSAGE IS CORRECT TYPE OF DATA-TYPE (WORKING)
# MAKE SYSTEM THAT PULLS OUT DATA FROM LISTS OF CONTINENTS/COUNTRIES (Maybe possibly cities if viable?) ACCORDING TO USER INPUT
# MAKE SYSTEM THAT CALCULATES SUCH INFORMATION AND SPITS IT OUT
# **EXTRA PARTS**
# MAKE A WEBSITE ADVERTISING (FOR FUN) AND ADD AN GUI/POSSIBLY MAKE APP? (ALSO FOR FUN)


# some variables and a system that tells you to put in a certain type of answer because I thought that was cool
# this part of the code basically grabs a bunch of data from you and uses it to

import sys

print("Please do not take these as an actual basis to budget yourself under, these are very rough calculations that you should use a skeleton for your budget.")
salary = input("What is your salary? (In USD, do not put comma): ").lower()
random_var = 1
user_data = []



# Checks if salary is digit, if not then returns
if salary.isdigit():
    random_var += 1
    user_data.append(salary)
else:
    print("Input is not integer, please put in integer.")
    sys.exit()

location = str(input("What's your location?: ")).lower()

if not location.isdigit():
    user_data.append(location)
else:
    print("Location is not in letters, please write normally.")
    sys.exit()

working_status = input("Are you in school or employed?: ").lower()

if working_status == "school" or working_status == "in school":
    education_status = input("College or lower?: ").lower()
    user_data.append(working_status)
    if education_status == "college" or working_status == "university":
        college_loans = input("How much are your college loans? (yearly): ")
        user_data.append(education_status)
    else:
        print("Thank you for answering questions!")

# Will not have enough time to scrounge through each countries expenses, so for information, I will only be using data from continents, if not continents then most likely cities/countries.
# First index is average rate of living, 2nd index is average tax rate (may be inaccurate, not much research due to time)


# REMINDER FOR SELF: FROM ANTARCTICA, (INCLUDING THAT), THE DATA IS NOT TRUE AND RANDOMLY GENERATED.
n_america = [12000, 0.245]
s_america = [12000, 0.35]
antarctica = [73644, 0.279]
asia = [8000, 0.345]


# Function that calculates how much money is gone

def findMoney(data, user_info=user_data):
    tax = int(data[1])
    salary = int(user_info[0])
    rate_living = int(data[0])
    tax_money = salary * tax
    after_living_money = salary - rate_living 
    leftover_money = after_living_money - tax_money
    return leftover_money

print(findMoney(s_america))

print(user_data)