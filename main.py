import pyautogui, time, random

# Data used to fill out the email
emailData = [
    {"senderEmail": "jenny.smith@fakemail.com", "recieverEmail": "alex.johnson@notreal.net", "subject": "Follow-Up on Project Timeline", "greeting": "Hi Alex,", 
     "message": "Any updates on Phase 2 deliverables? Let me know if you need anything.","goodbye": "Best, Jenny"},
    {"senderEmail": "mark.thompson@imaginarymail.org", "recieverEmail": "kelly.green@madeupmail.com", "subject": "Lunch Meeting on Thursday", "greeting": "Hi Kelly,",
     "message": "Are we still on for lunch Thursday at 12:30? Let me know.", "goodbye": "Cheers,Mark"},
    {"senderEmail": "sophia.lee@pretendmail.net", "recieverEmail": "daniel.peters@bogusemail.org", "subject": "Feedback on Draft Proposal", "greeting": "Hey Daniel,",
     "message": "Your draft looks good. I have comments on sections 3 and 5. Let me know when to chat.", "goodbye": "Thanks! Sophia"}
]
while True:
    try:
        emailAmount = int(input("How many emails would you like to send: "))
        print("Submitting", emailAmount, "emails.")
        break
    except ValueError:
        print("Invalid Input / Please enter a number")



time.sleep(2)
pyautogui.hotkey("alt", "tab")
time.sleep(1)
pyautogui.hotkey("ctrl", "t")
pyautogui.write("gmail.com")
pyautogui.press("enter")
time.sleep(2)
pyautogui.hotkey("ctrl", "r")


for sender in emailData:
    # Allows user to kill script for 5 seconds
    print(">>>>>>5 SECOND PAUSE PRESS CRTL + C <<<<<")
    time.sleep(5)
    print("Also make sure to have your broswer open")
    

    




    
