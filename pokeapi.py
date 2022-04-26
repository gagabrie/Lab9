import requests

def get_pokemon_info(name):
    """
    Gets a dictionary of info from the PokeAPI for a pokemon.
    
    :param name: Pokemon's name (or poke index)
    :return : Dictionary of Pokemon information if successful: None if unsuccessful.
    """

    print("Getting user information...", end='')
    if name is None:            #If the name is missed give error(Used in lab 8)
        print('error: Missing name parameter')
        return

    name = name.lower()
    if name == '':              #If the name column is emptygive error(Used in lab 8)
        print('error: Empty name parameter')
        return

    URL = 'https://pokeapi.co/api/v2/pokemon/' + str(name)
    response = requests.get(URL)    #calling the get function

    if response.status_code == 200:   #if 200
        print('success')              #print success
        return response.json() 
    else:
        print('failed. Response code:', response.status_code)
        return

def get_pokemon_list(limit=2000, offset=0): #limit on the number of the pokemon
    """
    Gets a list of pokemon name from the PokeAPI for a pokemon.
    Function accepting two parameters limit and offset.
    
    :param : limit and offset
    :return : list of Pokemon name as per the limit.
    """

    print("Getting list of Pokemon...", end='')
    URL = 'https://pokeapi.co/api/v2/pokemon/'
    params = {                    #my small dictionary  
        'offset': offset,
        'limit' : limit,

    } #my small dictionary
    response = requests.get(URL, params=params)#calling the get function

    if response.status_code == 200:         #if 200 
        print('success')                    #print success
        poke_dict = response.json() #this will return a dictionary
        return [p['name'] for p in poke_dict['results']]#p is the dictionary structre
        #results will give the list of the names
    else:
        print('failed. Response code:', response.status_code)   

def get_pokemon_image_url(name):
    """
    Gets the url using the name of a pokemon from the dictionary.
    
    :param name: name of pokemon
    :return : URL
    """
    poke_dict = get_pokemon_info(name) 
    if poke_dict: #return none if we get a faliure.
        poke_url = poke_dict['sprites']['other']['official-artwork']['front_default']#different levels to reach appropiate url
        return poke_url                                                              #url used from resources for ditto