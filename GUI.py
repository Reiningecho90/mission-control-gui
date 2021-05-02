from tkinter import *
import random
import time

root = Tk()
root.title("Ground Control Telemetry Stream")
root.geometry('1920x1080')
root.configure(bg='white')

# Data Transmission
data_link = Text(root, bg='white', fg='black', height=1, width=3, font=('Courier', 14))
data_link.pack()
link_label = Label(root, text="Data Uplink Transmission Live:")
link_label.config(bg='white', fg='black', font = ('Courier', 14))
link_label.pack()
link_label.place(x=0, y=0)

# Fault Status
fault_status = Text(root, bg='white', fg='black', height=1, width=1, font=('Courier', 14))
fault_status.pack()
fault_label = Label(root, text="Fault Status (Mission Critical):")
fault_label.config(bg='white', fg='black', font = ('Courier', 14))
fault_label.pack()
fault_label.place(x=0, y=30)

while True:
    # Data Transmission Update Loop
    data_link.delete(1.0, END)
    data_link.place(x=335, y=0)
    data = random.randint(0, 1000)
    data_link.insert(END, data)
    data_link.update()
    data_link.pack()

    fault_status.delete(1.0, END)
    fault_status.place(x=360, y=30)
    data = 1
    fault_status.insert(END, data)
    fault_status.update()
    fault_status.pack()
    time.sleep(0.1)

root.mainloop()