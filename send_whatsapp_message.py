import pywhatkit as kit


# try:
choice = int(input("If you want to send a message instantly,  type 1; If you want to schedule send a message, type 2: "))
if choice == 1:
    message = input("Enter Your Message Here: ")
    phone_number = input("Enter Phone Number Here (With Country Code (ex. +1)): ")

    kit.sendwhatmsg_instantly(phone_number, message, wait_time=4, tab_close=False)

elif choice == 2:
    message = input("Enter Your Message Here: ")
    phone_number = input("Enter Phone Number Here (With Country Code (ex. +1)): ")
    hr = int(input("Enter Hour on the Clock You Want to Send the Message (in 24-hr format): "))
    mins = int(input("Enter Minute on the Clock You Want to Send the Message: "))
    kit.sendwhatmsg(phone_number, message, hr, mins)

else:
    print("Please enter either 1 or 2 and include the country code on the phone number.")
# except Exception:
    # print("There was an error, please try again.")
