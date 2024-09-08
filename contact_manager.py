import tkinter as tk
from tkinter import messagebox, simpledialog


contacts = []


def add_contact():
    name = simpledialog.askstring("Input", "Enter Contact Name:")
    if name:
        phone = simpledialog.askstring("Input", "Enter Phone Number:")
        email = simpledialog.askstring("Input", "Enter Email Address:")
        address = simpledialog.askstring("Input", "Enter Contact Address:")
        contacts.append({
            'name': name,
            'phone': phone,
            'email': email,
            'address': address
        })
        messagebox.showinfo("Success", f"Contact for {name} added successfully!")
        display_contacts()


def display_contacts():
    contact_list.delete(0, tk.END)  
    for idx, contact in enumerate(contacts, 1):
        contact_list.insert(tk.END, f"{idx}. {contact['name']} - {contact['phone']}")

def search_contact():
    search_query = simpledialog.askstring("Input", "Search by Name or Phone:")
    if search_query:
        found_contacts = [c for c in contacts if search_query in c['name'] or search_query in c['phone']]
        if found_contacts:
            contact_list.delete(0, tk.END)  
            for idx, contact in enumerate(found_contacts, 1):
                contact_list.insert(tk.END, f"{idx}. {contact['name']} - {contact['phone']}")
        else:
            messagebox.showinfo("Not Found", "No contact found with that name or phone number!")


def update_contact():
    contact_index = simpledialog.askinteger("Input", "Enter the Contact Number to Update:")
    if contact_index and 0 < contact_index <= len(contacts):
        contact = contacts[contact_index - 1]
        new_name = simpledialog.askstring("Input", f"Enter new name for {contact['name']} (or leave blank to keep current):")
        new_phone = simpledialog.askstring("Input", f"Enter new phone for {contact['phone']} (or leave blank to keep current):")
        new_email = simpledialog.askstring("Input", f"Enter new email for {contact['email']} (or leave blank to keep current):")
        new_address = simpledialog.askstring("Input", f"Enter new address for {contact['address']} (or leave blank to keep current):")
        
        
        if new_name:
            contact['name'] = new_name
        if new_phone:
            contact['phone'] = new_phone
        if new_email:
            contact['email'] = new_email
        if new_address:
            contact['address'] = new_address
        
        messagebox.showinfo("Updated", "Contact details updated successfully!")
        display_contacts()
    else:
        messagebox.showwarning("Invalid Input", "No valid contact number selected!")


def delete_contact():
    contact_index = simpledialog.askinteger("Input", "Enter the Contact Number to Delete:")
    if contact_index and 0 < contact_index <= len(contacts):
        contact = contacts.pop(contact_index - 1)
        messagebox.showinfo("Deleted", f"Deleted contact: {contact['name']}")
        display_contacts()
    else:
        messagebox.showwarning("Invalid Input", "No valid contact number selected!")


def quit_app():
    root.quit()


root = tk.Tk()
root.title("Contact Manager")
root.geometry("500x400")


add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.pack(pady=5)

view_button = tk.Button(root, text="View Contacts", command=display_contacts)
view_button.pack(pady=5)

search_button = tk.Button(root, text="Search Contact", command=search_contact)
search_button.pack(pady=5)

update_button = tk.Button(root, text="Update Contact", command=update_contact)
update_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.pack(pady=5)

quit_button = tk.Button(root, text="Quit", command=quit_app)
quit_button.pack(pady=5)


contact_list = tk.Listbox(root, width=60, height=15)
contact_list.pack(pady=10)


root.mainloop()
