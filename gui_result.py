import tkinter as t

#Results of calculation screen
def gui_results(selected_directory, total_size, byte_type):
    print("\n(gui_results): Update: Creating gui_results...", end="")
    #Function commands
    def button_okay():
        print("\n(gui_results): Update: User clicked okay. Returning to main screen")
        window.destroy()
    #GUI vars
    selected_directory = "Directory: " + selected_directory
    string_total_size = str(round(total_size[0], 2))
    string_total_size = "Total Size: " + string_total_size + byte_type.get()
    largest_file_string = "\nLargest file: " + total_size[1] + "\nSize: " + str(round(total_size[2], 4)) + byte_type.get() + "\nDirectory: " + total_size[3].replace("\\", "/")
    files_scanned_string = "Amount of files checked: " + str(total_size[4])
    print("\n")
    for file in total_size[5]:
        print(file)
    #GUI
    resolution = "800x240"
    title = "MrHatman26's Directory Size Calculator (Results)"
    #Window settings
    window = t.Tk()
    window.title(title)
    #window.geometry(resolution)
    window.resizable(False, False)
    #Window Widgets
    gui_results_label = t.Label(window, text="Results:", font=(None, 16)).pack(padx=10)
    gui_results_directory_label = t.Label(window, text=selected_directory, font=(None, 14)).pack(padx=10)
    gui_results_size_label = t.Label(window, text=string_total_size, font=(None, 14)).pack(padx=10)
    gui_results_largest_file_label = t.Label(window, text=largest_file_string, font=(None, 14)).pack(padx=10)
    gui_results_scanned_label = t.Label(window, text=files_scanned_string, font=(None, 10)).pack(padx=10)
    gui_results_okay_button = t.Button(window, text="Okay", command=button_okay, width=21, font=(None, 12)).pack(pady=10)
    print("Done!\n\n(gui_results): Waiting for user input")
    window.mainloop()
