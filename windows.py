import subprocess
import os

logo = """██╗   ██╗██╗██████╗ ███████╗ ██████╗     ██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗ 
██║   ██║██║██╔══██╗██╔════╝██╔═══██╗    ██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║   ██║██║██║  ██║█████╗  ██║   ██║    ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝
╚██╗ ██╔╝██║██║  ██║██╔══╝  ██║   ██║    ██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗
 ╚████╔╝ ██║██████╔╝███████╗╚██████╔╝    ██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║
  ╚═══╝  ╚═╝╚═════╝ ╚══════╝ ╚═════╝     ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝                                                                                                                       
"""



def video_downloader(link,video_qulity):
    download_command = f"yt-dlp {link} -f {video_qulity}"
    subprocess.run(download_command, shell=True, check=True)
command = "on"
while not command == "off":
    print(logo)
    print("""Welcome to video downloader.
[1] Youtube Video(HD/SD).
[2] Tiktok Video (No Watermark).
[3] Zoom Recording Download.
[4] Other Video(HD).
What Do you want to download ?"
""")
    command = input("> ")
    if command == "1":
        link = input("Enter Your Video Link : ")
        print("""Please select video quality.
[1] 144p
[2] 720p
""")
        video_quality = int(input("> "))
        queality_is_vaild = True
        if video_quality == 1:
            video_quality = 18
        elif video_quality == 2:
            video_quality = 22
        else:
            queality_is_vaild = False
            print("Invaild Input!.")

        if queality_is_vaild:
            video_downloader(link,video_quality)

    elif command == "2":
        link = input("Enter Your Video Link : ")
        download_command = f"yt-dlp {link} "
        subprocess.run(download_command, shell=True, check=True)

    elif command == "3":
        link = input("Enter Your Video Link : ")
        password_protected = input("Password Protected ? [y/n]: ")
        if password_protected == "y":
            video_passcode = input("Enter the video password : ")
            download_command = f"yt-dlp {link} --video-password {video_passcode}"
        else:
            download_command = f"yt-dlp {link} "

        print(download_command)
        subprocess.run(download_command, shell=True, check=True)

    elif command == "4":
        link = input("Enter Your Video Link : ")
        download_command = f"yt-dlp {link} "
        subprocess.run(download_command, shell=True, check=True)

    else:
        print("Invaild Input!.")
