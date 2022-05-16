Meun = {'Food' : 100 , 'Drink' : 50 , 'Desert' : 120}
Food_amount = 0
Drink_amount = 0
Desert_amount = 0
def current_invoice():
    f = open('Invoicenumber.txt','r')
    list_ = f.readlines()
    return list_[-1]
    f.close()

def update_current_invoice(slip_number):
    f = open('Invoicenumber.txt','a')
    f.write(f"{slip_number}")
    f.close()
    
def slip_createtion(Name,Food_amount,Drink_amount,Desert_amount,Employye,tip,slip_number ):
    food = (Meun['Food'] * Food_amount)
    drink = (Meun['Drink'] * Drink_amount)
    desert= (Meun['Desert'] * Desert_amount)
    Total = food + drink + desert 
    Sugested_tip = (Total*0.15)
    
    f = open(f"{Name}{slip_number}.txt",'w')
    f.write("_______________________________________________________\n")
    f.write(f"| {Name}\t\tInvoice:{slip_number}\t\tServed By: { Employye}\t\t|\n")
    f.write("|======================================================|\n")
    f.write(f"| Food * {Food_amount}\t\t\t\t\t                    {food}  |\n")
    f.write(f"| Drinks * {Drink_amount}\t\t\t\t\t                   {drink} |\n")
    f.write(f"| Desert* {Desert_amount}\t\t\t\t\t                  {desert} |\n")
    f.write("|                                                                                                                     |\n")
    f.write("|                                                                                                                     |\n")
    f.write("|                                                                                                                     |\n")
    f.write("|======================================================|\n")
    f.write(f"| Subtotal:\t\t\t\t\t {Total}  |\n")
    f.write(f"| Sugested Tip:\t\t\t\t\t {Sugested_tip}  |\n")
    f.write(f"| Tip:                    \t\t\t\t\t\t {tip}  |\n")
    f.write(f"| Total:\t\t\t\t\t\t {Total+tip }  |\n")
    f.write("|______________________________________________________|\n")
    f.close()
    
def print_slip(Name,slip_number ):
    f = open(f"{Name}{slip_number}.txt",'r')
    
    return f.read()

def MENU(): 
    Name = input('Enter clent name: ')
    Food_amount = int(input('How many food items did the clinet order: '))
    Drink_amount = int(input('How many drinks  did the clinet order: '))
    Desert_amount = int(input('How many desert items did the clinet order: '))
    Employye = input('WHo is this:')
    tip = int(input('tip amount: '))
    slip_number =int(current_invoice())
    slip_createtion(Name,Food_amount,Drink_amount,Desert_amount,Employye,tip,(slip_number +1) )
    print(print_slip(Name,(slip_number +1)))
    update_current_invoice(slip_number)
    
    
if __name__ == '__main__':
    MENU()
    