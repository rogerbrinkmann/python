from openpyxl import Workbook, load_workbook
from openpyxl.cell.cell import get_column_letter
import datetime
import random

def write_workbook():
    dates = [datetime.date(2019, month, 1) for month in range(1, 10)]
    times = [datetime.time(hour, 0, 0) for hour in range(6, 15)]

    wb = Workbook()

    ws = wb.active
    ws.title = "Sheet_1"

    column_widths = [8, 12, 8, 15, 15, 15]
    for i, column_width in enumerate(column_widths):
        ws.column_dimensions[get_column_letter(i + 1)].width = column_width

    ws.append(["Number", "Date", "Time", "Value 1", "Value 2", "Sum"])
    for num, (date, time) in enumerate(zip(dates, times), 1):
        ws.append(
            (
                num,
                date,
                time,
                random.random() * 10,
                random.random() * 10,
                f"=sum(D{num + 1},E{num + 1})",
            )
        )

    ws.auto_filter.ref = "A1:F10"

    wb.save(filename="excelfile.xlsx")


def read_workbook():
    wb = load_workbook(filename="excelfile.xlsx")
    ws = wb.worksheets[0]

    for row in ws.rows:
        print(row)

if __name__ == "__main__":
    write_workbook()
    read_workbook()
