import tkinter as tk

root = tk.Tk()
root.title("Vk-backup")

def access():
    print("enter")
def confirm():
    vk_id = usid.get()
    if vk_id.isdigit() and len(vk_id) == 9:
        usid.configure(state="disabled")
        btn.grid_forget()
        error.pack_forget()
        settings.pack()
    else:
        error.pack()



vk = tk.LabelFrame(width=200, height=200, text="Log in")
greeting = tk.Label(root, text="Welcome to the program 'vk-backup'")
greeting.pack()
vk.pack(fill="both", expand=True)
vkid = tk.Frame(vk)
label1 = tk.Label(vkid, text="Enter vk_id:")
btn = tk.Button(vkid, text="Confirm", activebackground="green", bg="blue",
                              fg="white", command=confirm)
usid = tk.Entry(vkid)
sp = tk.Spinbox(vk, from_=1, to=10)
label1.grid(sticky="w", row=0, column=0)
usid.grid(row=1, column=0)
btn.grid(row=1, column=2)
vkid.pack(padx=30, pady=20)


error = tk.Message(width=200, text="Incorrect id")
oauth = tk.Message(width=200, text="authorization")
settings = tk.LabelFrame(width=200, height=200, text="Settings")



y_radio = tk.Radiobutton(settings, text="Yandex.Disk")
g_radio = tk.Radiobutton(settings, text="Google.Drive")
y_radio.pack()
g_radio.pack()
ch1 = tk.IntVar()
check = tk.Checkbutton(settings, height=2, text="another album", onvalue=True, offvalue=False, variable=ch1)
check.pack()



if __name__ == "__main__":
    root.mainloop()


