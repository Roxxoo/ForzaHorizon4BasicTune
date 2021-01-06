from tkinter import *
from tkinter import ttk


def tuning_equation():

    weight = float(e1.get())
    weight_rear = 1.0 - weight
    rear_min = float(e_min_r.get())
    front_min = float(e_min.get())
    front_total = float(e_max.get()) - front_min
    rear_total = float(e_max_r.get()) - rear_min

    ans_front.configure(state=NORMAL)

    ans_front.delete(0, 'end')
    ans_front.insert(0, format((front_total * weight + front_min), '.2f'))
    ans_front.configure(state=DISABLED)
    ans_rear.config(state=NORMAL)
    ans_rear.delete(0, 'end')
    ans_rear.insert(0, format((rear_total * weight_rear + rear_min), '.2f'))
    ans_rear.config(state=DISABLED)


root = Tk()

root.title("my title")
root.geometry('600x320')
root.title("Forza Base Tune Calculator by Roxxoo")
# root.configure(background='white')
main_frame = ttk.Frame(root)
secondary_frame = Frame(root)

secondary_frame.grid(column=1, row=0, sticky=(N, W, E, S), padx=5, pady=5)
main_frame.grid(column=0, row=0, sticky=(N, W, E, S), padx=5, pady=5)

lbltest = Label(secondary_frame, text="TUNING NOTES")
lbltest.grid(column=0,row=0)

lbl_understeer = Label(secondary_frame,text="Understeering:\n1. - front anti-roll stiff\n2. - front springs\n3. + Power to Rear (AWD)\n4. + down force and bump stiff\n5. - front rebound stiff\n6. - Diff Lock %", justify=LEFT, anchor=CENTER, padx=5)
lbl_understeer.grid(column=0, row=1)
lbl_oversteer = Label(secondary_frame, text="Oversteering:\n1. - rear anti-roll stiff\n2. + rear downforce\n3. + rear toe-in\n4. - rear rebound stiff\n5. + diff lock\n6. Center diff towards 50% (AWD)", justify=LEFT, anchor=CENTER, padx=5)
lbl_oversteer.grid(column=1, row=1)
lbl_griploss = Label(secondary_frame, text="Grip loss:\n1. - Diff lock\n2. AWD + Center diff to 50%\n3. Adjust rebound/bump stiff\n4. - Rear rebound stiff\n5. Check camber\n6. Gearing towards speed\n7. Increase downforce\n8. Soften ARB/spring", justify=LEFT, anchor=CENTER)
lbl_griploss.grid(column=0, row=2)

# Front
label_front = ttk.Label(main_frame, text="Front Configuration")
label_front.grid(column=0, row=1, pady=5, padx=5)
label_fr = Label(main_frame, text="Enter Weight in decimal: ")
label_fr.grid(column=0, row=0)
e1 = Entry(main_frame, width=10)
e1.grid(column=1, row=0, padx=5, pady=5)

# max
label2 = ttk.Label(main_frame, text="Enter maximum value: ")
label2.grid(column=0, row=2, padx=2, pady=2)
e_max = Entry(main_frame, width=10)
e_max.grid(column=1, row=2, padx=2, pady=2)

# min
label3 = ttk.Label(main_frame, text="Enter minimum value: ")
label3.grid(column=0, row=3)
e_min = Entry(main_frame, width=10)
e_min.grid(column=1, row=3, padx=5, pady=5)


# Rear
label_front = ttk.Label(main_frame, text="Rear Configuration")
label_front.grid(column=0, row=4, pady=5, padx=5)

# max
label2_r = ttk.Label(main_frame, text="Enter maximum value: ")
label2_r.grid(column=0, row=6, padx=2, pady=2)
e_max_r = Entry(main_frame, width=10)
e_max_r.grid(column=1, row=6, padx=2, pady=2)

# min
label3_r = ttk.Label(main_frame, text="Enter minimum value: ")
label3_r.grid(column=0, row=7)
e_min_r = Entry(main_frame, width=10)
e_min_r.grid(column=1, row=7, padx=2, pady=2)

labelans = ttk.Label(main_frame, text="Front: ")
labelans.grid(column=0, row=10)
ans_front = Entry(main_frame, width=10)
ans_front.config(state=DISABLED)
ans_front.grid(column=1, row=10)
labelansr = ttk.Label(main_frame, text="Rear: ")
labelansr.grid(column=0, row=11)
ans_rear = Entry(main_frame,width=10)
ans_rear.config(state=DISABLED)
ans_rear.grid(column=1,row=11)
btn_calc = Button(main_frame, text="Calculate", command=tuning_equation)
btn_calc.grid(column=0, row=8, pady=5)

root.mainloop()

# This was made by github user Roxxoo