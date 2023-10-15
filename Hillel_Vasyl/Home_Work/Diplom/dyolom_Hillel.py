from tkinter import *
import tkinter
import openpyxl
from ClassPerosn import Person
from tkinter import messagebox


class Window:
    WORK_BOOK = None
    FIND_VALUE = ''
    ERRORS_VALUE = []

    def load_button():
        if not Window.check_inputs():
            tkinter.messagebox.showwarning(title='Error', message=f'{Person.print_errors(Window.ERRORS_VALUE)}')
            Window.ERRORS_VALUE.clear()
        else:
            Person.NAME.append(text_name.get())
            Person.SURNAME.append(text_surname.get())
            Person.SEC_SURNAME.append(text_sec_surname.get())
            Person.DATE_OF_BIRTH.append(text_birth.get())
            Person.DATE_OF_DEATH.append(text_death.get())
            Person.GENDER.append(text_gender.get())
            Person.AGE.append(Person.check_age(text_birth.get(), text_death.get()))

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
        except TypeError:
            tkinter.messagebox.showwarning(title='Error',
                                           message='File not Found.Perhaps file not created.')
            pass

    def create_file():
        Window.WORK_BOOK = openpyxl.Workbook()  # Create new file.
        Window.WORK_BOOK.create_sheet(title='Diplom Work', index=0)  # Create the Sheet

    def load_file_button():
        try:
            Window.WORK_BOOK = openpyxl.load_workbook('DiploM.xlsx')  # Open the file.
        except FileNotFoundError:
            tkinter.messagebox.showwarning(title='Error', message='File not found. Please create file.')

    def search_button():
        try:
            sheet = Window.WORK_BOOK['Diplom Work']
            rows = (sheet.max_row - 1)
            col = sheet.max_column
            se_val = search_val.get()  # search value
            array1 = sorted(set(Person.search_row(rows, 3, sheet, se_val)))
            find_value = Person.result_of_search(array1, sheet, col)
            text_uot = tkinter.Text(search_label_frame, width=100, height=16, )
            text_uot.insert(tkinter.END, Person.print_search_result(find_value, Person.age_word))
            text_uot.grid(row=40, column=1, sticky="news", padx=20, pady=10)
        except TypeError:
            tkinter.messagebox.showwarning(title='Error', message='No source file finded.')

    def check_inputs():
        result_check = True
        if not Person.input_str(text_name.get()) or not text_name.get():
            Window.ERRORS_VALUE.append('Error Name Input')
            result_check = False
        if not Person.input_str(text_surname.get()):
            Window.ERRORS_VALUE.append('Error Surname Input')
            result_check = False
        if not Person.input_str(text_sec_surname.get()):
            Window.ERRORS_VALUE.append('Error Second Name Input')
            result_check = False
        if not Person.check_data(text_birth.get()) or not text_birth.get():
            Window.ERRORS_VALUE.append('Error Data of Birth Input')
            result_check = False
        if text_death.get():
            date_dt = Person.check_data(text_death.get())
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
