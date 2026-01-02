'''
A cashier has currency notes of denominations 1, 5 and 10. If the amount to be withdrawn is input through the keyboard find the total number of currency notes of each denomination the cashier will have to give to the withdrawer.
'''
amount=int(input("Enter the amount : "))
if type(amount)!=int:
    amount=int(input("Enter the amount : "))
total_amt=amount
note={10:0,5:0,1:0}
note[10]=amount//10
amount=amount%10
note[5]=amount//5
amount=amount%5
note[1]=amount
print(f"Total Amount :{total_amt}\n 10 : {note[10]}\n 5 : {note[5]}\n 1 : {note[1]}")



    