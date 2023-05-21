import tkinter as t
import os
from gui_main import gui_main
from gui_calculation import gui_calculation
from gui_result import gui_results
from version_increase import vinc
restart = True
vinc("medium")
def main_loop():
    gui_main_return = gui_main()
    print("(main.py) Update: gui_main_return = \n" + str(gui_main_return[0]) + "\n" + str(gui_main_return[1]))
    if gui_main_return[0] is True:
        print("(main.py): Update: Received selected_directory.")
        print("(main.py): Running gui_calculation...")
        result = gui_calculation(gui_main_return[1], gui_main_return[2])
        print(result)
        print("\n(main.py): Calculations complete, displaying results screen...")
        if result is not None:
            gui_results(gui_main_return[1], result, gui_main_return[2])
        return True
    else:
        print("(main.py): Update: Calculate not clicked, exiting...")
        return False
while restart is True:
    restart = main_loop()
