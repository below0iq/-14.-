import requests
import os
import shutil



url = "https://random.dog/woof.json/"
payload = {"filter":"mp4,webm"}
folder = "dawgs"



def download_picture(folder, filename, url):
    filepath = os.path.join(folder, filename)
    response = requests.get(url)
    with open(filepath, "wb") as file:
        file.write(response.content)


def main():
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.mkdir(folder)
    for number in range(50):
        response = requests.get(url,params=payload)
        picture_link = response.json()["url"]
        link, picture_extension = os.path.splitext(picture_link)
        filename = f"dog_{number+1}{picture_extension}"
        download_picture(folder, filename, picture_link)

if __name__ == "__main__":
    main()