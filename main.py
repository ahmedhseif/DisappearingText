from tkinter import *
import tkinter.font as tkFont


class DisappearTextGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Disappearing Text Writing")
        self.window.geometry("800x600")

        self.frame = Frame(self.window)

        self.label = Label(self.frame, text="Keep writing and don't stop for 5 seconds!", wraplength=700,
                                  font=tkFont.Font(family='Helvetica', size=18))
        self.label.grid(row=0, column=0, columnspan=2, padx=5, pady=10)

        self.text = ""
        self.input_entry = Text(self.frame, width=40, font=("Helvetica", 24), yscrollcommand=True)
        self.input_entry.focus()
        self.input_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)

        self.frame.pack(expand=True)
        self.counter = 0
        self.window.after(1000, self.check_disappear)
        self.window.mainloop()

    def disappear_text(self):
        self.input_entry.delete(1.0, END)
        self.input_entry.insert(END, "")

    def check_disappear(self):
        if self.text == self.input_entry.get(1.0, END):
            if self.counter == 5:
                self.window.after(1000, self.disappear_text)
                self.counter = -1
            self.window.after(1000, self.check_disappear)
            self.counter += 1
        else:
            self.window.after(1000, self.check_disappear)
            self.text = self.input_entry.get(1.0, END)
            self.counter = 0

DisappearTextGUI()