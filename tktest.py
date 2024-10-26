import tkinter as tk


def btn_click(hello):
    name_str = name_txt.get()
    msg_txt.config(state=tk.NORMAL)
    msg_txt.insert(tk.END, f"{hello}, {name_str}.\n")
    msg_txt.config(state=tk.DISABLED)


root = tk.Tk()
root.title("Hello, Tkinter!")
root.geometry("300x200")

btn_frame = tk.Frame(root)
btn_frame.pack(side=tk.TOP)

btn1 = tk.Button(btn_frame, text="Hello", command=lambda: btn_click("Hello"))
btn2 = tk.Button(btn_frame, text="Bonjour", command=lambda: btn_click("Bonjour"))

btn1.pack(side=tk.LEFT)
btn2.pack(side=tk.LEFT)

name_frame = tk.Frame(root)
name_frame.pack(side=tk.TOP)

name_label = tk.Label(name_frame, text="Name:")
name_txt = tk.Entry(name_frame)

name_label.pack(side=tk.LEFT)
name_txt.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

msg_txt = tk.Text(root, wrap=tk.WORD, state=tk.DISABLED)
msg_txt.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

root.mainloop()
