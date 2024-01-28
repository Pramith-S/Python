print(' CASH REGISTER')
print('****************')
section=['Dairy','Vegetables','Fruits']
dairy=['Milk','Curd','Butter','Cheese']
veg=['Potato','Brinjal','Cabbage','Onion','Capsicum(Bell pepper)','Carrot']
fruit=['Apple','Orange','Banana','Lemon','Grapes','Mango']
dairy_value=[25,25,80,100]
veg_value=[30,50,40,20,60,80]
fruit_value=[150,120,40,300,500,600]
product_quantity={}
product_amount={}
global t
t=0
product_list=[]
global sorted_product_amount
sorted_product_amount={}
def table(product,product_value):
    print('\nSr.No\t\tProduct\t\tPrice(Per unit.)')
    for i in range(len(dairy)):
        print('  {}\t\t {}\t\t   Rs.{}'.format(i+1,product[i],product_value[i]))
def console(sub_section):
    while True:
        print('\nEnter the serial number of the product or press \'ENTER\' to exit section:')
        global f
        f=input()
        if f!='' and f.isdigit()==False :
            print('Enter a valid option!')
            continue
        elif f=='':
            break
        elif int(f)>len(sub_section) or int(f)<1:
            print('Enter a valid option!')
            continue
        return int(f)
        break
def process(product,product_value,product_quantity):
    while True:
        p=0
        if product[(int(f)-1)]=='Milk' or product[(int(f)-1)]=='Curd':
            p='litres'
        else:
            p='Kg'
        print('Enter the quantity of {} in {}:'.format(product[(int(f)-1)],p))
        q=input()
        if (q.isdecimal()==False and q.isdigit==False):
            print('Enter a valid quantity!')
            continue
        q=float(q)
        if product[(int(f)-1)] in product_quantity:
            product_amount[product[(int(f)-1)]]+=product_value[(int(f)-1)]*float(q)
            product_quantity[product[(int(f)-1)]]+=float(q)
        else:
            product_amount[product[(int(f)-1)]]=product_value[(int(f)-1)]*float(q)
            product_quantity[product[(int(f)-1)]]=float(q)
        print('To add more of same product enter 1 or press Enter to add other products:')
        n=input()
        if n=='1':
            continue
        else:
            break
while True:
    print('\nSr.No\t\tSection')
    for i in range(len(section)):
        print('  {}\t\t {}'.format(i+1,section[i]))
    while True:
        print('\nEnter the serial number of the section:')
        s=input()
        if (s.isdigit()==False):
            print('Enter a valid number!')
            continue
        elif (int(s)>len(section) or int(s)<1):
            print('Enter a valid number!')
            continue
        elif s=='1':
            while True:
                table(dairy,dairy_value)
                console(dairy)
                if f=='':
                    break
                process(dairy,dairy_value,product_quantity)
        elif s=='2':
            while True:
                table(veg,veg_value)
                console(veg)
                if f=='':
                    break
                process(veg,veg_value,product_quantity)
        elif s=='3':
            while True:
                table(fruit,fruit_value)
                console(fruit)
                if f=='':
                    break
                process(fruit,fruit_value,product_quantity)
        break
    sorted_product_amount={k:v for k,v in sorted(product_amount.items(),key=lambda item:item[1],reverse=True)}
    product_list=list(sorted_product_amount.items())
    while True:
        print('\nProducts in your cart include:')
        print('\nSr.No.\t\tProduct\t\tQuantity\t\tAmount')
        n=0
        for i,j in sorted_product_amount.items():
            n=n+1
            k='\t'
            p='kg'
            if i=='Milk' or i=='Curd':
                p='litres'
                k=''
            else:
                p='Kg'
            print('  {}\t\t{}\t\t  {}{}\t\t{}Rs.{}'.format(n,i,product_quantity[i],p,k,j))
        print('\nTo add more products enter 1\nTo delete products enter 2\nTo print bill press \'ENTER\'')
        f=input()
        if f!='' and f.isdigit()==False:
            print(f,type(f))
            print('Enter a valid option!')
            continue
        elif f=='2':
            while True:
                p
                print('Enter the serial number of the product to delete or press \'ENTER\' to exit:')
                d=input()
                if d!='' and d.isdigit()==False:
                    print('Enter a valid option!')
                    continue
                elif int(d)<1 or int(d)>len(product_list):
                    print('Enter a valid option!')
                    continue
                elif d.isdigit()==True:
                    product_amount.pop(product_list[int(d)-1][0])
                    product_list.pop(int(d)-1)
                    sorted_product_amount=dict(product_list)
                    print('To delete more enter 1 or to exit press \'ENTER\'')
                    p=input()
                if p=='1':
                    continue
                else:
                    break           
        if f=='2':
            continue
        else:
            break
            
    if f=='1':
        continue
    elif f=='':
        break
print(' BILL')
print('*****')
print('\nSr.No.\t\tProduct\t\tQuantity\t\tAmount')
n=0
for i in product_list:
    p='kg'
    k='\t'
    n=n+1
    t+=i[1]
    if i[0]=='Milk' or i[0]=='Curd':
        p='litres'
        k=''
    else:
        p='Kg'
    print('  {}\t\t{}\t\t  {}{}\t\t{}Rs.{}'.format(n,i[0],product_quantity[(i[0])],p,k,i[1]))
print('\nTotal Amount: Rs.{}'.format(t))