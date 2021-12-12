import os
import re
import requests

# Maps all files > Iterate all the file > Search all imgur links > Download the images in the attachments folder > Replace the links in the file

path = "E:\Testing\ObsidianLocalBackup\Vault" #! Vault absolute directory
attachmentsDirectory = "attachments" #! Relative attachements direcory in the vault
regexImgurLink = 'https:\/\/i.imgur.com\/...+\.[a-zA-Z]{3}'
# regexImageLink = '!\[.*?\]\(https:\/\/i.imgur.com\/...+.[a-zA-Z]{3}\)'
list_of_files = []

def saveImages(image_url):
    img_data = requests.get(image_url).content
    with open(f'{path}\\{attachmentsDirectory}\\{image_url[20:]}', 'wb') as handler:
        handler.write(img_data)
    # print(f'{image_url[20:]} downloaded in {path}\\attachments\\{image_url[20:]}')


# Create attachment directory if there isn't
if not os.path.isdir(f'{path}\\{attachmentsDirectory}'):
    os.mkdir(f'{path}\\{attachmentsDirectory}')

# Maps all .md files
for root, dirs, files in os.walk(path):
    for file in files:
        if file[-2:] == 'md':
            list_of_files.append(os.path.join(root,file))

totalFiles = len(list_of_files)
counter = 0

# Maps all images for file and replace it
for file in list_of_files:
    newFileData = None
    with open(file, mode='r', encoding='utf8') as f:
        list_of_images_url = []
        fileData = f.read()
        urls = re.findall(regexImgurLink, fileData)
        for url in urls: 
            list_of_images_url.append(url)
        
        for image_url in list_of_images_url:
            saveImages(image_url)

        newFileData = fileData
        for image_url in list_of_images_url:
            newFileData = re.sub(f'https:\/\/i.imgur.com\/(?:{image_url[20:]})', f'{image_url[20:]}' , newFileData)

    with open(file, mode='w', encoding='utf8') as f:
        f.write(newFileData)

    counter += 1
    print(f'[{counter}/{totalFiles}] - Images replaced in {file}')

