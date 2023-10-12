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
    FIND_VALUE = ''

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


    @staticmethod
    def search_row(rows, col, sheet, val):
        array1 = []
        for item in range(col):
            for i in range(rows):
                cell = sheet.cell(row=i + 2, column=item + 1)
                x = (str(cell.value.lower()).find(val.lower()))
                if x < 0:
                    pass
                else:
                    array1.append(i + 2)
        return array1

    @staticmethod
    def result_of_search(val, sheet, col):  # Val:array;
        find_value = []
        for v in range(len(val)):
            row_list = []
            for i in range(col):
                cell = sheet.cell(row=int(list(val)[v]), column=i + 1)
                row_list.append(cell.value)
            find_value.append(row_list.copy())
            row_list.clear()
        return find_value

    @staticmethod
    def age_word(x):
        t = x[-1:]
        result_qty = lambda t: 'рік' if int(t) == 1 else 'роки' if 2 <= int(t) <= 4 else 'років'
        return result_qty(t)

    @staticmethod
    def print_search_result(find_value):
        ret_val = []
        gg_val = ''
        for i in find_value:
            final_print = []
            final_print.append(f'{i[0].title()} ')
            if not i[1] == None:
                final_print.append(f'{i[1].title()} ')
            if not i[2] == None:
                final_print.append(f'{i[2].title()} ')
            final_print.append(f'{i[6]} ')
            final_print.append(f'{Window.age_word(str(i[6]))}, ')
            if ((i[5]).lower()) == 'm' and (not i[4] == None):
                final_print.append(f'чоловік. Народився {i[3]}. Помер {i[4]}.')
            elif ((i[5]).lower()) == 'm' and i[4] == None:
                final_print.append(f'чоловік. Народився {i[3]}.')
            if ((i[5]).lower()) == 'f' and (not i[4] == None):
                final_print.append(f'жінка. Народилася {i[3]}. Померла {i[4]}.')
            elif ((i[5]).lower()) == 'f' and i[4] == None:
                final_print.append(f'жінка. Народилася {i[3]}.')

            ret_val.append(final_print.copy())
            final_print.clear()
        for item in ret_val:
            gg_val = gg_val + ''.join(map(str, item)) + '\n'
        return gg_val

    @staticmethod
    def search_button():
        sheet = Window.WORK_BOOK['Diplom Work']
        rows = (sheet.max_row - 1)
        col = sheet.max_column
        se_val = search_val.get()  # search value
        array1 = sorted(set(Window.search_row(rows, 3, sheet, se_val)))
        find_value = Window.result_of_search(array1, sheet, col)
        text_uot = tk.Text(width=80, height=16, )
        text_uot.insert(tk.END, Window.print_search_result(find_value))
        text_uot.grid(row=40, column=1, sticky="E", padx=20, pady=10)




window = tk.Tk()
window.geometry("920x780")
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


create_button = tk.Button(text="Create File", command=Window.create_file, font= ("Helvetica", 13))
create_button.grid(row=20, column= 1, sticky="W", padx=90, pady=10)

create_button = tk.Button(text="Load People", command=Window.load_button, font= ("Helvetica", 13))
create_button.grid(row=20, column= 1, sticky="W", padx=200, pady=10)

create_button = tk.Button(text="Safe File", command=Window.safe_file_button, font= ("Helvetica", 13))
create_button.grid(row=20, column= 1, sticky="E", padx=110, pady=10)

create_button = tk.Button(text="Load File", command=Window.load_file_button, font= ("Helvetica", 13))
create_button.grid(row=20, column= 1, sticky="E", padx=20, pady=10)

create_button = tk.Button(text="Search People", command=Window.search_button, font= ("Helvetica", 13))
create_button.grid(row=30, column= 0, sticky="W", padx=20, pady=10)

search_label = tk.Label(window, text=" Put the Search name: ", font= ("Helvetica", 13))
search_label.grid(row=26, column=0, stick="W", padx=20, pady=10)
search_val = tk.Entry(width=60)
search_val.grid(row=26, column=1, sticky="E", padx=20, pady=10)



if __name__ == "__main__":
    window.mainloop()
