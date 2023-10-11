import tkinter as tk
from tkinter import *
import openpyxl
from datetime import date


class Person:
    NAME = []
    SURNAME = []
    SEC_SURNAME = []
    DATE_OF_BIRTH = []
    DATE_OF_DEATH = []
    GENDER = []
    AGE = []
    INIT_TABLE = ['NAME', 'SURNAME', 'SEC_SURNAME',
                  'DATE_OF_BIRTH', 'DATE_OF_DEATH',
                  'GENDER', 'AGE']

    @classmethod
    def init_table(cls, shee):
        for row_id, value in enumerate(cls.INIT_TABLE):
            cell = shee.cell(row=1, column=row_id + 1)
            cell.value = value

    @staticmethod
    def table_crea(shee):
        rows = shee.max_row
        for item, value in enumerate(Person.NAME):
            cell = shee.cell(row=(rows + item + 1), column=1)
            cell.value = value

        for item, value in enumerate(Person.SURNAME):
            cell = shee.cell(row=(rows + item + 1), column=2)
            cell.value = value

        for item, value in enumerate(Person.SEC_SURNAME):
            cell = shee.cell(row=(rows + item + 1), column=3)
            cell.value = value

        for item, value in enumerate(Person.DATE_OF_BIRTH):
            cell = shee.cell(row=(rows + item + 1), column=4)
            cell.value = value

        for item, value in enumerate(Person.DATE_OF_DEATH):
            cell = shee.cell(row=(rows + item + 1), column=5)
            cell.value = value

        for item, value in enumerate(Person.GENDER):
            cell = shee.cell(row=(rows + item + 1), column=6)
            cell.value = value

        for item, value in enumerate(Person.AGE):
            cell = shee.cell(row=(rows + item + 1), column=7)
            cell.value = value


class Window:
    WORK_BOOK = None

    @staticmethod
    def load_button():
        Person.NAME.append(text_name.get())
        Person.SURNAME.append(text_surname.get())
        Person.SEC_SURNAME.append(text_sec_surname.get())
        Person.DATE_OF_BIRTH.append(text_birth.get())
        Person.DATE_OF_DEATH.append(text_death.get())
        Person.GENDER.append(text_gender.get())
        Person.AGE.append(Window.check_age(text_birth.get(), text_death.get()))

        text_name.delete(0, END)
        text_surname.delete(0, END)
        text_sec_surname.delete(0, END)
        text_birth.delete(0, END)
        text_death.delete(0, END)
        text_gender.delete(0, END)

    @staticmethod
    def safe_file_button():
        sheet = Window.WORK_BOOK['Diplom Work']
        Person.init_table(sheet)
        Person.table_crea(sheet)
        Window.WORK_BOOK.save('DiploM.xlsx')  # Save new file.

    @staticmethod
    def create_file():
        Window.WORK_BOOK = openpyxl.Workbook()  # Create new file.
        Window.WORK_BOOK.create_sheet(title='Diplom Work', index=0)  # Create the Sheet

    @staticmethod
    def load_file_button():
        Window.WORK_BOOK = openpyxl.load_workbook('DiploM.xlsx')  # Open the file.

    @staticmethod
    def check_age(data, other):  # Insert the date
        if other == '':
            dat = date.today()
            dat_t = dat.strftime("%d/%m/%Y")
            sym_v = ''
            for val in dat_t:
                if not val.isdigit():
                    sym_v += val
                    break
            dat_new = dat_t.split(sym_v)
            sym_val = ''
            for val in data:
                if not val.isdigit():
                    sym_val += val
                    break
            new_l = data.split(sym_val)
            age = int(dat_new[2]) - int(new_l[2])
            if int(dat_new[1]) <= int(new_l[1]):
                if int(dat_new[0]) < int(new_l[0]):
                    age -= 1
            return age
        else:
            sym_v = ''
            for val in other:
                if not val.isdigit():
                    sym_v += val
                    break
            dat_new = other.split(sym_v)
            sym_val = ''
            for val in data:
                if not val.isdigit():
                    sym_val += val
                    break
            new_l = data.split(sym_val)
            age = int(dat_new[2]) - int(new_l[2])
            if int(dat_new[1]) <= int(new_l[1]):
                if int(dat_new[0]) < int(new_l[0]):
                    age -= 1
            return age


window = tk.Tk()
window.geometry("700x800")
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


create_button = tk.Button(text="Create File", command=Window.create_file)
create_button.grid(row=20, column= 1, sticky="W", padx=90, pady=10)

create_button = tk.Button(text="Load People", command=Window.load_button)
create_button.grid(row=20, column= 1, sticky="W", padx=200, pady=10)

create_button = tk.Button(text="Safe File", command=Window.safe_file_button)
create_button.grid(row=20, column= 1, sticky="E", padx=20, pady=10)

create_button = tk.Button(text="Load File", command=Window.load_file_button)
create_button.grid(row=20, column= 1, sticky="E", padx=100, pady=10)


if __name__ == "__main__":
    window.mainloop()
