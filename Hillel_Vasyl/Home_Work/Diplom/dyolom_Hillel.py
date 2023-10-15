from tkinter import *
import tkinter
import openpyxl
from datetime import date
from datetime import datetime
from ClassPerosn import Person
from tkinter import messagebox


class Window:
    WORK_BOOK = None
    FIND_VALUE = ''
    ERRORS_VALUE = []

    def load_button():
        if not Window.check_inputs():
            tkinter.messagebox.showwarning(title='Error', message=f'{Window.print_errors(Window.ERRORS_VALUE)}')
        else:
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

    def safe_file_button():
        try:
            sheet = Window.WORK_BOOK['Diplom Work']
            Person.init_table(sheet)
            Person.table_crea(sheet)
            Window.WORK_BOOK.save('DiploM.xlsx')  # Save new file.
        except Exception:
            pass

    def create_file():
        Window.WORK_BOOK = openpyxl.Workbook()  # Create new file.
        Window.WORK_BOOK.create_sheet(title='Diplom Work', index=0)  # Create the Sheet

    def load_file_button():
        try:
            Window.WORK_BOOK = openpyxl.load_workbook('DiploM.xlsx')  # Open the file.
        except FileNotFoundError:
            tkinter.messagebox.showwarning(title='Error', message='File not found. Please create file.')

    @staticmethod
    def check_data(data):
        year = datetime.now().year
        sym_val = ''
        try:
            for val in data:
                if not val.isdigit():
                    sym_val += val
                    break
            new_l = data.split(sym_val)
            if (0 < int(new_l[0]) <= 31) and (12 >= int(new_l[1]) > 0) and (4 >= len(new_l[2]) >= 2):
                if int(new_l[2]) < year:
                    new_l[2] = '20' + new_l[2]
                return new_l
            else:
                raise Exception

        except Exception:
            return False

    @staticmethod
    def input_str(array):
        for i in array:
            if not i.isalpha():
                return False

        return True

    def check_inputs():
        result_check = True
        if not Window.input_str(text_name.get()) or not text_name.get():
            Window.ERRORS_VALUE.append('Error Name Input')
            result_check = False
        if not Window.input_str(text_surname.get()):
            Window.ERRORS_VALUE.append('Error Surname Input')
            result_check = False
        if not Window.input_str(text_sec_surname.get()):
            Window.ERRORS_VALUE.append('Error Second Name Input')
            result_check = False
        if not Window.check_data(text_birth.get()) or not text_birth.get():
            Window.ERRORS_VALUE.append('Error Data of Birth Input')
            result_check = False
        if text_death.get():
            date_dt = Window.check_data(text_death.get())
            if not date_dt:
                Window.ERRORS_VALUE.append('Error Data of Dead Input')
                result_check = False
        if text_gender.get():
            if text_gender.get().lower() == 'f':
                ...
            elif text_gender.get().lower() == 'm':
                ...
            else:
                Window.ERRORS_VALUE.append('Error Title Input')
                result_check = False
        else:
            Window.ERRORS_VALUE.append('Error Title Input')
            result_check = False
        return result_check

    @staticmethod
    def print_errors(errors):
        gg_val = ''
        for item in errors:
            gg_val = gg_val + ''.join(map(str, item)) + '\n'
        return gg_val

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
    def print_search_result(find_value, age_func):
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
            final_print.append(f'{age_func(str(i[6]))}, ')
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

    def search_button():
        try:
            sheet = Window.WORK_BOOK['Diplom Work']
            rows = (sheet.max_row - 1)
            col = sheet.max_column
            se_val = search_val.get()  # search value
            array1 = sorted(set(Window.search_row(rows, 3, sheet, se_val)))
            find_value = Window.result_of_search(array1, sheet, col)
            text_uot = tkinter.Text(search_label_frame, width=80, height=16, )
            text_uot.insert(tkinter.END, Window.print_search_result(find_value, Window.age_word))
            text_uot.grid(row=40, column=1, sticky="E", padx=20, pady=10)
        except TypeError:
            tkinter.messagebox.showwarning(title='Error', message='No source file finded.')


window = tkinter.Tk()
window.title("!!! DIPLOM !!!")

