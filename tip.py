import math


print('Enter card tip')
card_tip = input()
card_tip = float(card_tip)

print('Enter cash tip')
cash_tip = input()
cash_tip = float(cash_tip)

total_tip = (card_tip * 0.97) + cash_tip
total_tip = float(total_tip)
tip_fee = card_tip * 0.03

print('Total tip is: ${:.2f}'.format(total_tip))
print('Card tip fee is ${:.2f}'.format(tip_fee))


# Getting information of tips
# Calculate kitchen tips and waitress tips


w_tip = total_tip * 0.7
k_tip = total_tip - w_tip
print("Waitress total tip is {:.2f}".format(w_tip))
print("Kitchen tip is {:.2f}".format(k_tip))

# Check how many waitress work today
print("How many waitress work today?")
n_waitress = input()
n_waitress = int(n_waitress)

# Create dictionary and make the number of key regards to the number of waitress
timeTable = {}
for i in range(n_waitress):
    orderOfWaitress = i + 1
    print("how many hours work {} wairtess?".format(orderOfWaitress))
    hours = input()
    hours = float(hours)
    timeTable.update({i+1 : hours})

# Calculate total hour of waitress
total_hours = sum(timeTable.values())

# Calculate each waitress tips
for i in range(n_waitress):
    x = timeTable.get(i+1)
    ratioTips = float(x / total_hours)
    each_tips = ratioTips * w_tip
    print("Waitress {} will get {:.2f}".format(i+1, each_tips))
