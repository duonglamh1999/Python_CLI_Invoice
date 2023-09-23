import calendar
import datetime

import numpy as np
import pandas as pd

import read
import util

HEADERS = ["Date", "Tasks", "Hours", "Rate", "Total"]


def log(year: int, month: int,file_path: str):
    if not util.is_file(file_path):
        print("Generating new report")
        generate_default_csv(file_path, populate_default_contents(year, month))
    else:
        print("Populating existed report")
    df = read.read(file_path)
    edited_df = edit(df)
    edited_df.to_csv(file_path, encoding='utf-8', index=False)


def generate_default_csv(file_path: str, contents: [[]]):
    matrix = np.array(contents)
    df = pd.DataFrame(matrix, columns=HEADERS)
    df.to_csv(file_path, encoding='utf-8', index=False)


def populate_week_days(year: int, month: int):
    num_days = calendar.monthrange(year, month)[1]
    return [f"{i + 1}/{month}" for i in range(num_days) if datetime.date(year, month, i + 1).weekday() < 5]


def populate_default_contents(year: int, month: int):
    rate: int = util.read_config("rate")
    return [[day, "", 0, rate, 0] for day in populate_week_days(year, month)]


def edit_line(dataframe, row: int):
    is_editing = True
    while is_editing:
        print(dataframe.loc[row])
        print("[T]:Tasks\t[H]:Hours\t[D]:Delete\t[E]:Exit")
        option = input()
        match option.lower():
            case "t":
                dataframe.loc[row, 'Tasks'] = input("Tasks:\n")
            case "h":
                hours = int(input("Hours:\n"))
                dataframe.loc[row, 'Hours'] = hours
                dataframe.loc[row, 'Total'] = hours * int(dataframe.loc[row, 'Rate'])
            case "d":
                dataframe.drop(row, inplace=True)
                dataframe.reset_index(drop=True, inplace=True)
                is_editing = False
            case "e":
                is_editing = False
            case _:
                raise Exception("Invalid Input")


def edit(dataframe):
    is_editing = True
    while is_editing:
        print("[index]:Edit by index\t[E]:Exit")
        option = input()
        if option.lower() == 'e':
            is_editing = False
        elif not isinstance(int(option), int):
            raise Exception("Invalid Input")
        elif len(dataframe.index) > int(option) >= 0:
            edit_line(dataframe, int(option))
        else:
            raise Exception("Invalid index")
        print(dataframe.to_string())
    return dataframe
