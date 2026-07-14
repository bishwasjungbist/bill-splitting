
import numpy as np
def bill_splitter(grandTotal,rochakPayment ,n):
    #since rochak also had payed during trip too
    return(grandTotal/n-rochakPayment)
def grand_total_calculator(prompt):
    total = 0
    while True:
        #here the prompt is the string I passed because i didnt want to do Input(*specific message everytime*)
        cost = input(prompt)
        if cost.lower() == "q":
            
            return total
        try:
            #I typecasted cost because its string when input is given unless i typecast it at input itself but it would ignore q
            total += float(cost)
            print(total)
        #here bare except error would have even catched keyboard interrupt
        except ValueError:
            print("please enter a valid number")
def main():
    #this finds grandtotal of spending before any splitting is taken into consideration
    grandTotal=grand_total_calculator("enter amount(q to finish): ")
    print('The total expenditure:',grandTotal)

    #now for taking number of people in consideration and splitting 
    numberOfParticipants = int(input("How many people are there: "))

    #this is an float array using numpy library, ill optimize it later
    #person payment holds the final addition of how much an indivual contributed
    person_payment_arr = np.empty(numberOfParticipants, dtype=float)

    #person ower holds the final addition of how much an indivual owes
    person_owe_arr = np.empty(numberOfParticipants, dtype=float) 

    #since for size 2 (2 number of people)to array its initilized as a[0], a[1] so i cant start with 2
    counter = numberOfParticipants -1
    while(counter >= 0):
        #this calls the grand total calcultor which sums up indiviuals payment sequentially
        person_payment_arr[counter] = grand_total_calculator(f"enter person {counter+1} payement (q to finish): ")  
        print('the total coverage by person ',counter + 1 ,": ", person_payment_arr[counter])
        #this bill spllitting function which takes the total payment made by that person and subtracts with per head cost
        person_owe_arr[counter] = bill_splitter(grandTotal,person_payment_arr[counter],numberOfParticipants)
        print('the person ', counter +1 , 'owes: ', person_owe_arr[counter])
        counter -= 1    
main()