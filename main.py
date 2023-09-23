import util
import start_up
import subprocess


def main_menu():
    year = util.get_year()
    month = util.get_month()
    start_up.match_mode(year, month)


main_menu()