frame = tkinter.Frame(window)
frame.pack()

welcome_label_frame = tkinter.LabelFrame(frame, text='User Information')
welcome_label_frame.grid(row=0, column=0, sticky="news", padx=20, pady=10)


button_label_frame = tkinter.LabelFrame(frame, text='File managing Button')
button_label_frame.grid(row=14, column=0, sticky="news", padx=20, pady=10)

search_label_frame = tkinter.LabelFrame(frame, text='Search load Peoples')
search_label_frame.grid(row=22, column=0, sticky="news", padx=20, pady=10)


name_label = tkinter.Label(welcome_label_frame, text=" Put the Name: ", font=("Helvetica", 13))
name_label.grid(row=2, column=0, stick="W", padx=20, pady=10)
text_name = tkinter.Entry(welcome_label_frame, width=60)
text_name.grid(row=2, column=1, sticky="E", padx=20, pady=10)

surname_label = tkinter.Label(welcome_label_frame, text=" Put the Surname: ", font=("Helvetica", 13))
surname_label.grid(row=4, column=0, stick="W", padx=20, pady=10)
text_surname = tkinter.Entry(welcome_label_frame, width=60)
text_surname.grid(row=4, column=1, sticky="E", padx=20, pady=10)

sec_surname_label = tkinter.Label(welcome_label_frame, text=" Put the Second Surname: ", font=("Helvetica", 13))
sec_surname_label.grid(row=6, column=0, stick="W", padx=20, pady=10)
text_sec_surname = tkinter.Entry(welcome_label_frame, width=60)
text_sec_surname.grid(row=6, column=1, sticky="E", padx=20, pady=10)

birth_label = tkinter.Label(welcome_label_frame, text=" Put the Birth date: ", font=("Helvetica", 13))
birth_label.grid(row=8, column=0, stick="W", padx=20, pady=10)
text_birth = tkinter.Entry(welcome_label_frame, width=60)
text_birth.grid(row=8, column=1, sticky="E", padx=20, pady=10)

death_label = tkinter.Label(welcome_label_frame, text=" Put the Death date: ", font=("Helvetica", 13))
death_label.grid(row=10, column=0, stick="W", padx=20, pady=10)
text_death = tkinter.Entry(welcome_label_frame, width=60)
text_death.grid(row=10, column=1, sticky="E", padx=20, pady=10)

gender_label = tkinter.Label(welcome_label_frame, text=" Put the Title: ", font=("Helvetica", 13))
gender_label.grid(row=12, column=0, stick="W", padx=20, pady=10)
text_gender = tkinter.Entry(welcome_label_frame, width=60, )
text_gender.grid(row=12, column=1, sticky="E", padx=20, pady=10)


create_button = tkinter.Button(button_label_frame, text="Create File",
                               command=Window.create_file, font=("Helvetica", 13))
create_button.grid(row=20, column=0, sticky="W", padx=40, pady=10)

load_people_button = tkinter.Button(button_label_frame, text="Load People",
                                    command=Window.load_button, font=("Helvetica", 13))
load_people_button.grid(row=20, column=1, sticky="e", padx=40, pady=10)

safe_button = tkinter.Button(button_label_frame, text="Safe File",
                             command=Window.safe_file_button, font=("Helvetica", 13))
safe_button.grid(row=20, column=2, sticky="E", padx=40, pady=10)

load_button = tkinter.Button(button_label_frame, text="Load File",
                             command=Window.load_file_button, font=("Helvetica", 13))
load_button.grid(row=20, column=3, sticky="E", padx=40, pady=10)

create_button = tkinter.Button(search_label_frame, text="Search People",
                               command=Window.search_button, font=("Helvetica", 13))
create_button.grid(row=30, column=0, sticky="W", padx=20, pady=10)

search_label = tkinter.Label(search_label_frame, text=" Put the Search name: ", font=("Helvetica", 13))
search_label.grid(row=26, column=0, stick="W", padx=20, pady=10)
search_val = tkinter.Entry(search_label_frame, width=60)
search_val.grid(row=26, column=1, sticky="E", padx=20, pady=10)

if __name__ == "__main__":
    window.mainloop()
