
def BillSpliter(grandTotal,rochakPayment):
    #since rochak had payed during trip too
    return((grandTotal/2)-rochakPayment)
def grandTotalCalculator():
    add=0
    cost = 0
    while True:
        #if i had done normal while the conditonal cost==0 would stop inside
        #  code from executing so its a bypass to let cost update
        cost=input("enter the cost(enter q to conclude): ")
        if cost.lower() == "q":
            cost = 0
            return add
        try:
            add += float(cost)
            print(add)
        except:
            print("please enter a valid number")
grandTotal=grandTotalCalculator()
print('The total expenditure:',grandTotal)
print('How much has rochak payed?: ')
rochakPayement=grandTotalCalculator()
print('The total rochak coverage:',rochakPayement)
print('Rochak Owe: ',BillSpliter(grandTotal,rochakPayement)) #this prints what rochak owes me
