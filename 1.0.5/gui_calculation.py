import tkinter as t
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar
import os
from functions import button_exit
import threading

#Calculation screen
def gui_calculation(selected_directory, byte_type):
    print("\n(gui_calculation): Update: Creating gui_calculation...", end="")
    #Function commands
    def directory_size_calculation(sd, bt):
        print("(gui_calculation): Update: Calculating directory size...", end="")
        if os.path.isdir(sd):
            global total_size
            global largest_file
            global largest_file_size
            global largest_file_dir
            global scanned_files
            total_size = 0
            largest_file = None
            largest_file_dir = None
            largest_file_size = 0
            scanned_files = 0
            for dirpath, dirnames, filenames in os.walk(sd):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    if not os.path.islink(fp):
                        total_size += os.path.getsize(fp)
                        if os.path.getsize(fp) > largest_file_size:
                            largest_file = str(f)
                            largest_file_size = os.path.getsize(fp)
                            largest_file_dir = fp
                    scanned_files += 1
                    gui_calculating_p_bar.update()
            if bt.get() == "KB":
                total_size = total_size / 1024
                largest_file_size = largest_file_size / 1024
            if bt.get() == "MB":
                total_size = total_size / 1024
                total_size = total_size / 1024
                largest_file_size = largest_file_size / 1024
                largest_file_size = largest_file_size / 1024
            if bt.get() == "GB":
                total_size = total_size / 1024
                total_size = total_size / 1024
                total_size = total_size / 1024
                largest_file_size = largest_file_size / 1024
                largest_file_size = largest_file_size / 1024
                largest_file_size = largest_file_size / 1024
            if bt.get() == "TB":
                total_size = total_size / 1024
                total_size = total_size / 1024
                total_size = total_size / 1024
                total_size = total_size / 1024
                largest_file_size = largest_file_size / 1024
                largest_file_size = largest_file_size / 1024
                largest_file_size = largest_file_size / 1024
                largest_file_size = largest_file_size / 1024
            print("Done.")
            print("(gui_calculation): Update: Total Size is " + str(total_size) + str(bt.get()))
            print("(gui_calculation): Update: Largest file is " + str(largest_file) + " with a size of " + str(largest_file_size) + str(bt.get()))
            print("(gui_calculation): Closing GUI and displaying results")
        else:
            print("Failed!\n(gui_calculation): Update: Directory does not exist!")
            t.messagebox.showerror("Error!", "Error: The selected directory does not exist.")
            print("(gui_calculation): Update: Deleting global vars...", end="")
            try:
                del largest_file
                del largest_file_dir
                del largest_file_size
                del scanned_files
                print("Done.")
            except:
                print("Failed. (They may already have been deleted")
        window.destroy()
    def start_thread(sd, bt):
        thread = None
        thread = threading.Thread(target=directory_size_calculation(sd, bt), daemon=True)
        try:
            thread.start()
        except:
            thread.join()
    def button_cancel():
        print("\n(gui_calculation): Update: User clicked cancel.")
        window.destroy()
    #GUI
    resolution = "800x100"
    title = "MrHatman26's Directory Size Calculator (Calculating...)"
    #Window settings
    window = t.Tk()
    window.geometry(resolution)
    window.title(title)
    window.resizable(False, False)
    #Window Widgets
    gui_calculating_label = t.Label(window, text="Calculating...").pack()
    gui_calculating_p_bar = Progressbar(window, orient='horizontal', length=675, mode='indeterminate')
    gui_calculating_p_bar.pack()
    gui_calculating_cancel_button = t.Button(window, text="Cancel", command=button_cancel, width=21).pack(pady=10)
    print("Done.\n\n(gui_calculation): Update running function and window")
    gui_calculating_p_bar.start()
    window.after(1000, start_thread, selected_directory, byte_type)
    window.mainloop()
    try:
        return [total_size, largest_file, largest_file_size, largest_file_dir, scanned_files]
    except:
        return None
