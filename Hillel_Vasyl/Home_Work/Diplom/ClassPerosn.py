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