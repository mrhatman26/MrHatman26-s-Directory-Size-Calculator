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
    second_largest_files_string = ""
    def print_second_largest_files():
        for file in total_size[5]:
            if file is not None:
                file_info = file.split("!+!")
                print(file_info)
                if gui_results_second_files_box.compare("end-1c", "!=", "1.0"):
                    gui_results_second_files_box.configure(state="normal")
                    gui_results_second_files_box.insert("end", "\n\nFilename: " + file_info[0] + "\nSize: " + file_info[1] + byte_type.get() + "\nDirectory: " + file_info[2])
                    gui_results_second_files_box.configure(state="disabled")
                else:
                    gui_results_second_files_box.configure(state="normal")
                    gui_results_second_files_box.insert("1.0", "Filename: " + file_info[0] + "\nSize: " + file_info[1] + byte_type.get() + "\nDirectory: " + file_info[2])
                    gui_results_second_files_box.configure(state="disabled")
                gui_results_second_files_box.config(yscrollcommand=gui_results_second_files_scroll.set)
                gui_results_second_files_scroll.update()
            
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
    gui_results_second_files_label = t.Label(window, text="\nOther largest files:", font=(None, 14)).pack()
    gui_results_second_files_box = t.Text(window, height=10, width=100, bg="white")
    gui_results_second_files_box.pack(padx=10)
    gui_results_second_files_box.configure(state="disabled")
    gui_results_scanned_label = t.Label(window, text=files_scanned_string, font=(None, 10)).pack(padx=10)
    gui_results_okay_button = t.Button(window, text="Okay", command=button_okay, width=21, font=(None, 12)).pack(pady=10)
    gui_results_second_files_scroll = t.Scrollbar(window, command=gui_results_second_files_box.yview, width=15)
    gui_results_second_files_scroll.place(x=859, y=230, height=164)
    print_second_largest_files
    print("Done!\n\n(gui_results): Waiting for user input")
    window.mainloop()
