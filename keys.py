client_id = "5zNzCfd86iCaL6MPLmAQNQ"
api_key = "eE41dxlEQ_PxpyDWqc6HzSlOKrO7Yij6t0PFpeD9g8615PcVTyVSCTbb1VzRcLSnzVoF-3Ze5VIH9LLWOk7Zj5xmW_POR3DjdUrq8biT74WzPfc9Sa5vyHfjLjuUYHYx"


'''
def parsed_data(list_of_data):
    # Container to hold the pharsed data 
    parsed_data = []

    # Loop through the businesses

    # Pharse each individual business into a tuple
    
    # Add each individual business tuple to our data container

    # Return the container with the pharsed results
    return parsed_data


def df_safe(csv filepath, parsed results):
    # your code to open the csv file, concat the current data, and save the data. 



# create a variable  to keep track of which result you are in. 
cur = 0

#set up a while loop to go through and grab the result 
while cur < num and cur < 1000:
    #set the offset parameter to be where you currently are in the results 
    url_params['offset'] = cur
    #make your API call with the new offset number
    results = yelp_call(url_params, api_key)
    
    #after you get your results you can now use your function to parse those results
    parsed_results = parse_results(results)
    
    # use your function to insert your parsed results into the db
    df_save(parsed_results)
    #increment the counter by 50 to move on to the next results
    cur += 20
'''