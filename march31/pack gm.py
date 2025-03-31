import tkinter as tk

# Window 1: Using pack geometry manager
def window1():
    win1 = tk.Tk()
    win1.title("Window 1 - pack")

    label1 = tk.Label(win1, text="Button 1")
    label1.pack(pady=5)
    button1 = tk.Button(win1, text="Click Me 1", command=lambda: label1.config(text="Button 1 Clicked"))
    button1.pack(pady=5)

    label2 = tk.Label(win1, text="Button 2")
    label2.pack(pady=5)
    button2 = tk.Button(win1, text="Click Me 2", command=lambda: label2.config(text="Button 2 Clicked"))
    button2.pack(pady=5)

    win1.geometry("200x200")
    win1.mainloop()

# Window 2: Using grid geometry manager
def window2():
    win2 = tk.Tk()
    win2.title("Window 2 - grid")

    label1 = tk.Label(win2, text="Button 1")
    label1.grid(row=0, column=0, padx=10, pady=5)
    button1 = tk.Button(win2, text="Click Me 1", command=lambda: label1.config(text="Button 1 Clicked"))
    button1.grid(row=0, column=1, padx=10, pady=5)

    label2 = tk.Label(win2, text="Button 2")
    label2.grid(row=1, column=0, padx=10, pady=5)
    button2 = tk.Button(win2, text="Click Me 2", command=lambda: label2.config(text="Button 2 Clicked"))
    button2.grid(row=1, column=1, padx=10, pady=5)

    win2.geometry("250x150")
    win2.mainloop()

# Window 3: Using place geometry manager
def window3():
    win3 = tk.Tk()
    win3.title("Window 3 - place")

    label1 = tk.Label(win3, text="Button 1")
    label1.place(x=50, y=30)
    button1 = tk.Button(win3, text="Click Me 1", command=lambda: label1.config(text="Button 1 Clicked"))
    button1.place(x=150, y=25)

    label2 = tk.Label(win3, text="Button 2")
    label2.place(x=50, y=80)
    button2 = tk.Button(win3, text="Click Me 2", command=lambda: label2.config(text="Button 2 Clicked"))
    button2.place(x=150, y=75)

    win3.geometry("300x150")
    win3.mainloop()

# Run each window in its own thread to show them simultaneously
import threading

# Create threads for each window to run them concurrently
thread1 = threading.Thread(target=window1)
thread2 = threading.Thread(target=window2)
thread3 = threading.Thread(target=window3)

# Start the threads
thread1.start()
thread2.start()
thread3.start()
