
import ctypes
from tkinter import *
from tkinter import ttk
from library import download_image_from_url, set_desktop_background_image
from pokeapi import get_pokemon_list, get_pokemon_image_url 
import os 
import sys 

def main():
   #creating the GUI
   
   script_dir = sys.path[0]    #contains full path to the directory in which this script resides
   image_dir = os.path.join(script_dir, 'images') #creating images directory
   if not os.path.isdir(image_dir):   #checking if directory exists
      os.mkdir(image_dir)             #creating directory if not exists

   #creating the window
   root = Tk()
   root.title('Pokemon Image Viewer')  #title of the GUI
   app_id = 'pokemon.image.viewer'
   ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id) #setting up the icon in taskbar
   root.iconbitmap(os.path.join(script_dir, 'pokeball.ico'))   #icon adjacent to the title of GUI
   root.rowconfigure(0, weight=1) #distribute extra space 
   root.columnconfigure(0, weight=1)  #distribute extra space
   root.minsize(500, 600) #fixing the minimun size


   #creating the frame
   frm = ttk.Frame(root)
   frm.grid(sticky=(N,S,E,W)) #stickness at each direction rather than shrinking
   frm.rowconfigure(0, weight=1) #distribute extra space
   frm.columnconfigure(1, weight=1) #distribute extra space
   

   img_poke = PhotoImage(file=os.path.join(script_dir, 'pokeballl.png'))
   lbl_img = ttk.Label(frm, image=img_poke) #assigning image to the label
   lbl_img.grid(row=0, column=0, padx=10, pady=10)


   #creating the combobox
   pokemon_list = get_pokemon_list()  #fetching list of pokemon
   pokemon_list.sort()     #sorting alphabateically
   pokemon_list = [p.capitalize() for p in pokemon_list]
   cbo_pokemon = ttk.Combobox(frm, values=pokemon_list, state='readonly',) #getting the list of pokemon in combobox
   cbo_pokemon.set('Select a Pokemon') #setting initial text #readonly prevent user to type
   cbo_pokemon.grid(row=1, column=0, padx=10, pady=10) #putting combobox on frame on row 1

   def handle_poke_select(event):
      """
      Gets the name of pokemon from combox and use the name to download url and then download image
    
      :param name: event (not even used the parameter) 
      :return : Image in the PhotoImage
      """
      pokemon_name = cbo_pokemon.get() #getting name of pokemon
      image_url = get_pokemon_image_url(pokemon_name) #getting pokemon image url by passing name of pokemon
      image_path = os.path.join(image_dir, pokemon_name + '.png') #creating path for the images
      download_image_from_url(image_url, image_path) #downloading image using image url and image path
      img_poke['file'] = image_path          
      btn_set_desktop.state(['!disabled']) #not disabled
      

   cbo_pokemon.bind('<<ComboboxSelected>>', handle_poke_select) #name of the event and name of the function
   #creating a button
   def handle_btn_set_desktop():
      """
      Creates the button for changing the desktop background
    
      :param name:  
      :return : Button for controlling the pokemon image
      """
      pokemon_name = cbo_pokemon.get()  #getting name of pokemon
      image_path = os.path.join(image_dir, pokemon_name + '.png')   #creating path for the images
      set_desktop_background_image(image_path)
      
   
   btn_set_desktop = ttk.Button(frm, text='Set as Desktop Image', command=handle_btn_set_desktop) #title for the button
   btn_set_desktop.state(['disabled'])  #disabled
   btn_set_desktop.grid(row=2, column=0,padx=10, pady=10) #putting button on the grid on row 2
   root.mainloop()

main()
