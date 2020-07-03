from tkinter import*
import random
import time;

########################## Window Frame#############################################
root = Tk()

root.geometry("1200x800+0+0")
root.title('Nami Sushi Tip calculator')
root.resizable(True, True)


Tops = Frame(root, width = 800, height = 100, bg = 'powder blue', relief = SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width = 500, height = 500, relief = SUNKEN)
f1.pack(side=LEFT)

###############################Calculate Button################################
b = Button(f1, padx = 3, pady = 3, font = ('arial', 15, 'bold'), text = 'Calculate')
b.grid(row = 6, column = 12)

b1 = Button(f1, padx = 3, pady = 3, font = ('arial', 15, 'bold'), text = 'Calculate')
b1.grid(row = 17, column = 12)

################################locaal time#####################################
localtime =  time.asctime(time.localtime(time.time()))


################################Info and title############################################
lblInfo = Label(Tops, font = ('arial', 30, 'bold'),
                text = 'Nami Suhi',
                fg = 'Steel Blue', bd = 10,
                anchor = 'w')

lblInfo.grid(row = 0, column = 1)

lblInfo = Label(Tops, font = ('arial', 10, 'bold'),
                text = localtime,
                fg = 'Steel Blue', bd = 10,
                anchor = 'w')
lblInfo.grid(row = 1, column = 1)


############################### Morning Section ####################################


label_morning = Label(f1, font = ('arial', 15, 'bold'), text = 'Morning')
label_morning.grid(row = 0, column = 1)

label_c = Label(f1, font = ('arial', 15, 'bold'), text = 'Cash')
label_c.grid(row = 1, column = 0,)
input_c = Entry(f1, width = 20, bg = 'powder blue')
input_c.grid(row = 1, column = 1)

label_card = Label(f1, font = ('arial', 15, 'bold'), text = 'Card')
label_card.grid(row = 2, column = 0)
input_card = Entry(f1, width = 20, bg = 'powder blue')
input_card.grid(row = 2, column = 1)


label_uber = Label(f1, font = ('arial', 15, 'bold'), text = 'Uber')
label_uber.grid(row = 3, column = 0)

input_uber = Entry(f1, width = 20, bg = 'powder blue')
input_uber.grid(row = 3, column = 1)

label_door = Label(f1, font = ('arial', 15, 'bold'), text = 'Door')
label_door.grid(row = 4, column = 0)

input_door = Entry(f1, width = 20, bg = 'powder blue')
input_door.grid(row = 4, column = 1)
space = Label(f1, font = ('arial', 3, 'bold'), text = '  ')
space.grid(row = 5, column = 0)

############################### Afternoon Section ####################################

space = Label(f1, font = ('arial', 3, 'bold'), text = '  ')
space.grid(row = 9, column = 0)

label_afternoon = Label(f1, font = ('arial', 15, 'bold'), text = 'Afternoon')
label_afternoon.grid(row = 10, column = 1)

label_c1 = Label(f1, font = ('arial', 15, 'bold'), text = 'Cash')
label_c1.grid(row = 11, column = 0,)
input_c1 = Entry(f1, width = 20, bg = 'powder blue')
input_c1.grid(row = 11, column = 1)

label_card1 = Label(f1, font = ('arial', 15, 'bold'), text = 'Card')
label_card1.grid(row = 12, column = 0)
input_card1 = Entry(f1, width = 20, bg = 'powder blue')
input_card1.grid(row = 12, column = 1)

label_uber1 = Label(f1, font = ('arial', 15, 'bold'), text = 'Uber')
label_uber1.grid(row = 13, column = 0)
input_uber1 = Entry(f1, width = 20, bg = 'powder blue')
input_uber1.grid(row = 13, column = 1)

label_door1 = Label(f1, font = ('arial', 15, 'bold'), text = 'Door')
label_door1.grid(row = 14, column = 0)
input_door1 = Entry(f1, width = 20, bg = 'powder blue')
input_door1.grid(row = 14, column = 1)


