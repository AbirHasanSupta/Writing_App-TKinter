from tkinter import *
BACKGROUND_COLOR = "#E2F4C5"
FONT = "Courier"
timer = None

root = Tk()
root.title("Dangerous Writing")

root.resizable(width=False, height=False)
root.minsize(width=900, height=500)
root.config(background=BACKGROUND_COLOR, padx=30, pady=30)
container = Frame(root)
container.grid(row=0, column=0)

main_page = Frame(container)
main_page.config(background=BACKGROUND_COLOR, padx=30, pady=30)
main_page.grid(row=0, column=0)
writing_page = Frame(container)
writing_page.config(background=BACKGROUND_COLOR, padx=30, pady=30)
writing_page.grid(row=0, column=0)


def home_window():
    main_page.tkraise()
    title = Label(main_page, text="The Most Dangerous Writing App", bg=BACKGROUND_COLOR, font=(FONT, 30, "bold"),
                  fg="#BE7B72")
    title.grid(row=1, column=1)
    subtitle = Label(main_page, text="Don’t stop writing, or all progress will be lost.", bg=BACKGROUND_COLOR,
                     font=(FONT, 15, "bold"))
    subtitle.grid(row=2, column=1)
    start = Button(main_page, text="Start Writing Now", bg="#58A399", command=writing_window)
    start.grid(row=3, column=1)
    if timer is not None:
        root.after_cancel(timer)
    for item in writing_page.winfo_children():
        item.destroy()


def writing_window():
    global timer
    writing_page.tkraise()
    title_text = Label(writing_page, text="Start Writing Here....", bg=BACKGROUND_COLOR, font=(FONT, 18, "bold"))
    title_text.grid(row=1, column=0)
    type_field = Text(writing_page, height=20, width=100, bg="#DFF5FF")
    type_field.grid(row=2, column=0)
    back = Button(writing_page, text="Quit Writing", bg="#D37676", command=home_window, width=14)
    back.grid(row=3, column=0)

    def writing(event):
        global timer
        title_text.config(text="Keep Typing.....")
        type_field.config(bg="#DFF5FF")
        root.after_cancel(timer)
        timer = root.after(5000, delete_text)

    def delete_text():
        global timer
        title_text.config(text="Time Out!!!")
        type_field.config(bg="#496989")
        type_field.delete("1.0", END)
        timer = root.after(5000, delete_text)

    root.bind("<Key>", writing)
    timer = root.after(5000, delete_text)


home_window()

root.mainloop()
