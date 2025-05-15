import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.title("Delivery Cost Calculator")

# Prices for different locations and weights
prices = {
    "PAU": {"under_10kg": 1500, "over_10kg": 2000},
    "EPE": {"under_10kg": 4000, "over_10kg": 5000}
}

# Function to calculate and display cost
def calculate():
    location = location_var.get()
    try:
        weight = float(weight_entry.get())
        
        if weight >= 10:
            cost = prices[location]["over_10kg"]
        else:
            cost = prices[location]["under_10kg"]
            
        result_label.config(text=f"Cost: N{cost}")
    except:
        messagebox.showerror("Error", "Please enter a valid weight")

# Location selection
tk.Label(window, text="Select Location:").pack()
location_var = tk.StringVar(value="PAU")
tk.OptionMenu(window, location_var, "PAU", "EPE").pack()

# Weight input
tk.Label(window, text="Enter Weight (kg):").pack()
weight_entry = tk.Entry(window)
weight_entry.pack()

# Calculate button
tk.Button(window, text="Calculate Cost", command=calculate).pack(pady=10)

# Result display
result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack()

# Run the application
window.mainloop()