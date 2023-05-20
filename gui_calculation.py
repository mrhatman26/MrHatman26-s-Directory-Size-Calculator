import tkinter as t
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar
import os
from functions import button_exit
#Calculation screen
def gui_calculation(selected_directory, byte_type):
    global return_empty
    return_empty = False
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
            global second_largest_files
            global second_largest_files_dirs
            total_size = 0
            largest_file = None
            largest_file_dir = None
            largest_file_size = 0
            scanned_files = 0
            second_largest_files = [None, None, None, None, None, None, None, None, None, None]
            gui_calculating_file_log.configure(state="normal")
            gui_calculating_file_log.delete("1.0", "end")
            gui_calculating_file_log.configure(state="disabled")
            for dirpath, dirnames, filenames in os.walk(sd):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    if not os.path.islink(fp):
                        total_size += os.path.getsize(fp)
                        if os.path.getsize(fp) > largest_file_size:
                            largest_file = str(f)
                            largest_file_size = os.path.getsize(fp)
                            largest_file_dir = fp
                        else:
                            if second_largest_files[0] is None:#len(second_largest_files) < 1:
                                second_largest_files[0] = str(f) + "+" + str(os.path.getsize(fp)) + "+" + fp
                            else:
                                old_value = ""
                                old_value_alt = ""
                                space_found = False
                                index = 0
                                for file in second_largest_files:
                                    if file is None:
                                        second_largest_files[index] = str(f) + "+" + str(os.path.getsize(fp)) + "+" + fp
                                        break
                                    if space_found is False:                                        
                                        if int(os.path.getsize(fp)) > int(file.split("+")[1]):
                                            old_value = file
                                            second_largest_files[index] = str(f) + "+" + str(os.path.getsize(fp)) + "+" + fp
                                            space_found = True
                                    else:
                                        if int(old_value.split("+")[1]) > int(file.split("+")[1]):
                                            old_value_alt = old_value
                                            old_value = file
                                            second_largest_files[index] = old_value_alt
                                    index += 1
                                    gui_calculating_p_bar.update()                                            
                    scanned_files += 1
                    gui_calculating_p_bar.update()
                    gui_calculating_file_log.configure(state="normal")
                    gui_calculating_file_log.insert("end", str(f) + fp + "\n")
                    gui_calculating_file_log.see("end")
                    gui_calculating_file_log.configure(state="disabled")
            index = 0
            if bt.get() == "KB":
                total_size = total_size / 1024
                largest_file_size = largest_file_size / 1024
                for file in second_largest_files:
                    file_info = second_largest_files[index].split("+")
                    file_info[1] = str(int(file_info[1]) / 1024)
                    second_largest_files[index] = file_info[0] + "+" + file_info[1] + "+" + file_info[2]
                    index += 1
                    gui_calculating_p_bar.update()
            if bt.get() == "MB":
                total_size = total_size / 1024
                total_size = total_size / 1024
                largest_file_size = largest_file_size / 1024
                largest_file_size = largest_file_size / 1024
                for file in second_largest_files:
                    file_info = second_largest_files[index].split("+")
                    file_info[1] = int(file_info[1]) / 1024
                    file_info[1] = str(file_info[1] / 1024)
                    second_largest_files[index] = file_info[0] + "+" + file_info[1] + "+" + file_info[2]
                    index += 1
                    gui_calculating_p_bar.update()
            if bt.get() == "GB":
                total_size = total_size / 1024
                total_size = total_size / 1024
                total_size = total_size / 1024
                largest_file_size = largest_file_size / 1024
                largest_file_size = largest_file_size / 1024
                largest_file_size = largest_file_size / 1024
                for file in second_largest_files:
                    file_info = second_largest_files[index].split("+")
                    file_info[1] = int(file_info[1]) / 1024
                    file_info[1] = file_info[1] / 1024
                    file_info[1] = str(file_info[1] / 1024)
                    second_largest_files[index] = file_info[0] + "+" + file_info[1] + "+" + file_info[2]
                    index += 1
                    gui_calculating_p_bar.update()
            if bt.get() == "TB":
                total_size = total_size / 1024
                total_size = total_size / 1024
                total_size = total_size / 1024
                total_size = total_size / 1024
                largest_file_size = largest_file_size / 1024
                largest_file_size = largest_file_size / 1024
                largest_file_size = largest_file_size / 1024
                largest_file_size = largest_file_size / 1024
                for file in second_largest_files:
                    file_info = second_largest_files[index].split("+")
                    file_info[1] = int(file_info[1]) / 1024
                    file_info[1] = file_info[1] / 1024
                    file_info[1] = file_info[1] / 1024
                    file_info[1] = str(file_info[1] / 1024)
                    second_largest_files[index] = file_info[0] + "+" + file_info[1] + "+" + file_info[2]
                    index += 1
                    gui_calculating_p_bar.update()
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
        directory_size_calculation(sd, bt)
    def button_cancel():
        global return_empty
        print("\n(gui_calculation): Update: User clicked cancel.")
        window.destroy()
        return_empty = True
        
    #GUI
    resolution = "800x260"
    title = "MrHatman26's Directory Size Calculator (Calculating...)"
    #Window settings
    window = t.Tk()
    window.geometry(resolution)
    window.title(title)
    window.resizable(False, False)
    #Window Widgets
    gui_calculating_label = t.Label(window, text="Calculating...").pack()
    gui_calculating_p_bar = Progressbar(window, orient='horizontal', length=675, mode='indeterminate')
    gui_calculating_p_bar.pack(pady=5)
    gui_calculating_file_log = t.Text(window, height=10, width=84, bg="white")
    gui_calculating_file_log.pack()
    gui_calculating_file_log.configure(state="disabled")
    gui_calculating_cancel_button = t.Button(window, text="Cancel", command=button_cancel, width=21).pack(pady=10)
    print("Done.\n\n(gui_calculation): Update running function and window")
    gui_calculating_p_bar.start()
    window.after(1000, start_thread, selected_directory, byte_type)
    window.mainloop()
    try:
        if return_empty is False:
            print("(gui_calculation): return is NOT empty!")
            return [total_size, largest_file, largest_file_size, largest_file_dir, scanned_files, second_largest_files]
        else:
            print("(gui_calculation): return is NOT None! (Normal)")
            return None
    except:
        print("(gui_calculation): return is NOT None! (Exception)")
        return None
