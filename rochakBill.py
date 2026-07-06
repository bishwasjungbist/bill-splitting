
def bill_splitter(grandTotal,rochakPayment):
    #since rochak also had payed during trip too
    return(grandTotal/2-rochakPayment)
def grand_total_calculator(prompt):
    total = 0
    while True:
        #if i had done normal while the conditonal cost==0 would stop inside
        #  code from executing so its a bypass to let cost update
        cost = input(prompt)
        if cost.lower() == "q":
            
            return total
        try:
            total += float(cost)
            print(total)
        except ValueError:
            print("please enter a valid number")
def main():        
    grandTotal=grand_total_calculator("enter amount(q to finish): ")
    print('The total expenditure:',grandTotal)
    rochakPayement=grand_total_calculator("enter rochaks payement(q to finish): ")
    print('The total rochak coverage:',rochakPayement)
    print('Rochak Owe: ',bill_splitter(grandTotal,rochakPayement)) #this prints what rochak owes me

main()