# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 16:36:05 2018

@author: OLUWABAMISE
"""

# Set the default values.

semi_annual_raise = 0.07
r_annual = 0.04
r = r_annual/12
home_cost = 1000000
down_payment_percent = 0.25
down_payment = down_payment_percent * home_cost
savings = 0
month_limit = 36
savings_rate = 0.50

# Counters

month_counter = 0
step_counter = 1


# Range

min = 0
max = 10000

# Request the user's starting salary

current_salary = int(input("Enter the starting salary: "))


# Save this to a separate variable so it can be reset later, when rerunning the bisection method.

present_salary = current_salary


# Function to run the bisection method with a lower and upper limit

def compute_rate(lower, upper):


# Bring in all the variables to be modified.

   global savings, current_salary, month_counter, max, min, step_counter, savings_rate


# As long as the amount in Savings is less than the down payment (25% on 1MM = $250,000), do this:

   while (savings < down_payment):


# Define variables and how they're calculated.

       savings_rate = ((upper+lower)/2)/10000
       monthly_salary = current_salary/12
       monthly_return = savings * r
       monthly_contribution = monthly_salary * savings_rate

# This equation changes the value of savings as we expect it to.

       savings = savings + monthly_contribution + monthly_return

# For every time we go through this, increase month count by 1.

       month_counter += 1

# As we increase the month count, if it happens to be divisible by 6 and yields a remainder of 0, increase the currentSalary

       if month_counter % 6 == 0:

           current_salary = current_salary + (current_salary*semi_annual_raise)


# While loop repeats until savings are no longer less than the down payment needed.


# Check to see if we got to our goal in our set timeframe.

# If not, reset all the variables (including salary!), increase the step counter (aka # of iterations of the bisection method) by 1, and run the bisection method again.

# Since we took LONGER than our goal timeframe, change the minimum value for the bisection method to the savings rate used in the last iteration.

   if month_counter > month_limit:


       month_counter = 0

       savings = 0

       current_salary = present_salary

       step_counter += 1

       min = savings_rate*10000

       compute_rate(min, max)


# Since we achieved our goal FASTER our goal timeframe, change the maximum value for the bisection method to the savings rate used in the last iteration.

# Don't forget to reset variables and increase iteration count by 1

#### Since I reset the varaibles so frequently, maybe it should have it's own function?

#### e.g. def reset():

   elif month_counter < month_limit:


       month_counter = 0

       savings = 0

       current_salary = present_salary

       step_counter += 1

       max = savings_rate * 10000

       compute_rate(min, max)


# Just because we finally got to our savings goal at the expected timeframe, doesn't mean we did it right.

# Confirm that the savings value is within $100 of the down payment amount.

# If not, run it again.

# Change the savings rate by 1 (0.001, technically)

# decrease it by 0.001 if savings exceed down payment + 100

# increase it by 0.001 if savings exceed down payment - 100

# repeat as necessary

   elif savings > down_payment + 100:


       month_counter = 0

       savings = 0

       current_salary = present_salary

       step_counter += 1

       max = (savings_rate * 10000)-1

       compute_rate(min, max)


   elif savings < down_payment - 100:


       month_counter = 0

       savings = 0

       current_salary = present_salary

       step_counter += 1

       max = (savings_rate * 10000)+1

       compute_rate(min, max)

# Displays the results.

compute_rate(min, max)

print("Best savings rates:", savings_rate)

#print("Savings:", savings)
#
#print("Months:", month_counter)

print("Steps in bisection search:", step_counter)