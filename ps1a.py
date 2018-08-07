# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 17:09:41 2018

@author: OLUWABAMISE
"""
#I worked with Shuayb (Posh) as a team on this task.

#Purpose of Program:
#Write a program to calculate how many months it will take you to save up enough 
#money for a down payment


#Users Inputs
total_cost = float(input('Enter the cost of your dream home:')) #total cost of the dream house
annual_salary = float(input('Enter your annual salary:'))
portion_saved = float(input('Enter the percent of your salary to save, in decimal:'))

#Variables. All amounts are in naira(#)
portion_down_payment = 0.25 * total_cost
current_savings = 0 #the amount saved so far, starting from 0
r = 0.04 #annual rate
annual_return = (current_savings * r) / 12
monthly_salary = annual_salary / 12
portion_saved = portion_saved * monthly_salary
time = 0


#Iterations
while (current_savings <= portion_down_payment):
    time += 1
    current_savings += (current_savings * r / 12) + portion_saved
print('Number of months: %d'%time)
