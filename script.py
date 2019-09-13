#Import SenseHat
from sense_hat import SenseHat
sense = SenseHat()

#Prompt user for colour and speed

print("Welcome  to the SenseHat program!")

while True:
    print("Welcome  to a new round! Type quit to quit.")
    
    print("There are three colours: red(355), green(567) or blue(789).")
    user_textcolour = input("Choose text color: ")
    if user_textcolour in ("355" ,"red"):
        color_msg = (255, 0, 0) #red
    elif user_textcolour in ("567" , "green"):
        color_msg = (0, 255, 0) #green
    elif user_textcolour in ("789" , "blue"):
        color_msg = (0, 0, 255) #blue
    elif user_textcolour == "quit":
        break
    else:
        print("Invalid input. Please try again!")
        continue
    
    print("There are three colours: red(345), green(564) or blue(678).")
    user_bgcolour = input("Choose background color: ")
    if user_bgcolour in ("345" , "red"):
        color_bg = (255, 0, 0) #red
    elif user_bgcolour in ("564" , "green"):
        color_bg = (0, 255, 0) #green
    elif user_bgcolour in ("678" , "blue"):
        color_bg = (0, 0, 255) #blue
    elif color_bg == "quit":
        break
    else:
        print("Invalid input. Please try again!")
        continue
    
    print("There are two speeds: fast or slow.")
    user_speed = input("Choose your speed: ")
    if user_speed == "fast":
        speed = 0.02
    elif user_speed == "slow":
        speed = 0.1
    elif user_speed == "quit":
        break
    else:
        print("Invalid input. Please try again!")
        continue
        
    #Show the message
    sense.show_message("This is fun!", text_colour = color_msg, back_colour = color_bg, scroll_speed = speed)

print("Thanks for playing. Bye!")