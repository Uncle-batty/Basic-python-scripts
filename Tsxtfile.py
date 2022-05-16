file = open(f'txtxe.txt','w')
file.write("List of numbers to 100 \n")
for k in range(1,101):
   file.write(str(k)+"\n")
file.close()