sales_total1 = Label(f1, font = ('arial', 3, 'bold'), text = '  ')
sales_total1.grid(row = 15, column = 0)

tip_space = Label(f1, font = ('arial', 15, 'bold'), text = '   ')
tip_space.grid(row = 16, column = 3)

total_tip = Label(f1, font = ('arial', 15, 'bold'), text = 'Total Tip')
total_tip.grid(row = 16, column = 4)
total_tip_input = Entry(f1, width = 20)
total_tip_input.grid(row = 16, column = 5)

Card_tip_fee = Label(f1, font = ('arial', 15, 'bold'), text = 'Card Tip Fee')
Card_tip_fee.grid(row = 17, column = 4)
Card_tip_fee_input = Entry(f1, width = 20)
Card_tip_fee_input.grid(row = 17, column = 5)

space = Label(f1, font = ('arial', 20, 'bold'), text = '  ')
space.grid(row = 19, column = 0)



################################ User Type Section##############################



################################ Morning Tip Section  ##################################

tip_space = Label(f1, font = ('arial', 15, 'bold'), text = '   ')
tip_space.grid(row = 1, column = 3)

tip = Label(f1, font = ('arial', 15, 'bold'), text = 'Cash Tip')
tip.grid(row = 1, column = 4)

input_tip = Entry(f1, width = 20, bg = 'powder blue')
input_tip.grid(row = 1, column = 5)

tip_card = Label(f1, font = ('arial', 15, 'bold'), text = 'Card Tip')
tip_card.grid(row = 2, column = 4)

input_tip_card = Entry(f1, width = 20, bg = 'powder blue')
input_tip_card.grid(row = 2, column = 5)



################################ Afternoon Tip Section  ##################################
tip1 = Label(f1, font = ('arial', 15, 'bold'), text = 'Cash Tip')
tip1.grid(row = 11, column = 4)

input_tip1 = Entry(f1, width = 20, bg = 'powder blue')
input_tip1.grid(row = 11, column = 5)

tip_card1 = Label(f1, font = ('arial', 15, 'bold'), text = 'Card Tip')
tip_card1.grid(row = 12, column = 4)

input_tip_card1 = Entry(f1, width = 20, bg = 'powder blue')
input_tip_card1.grid(row = 12, column = 5)

############################Kitchen and waitress tip section#################################
tip_space = Label(f1, font = ('arial', 15, 'bold'), text = '   ')
tip_space.grid(row = 1, column = 6)

kitchen_tip = Label(f1, font = ('arial', 15, 'bold'), text = 'Kitchen Tip')
kitchen_tip.grid(row = 1, column = 7)
input_kitchen_tip = Entry(f1, width = 20)
input_kitchen_tip.grid(row = 1, column = 8)

tip_space = Label(f1, font = ('arial', 15, 'bold'), text = '   ')
tip_space.grid(row = 2, column = 6)

waitress_tip = Label(f1, font = ('arial', 15, 'bold'), text = 'Waitress tip')
waitress_tip.grid(row = 2, column = 7)
input_waitress_tip = Entry(f1, width = 20)
input_waitress_tip.grid(row = 2, column = 8)


tip_space1 = Label(f1, font = ('arial', 15, 'bold'), text = '   ')
tip_space1.grid(row = 11, column = 6)

kitchen_tip1 = Label(f1, font = ('arial', 15, 'bold'), text = 'Kitchen Tip')
kitchen_tip1.grid(row = 11, column = 7)
input_kitchen_tip1 = Entry(f1, width = 20)
input_kitchen_tip1.grid(row = 11, column = 8)


tip_space = Label(f1, font = ('arial', 15, 'bold'), text = '   ')
tip_space.grid(row = 12, column = 6)

waitress_tip1 = Label(f1, font = ('arial', 15, 'bold'), text = 'Waitress tip')
waitress_tip1.grid(row = 12, column = 7)
input_waitress_tip1 = Entry(f1, width = 20)
input_waitress_tip1.grid(row = 12, column = 8)

