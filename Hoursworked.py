hours = input('hours : ',)

if int(hours) > 8 :
    extra_cash = 80 *( int(hours) - 8 )
    pay =( int(hours) * 100) + extra_cash
else:
    pay = int(hours )* 100
    
    
print(str(pay))
    

    
