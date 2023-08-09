
# choose your own adventure


print("Welcome to X-Adventure")
userInput=input("Do you want to play this game:")
if(userInput.lower()=="yes"):
    print("Now you are on a bridge")
    print("there are three ways to go")
    print("you move to bridge")
    print("you can swim")
    print("you can use boat to cross the river but you cant drive the boat diver is available on the boat")
    inputUserfirst=int(input("Select one of the following Select {1,2,3}:"))
    if(inputUserfirst==2):
        print("you Select right path!")
        print("Now There are two ways")
        print("1 move straight")
        print("2 move right")
        inputUserSecond=int(input("Select one of the following Select {1,2}:"))
        if(inputUserSecond==1):
            print("you Select right path!")
            print("Now There are three ways")
            print("1 move straight")
            print("2 move right")
            print("3 move left")
            inputUserThird=int(input("Select one of the following Select {1,2,3}:"))
            if(inputUserThird==2):
                print("You Select right path")
                print("Now you enter in a Jungle")
                print("There are two ways")
                print("1 move straight")
                print("2 move right")
                inputUserFourth=int(input("Select one of the following Select {1,2}:"))
                if(inputUserFourth==2):
                    print("you Select right path")
                    print("now you are very close to the game ")
                    print("Select only one way ")
                    print("1 left")
                    print("2 right")
                    print("3 straight")
                    inputUserSixth=int(input("Select one of the following {1,2,3}"))
                    if(inputUserSixth==2):
                        print("you won the game")
                    else:
                        print("Bad luck you lose the game")
                else:
                    print("sorry you kill by lion in jungle")

                
            elif(inputUserThird==3):
                print("you Select right path")
                print("Now you enter in village")
                print("There are two ways")
                print("1 move straight")
                print("2 move left")
                inputUserFifth=int(input("Select one of the following Select {1,2}:"))
                if(inputUserFifth==2):
                    print("you Select right path")
                    print("now you are very close to the game ")
                    print("Select only one way ")
                    print("1 left")
                    print("2 right")
                    print("3 straight")
                    inputUserSeven=int(input("Select one of the following {1,2,3}"))
                    if(inputUserSeven==1):
                        print("you won the game")
                    else:
                        print("Bad luck you lose the game")
                    
                    
                    
                    
                    
                    
                    
                else:
                    print("sorry you kill by village locals")

            else:
                print("sorry you Select wrong path")
            
            
        else:
            print("sorry you enter in maze ")
            
        
    elif(inputUserfirst==1):
        print("Sorry the bridge is broken and you fall into the river")
    else:
        print("Sorry the boat driver kill you")
    
    