# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 14:12:42 2022

@author: dwand
"""


""" 
You move to the San Francisco Bay Area and
decide that you want to start saving to buy a house.  As housing prices are very high in the Bay Area,
you realize you are going to have to save for several years before you can afford to make the down
payment on a house. In Part A, we are going to determine how long it will take you to save enough
money to make the down payment given the following assumptions:

Assumptions: 
portion_down_payment = .25
current_savings = 0 (i.e. start with no savings)
[Annual Return] r = .04 (4%)
"""



total_cost = int(input("Enter the cost of your dream home: "))
annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))

portion_down_payment = int(.25 * total_cost)
monthly_salary = annual_salary / 12
current_savings = 0   
r = .04/12

counter = []   
for current_savings in range(0, portion_down_payment)
    if current_savings != portion_down_payment:
        current_savings += monthly_salary * (r + portion_saved)
        counter.append(current_savings)
    elif current_savings == portion_down_payment:
        print(current_savings[-1])
        print("You have saved enough money for the down payment!")
        


        
    

        
        

        