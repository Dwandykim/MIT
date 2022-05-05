# -*- coding: utf-8 -*-
"""
created on thu feb 17 14:30:21 2022

@author: dwand
"""

total_cost = int(input("enter the cost of your dream home: "))
annual_salary = int(input("enter your annual salary: "))
portion_saved = float(input("enter the percent of your salary to save, as a decimal: "))
semi_annual_raise = float(input("enter the semi-annual raise, as a decimal: "))


portion_down_payment = .25 * total_cost
monthly_salary = annual_salary / 12
portion_saved_monthly = monthly_salary * portion_saved

r = .04 / 12 

current_savings = 0   
no_of_months = []
months = 0

while current_savings < portion_down_payment:
    current_savings += current_savings * r + portion_saved_monthly
    no_of_months.append(current_savings)
    months += 1  
    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        monthly_salary = annual_salary / 12
        portion_saved_monthly = monthly_salary * portion_saved      
                
     

print("it will take you", len(no_of_months),"months to save up to make your down payment.")
