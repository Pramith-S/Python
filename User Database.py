# Simple python program to save username and passwords in a .txt and access it to login user
# Use it before a block of code to secure it or specify it for a particular user in the database
while True:
    print('\n\n\t\t\t\t\tPress 1 to login or press enter to sign up')
    a=input()
    if a=='1':
        while True:
            with open('userinfo.txt','r') as info: # (IMPORTANT): Create .txt file with the same name or change the name of the .txt file according to the one in your system
                user_details=info.readlines()
            print('Enter your Username:')
            global username
            username=input()
            c=0
            for i in range(len(user_details)):
                test=user_details[i]
                test=test.rstrip('\n')
                global b
                b=i
                if username==test:
                    c=1
                    break 
            if c==1:
                print ('Enter your password:')
                password=input()
                d=0
                if password in user_details[b+1].rstrip('\n'):
                    d=1
                if d==1:
                    print('\t\t\t\tAccess granted welcome')
                    break
                else:
                    print('\t\t\t\tWrong Password')
                    continue
                break
            else:
                print('\t\t\t\tUsername not found')
                continue
        break    
    else:
        with open('userinfo.txt','r') as info:
                user_details=info.readlines()
                
        print('Enter new Username:')
        username=input()
        print('Enter Password:')
        password=input()
        user_details.append(username+'\n')
        user_details.append(password+'\n')
        with open('userinfo.txt','w') as info:
            for i in user_details:
                info.write(i)
        continue