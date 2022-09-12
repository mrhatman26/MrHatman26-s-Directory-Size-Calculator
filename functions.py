import tkinter as t
import os
import sys

#Exit function
def button_exit(window):
    print("\n(button_exit): Update: User clicked exit button. Exiting...")
    window.destroy()
    sys.exit()
