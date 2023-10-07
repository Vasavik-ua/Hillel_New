import tkinter as tk


def delete_text():
    ...


window = tk.Tk()
window.geometry("700x550")
window.title("!!! DIPLOM !!!")
window.grid_columnconfigure(0, weight=1)

welcome_label = tk.Label(window, text="Register of peoples: ",
                         font=("Helvetica", 13))
welcome_label.grid(row=0, column=1, sticky="W", padx=20, pady=10)

name_label = tk.Label(window, text=" Put the Name: ", font= ("Helvetica", 13))
name_label.grid(row=2, column=0, stick="W", padx=20, pady=10)
text_name = tk.Entry(width=60)
text_name.grid(row=2, column=1, sticky="E", padx=20, pady=10)

surname_label = tk.Label(window, text=" Put the Surname: ", font= ("Helvetica", 13))
surname_label.grid(row=4, column=0, stick="W", padx=20, pady=10)
text_surname = tk.Entry(width=60)
text_surname.grid(row=4, column=1, sticky="E", padx=20, pady=10)

sec_surname_label = tk.Label(window, text=" Put the Second Surname: ", font= ("Helvetica", 13))
sec_surname_label.grid(row=6, column=0, stick="W", padx=20, pady=10)
text_sec_surname = tk.Entry(width=60)
text_sec_surname.grid(row=6, column=1, sticky="E", padx=20, pady=10)

birth_label = tk.Label(window, text=" Put the Birth date: ", font= ("Helvetica", 13))
birth_label.grid(row=8, column=0, stick="W", padx=20, pady=10)
text_birth = tk.Entry(width=60)
text_birth.grid(row=8, column=1, sticky="E", padx=20, pady=10)

death_label = tk.Label(window, text=" Put the Death date: ", font= ("Helvetica", 13))
death_label.grid(row=10, column=0, stick="W", padx=20, pady=10)
text_death = tk.Entry(width=60)
text_death.grid(row=10, column=1, sticky="E", padx=20, pady=10)

gender_label = tk.Label(window, text=" Put the Gender: ", font= ("Helvetica", 13))
gender_label.grid(row=12, column=0, stick="W", padx=20, pady=10)
text_gender = tk.Entry(width=60)
text_gender.grid(row=12, column=1, sticky="E", padx=20, pady=10)


create_button = tk.Button(text="Load People", command=delete_text)
create_button.grid(row=16, column= 1, sticky="E", padx=20, pady=10)

create_button = tk.Button(text="Safe File with Input", command=delete_text)
create_button.grid(row=22, column= 1, sticky="E", padx=20, pady=10)

create_button = tk.Button(text="Load File ", command=delete_text)
create_button.grid(row=26, column= 1, sticky="E", padx=20, pady=10)




if __name__ == "__main__":
    window.mainloop()
