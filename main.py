import tkinter
import tkinter.messagebox
import customtkinter
import validators
from pytube import YouTube

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("YT Downloader")
        self.geometry(f"{600}x{350}")
        self.minsize(600, 350)
        self.maxsize(600, 350)

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((1, 2), weight=1)

        # TITLE FRAME
        self.title_frame = customtkinter.CTkFrame(self, width=225, height=45, corner_radius=0)
        self.title_frame.grid(row=0, column=1, columnspan=4, sticky="nsew")
        self.title_label = customtkinter.CTkLabel(self.title_frame, text="YT Downloader",
                                                  font=customtkinter.CTkFont(size=25, weight="bold"))
        self.title_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # MAIN FRAME
        self.main_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.main_frame.grid(row=1, column=1, columnspan=4, rowspan=2, sticky="nsew")
        self.link_entry = customtkinter.CTkEntry(master=self.main_frame, placeholder_text="Youtube Link", width=500,
                                                 height=30, border_width=2, justify='center')
        self.link_entry.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)
        self.download_path = tkinter.StringVar()
        self.download_path.set('Path')
        self.path_entry = customtkinter.CTkEntry(master=self.main_frame, width=410, height=30,
                                                 border_width=2, justify='center', state='disabled',
                                                 textvariable=self.download_path)
        self.path_entry.place(relx=0.43, rely=0.57, anchor=tkinter.CENTER)
        self.path_btn = customtkinter.CTkButton(master=self.main_frame, width=80, height=30, border_width=0,
                                                corner_radius=8, text="browse", command=self.browseFolders)

        self.path_btn.place(relx=0.845, rely=0.57, anchor=tkinter.CENTER)

        self.download_btn = customtkinter.CTkButton(master=self.main_frame, width=80, height=30, border_width=0,
                                                    corner_radius=8, text="Download", command=self.downloadVideo)

        self.download_btn.place(relx=0.5, rely=0.69, anchor=tkinter.CENTER)

    def browseFolders(self, *args):
        download_dir = tkinter.filedialog.askdirectory()
        self.download_path.set(download_dir)

    def downloadVideo(self, *args):
        vidLink = self.link_entry.get()

        if not validators.url(vidLink):
            tkinter.messagebox.showinfo(title=None, message="The URL entered is invalid")
        else:
            folder = self.download_path.get()
            try:
                get_video = YouTube(vidLink)
            except:
                tkinter.messagebox.showinfo(title=None, message=("Invalid URL entered. Please make sure that it is a "
                                                                 "URL to a YouTube video, not a playlist, channel, "
                                                                 "or YouTube homepage "))
            get_stream = self.getQualityStream(get_video)
            get_stream.download(folder)
            tkinter.messagebox.showinfo(title=None, message=("Video was successfully downloaded. The file can be found"
                                                             " at " + self.download_path.get()))

    def getQualityStream(self, link: object) -> None:
        resolutions = ["1080p", "720p", "480", "360p", "240p"]
        for reso in resolutions:
            streams = link.streams.filter(res=reso, progressive=True)
            if len(streams) != 0:
                return streams.first()


if __name__ == "__main__":
    app = App()
    app.mainloop()
