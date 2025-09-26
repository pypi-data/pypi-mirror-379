import requests
import pandas as pd
import primrea.kh_table_gen.entry_based as entry_based_table_gen

def api_to_df(api_str):
    '''This function takes in a string of the api, and returns a corresponding pandas dataframe."'''
    api_response = requests.get(api_str)
    api_response_json = api_response.json()
    api_df = pd.DataFrame(api_response_json)
    return api_df

    
class primrea_data():
    '''
    
    '''
    def __init__(self):
        # Return raw pandas dataframes corresponding to api contents
        tethys_api = 'https://tethys.pnnl.gov/api/primre_export'
        tethys_e_api = 'https://tethys-engineering.pnnl.gov/api/primre_export'
        #tethys_dataframe = api_to_df(tethys_api)
        #tethys_e_dataframe = api_to_df(tethys_e_api)
        
        # Initialize Tethys tables
        self.tethys_dataframe_raw = api_to_df(tethys_api)
        self.tethys_core = entry_based_table_gen.construct_core_table(self.tethys_dataframe_raw)
        self.tethys_authors = entry_based_table_gen.construct_authors_table(self.tethys_dataframe_raw)
        self.tethys_organizations = entry_based_table_gen.construct_organizations_table(self.tethys_dataframe_raw)
        self.tethys_tags = entry_based_table_gen.construct_tags_table(self.tethys_dataframe_raw)

        # Initialize Tethys Engineering tables
        self.tethys_e_dataframe_raw = api_to_df(tethys_e_api)
        self.tethys_e_core = entry_based_table_gen.construct_core_table(self.tethys_e_dataframe_raw)
        self.tethys_e_authors = entry_based_table_gen.construct_authors_table(self.tethys_e_dataframe_raw)
        self.tethys_e_organizations = entry_based_table_gen.construct_organizations_table(self.tethys_e_dataframe_raw)
        self.tethys_e_tags = entry_based_table_gen.construct_tags_table(self.tethys_e_dataframe_raw)

