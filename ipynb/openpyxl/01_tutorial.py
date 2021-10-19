
from distutils.dir_util import copy_tree
from tempfile import NamedTemporaryFile

import openpyxl as xl

WBFILE1 = "data/tutorial.xlsx"
WBFILE2 = 'data/balances.xlsx'
WBFILE3 = 'data/document_template.xltx'
WBFILE4 = 'data/document.xlsx'

def tutorial():
    """
    Tutorial (https://openpyxl.readthedocs.io/en/stable/tutorial.html)
    """
    print(80*'-')
    print("Create Workbook")
    print(40*'-')
    wb = xl.Workbook()
    print("initial wb.sheetnames = {}".format(wb.sheetnames))

    ws = wb.active

    # insert at the end (default)
    ws1 = wb.create_sheet("Mysheet1")
    ws1['A1'] = "Mysheet1"

    # or
    # insert at first position
    ws2 = wb.create_sheet("Mysheet2", 0)
    ws2['A1'] = "Mysheet2"

    # or
    # insert at the penultimate position
    ws3 = wb.create_sheet("Mysheet3", -1)
    ws3['A1'] = "Mysheet3"

    # create a named sheet
    ws.title = "New Title"
    ws.sheet_properties.tabColor = "1072BA"

    ws4 = wb["New Title"]
    ws4['A1'] = "New Title"

    print("final wb.sheetnames = {}".format(wb.sheetnames))

    print(20*'-')
    print("print loop of sheet.title")
    for sheet in wb:
        print(sheet.title)

    print(20 * '-')
    print("You can create copies of worksheets within a single workbook:")
    source = wb.active
    print("source sheet name: {}".format(source.title))

    target = wb.copy_worksheet(source)
    print("wb.copy_worksheet(source) = {}".format(target.title))

    print(80*'-')
    print("Playing with Data")
    print(40*'-')
    print("Accessing one cell")

    c = ws['A4']

    ws['A4'] = 4
    wb.save(WBFILE1)
    print("after ws['A4'] = {}".format(ws['A4']))

    d = ws.cell(row=4, column=2, value=10)
    print(d)

    print(40*'-')
    print("Accessing many cells")
    print(40*'-')

    print("cell_range = ws['A1':'C4']")
    cell_range = ws['A1':'C4']
    print(20*'-')

    print("col_a = ws['A']")
    col_a = ws['A']
    for row in col_a:
        print(row.value)
    print(20*'-')

    print("col_range = ws['A:B']")
    col_range = ws['A:B']
    print(10*'-')

    for col in col_range:
        print("col[0].column_letter = {}".format(col[0].column_letter))
        print(5 * '-')
        for row in col:
            print(row.value)
        print(10 * '-')
    print(20*'-')

    print("row4 = ws[4]")
    row4 = ws[4]
    for cell in row4:
        print(cell.value)
    print(20*'-')

    print("row_range = ws[1:5]")
    row_range = ws[1:5]
    for row in row_range:
        for cell in row:
            print("cell({}) = {}".format(cell.column_letter + str(cell.row), cell.value))
            print(5 * '-')
        print(10*'-')
    print(20*'-')

    print("\nws.iter_rows")
    print("for row in ws.iter_rows(min_row=1, max_col=3, max_row=2)")
    print(10 * '-')
    for row in ws.iter_rows(min_row=1, max_col=3, max_row=2):
        for cell in row:
            print("cell({}) = {}".format(cell.column_letter + str(cell.row), cell.value))
    print(20*'-')

    print("\nws.iter_cols")
    print("for col in ws.iter_cols(min_row=1, max_col=3, max_row=2)")
    print(10 * '-')
    for col in ws.iter_cols(min_row=1, max_col=3, max_row=2):
        for cell in col:
            print("cell({}) = {}".format(cell.column_letter + str(cell.row), cell.value))
    print(20*'-')

    ws = wb.active
    ws['C9'] = 'hello world'
    tuple(ws.rows)

    tuple(ws.columns)

    print(40 * '-')
    print("Values only")
    print(40 * '-')
    for row in ws.values:
        for value in row:
            print(value)

    for row in ws.iter_rows(min_row=1, max_col=3, max_row=2, values_only=True):
        print(row)

    print(80 * '-')
    print("Data Storage")
    print(40 * '-')

    c.value = 'hello, world'
    print(c.value)

    d.value = 3.14
    print(d.value)

    print(40 * '-')
    print("Saving to a file")
    print(20 * '-')
    wb.save(WBFILE2)

    print(40 * '-')
    print("Saving as a stream")
    print(20 * '-')
    with NamedTemporaryFile() as tmp:
        wb.save(tmp.name)
        tmp.seek(0)
        stream = tmp.read()

    wb = xl.load_workbook(WBFILE2)
    wb.template = True
    wb.save(WBFILE3)

    wb = xl.load_workbook(WBFILE3)
    wb.template = False
    wb.save(WBFILE4)

    print(80 * '-')
    print("Loading from a file")
    wb2 = xl.load_workbook(WBFILE4)
    print(wb2.sheetnames)

    print(80 * '-')
    print("EOF")
    print(80 * '-')

if __name__ == "__main__":
    copy_tree('archive/', 'data/')
    tutorial()

