import math


def main():
    close = False
    while not close:
        try:
            info = input("Input race time (hours:minutes), estimated pace (minutes:seconds), "
                         "fuel per lap & safety margin separated by spaces:\n")
            info = info.split(" ")
            time = info[0].split(":")
            if len(time) == 1:
                time_parsed = float(time[0])
            else:
                time_parsed = int(time[0]) * 60 + int(time[1])
            pace = info[1].split(":")
            if len(pace) == 1:
                pace_parsed = float(pace[0]) / 60
            else:
                pace_parsed = int(pace[0]) + float(pace[1]) / 60
            consumption = float(info[2])
            margin = int(info[3])
            laps = math.ceil(time_parsed / pace_parsed)
            laps_margin = laps + margin
            fuel_needed = math.ceil(laps_margin * consumption)
            print("\nEstimated laps:", laps)
            print("Safety margin:", margin, "laps")
            print("Fuel needed:", fuel_needed, "liters\n")
            cont = input("Choose 1 to calculate again or 2 to close program: ")
            if cont == "2":
                close = True
            else:
                print()
        except ValueError:
            close = False
            print("Invalid values\n")
        except IndexError:
            close = False
            print("Invalid values\n")


main()