#################################Calculation Part#####################################
sales_total = Label(f1, font = ('arial', 15, 'bold'), text = 'Sales Total')
sales_total.grid(row = 6, column = 0)
calculate_total = Entry(f1, width = 20)
calculate_total.grid(row = 6, column = 1)

tax = Label(f1, font = ('arial', 15, 'bold'), text = 'Tax')
tax.grid(row = 7, column = 0)
tax_input = Entry(f1, width = 20)
tax_input.grid(row = 7, column = 1)

total = Label(f1, font = ('arial', 15, 'bold'), text = 'Total')
total.grid(row = 8, column = 0)
total_input = Entry(f1, width = 20)
total_input.grid(row = 8, column = 1)

sales_total1 = Label(f1, font = ('arial', 15, 'bold'), text = 'Sales Total')
sales_total1.grid(row = 16, column = 0)
calculate_total1 = Entry(f1, width = 20)
calculate_total1.grid(row = 16, column = 1)


tax1 = Label(f1, font = ('arial', 15, 'bold'), text = 'Tax')
tax1.grid(row = 17, column = 0)
tax_input1 = Entry(f1, width = 20)
tax_input1.grid(row = 17, column = 1)

total1 = Label(f1, font = ('arial', 15, 'bold'), text = 'Total')
total1.grid(row = 18, column = 0)
total_input1 = Entry(f1, width = 20)
total_input1.grid(row = 18, column = 1)


#####################################Calculation Tip###################################
tip_space = Label(f1, font = ('arial', 15, 'bold'), text = '   ')
tip_space.grid(row = 6, column = 3)

total_tip = Label(f1, font = ('arial', 15, 'bold'), text = 'Total Tip')
total_tip.grid(row = 6, column = 4)
total_tip_input = Entry(f1, width = 20)
total_tip_input.grid(row = 6, column = 5)

Card_tip_fee1 = Label(f1, font = ('arial', 15, 'bold'), text = 'Card Tip Fee')
Card_tip_fee1.grid(row = 7, column = 4)
Card_tip_fee_input1 = Entry(f1, width = 20)
Card_tip_fee_input1.grid(row = 7, column = 5)



########################################Enter button Click######################################

###################################

hr_space = Label(f1, font = ('arial', 15, 'bold'), text = '   ')
hr_space.grid(row = 1, column = 9)


scrollbar = Scrollbar(f1)

listbox = Listbox(f1, selectmode = 'extended', height = 1, yscrollcommand = scrollbar.set)
listbox.insert(0,'waitress 1')
listbox.insert(END,'waitress 2')
listbox.insert(END,'waitress 3')
listbox.insert(END,'waitress 4')
listbox.grid(row = 1, column = 10)
scrollbar.grid(row = 1, column = 11)

scrollbar.config(command = listbox.yview)

scrollbar1 = Scrollbar(f1)
listbox1 = Listbox(f1, selectmode = 'extended', height = 1, yscrollcommand = scrollbar1.set)
listbox1.insert(0,'waitress 1')
listbox1.insert(END,'waitress 2')
listbox1.insert(END,'waitress 3')
listbox1.insert(END,'waitress 4')
listbox1.grid(row = 2, column = 10)
scrollbar1.grid(row = 2, column = 11)

scrollbar1.config(command = listbox1.yview)

scrollbar2 = Scrollbar(f1)
listbox2 = Listbox(f1, selectmode = 'extended', height = 1, yscrollcommand = scrollbar2.set)
listbox2.insert(0,'waitress 1')
listbox2.insert(END,'waitress 2')
listbox2.insert(END,'waitress 3')
listbox2.insert(END,'waitress 4')
listbox2.grid(row = 3, column = 10)
scrollbar2.grid(row = 3, column = 11)

scrollbar2.config(command = listbox2.yview)

