e_mail = input('Enter your E-mail: ').strip()

user_name = e_mail[:e_mail.index('@')]

domin_name = e_mail[e_mail.index('@')+1:]

username_slice = (f"Your user name is'{user_name}'") 
domin_slice = (f"Your domin is '{domin_name}'")


print(username_slice)
print(domin_slice)
