print("select the operation:")
print("1. Add ")
print("2. subtraction ")
print("3. Multiplication ")
print("4. divide ")
print("5. stop ")
try:
 while True:
  operation = input("select the operation:")
  if operation=='stop' or operation=="5":
      break
  if operation == '1':
   # code for add
    num1 = input('enter the first number:')
    num2 = input('enter the second number:')
    print('sum of these num =' + str(int(num1)+int(num2)))
  elif operation == "2":
   # code for sub
    num1=input('enter the first number:')
    num2=input('enter the second number:')
    print('sub of these num ='+str(int(num1)-int(num2)))
  elif operation == "3":
    # code for multiplication
    num1 = input('enter the first number:')
    num2 = input('enter the second number:')
    print('sum of these num ='+str(int(num1)*int(num2)))
  elif operation == "4":
    # code for div
    num1 = input('enter the first number:')
    num2 = input('enter the second number:')
    print('div of these num ='+str(int(num1)/int(num2)))
  else:
    print("Invalid Entry")
except:
    print("intrupt")



