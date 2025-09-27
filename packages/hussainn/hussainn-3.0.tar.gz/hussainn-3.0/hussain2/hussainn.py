def indexes():
    cars=['mehran','suzuki','fx','suzuki','alto','corolla','suzuki','xli']
    print(cars)
    indexes=[]
    check=input('Which car you want to check:')

    for i in range(len(cars)):
        if cars[i]==check:
            indexes.append(i)
    if check=='suzuki':
        print(f'keyword:{check}')
        print('count:',cars.count('suzuki'))
        print('indexes:' ,' ,'.join(map(str,indexes)))
    
    else:
        print('invalid input')
        
def booking():
    list1=[0,1]
    name=input('Enter your name:')
    cnic=int(input('Enter your cnic no:'))
    seats=int(input('Enter seats available in next trip:'))


    while True:
    
        a=int(input('press 0 for available\npress 1 for booked\n'))
        if list1[0]== a:
            if seats <= 47:
                print('Seats Available')
                print(f'{seats} seat left')
                b=int(input('Enter a number of seat you need:'))
                seats -= b
                print(f'name={name};\ncnic={cnic};\n{b} seats booked\nThankyou')
                print(f'remaining {seats} left')
                g=int(input('press 3 for continue\npress 4 for quit\n'))
                if g==3:
                    continue
                else:
                    break
            else:
                print('All seat are booked')
        elif list1[1]== a:
            print('All seats are Booked')
            break

def printing():
    while True:
        p=int(input('press 1 for square\npress 2 for triangle\npress 3 for dymand\npress 4 for half kite\n'))

        if p==1:
            for x in range(1,5): 
                print('*' * 6)
            b=int(input('2 for break 0 for continue'))
            if b==2:
                break
            else:
                continue
        elif p==2:
            x=5    
            for i in range(1,5):
                print(' '(x-i)+'' *(2*i-1))
                b=int(input('2 for break 0 for continue'))
                if b==2:
                    break
                else:
                    continue
        elif p==3:
            x=5    
            for i in range(1,5):
                print(' '(x-i)+'' *(2*i-1))
    
            x=5    
            for i in range(5,0,-1):
                print(' '(x-i)+'' *(2*i-1))
                b=int(input('2 for break 0 for continue'))
                if b==2:
                    break
                else:
                    continue
        elif p==4:
            for x in range(1,8):
                print('*' * x)
                b=int(input('2 for break 0 for continue'))
                if b==2:
                    break
                else:
                    continue
