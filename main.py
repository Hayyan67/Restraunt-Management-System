import tkinter as tk
from tkinter import ttk, messagebox

class RestrauntOrderManagement:
    def __ini__(self, root):
        self.root = root
        self.root.title("Restraunt Management app")

        self.menue_items = {
            "FRIES" : 2
            "LUNCH MEAL" : 4
            "CHEESE BURGER" : 3
            "PIZZA" : 4
        }
        
        self.exchange_rate = 86
        self.setup_background(root)

        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        ttk.Label(frame, text="RESTRAUNT ORDER MANAGEMENT", font=("Arial", 20, "bold")).grid(row=0,
                                                                                             columnspan=3,
                                                                                             padx=10,
                                                                                             pady=10)
        self.menue_labels = {}
        self.menue_quantities = {}

        for i (item, price) in enumerate(self.menue_items.items(), start=1):
            label = ttk.Label(frame,
                              text=f"{item} (${price}):",
                              font=("Arial", 12))
            label.grid(row=i, column=0, padx=10, pady=5)
            self.menue_labels[item] = label
            
            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5 )
            self.menue_quantities[item] = quantity_entry

        self.currency_var = ttk.StringVar()
        ttk.Label(frame, text="Currency:", font=("Arial", 12)).grid(row=0,
                                                                     columnspan=3,
                                                                     padx=10,
                                                                    pady=5)
        
        currency_dropdown = ttk.Combobox(frame,
                                         textvariable=self.currency_var,
                                         state="readonly",
                                         width=18,
                                         values=("USD", "INR"))
        currency_dropdown.grid(row=len(self.menue_items)+1,
                               column=1,
                               padx=10,
                               pady=5)
        currency_dropdown.current(0)
        self.currency_var.trace('w', self.update_menue.prices)
                               