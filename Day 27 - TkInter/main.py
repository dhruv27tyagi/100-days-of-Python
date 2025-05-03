import tkinter as tk

#window = tk.Tk()
#window.title("First GUI Program")

#Label 

#my_label = tk.Label(text="I am a label")
#my_label.pack()

def add(*n):
    sum = 0
    for i in n:
        sum = sum + i

    return sum


print(add(5,6,7,8,9))






#window.mainloop()