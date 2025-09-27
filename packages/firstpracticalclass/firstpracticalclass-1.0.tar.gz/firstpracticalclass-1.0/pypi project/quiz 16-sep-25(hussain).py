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
        