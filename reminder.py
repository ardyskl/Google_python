#!/usr/bin/env python3

import time
import sys
import traceback
import os

def main():

    try:
        def reminder():
            text = str(input("What shall I remind you about?\n"))
            time_input = float(input("In how many minutes?\n"))

            local_time = time_input * 60

            time.sleep(local_time)

            os.system('afplay /System/Library/Sounds/Sosumi.aiff')
            return text

        cont = "y"
        while(cont.lower() == "y"):

            print(reminder())

            cont = input("Do you want another reminder? [y to continue] & [n to exit]: ")

            if cont == "n":
                print("Thanks for using our reminder app!")
                quit()

    except (EOFError):
        print("\n--- Interrupted exiting ---")

    except Exception:
        traceback.print_exc(file=sys.stdout)
        sys.exit(0)

    except KeyboardInterrupt:
        input_key = input("\n--- Press [ENTER] to exit ---")
        if input_key == '':
            quit()

    except Exception:
        traceback.print_exc(file=sys.stdout)
        sys.exit(0)

if __name__ == "__main__":
    main()
