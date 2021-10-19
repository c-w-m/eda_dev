
from distutils.dir_util import copy_tree

import openpyxl as xl
import pprint as pp


WBFILE1 = "data/my_range.xlsx"
WSNAME = "range_test"
WSRANGE1 = "newrange"
WSRANGE1CELLS = (WSNAME + "!$A$1:$A$5")
WSRANGE2 = "privaterange"
WSRANGE2CELLS = (WSNAME + "!$A$6")

def create_new_named_ranges():
    wb = xl.Workbook()
    ws = wb.create_sheet(title=WSNAME)
    new_range = xl.workbook.defined_name.DefinedName(WSRANGE1,
                                                     attr_text=WSRANGE1CELLS)
    wb.defined_names.append(new_range)

    # create a local named range (only valid for a specific sheet)
    sheetid = wb.sheetnames.index(WSNAME)
    private_range = xl.workbook.defined_name.DefinedName(WSRANGE2,
                                                         attr_text=WSRANGE2CELLS,
                                                         localSheetId=sheetid)
    wb.defined_names.append(private_range)
    # this local range can't be retrieved from the global defined names
    assert(WSRANGE2 not in wb.defined_names)

    # the scope has to be supplied to retrieve local ranges:
    print(wb.defined_names.localnames(sheetid))
    print(wb.defined_names.get(WSRANGE2, sheetid).attr_text)

    wb.save(WBFILE1)


def sample_use_for_ranges():
    wb = xl.load_workbook(WBFILE1)
    ws_names = wb.sheetnames
    ws = wb.get_sheet_by_name(WSNAME)
    my_range = wb.defined_names[WSRANGE1]

    # if this contains a range of cells then the destinations attribute is not None
    dests = my_range.destinations  # returns a generator of (worksheet title, cell range) tuples

    cells = []
    for title, coord in dests:
        ws = wb[title]
        cells.append(ws[coord])

    print("{} = ".format(WSRANGE1))
    pp.pprint(cells)


if __name__ == "__main__":
    copy_tree('archive/', 'data/')
    create_new_named_ranges()
    sample_use_for_ranges()
