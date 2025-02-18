import tkinter as tk
from tkinter import PhotoImage

class WarningWindow:
    def __init__(self, file_name):
        """
            This function is a constructor for theWarningWindow with the file name that triggered the virus alert.
            :param file_name: The name of the file that was found to be malicious.
        """
        self.__file_name = file_name

    def center_window(self, window, width, height):
        """
            This function centers the given window on the screen.
            :param window: The tkinter window to center.
            :param width: The width of the window.
            :param height: The height of the window.
            :return: None
        """
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        window.geometry(f"{width}x{height}+{x}+{y}")

    def show_window(self):
        """
            This function displays the warning window indicating that a virus has been detected.
            :return: None
        """
        root = tk.Tk()
        root.title("Virus Detected!")
        window_width = 400
        window_height = 300
        self.center_window(root, window_width, window_height)

        frame = tk.Frame(root, bg="pink", width=window_width, height=window_height)
        frame.pack()

        label = tk.Label(frame, text="Warning!", font=("Helvetica", 20), bg="yellow")
        label.place(relx=0.5, rely=0.1, anchor="center")

        subtitle_label = tk.Label(frame, text=f"Found virus: {self.__file_name}", font=("Helvetica", 16), bg="pink")
        subtitle_label.place(relx=0.5, rely=0.2, anchor="center")

        delete_label = tk.Label(frame, text="File has been deleted.", font=("Helvetica", 16), bg="pink")
        delete_label.place(relx=0.5, rely=0.3, anchor="center")

        image_path = "alert.png"
        image = PhotoImage(file=image_path)
        image_label = tk.Label(frame, image=image, bg="pink")
        image_label.place(relx=0.5, rely=0.7, anchor="center")

        root.mainloop()

