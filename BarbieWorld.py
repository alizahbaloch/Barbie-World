print("===Welcome to Barbie's world===")
name=input("\n What is the name of your Barbie?")
print("Hello ", name,)
print( "Let's plan your day!")
dress=int(input("What does barbie wanna wear? \n 1.Pink dress  2.Swim suit  3.Sports kit\n"))
score=0
if dress==1:
    print("Barbie looks like a DIVA!!!\n")
    score+=3
elif dress==2:
    print("Barbie is ready to dive...shooooo\n")
    score+=1
elif dress==3:
    print("Barbie is ready for an active day\n")
    score+=2
else:
    print("Choose a valid option:")

place=int(input("Where does Barbie wanna go? \n 1.To a kitty party  2.To a swimming club  3.To play Badminton\n"))
if place==1:
    print("So it's a gossips day, hehe!!\n")
    score+=1
elif place==2:
    print("Barbie is gonna slay in water, hm hm!!\n")
    score+=2
elif place==3:
    print("Barbie has really got a taste! Best of luck to knock out your opponent in match, we know Barbie can do anything...\n")
    score+=3
else:
    print("Choose a valid option:")

restaurant=int(input("In which restaurant does Barbie wanna have dinner? \n 1.Desi hut  2.Kurtos Bistro  3.KFC\n"))
if restaurant==1:
    print("The barbie is a desi girl..\n")
    score+=1
elif restaurant==2:
    print("Great taste, barbie...\n")
    score+=2
elif restaurant==3:
    print("The reasonable choice, have fun with KFC's great taste..\n")
    score+=3
else:
    print("Choose a valid option:")

dinner=int(input("What does  barbie wanna have for dinner? \n 1.Burger  2.Drum sticks  3.Alferado pasta" +("(Available only at DESI HUT & KURTOS BISTRO)\n")))
if dinner==1:
    burger=input("Which  burger does "+ name + " wanna have? \n a.Zinger Burger  b.Mighty Burger c.Crunch Burger")
    if burger=="a":
        print("Yum, great tastee, my personally fav:\n")
    elif burger=="b":
        print("Seema like Barbie has a great appetite..\n")
    elif burger=="c":
        print("Have fun with Crunch Burger, baddie\n")
    score+=3
elif dinner==2:
    print("Yum, chicken is loveeee!!\n")
    score+=2
elif restaurant==3:
    print("Barbie seems like a pasta lover!!\n")
    score+=1
else:
    print("Choose a valid option:")

print("\n==Rating barbie's dayyyyy==")
print("Score of the day:", score)

if score>=8:
    print("Barbie is such a fun-loving lady with great taste, A day well spent.\n RATING:10/10")
elif score>=5:
    print("The day was good, but barbie still needs to work on her taste:\n RATING 7/10")
else:
    print("It was just an average day: Try to enhance your routine divaa \n RATING 4/10")










