import xlrd3 as xlrd

FILE = r'Test/Test.xlsx'


def parsing(file):
    book = xlrd.open_workbook(file)
    sh = book.sheet_by_index(0)
    for row_number in range(sh.nrows):
        for col_number in range(sh.ncols):
            print(sh.cell_value(rowx=row_number, colx=col_number))


def do(file):
    articles = []
    expenses = []
    book = xlrd.open_workbook(file)
    sh = book.sheet_by_index(0)
    for row_number in range(sh.nrows):
        row = sh.row_values(row_number)
        if isinstance(row[1], float):
            expenses.append(row)
        else:
            articles.append(row)
    print(articles)
    print(expenses)


if __name__ == '__main__':
    # parsing(FILE)
    do(FILE)
