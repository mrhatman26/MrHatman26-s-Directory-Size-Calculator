import tkinter as t
from tkinter import filedialog, messagebox
import os
from functions import button_exit

#Main Screen
def gui_main():
    print("(gui_main): Update: Creating gui_main...", end="")
    #Functions/Commands
    def directory_select():
        #global selected_directory
        print("\n(gui_main): Update: User clicked browse button. Displaying browse window")
        file = t.filedialog.askdirectory()
        print(file)
        gui_main_frame_dir_entry.delete(0, "end")
        if file is None or not file:
            #selected_directory = "C:/"
            gui_main_frame_dir_entry.insert(0, "C:/")
        else:
            #selected_directory = file
            gui_main_frame_dir_entry.insert(0, str(file))
        #gui_main_frame_dir_entry.delete(0, "end")
        #gui_main_frame_dir_entry.insert(0, str(selected_directory))
        print("(gui_main): Update: User selected directory.")
        print("(gui_main): Selected directory: " + str(selected_directory))
        print("\n(gui_main): Waiting for user input...")
    def button_calculate():
        print("\n(gui_main): Update: User clicked calculate button. Returning directory to main.py")
        global rubbish
        rubbish = True
        global selected_directory
        selected_directory = gui_main_frame_dir_entry.get()
        window.destroy()
    def button_about():
        print("\n(gui_main): Update: User clicked infor button. Showing program info")
        mesg = "This program was made by MrHatman26, AKA nobody important.\n\nWhat is this?: This is a tool to calculate the size of a directory and show the largest file in said directory.\n\nThis program was made using Python and uses the following libraries:\n-tkinter\n-os\n-threading\n\nCurrent Version: 1.0.5"
        t.messagebox.showinfo("Info", mesg)
    #GUI
    resolution = "620x205"
    title = "MrHatman26's Directory Size Calculator"
    window = t.Tk();
    #Function vars
    byte_type = t.StringVar()
    byte_type.set("GB")
    global selected_directory
    selected_directory = "C:/"
    #Window settings
    window.geometry(resolution)
    window.title(title)
    window.resizable(False, False)
    #Window widgets
    gui_main_frame = t.Frame(window)
    gui_main_frame_dir_label = t.Label(gui_main_frame, text="Directory:").grid(row=0, column=1)
    gui_main_frame_browse_frame = t.Frame(gui_main_frame)
    gui_main_frame_dir_entry = t.Entry(gui_main_frame_browse_frame, width=40)
    gui_main_frame_dir_entry.pack(side=t.LEFT)
    gui_main_frame_dir_entry.insert(0, selected_directory)
    gui_main_frame_dir_browse_button = t.Button(gui_main_frame_browse_frame, text="Browse", command=directory_select, width=21).pack(side=t.RIGHT, padx=5)
    gui_main_frame_browse_frame.grid(row=1, column=1)
    gui_main_frame_dropdown_frame = t.Frame(gui_main_frame)
    gui_main_frame_dropdown_label = t.Label(gui_main_frame_dropdown_frame, text="Size unit to display:").pack(side=t.LEFT)
    gui_main_frame_byte_drop = t.OptionMenu(gui_main_frame_dropdown_frame, byte_type, "B", "KB", "MB", "GB", "TB")
    gui_main_frame_byte_drop.pack(side=t.RIGHT)
    gui_main_frame_dropdown_frame.grid(row=2, column=1, pady=5)
    gui_main_frame_calc_button = t.Button(gui_main_frame, text="Calculate", command=button_calculate, width=21).grid(row=3, column=1, pady=5)
    gui_main_frame_info_button = t.Button(gui_main_frame, text="About", command=button_about, width=21).grid(row=4, column=1, pady=5)
    gui_main_frame_exit_button = t.Button(gui_main_frame, text="Exit", command=lambda: button_exit(window), width=21).grid(row=5, column=1, pady=5)
    gui_main_frame.columnconfigure(0, weight=1)
    gui_main_frame.columnconfigure(1, weight=1)
    gui_main_frame.columnconfigure(2, weight=1)
    gui_main_frame.pack(fill=t.BOTH)
    print("Done!\n\n(gui_main): Waiting for user input...")
    window.mainloop()
    try:
        if "\\" in selected_directory:
            selected_directory = selected_directory.replace("\\", "/")
        return [rubbish, selected_directory, byte_type]
    except:
        return [False, None]
