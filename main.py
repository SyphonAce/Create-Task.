import pyautogui, time, random

# Data used to fill out the email
emailData = [
    {"receiverEmail": "exampleemail38293238@gmail.com", "subject": "Follow-Up on Project Timeline", "greeting": "Hi Alex,", 
     "message": "Any updates on Phase 2 deliverables? Let me know if you need anything.","goodbye": "Best, Jenny"},
    {"receiverEmail": "exampleemail38293238@gmail.com", "subject": "Lunch Meeting on Thursday", "greeting": "Hi Kelly,",
     "message": "Are we still on for lunch Thursday at 12:30? Let me know.", "goodbye": "Cheers,Mark"},
    {"receiverEmail": "exampleemail38293238@gmail.com", "subject": "Feedback on Draft Proposal", "greeting": "Hey Daniel,",
     "message": "Your draft looks good. I have comments on sections 3 and 5. Let me know when to chat.", "goodbye": "Thanks! Sophia"}
]
# If and else statement to ensure the user is inputting the correct data value
while True:
   
    emailAmount = (input("How many emails would you like to send: "))
    
    if emailAmount.isnumeric():
        print("Submitting", emailAmount, "emails.")
        break
    else:       
        print("Invalid Input / Please enter a number")
        
        

print("Make sure to have your browser open")

# Switches to browser window and opens a new gmail tab / brief stops in between actions to ensure accuracy
time.sleep(2)
pyautogui.hotkey("alt", "tab")
time.sleep(2)
pyautogui.hotkey("ctrl", "t")
pyautogui.write("gmail.com")
pyautogui.press("enter")
time.sleep(2)
pyautogui.hotkey("ctrl", "r")
print("ensuring reload")
time.sleep(2)


for num in range(0, int(emailAmount)): 
    
    for i in range(0, 13): 
        pyautogui.write("\t")
        time.sleep(0.01)

    pyautogui.press("enter")
    time.sleep(1)

    pyautogui.write(emailData[random.randint(0, len(emailData) - 1)]["receiverEmail"])
    pyautogui.press("esc")
    pyautogui.press("\t")
    time.sleep(0.1)

    pyautogui.write(emailData[random.randint(0, len(emailData) - 1)]["subject"] + "\t")
    time.sleep(0.1)

    pyautogui.write(emailData[random.randint(0, len(emailData) - 1)]["greeting"])
    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(0.1)

    pyautogui.write(emailData[random.randint(0, len(emailData) - 1)]["message"])
    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(0.1)

    pyautogui.write(emailData[random.randint(0, len(emailData) - 1)]["goodbye"])
    time.sleep(0.1)

    pyautogui.hotkey("ctrl", "enter")
    

    time.sleep(1)

    pyautogui.hotkey("ctrl", "r")

    time.sleep(1)

    pyautogui.press("enter")
    time.sleep(1)

    





    
    
    

    




    
