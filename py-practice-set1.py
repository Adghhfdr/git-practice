'''
A cashier has currency notes of denominations 1, 5 and 10. If the amount to be withdrawn is input through the keyboard find the total number of currency notes of each denomination the cashier will have to give to the withdrawer.
'''
amount=int(input("Enter the amount : "))
if type(amount)!=int:
    amount=int(input("Enter the amount : "))
amt=amount
note_10= amount//10
amount=amount%10
note_5=amount//5
amount=amount%5
note_1=amount

print(f"Total Amount :{amt}\n 10 : {note_10}\n 5 : {note_5}\n 1 : {note_1}")



    