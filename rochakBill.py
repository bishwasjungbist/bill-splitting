
import numpy as np
def bill_splitter(grandTotal,rochakPayment ,n):
    #since rochak also had payed during trip too
    return(grandTotal/n-rochakPayment)
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
    numberOfParticipants = int(input("How many people are there: "))
    person_payment_arr = np.empty(numberOfParticipants, dtype=float) 
    person_owe_arr = np.empty(numberOfParticipants, dtype=float) 
    counter = numberOfParticipants -1
    while(counter >= 0):
        person_payment_arr[counter] = grand_total_calculator(f"enter person {counter+1} payement (q to finish): ")  
        print('the total coverage by person ',counter + 1 ,": ", person_payment_arr[counter])
        person_owe_arr[counter] = bill_splitter(grandTotal,person_payment_arr[counter],numberOfParticipants)
        print('the person ', counter +1 , 'owes: ', person_owe_arr[counter])
        counter -= 1    
main()