scrollbar3 = Scrollbar(f1)
listbox3 = Listbox(f1, selectmode = 'extended', height = 1, yscrollcommand = scrollbar3.set)
listbox3.insert(0,'waitress 1')
listbox3.insert(END,'waitress 2')
listbox3.insert(END,'waitress 3')
listbox3.insert(END,'waitress 4')
listbox3.grid(row = 4, column = 10)
scrollbar3.grid(row = 4, column = 11)

scrollbar3.config(command = listbox3.yview)


hr_space = Label(f1, font = ('arial', 15, 'bold'), text = '   ')
hr_space.grid(row = 11, column = 9)


scrollbar4 = Scrollbar(f1)

listbox4 = Listbox(f1, selectmode = 'extended', height = 1, yscrollcommand = scrollbar4.set)
listbox4.insert(0,'waitress 1')
listbox4.insert(END,'waitress 2')
listbox4.insert(END,'waitress 3')
listbox4.insert(END,'waitress 4')
listbox4.grid(row = 11, column = 10)
scrollbar4.grid(row = 11, column = 11)

scrollbar4.config(command = listbox4.yview)

scrollbar5 = Scrollbar(f1)
listbox5 = Listbox(f1, selectmode = 'extended', height = 1, yscrollcommand = scrollbar5.set)
listbox5.insert(0,'waitress 1')
listbox5.insert(END,'waitress 2')
listbox5.insert(END,'waitress 3')
listbox5.insert(END,'waitress 4')
listbox5.grid(row = 12, column = 10)
scrollbar5.grid(row = 12, column = 11)

scrollbar5.config(command = listbox5.yview)

scrollbar6 = Scrollbar(f1)
listbox6 = Listbox(f1, selectmode = 'extended', height = 1, yscrollcommand = scrollbar6.set)
listbox6.insert(0,'waitress 1')
listbox6.insert(END,'waitress 2')
listbox6.insert(END,'waitress 3')
listbox6.insert(END,'waitress 4')
listbox6.grid(row = 13, column = 10)
scrollbar6.grid(row = 13, column = 11)

scrollbar6.config(command = listbox6.yview)

scrollbar7 = Scrollbar(f1)
listbox7 = Listbox(f1, selectmode = 'extended', height = 1, yscrollcommand = scrollbar7.set)
listbox7.insert(0,'waitress 1')
listbox7.insert(END,'waitress 2')
listbox7.insert(END,'waitress 3')
listbox7.insert(END,'waitress 4')
listbox7.grid(row = 14, column = 10)
scrollbar7.grid(row = 14, column = 11)

scrollbar7.config(command = listbox7.yview)

###########################waitress HR##################################
input_hr = Entry(f1, width = 5, bg = 'powder blue')
input_hr.grid(row = 1, column = 12)

label_hr = Label(f1, font = ('arial', 10, 'bold'), text = 'hr')
label_hr.grid(row = 1, column = 13,)

input_hr1 = Entry(f1, width = 5, bg = 'powder blue')
input_hr1.grid(row = 2, column = 12)

label_hr1 = Label(f1, font = ('arial', 10, 'bold'), text = 'hr')
label_hr1.grid(row = 2, column = 13,)

input_hr2 = Entry(f1, width = 5, bg = 'powder blue')
input_hr2.grid(row = 3, column = 12)

label_hr2 = Label(f1, font = ('arial', 10, 'bold'), text = 'hr')
label_hr2.grid(row = 3, column = 13,)

input_hr3 = Entry(f1, width = 5, bg = 'powder blue')
input_hr3.grid(row = 4, column = 12)

label_hr3 = Label(f1, font = ('arial', 10, 'bold'), text = 'hr')
label_hr3.grid(row = 4, column = 13,)

input_hr = Entry(f1, width = 5, bg = 'powder blue')
input_hr.grid(row = 1, column = 12)

label_hr = Label(f1, font = ('arial', 10, 'bold'), text = 'hr')
label_hr.grid(row = 1, column = 13,)

input_hr1 = Entry(f1, width = 5, bg = 'powder blue')
input_hr1.grid(row = 2, column = 12)

