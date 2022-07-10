from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=150)
window.config(padx=20,pady=40)


#Entries
entry = Entry(width=10)
entry.insert(END, string="")
print(entry.get())
entry.grid(column=1,row=0)

#Labels
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0,row=1)

#Labels
mile_label = Label(text="Miles")
mile_label.grid(column=2,row=0)

#Labels
km_label = Label(text="Km")
km_label.grid(column=2,row=1)


#Labels
km_result_label = Label(text="0")
km_result_label.grid(column=1,row=1)

# Buttons
def action():
    mile=float(entry.get())
    km=1.609*mile
    km_result_label.config(text=f"{round(km)}")

button = Button(text="Convert", command=action)
button.grid(column=1,row=2)






window.mainloop()
