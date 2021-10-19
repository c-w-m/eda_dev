"""
# Simple Usage of openpyxl
"""
import openpyxl as xl
from distutils.dir_util import copy_tree
import pprint as pp

copy_tree('archive/', 'data/')

WBFILE1 = "data/empty_book.xlsx"
WBFILE2 = "data/formula.xlsx"
IMGFILE1 = "data/logo.png"
WBFILE3 = "data/logo.xlsx"
WBFILE4 = 'data/group.xlsx'


def write_workbook():
    print(80 * '-')
    print("Write Workbook")
    print(40 * '-')

    wb = xl.Workbook()

    dest_filename = WBFILE1

    ws1 = wb.active
    ws1.title = "range names"

    for row in range(1, 40):
        ws1.append(range(10))

    ws2 = wb.create_sheet(title="Pi")
    ws2['A3'] = 3.14

    ws3 = wb.create_sheet(title="Data")
    for row in range(1, 10):
        for col in range(1, 10):
            _ = ws3.cell(column=col, row=row, value="{0}".format(str(xl.utils.get_column_letter(col)) + str(row)))
        print(ws3['AA10'].value)

    wb.save(filename=dest_filename)


def read_workbook():
    print(80 * '-')
    print("Read Workbook")
    print(40 * '-')

    wb = xl.Workbook()
    wb = xl.load_workbook(filename=WBFILE1)
    sheet_ranges = wb['range names']
    print(sheet_ranges['D18'].value)


def number_formats():
    print(80 * '-')
    print("Number Formats")
    print(40 * '-')

    import datetime
    wb = xl.Workbook()
    ws = wb.active
    # set date using a Python datetime
    ws['A1'] = datetime.datetime(2010, 7, 21)

    ws['A1'].number_format


def using_formulae():
    print(80 * '-')
    print("Using Formulae")
    print(40 * '-')

    wb = xl.Workbook()
    ws = wb.active
    # add a simple formula
    ws["A1"] = "=SUM(1, 1)"
    wb.save(WBFILE2)

    from openpyxl.utils import FORMULAE
    print("HEX2DEC" in FORMULAE)


def merge_unmerge_cell():
    wb = xl.Workbook()
    ws = wb.active

    ws.merge_cells('A2:D2')
    ws.unmerge_cells('A2:D2')
    # or equivalently
    ws.merge_cells(start_row=2, start_column=1, end_row=4, end_column=4)
    ws.unmerge_cells(start_row=2, start_column=1, end_row=4, end_column=4)


def insert_image():
    wb = xl.Workbook()
    ws = wb.active
    ws['A1'] = 'You should see a logo image below'

    # create an image
    img = xl.drawing.image.Image(IMGFILE1)

    # add to worksheet and anchor next to cells
    ws.add_image(img, 'A3')
    wb.save(WBFILE3)


def fold_outline():
    print(80 * '-')
    print("Fold Outline")
    print(40 * '-')

    wb = xl.Workbook()
    ws = wb.create_sheet()
    ws.column_dimensions.group('A', 'D', hidden=True)
    ws.row_dimensions.group(1, 10, hidden=True)
    wb.save(WBFILE4)


if __name__ == "__main__":
    copy_tree('archive/', 'data/')
    write_workbook()
    read_workbook()
    number_formats()
    using_formulae()
    merge_unmerge_cell()
    insert_image()
    fold_outline()