label_hr1 = Label(f1, font = ('arial', 10, 'bold'), text = 'hr')
label_hr1.grid(row = 2, column = 13,)

input_hr2 = Entry(f1, width = 5, bg = 'powder blue')
input_hr2.grid(row = 3, column = 12)

label_hr2 = Label(f1, font = ('arial', 10, 'bold'), text = 'hr')
label_hr2.grid(row = 3, column = 13,)

input_hr3 = Entry(f1, width = 5, bg = 'powder blue')
input_hr3.grid(row = 4, column = 12)

label_hr3 = Label(f1, font = ('arial', 10, 'bold'), text = 'hr')
label_hr3.grid(row = 4, column = 13,)


input_hr4 = Entry(f1, width = 5, bg = 'powder blue')
input_hr4.grid(row = 11, column = 12)

label_hr4 = Label(f1, font = ('arial', 10, 'bold'), text = 'hr')
label_hr4.grid(row = 11, column = 13,)

input_hr5 = Entry(f1, width = 5, bg = 'powder blue')
input_hr5.grid(row = 12, column = 12)

label_hr5 = Label(f1, font = ('arial', 10, 'bold'), text = 'hr')
label_hr5.grid(row = 12, column = 13,)

input_hr6 = Entry(f1, width = 5, bg = 'powder blue')
input_hr6.grid(row = 13, column = 12)

label_hr6 = Label(f1, font = ('arial', 10, 'bold'), text = 'hr')
label_hr6.grid(row = 13, column = 13,)

input_hr7 = Entry(f1, width = 5, bg = 'powder blue')
input_hr7.grid(row = 14, column = 12)

label_hr7 = Label(f1, font = ('arial', 10, 'bold'), text = 'hr')
label_hr7.grid(row = 14, column = 13,)


#######################################tip################final_tip########
label_final_tip = Label(f1, font = ('arial', 10, 'bold'), text = '$')
label_final_tip.grid(row = 1, column = 14,)

input_final_tip = Entry(f1, width = 15)
input_final_tip.grid(row = 1, column = 15)

label_final_tip1 = Label(f1, font = ('arial', 10, 'bold'), text = '$')
label_final_tip1.grid(row = 2, column = 14,)

input_final_tip1 = Entry(f1, width = 15)
input_final_tip1.grid(row = 2, column = 15)

label_final_tip2 = Label(f1, font = ('arial', 10, 'bold'), text = '$')
label_final_tip2.grid(row = 3, column = 14,)

input_final_tip2 = Entry(f1, width = 15)
input_final_tip2.grid(row = 3, column = 15)

label_final_tip3 = Label(f1, font = ('arial', 10, 'bold'), text = '$')
label_final_tip3.grid(row = 4, column = 14,)

input_final_tip3 = Entry(f1, width = 15)
input_final_tip3.grid(row = 4, column = 15)


label_final_tip4 = Label(f1, font = ('arial', 10, 'bold'), text = '$')
label_final_tip4.grid(row = 11, column = 14,)

input_final_tip4 = Entry(f1, width = 15)
input_final_tip4.grid(row = 11, column = 15)

label_final_tip5 = Label(f1, font = ('arial', 10, 'bold'), text = '$')
label_final_tip5.grid(row = 12, column = 14,)

input_final_tip5 = Entry(f1, width = 15)
input_final_tip5.grid(row = 12, column = 15)

label_final_tip6 = Label(f1, font = ('arial', 10, 'bold'), text = '$')
label_final_tip6.grid(row = 13, column = 14,)

input_final_tip6 = Entry(f1, width = 15)
input_final_tip6.grid(row = 13, column = 15)

label_final_tip7 = Label(f1, font = ('arial', 10, 'bold'), text = '$')
label_final_tip7.grid(row = 14, column = 14,)

input_final_tip7 = Entry(f1, width = 15)
input_final_tip7.grid(row = 14, column = 15)

root.mainloop()