# RAW
# KH_tables_from_calls_Projects_DB.ipynb

import requests
import pandas as pd

ask_query = 'https://openei.org/wiki/Special:Ask/-5B-5BCategory:PRIMRE-20Projects-20Database-20Devices-5D-5D/-3FName/-3FOrganization/mainlabel=/limit=500/prettyprint=true/format=csv'
test_query = 'https://openei.org/wiki/Special:Ask/-5B-5BCategory:PRIMRE-20Projects-20Database-20Devices-5D-5D/-3FName/-3FOrganization/mainlabel=/limit=100/format=csv'

ask_response = requests.get(test_query)
ask_response_str = str(ask_response.text)



def compose_ask_query_relational_table(ask_query):
    '''
    This Function is designed to 

    '''
    # Retrieve data from ask query
    ask_response = requests.get(ask_query)
    ask_response_str = str(ask_response.text)
    
    # Clean data
    ask_response_str_splt1 = ask_response_str.split('\n')
    ask_response_str_splt1_2 = ask_response_str_splt1[1:-1]
    
    all_data = list()
    for i in range(0, len(ask_response_str_splt1_2)):
        row = ask_response_str_splt1_2[i].split(',')
        
        # Clean funky "s that are sometimes included in the data.
        row_new = list()
        for i in range(1, 3):                # Clean only the elements that will form the columns we will use
            first_char = row[i][0]
            last_char = row[i][-1]
            if first_char == '"':
                if last_char == '"':
                    new_str = row[i][1:-1]
                else:
                    new_str = row[i][1:]
            else:
                if last_char == '"':
                    new_str = row[i][:-1]
                else:
                    new_str = row[i]
        
            row_new.append(new_str)
            
        all_data.append(row_new[0])
        all_data.append(row_new[1])
    
    device_nam_lst = all_data[0::2]
    device_org_lst = all_data[1::2]
    
    table = pd.DataFrame({'Device Name':device_nam_lst, 'Organization':device_org_lst})

    return table