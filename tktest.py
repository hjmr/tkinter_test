import tkinter as tk

root = tk.Tk()
root.title("Hello, Tkinter!")
root.geometry("300x200")

frame = tk.Frame(root)
frame.pack(side=tk.TOP)

btn1 = tk.Button(frame, text="Button 1")
btn2 = tk.Button(frame, text="Button 2")

btn1.pack(side=tk.LEFT)
btn2.pack(side=tk.LEFT)

txt = tk.Text(root, height=5, width=25)
txt.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

txt.bind("<KeyPress>", lambda e: print(e))

root.mainloop()
