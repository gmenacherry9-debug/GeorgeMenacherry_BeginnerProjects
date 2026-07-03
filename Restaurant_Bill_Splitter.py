Total_bill = input('Total bill amount: ')
Num_of_guests = input("How many guests are here? ")
Split_tip = 0
if int(Num_of_guests) >= 6:
    Total_with_tip = float(Total_bill) * 0.2 + float(Total_bill)
    print('Tip is 20%')
    print('Total: ', Total_with_tip)
    Split_tip = Total_with_tip / float(Num_of_guests)
    print('Split Amount: ', str(Split_tip))
    print(f'Rounded Amount for each person: ${round(Split_tip, 2)}')
else:
    Total_with_tip = float(Total_bill) * 0.15 + float(Total_bill)
    print('Tip is 15%')
    print('Total', Total_with_tip)
    Split_tip = Total_with_tip / float(Num_of_guests)
    print('Split Amount: ', str(Split_tip))
    print(f'Rounded Amount for each person: ${round(Split_tip, 2)}')
