# A simple python program of a math quiz utilizing basic math operations (+,-,*,/)
import random as r # All numbers will be randomly generated, change the range of the numbers according to your choice
print('Welcome to Math quiz')
print("*********************")
print('\n\nEnter your name:')
name=input()
while True:
    s=0
    a=r.randint(1,99)
    b=r.randint(1,99)
    print('\nQuestion 1:',a,'+',b,'=')
    q=int(input())
    if (a+b)==q:
        print('\nCorrect!')
        s+=1
    else:
        print('\nWrong')
    a=r.randint(1,99)
    b=r.randint(1,99)
    print('\nQuestion 2:',a,'-',b,'=')
    q=int(input())
    if (a-b)==q:
        print('\nCorrect!')
        s+=1
    else:
        print('\nWrong')
    while True:
        a=r.randint(50,99)
        b=r.randint(1,50)
        if (a/b)==(a//b):
            break
        else:
            continue
    print('\nQuestion 3:',str(a)+'/'+str(b),'=')
    q=float(input())
    if (a/b)==q:
        print('\nCorrect!')
        s+=1
    else:
        print('\nWrong')
    a=r.randint(1,9)
    b=r.randint(1,99)
    print('\nQuestion 4:',a,'*',b,'=')
    q=int(input())
    if (a*b)==q:
        print('\nCorrect!')
        s+=1
    else:
        print('\nWrong')
    # Add more questions utilizing utilizing the same pattern or a pattern of your choice
    print('\nName:',name,'\nScore:',str(s)+'/4')
    if s==4:                 # Manipulate the messages according to your choice
        print('Excellent!')
    elif s==3:
        print('Very Good')
    elif s>0:
        print('Good')
    elif s==0:
        print('Better luck next time')
    print('\nEnter 1 to retry\nPress enter to exit')
    i=input()
    if i=='1':
        continue
    else:
        break