<body style="background-color: white; color: black">

# <img src="YT-DownloaderLogo.icns" alt="drawing" width="60" height="60"/> Youtube Video Downloader

Desktop application that allows the user to download YouTube videos directly to their computer.
Developed with the use of python's front-end libraries tkinter, customtkinter, and with the use pytube on the
back-end.

<figure style="text-align: center">
    <p align="center"><img src="images/SC1.png" alt="drawing" width="600"/></p>
</figure>

The user inputs the link to the video they wish to download. Then they click on browse, which
opens a finder window that allows them to select a directory path to store the MP4 file. Lastly, they
clicked on download. Once the download is finished a message window will open to notify them and display
the path to the file

## Getting Started

Clone down this repository. You will need `Python` and `git` installed globally on your machine.

## 🛠 Installation and Setup Instructions

1. Travel to root directory

2. Create virtual enviorment: `python3 -m venv <env_name>`

3. Avtivate enviorment: `source <env_name>/bin/activate`

4. Install packages: `pip install -r requirements.txt`

5. Run the project with: `python3 main.py`

6. When done, run: `deactivate`

## Error Handling

<figure>
    <p align="center">
        <img src="images/SC2.png" alt="drawing" width="400"/>
        <img src="images/SC3.png" alt="drawing" width="400"/>
    </p>
</figure>

When an invalid url is entered a message window will open to notify the user. In addition to invalid URLs,
a valid URL may not belong to a YouTube video and a message is also sent in that instance.

## Future Plans

- Option to choose video quality
- Allow user to download as an mp3

### Thank You For Visiting `!!!`

</body>
