import tkinter as tk
from tkinter import messagebox
import json

# ---------- File to save customer data ----------
CUSTOMER_FILE = "customers.json"

# ---------- Load saved customers ----------
def load_customers():
    try:
        with open(CUSTOMER_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# ---------- Save customers ----------
def save_customers(customers):
    with open(CUSTOMER_FILE, "w") as f:
        json.dump(customers, f, indent=4)

# ---------- Add new customer ----------
def add_customer():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()

    if name == "" or email == "" or phone == "":
        messagebox.showwarning("Input Error", "Please fill all fields")
        return

    customers.append({"name": name, "email": email, "phone": phone})
    save_customers(customers)
    update_customer_list()
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

# ---------- Update selected customer ----------
def update_customer():
    selected = customer_list.curselection()
    if not selected:
        messagebox.showinfo("No Selection", "Select a customer to update")
        return
    index = selected[0]
    customers[index]["name"] = name_entry.get()
    customers[index]["email"] = email_entry.get()
    customers[index]["phone"] = phone_entry.get()
    save_customers(customers)
    update_customer_list()

# ---------- Delete selected customer ----------
def delete_customer():
    selected = customer_list.curselection()
    if not selected:
        messagebox.showinfo("No Selection", "Select a customer to delete")
        return
    index = selected[0]
    customers.pop(index)
    save_customers(customers)
    update_customer_list()

# ---------- Display customers ----------
def update_customer_list():
    customer_list.delete(0, tk.END)
    for i, c in enumerate(customers):
        customer_list.insert(tk.END, f"{i+1}. {c['name']} | {c['email']} | {c['phone']}")

# ---------- GUI Setup ----------
root = tk.Tk()
root.title("💼 Customer Relationship Management System")
root.geometry("600x400")

customers = load_customers()

# Input Fields
tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root, width=50)
name_entry.pack()

tk.Label(root, text="Email:").pack()
email_entry = tk.Entry(root, width=50)
email_entry.pack()

tk.Label(root, text="Phone:").pack()
phone_entry = tk.Entry(root, width=50)
phone_entry.pack()

# Buttons
tk.Button(root, text="Add Customer", command=add_customer).pack(pady=5)
tk.Button(root, text="Update Customer", command=update_customer).pack(pady=5)
tk.Button(root, text="Delete Customer", command=delete_customer).pack(pady=5)

# Customer List
customer_list = tk.Listbox(root, width=80, height=10)
customer_list.pack(pady=10)

# Initialize display
update_customer_list()

root.mainloop()
