#1.	create a python program that asks the user how far they want to travel.
# if they want to travel less than three miles tell them to ride Bicycle.
# if they want to travel more than three miles, but less than three hundred miles, tell them to ride Motor-cycle.
# if they want to travel three hundred miles or more tell them to driver Super-Car.

asking_user = int(input("How far would you like pt travel in mies?"))
if(asking_user<=3):
    print("I suggest you to walk")

elif(300<asking_user>3):
    print("i sugget you to ride motor cycle")

else:
    print("I suggest super-car to your destination")







#2.	Let's assume you are planning to use your python skills to build an App for Mobile.
#You decide to host your application on servers running in the cloud. you pick a hosting provider that charges $0.51 per hour. you will launch your services using one server and want to know how much it will cost to operate per day, per week, per month.
#Write a python program that displays the answers to the following questions:
#How much does it cost to operate one server per day?
#How much does it cost to operate one server per week?
#How much does it cost to operate one server per month?
#How much days can I operate one server with $918?

hourly_rate = 0.51

cost_per_day = hourly_rate * 24
cost_per_week = cost_per_day * 7
cost_per_month = cost_per_day * 30

budget = 918
days_with_budget = budget / cost_per_day
print(f"Cost to operate one server per day: ${cost_per_day:.2f}")
print(f"Cost to operate one server per week: ${cost_per_week:.2f}")
print(f"Cost to operate one server per month (30 days): ${cost_per_month:.2f}")
print(f"With ${budget}, you can operate one server for approximately {days_with_budget:.2f} days.")
