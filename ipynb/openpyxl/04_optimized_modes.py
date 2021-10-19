"""
# [Optimised Modes](https://openpyxl.readthedocs.io/en/stable/optimized.html)

## Create Target Data
"""
import openpyxl as xl
from distutils.dir_util import copy_tree

copy_tree('archive/', 'data/')

WB_1_FILE = "data/large_file.xlsx"
WB_2_FILE = "data/new_big_file.xlsx"
WB_3_FILE = "data/write_only_file.xlsx"
WS_1_NAME = "big_data"
WS_2_NAME = "Pi"
WS_3_NAME = "Data"


def write_workbook():
    """
    Create a workbook for testing.
    """
    print(80 * '-')
    print("Write Workbook")
    print(40 * '-')

    wb = xl.Workbook()

    dest_filename = WB_1_FILE

    ws1 = wb.active
    ws1.title = WS_1_NAME

    for row in range(1, 40):
        ws1.append(range(10))

    ws2 = wb.create_sheet(title=WS_2_NAME)
    ws2['A3'] = 3.14

    ws3 = wb.create_sheet(title=WS_3_NAME)
    for row in range(1, 10):
        for col in range(1, 10):
            key = "{0}".format(str(xl.utils.get_column_letter(col)) + str(row))
            _ = ws3.cell(column=col, row=row, value=key)
            print(ws3[key].value)

    wb.save(filename=dest_filename)


def read_only_mode():
    """
    Optimized `read_only_mode` for lazy load of file
    """
    wb = xl.load_workbook(filename=WB_1_FILE, read_only=True)
    ws = wb[WS_3_NAME]

    for row in ws.rows:
        for cell in row:
            print(cell.value)

    # get max_column and max_row
    wb_active_max_column = wb.active.max_column
    print("wb_active_max_column = {}".format(wb_active_max_column))

    wb_active_max_row = wb.active.max_row
    print("wb_active_max_row = {}".format(wb_active_max_row))

    # zero max row/column
    ws.reset_dimensions()

    # set max row/column force: self._calculate_dimension()
    ws.calculate_dimension(force=True)

    # Close the workbook after reading
    wb.close()


if __name__ == "__main__":
    copy_tree('archive/', 'data/')
    write_workbook()
    read_only_mode()
