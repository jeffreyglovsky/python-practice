a = input('Enter Temp\n') #enter temp

while True:  #ensure that temp is an integer
    try:
        a = int(a)
        break
    except:
        print('Enter Number \n')
        a = input()

b = input('C or F?\n') #enter if its C or F

while b != 'C' and b != 'F':
    b = input('Please type C or F \n')

if b == 'C': 
    d = int(((a*9)/5)+32)
    e = 'F'
else:
    d = int((a-32)*(5/9))
    e = 'C'

    
    
print(a,'degrees',b,'is',d,'degrees',e)