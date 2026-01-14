import tkinter as tk

# Create main window
root = tk.Tk()
root.title("My First Tkinter App")
root.geometry("400x200")  # Width x Height

# Function to run when button is clicked
def on_click():
    label.config(text="Hello, Tkinter!")

# Create a label
label = tk.Label(root, text="Welcome!", font=("Arial", 16))
label.pack(pady=20)

# Create a button
button = tk.Button(root, text="Click Me", command=on_click, font=("Arial", 14))
button.pack(pady=10)

# Run the app
root.mainloop()
