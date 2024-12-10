import calendar
from datetime import datetime
def taxi():
    people=int(input("how many people needs a  ride : "))
    taxi=int(input("how many can fit in a taxi: "))
    number_of_taxi_neaded=people // taxi
    if people % taxi!=0:
        number_of_taxi_neaded+1
    print(f"number of taxies {number_of_taxi_neaded+1}")
##taxi()
def Ticket_Purchase_System():
    name=input("enter your name :")
    vip="vip"
    if name==vip:
        print("welcome for free")
    else:
        prix=100
        ticket=int(input("How many tickets would you like to buy?"))
        print(f"The total cost is {prix*ticket} da")
        print("Enjoy your tickets!")        
##Ticket_Purchase_System()
def temperature_check():
    temp = int(input("Please type in the temperature: "))
    if temp < 0:
        print("It's freezing!")
    if temp < 10:
        print("It's cold!")
    if temp < 20:
        print("It's cool!")
    print("Stay safe!")
##temperature_check()
def  Discount_Calculation():
    total=int(input("Total amount "))
    nbItem=int(input("Number of items "))
    if nbItem>=5:
        reduction=0.05
    else:
        reduction = 0
    today = datetime.today()
    weekday = calendar.day_name[today.weekday()]
    if weekday == "Saturday" or weekday == "Sunday":
        reduction += 0.2
    else:
        reduction += 0.1
    print(f"today{weekday}")
    total=total-reduction*total
    print(f"totale{total}")
##Discount_Calculation()
def compare_ages():
    age1 = int(input("Please type in the age of the first person: "))
    age2 = int(input("Please type in the age of the second person: "))
    if age1 > age2:
        print(f"The older age is: {age1}")
    elif age2 > age1:
        print(f"The older age is: {age2}")
    else:
        print("Both people are the same age!")
#compare_ages()
def determine_faster_runner():
    name1 = input("Runner 1:\nName: ")
    time1 = float(input("Time (in seconds): "))
    
    name2 = input("Runner 2:\nName: ")
    time2 = float(input("Time (in seconds): "))
    
    if time1 < time2:
        print(f"The faster runner is {name1}")
    elif time2 < time1:
        print(f"The faster runner is {name2}")
    else:
        print(f"{name1} and {name2} have the same time")

#determine_faster_runner()
def ceparation():
    price =float(input("enter the price ==>"))
    integer=price.__floor__()
    dicim=price-price.__floor__()
    print(f"Dinars{integer}")
    print(f"\nDinars{dicim}")
##ceparation()
def test():
    string =input("please write  somthing :")
    if len(string)>1:
        print(f"you typed {len(string)} you typed {string}")
##test()
def test2():
    age =(input("please enter your age:"))
    if age % 2 ==0:
        print(f"{age} is even")
    if age > 20:
        print(f"you are {age} years old you are mature")
##test2()
def test3(equipe1,equipe2):
    if   equipe1 <equipe2:
        print("equipe2 won")
    elif equipe1 >equipe2:
        print("equipe1 won")
    else :
        print("egalite")   
equipe1=int(input("equipe1 result"))
equipe2=int(input("equipe2 result"))
test3(equipe1,equipe2)
