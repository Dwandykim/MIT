# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 12:07:30 2022

@author: dwand
"""
# Finding the right amount to save away
# In Part B, you had a chance to explore how both the percentage of your salary that you save each month 
# and your annual raise affect how long it takes you to save for a down payment.  This is nice, but
# suppose you want to set a particular goal, e.g. to be able to afford the down payment in three years.
# How much should you save each month to achieve this?  In this problem, you are going to write a 
# program to answer that question.  To simplify things, assume:\
    
# 1. Your semi­annual raise is .07 (7%)
# 2. Your investments have an annual return of 0.04 (4%)  
# 3. The down payment is 0.25 (25%) of the cost of the house 
# 4. The cost of the house that you are saving for is $1M.

# You are now going to try to find the best rate of savings to achieve a down payment on a $1M house in 
# 36 months. Since hitting this exactly is a challenge, we simply want your savings to be within $100 of 
# the required down payment.

## Find best savings rate to make down payment in 36 months
total_cost = 1000000
semi_annual_raise = .07
down_payment = total_cost * .25
annual_salary = int(input("enter your annual salary: "))
monthly_salary = annual_salary / 12
goal = 36  ## 36 months (3 years)


r = 0.04/12
current_savings = 0 
optimal_savings_rate = current_savings / (annual_salary / 12)
low = 0
high = down_payment

monthly_salaries = []
for amt in range(goal):
    
    if amt%6 == 0:
        current_savings += monthly_salary * semi_annual_raise  
        current_savings += monthly_salary * r
        monthly_salaries.append(current_savings)
    else:
        current_savings += monthly_salary + monthly_salary * r
        monthly_salaries.append(current_savings)

print(len(monthly_salaries))
print(monthly_salaries)
