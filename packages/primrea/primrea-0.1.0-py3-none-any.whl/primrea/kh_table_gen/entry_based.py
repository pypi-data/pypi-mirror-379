import requests
import pandas as pd
import re


def find_entry_id(entry_uri):
    '''
    This function takes in the url of a MHKDR entry, and returns the entry_id of that page. 
    The 'entry_id' is the integer at the end of the url, which is unique to each MHKDR entry.
    The regex used in this function relies on the fact that the only number in the url is the id.
    '''
    rule = re.compile(r'\d+')
    matches_rule = rule.findall(entry_uri)
    entry_id = int(matches_rule[0])

    return entry_id


def construct_core_table(tethyss_df):
    '''
    This function creates a normalized table for the entity "entry." The primary key of the resulting table is
    "entry_id," and it may be used to connect entries represented in this table to associated entities, such
    as authors, organizations, or tags.
    '''
    # Constructing the entry_id data
    tethyss_df_len = len(tethyss_df)
    entry_ids = list()
    for i in range(0, tethyss_df_len):
        entry_id = find_entry_id(tethyss_df['URI'][i])
        entry_ids.append(entry_id)

    # Add entry_id column
    tethyss_df['entry_id'] = entry_ids

    # Correct datatype of the datetime columns
    tethyss_df['originationDate2'] = pd.to_datetime(tethyss_df['originationDate'], errors='coerce')
    tethyss_df['modifiedDate2'] = pd.to_datetime(tethyss_df['modifiedDate'])

    # Slice working df to final col list
    tethyss_df_final = tethyss_df[['entry_id', 'originationDate2', 'modifiedDate2', 'URI', 'landingPage', 
                                   'sourceURL', 'title', 'description', 'signatureProject']]
    tethyss_df_final = tethyss_df_final.rename(columns={'originationDate2': 'originationDate', 'modifiedDate2': 'modifiedDate'})
    tethyss_df_final = tethyss_df_final.drop_duplicates(subset='entry_id')
    
    return tethyss_df_final


def construct_mhkdr_core_table(mhkdr_df_1, mhkdr_df_2):
    '''
    This function creates a normalized table for the entity "entry." The primary key of the resulting table is
    "entry_id," and it may be used to connect entries represented in this table to associated entities, such
    as authors, organizations, or tags.
    '''
    # Constructing the entry_id data
    mhkdr_df_1_len = len(mhkdr_df_1)
    entry_ids = list()
    for i in range(0, mhkdr_df_1_len):
        entry_id = find_entry_id(mhkdr_df_1['URI'][i])
        entry_ids.append(entry_id)

    # Add entry_id column
    mhkdr_df_1['entry_id'] = entry_ids

    # Correct datatype of the datetime columns
    mhkdr_df_1['originationDate2'] = pd.to_datetime(mhkdr_df_1['originationDate'], errors='coerce')
    mhkdr_df_1['modifiedDate2'] = pd.to_datetime(mhkdr_df_1['modifiedDate'])

    # Slice working df to final col list
    mhkdr_df_1_final = mhkdr_df_1[['entry_id', 'originationDate2', 'modifiedDate2', 'URI', 'landingPage', 
                                   'sourceURL', 'title', 'description', 'signatureProject']]
    mhkdr_df_1_final = mhkdr_df_1_final.rename(columns={'originationDate2': 'originationDate', 'modifiedDate2': 'modifiedDate'})
    mhkdr_df_1_final = mhkdr_df_1_final.drop_duplicates(subset='entry_id')

    # Additional work to integrate unqiue MHKDR data.
    

    
    return mhkdr_df_final
    

def construct_authors_table(mhkdr_dataframe):
    '''
    This function creates a normalized table for the json element "author," connected to an "entry_id" that 
    may be called as a primary key to join this table to others. This disentangles the nested list structure
    present in the json to enable reporting e.g. associations among researchers, number of documents 
    attributed to each author.
    '''
    authors_of_entries = list(mhkdr_dataframe['author'])
    landing_page_uris = list(mhkdr_dataframe['URI'])
    
    entry_ids = list()  # This list will contain duplicate entry ids, as it represents the final column that will map to entry
    authors = list()    # This list will contain duplicate authors when an author contributes to multiple entries
    
    for i in range(0, len(mhkdr_dataframe)):
        # Construct "entry_id" - This will be a primary key for all future merge operations.
        entry_id = find_entry_id(landing_page_uris[i])
        
        # Construct "author" column
        num_authors = len(authors_of_entries[i])
        for j in range(0, num_authors):
            entry_ids.append(entry_id)
            authors.append(authors_of_entries[i][j])
    
    final_df = pd.DataFrame({'entry_id':entry_ids, 'author':authors})
    
    return final_df


def construct_organizations_table(mhkdr_dataframe):
    '''
    This function creates a normalized table for the json element "organization," connected to an "entry_id" that 
    may be called as a primary key to join this table to others. This disentangles the nested list structure
    present in the json to enable reporting e.g. associations among organizations, number of documents 
    attributed to each organization.
    '''
    orgs_of_entries = list(mhkdr_dataframe['organization'])
    landing_page_uris = list(mhkdr_dataframe['URI'])
    
    entry_ids = list()  # This list will contain duplicate entry ids, as it represents the final column that will map to entry
    orgs = list()    # This list will contain duplicate authors when an author contributes to multiple entries
       
    for i in range(0, len(mhkdr_dataframe)):
        # Construct "entry_id" - This will be a primary key for all future merge operations.
        entry_id = find_entry_id(landing_page_uris[i])

        # Construct "author" column
        num_orgs = len(orgs_of_entries[i])
        for j in range(0, num_orgs):
            entry_ids.append(entry_id)
            orgs.append(orgs_of_entries[i][j])
    
    final_df = pd.DataFrame({'entry_id':entry_ids, 'organization':orgs})
    
    return final_df


def construct_tags_table(mhkdr_dataframe):
    '''
    This function creates a normalized table for the json element "tags," connected to an "entry_id" that 
    may be called as a primary key to join this table to others. This disentangles the nested list structure
    present in the json to enable reporting e.g. associations among tags, number of documents 
    associated with each tag.
    '''
    tags_of_entries = list(mhkdr_dataframe['tags'])
    landing_page_uris = list(mhkdr_dataframe['URI'])
    
    entry_ids = list()  # This list will contain duplicate entry ids, as it represents the final column that will map to entry
    tags = list()    # This list will contain duplicate authors when an author contributes to multiple entries
    
    for i in range(0, len(mhkdr_dataframe)):
        # Construct "entry_id" - This will be a primary key for all future merge operations.
        entry_id = find_entry_id(landing_page_uris[i])
        
        # Construct "tag" column
        num_tags = len(tags_of_entries[i])
        for j in range(0, num_tags):
            entry_ids.append(entry_id)
            tags.append(tags_of_entries[i][j])
    
    final_df = pd.DataFrame({'entry_id':entry_ids, 'tag':tags})
    
    return final_df