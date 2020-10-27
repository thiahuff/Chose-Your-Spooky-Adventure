
#An adventure game that has your user make at least two decisions throughout the course of the game (using at least two if/elif/else conditionals). 

username = input("What is your name?: ")
sidekick = input("What's the name of someone you would like to go on a spooky adventure with?: ")

print("\n")
print("You and {} are walking down the road when you see an old mansion that looks very spooky.".format(sidekick))
print("{} turns to you and says \"{}, that is the old Waldorf house, I heard that it's haunted, let's check it out.\"".format(sidekick, username))
print("If you want to check the front door chose 1.")
print("if you want to break a window to get in chose 2.")

how_to_enter = int(input("What do you want to do?:"))

if how_to_enter == 1:
    print("You try the front door and it is unlocked")
    print("{} tells you they have a bad feeling".format(sidekick))
    print("Chose 1 if you want to keep enter the house.")
    print ("Chose 2 if you are too scared to enter")

    will_enter = int(input(">"))

    if will_enter == 1:
        print("You explore the front room. It feels like you have stepped into the past.")
        print("the room is full of cobwebs and the ornate furniture is covered in a thick layer of dust, untouched over the years.")
        print("The glint of something gold catches your eye. It is a gold plaque sitting next to an ancient looking urn")
        print("{} says that the writing appears to be Latin and can translate it.".format(sidekick))
        print("After a few minutes of concentrating {} says \"The plaque reads: Dark wishes or deep desires, only the brave or foolish dare break me open to learn my secrets.\"".format(sidekick))
        print("{} asks if you want to break the urn open or get out of here".format(sidekick))
        print("Chose 1 if you want to break the urn.")
        print ("Chose 2 if you want to get out of here")


        break_urn = int(input(">"))

        if break_urn == 1:
            print("You lift the urn above your head and slam it down to the floor.")
            print("The urn shatters into impossibly tiny shards and a cloud of ash blooms up filling the room.")
            print("A ghostly figure in a beeaded shift dress forms, thanks you for freeing her and offers you a pearl")
            print("The apparition says \"If you speak a wish while holding the pearl it will disappear and your wish will come true.\"")
            print("This was a very good adventure, now you and {} just have to decide who gets the wish!".format(sidekick))

        elif break_urn == 2:
            print ("You turn back, {} reassures you that you made the right choice, but you cannot shake the feeling that you missed out on a solving some great mystery.".format(sidekick))
        
        else:
           print("You didn't enter a valid choice, I guess your adventure ends here") 


    elif will_enter == 2:
        print ("You turn back, {} reassures you that you made the right choice, but you cannot shake the feeling that you missed out on a great adventure.")
    else:
        print("You didn't enter a valid choice, I guess your adventure ends here")

if how_to_enter == 2:
    print("You grab a rock and break a window at the front of the house")
    print("You carefully avoid the glass around the frame, but {} cuts their hand when they come through.".format(sidekick))
    print("You explore the front room. It feels like you have stepped into the past.")
    print("the room is full of cobwebs and the ornate furniture is covered in a thick layer of dust, untouched over the years.")
    print("The glint of something gold catches your eye. It is a gold plaque sitting next to an ancient looking urn")
    print("{} says that the writing appears to be Latin and can translate it.".format(sidekick))
    print("After a few minutes of concentrating {} says \"The plaque reads: Dark wishes or deep desires, only the brave or foolish dare break me open to learn my secrets.\"".format(sidekick))
    print("{} asks if they should break the urn open or get out of here".format(sidekick))
    print("Chose 1 if you want to break the urn.")
    print ("Chose 2 if you want to get out of here")


    break_urn = int(input(">"))

    if break_urn == 1:
        print("{} grabs the urn, their blood streaking down the side, then lifts the urn above their head  and slams it down to the floor.".format(sidekick))
        print("The urn shatters into impossibly tiny shards and a cloud of ash blooms up filling the room.")
        print("A ghostly figure in a beeaded shift dress forms, and says \"Thank you for paying the price to free me with your blood.\" then offers you a handful pearls")
        print("The apparition says \"If you speak a wish while holding one of the pearls it will disappear and your wish will come true.\"")
        print("This was a very good adventure, now you and {} just have to decide what to wish for!".format(sidekick))

    elif break_urn == 2:
        print ("You turn back, {} reassures you that you made the right choice, but you cannot shake the feeling that you missed out on a solving some great mystery.".format(sidekick))
        
    else:
        print("You didn't enter a valid choice, I guess your adventure ends here") 
