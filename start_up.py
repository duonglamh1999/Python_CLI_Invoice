import populate
import util
import log
import read

def match_mode(year, month):
    is_running = True
    path = util.get_path(year, month)
    file_path = path + ".csv"

    while is_running:
        if util.is_file(file_path):
            print("Choose mode(case-insensitive):\t[L]:Log \t[P]:Populate \t[R]:Read\t[E]:Exit")
            mode = input()
            match mode.lower():
                case "l":
                    log.log(year, month,file_path)
                case "p":
                    populate.populate(year,month)
                case "r":
                    read.read(file_path)
                case 'e':
                    is_running = False
                case _:
                    raise Exception("Invalid Input")
        else:
            print("Choose mode(case-insensitive):\t[L]:Log \t[E]:Exit")
            mode = input()
            match mode.lower():
                case "l":
                    log.log(year, month)
                case 'e':
                    is_running = False
                case _:
                    raise Exception("Invalid Input")