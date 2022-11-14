from tkinter import filedialog
import customtkinter as ctk
from pytube import YouTube
from tkinter import ttk
import tkinter as tk
import pyperclip
import os

class Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('300x100')
        self.title('Toplevel Window')

        ttk.Button(self,
                text='Close',
                command=self.destroy).pack(expand=True)

class App(ctk.Tk()):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")
        self.title("Youtube Converter")
        self.geometry(f'800x700+{int(self.winfo_screenwidth() / 2 - 800 / 2)}+{int(self.winfo_screenheight() / 2 - 700 / 2)}')
        self.resizable(False, False)

        global creator
        global title
        creator = ""
        title = ""
        folder_path = ""

    def browse_button(self):
        global folder_path
        file = filedialog.askdirectory()
        folder_path = file
        print(folder_path)

    def download_audio(self):
        url = YouTube(self.entry.get())
        self.label2.set_text(f'Author: {url.author}')
        self.label3.set_text(f'Title: {url.title}')
        download = url.streams.get_highest_resolution()
        print(folder_path)
        if folder_path:
            downloadFile = download.download(folder_path)
            base, ext = os.path.splitext(downloadFile)
            new_file = base + ".mp3"
            os.rename(downloadFile, new_file)
        else:
            print(os.environ['USERPROFILE'] + '\Desktop')
            downloadFile = download.download(os.environ['USERPROFILE'] + '\Desktop')
            base, ext = os.path.splitext(downloadFile)
            new_file = base + ".mp3"
            os.rename(downloadFile, new_file)

    def download_video(self):
        url = YouTube(self.entry.get())
        self.label2.set_text(f'Author: {url.author}')
        self.label3.set_text(f'Title: {url.title}')
        download = url.streams.get_highest_resolution()
        if folder_path:
            download.download(folder_path)
        else:
            print(os.environ['USERPROFILE'] + '\Desktop')
            download.download(os.environ['USERPROFILE'] + '\Desktop')

        label1 = ctk.CTkLabel(master=self, text="Standard download Location is the Desktop")
        label1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        label2 = ctk.CTkLabel(master=self, text="Author")
        label2.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

        label3 = ctk.CTkLabel(master=self, text="Title")
        label3.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        label4 = ctk.CTkLabel(master=self, text="")
        label4.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

        entry = ctk.CTkEntry(master=self)
        entry.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        button1 = ctk.CTkButton(master=self, text="Browse Location", command=lambda: self.browse_button())
        button1.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

        button2 = ctk.CTkButton(master=self, text="Download as MP3",
                                command=lambda: self.download_audio())
        button2.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        button3 = ctk.CTkButton(master=self, text="Download as MP4",
                                command=lambda: self.download_video())
        button3.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

    def open_window(self):
        window = Window(self)
        window.grab_set()

if __name__ == "__main__":
    app = App()
    app.mainloop()


