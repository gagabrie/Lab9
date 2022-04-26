import requests
import ctypes

def set_desktop_background_image(image_path):
    """
    Sets the desktop background using the path of the image
    
    :param name: Path of the image
    :return : wallpaper of the pokemon
    """
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0) 

def download_image_from_url(image_url, save_path):
    """
    Downloads and save the image from the url 
    
    :param name: image url and path where to save the image
    :return : downloaded image to the given path
    """

    print('Downloading image from URL..., end=''', end = '')
    response = requests.get(image_url) #this contains the data of the image

    if response.status_code == 200:             #if 200 print success
        with open(save_path, 'wb') as file: #with used for calling two functions together
            file.write(response.content)    #assigning the file handle to file
        print('success')    
    else:
        print('failed. Response code:', response.status_code) 


    