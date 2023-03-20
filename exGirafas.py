import random 
gif1=random.randint(1,5)
gif2=random.randint(1,5)
gif3=random.randint(1,5)
gif4=random.randint(1,5)
gif5=30
if gif1> gif2 and  gif3 and  gif4 and  gif5 :
    print("Girafa 1 é mais alta")

elif gif2 > gif3 and gif4 and gif5:
    print("girafa 2 mais alta")
elif  gif3 > gif4 and gif5:
    print("girafa 3 mais alta")
elif  gif4 > gif5:
    print("girafa 4 mais alta")
else:{
    print("Girafa 5 mais alta")
}