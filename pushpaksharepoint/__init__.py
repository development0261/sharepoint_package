from shillelagh.backends.apsw.db import connect
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.client_credential import ClientCredential
import pandas as pd
import pandasql as ps
import json
import csv



class sharepointconnect:
    def __init__(self,url,client_id,client_secret,title):
        self.connection = connect(":memory:")
        self.cursor = self.connection.cursor()
        self.url = url
        self.client_id = client_id
        self.client_secret = client_secret
        self.title = title
        data = []
        
    def connet_sharepoint(self,client_id,client_secret,url):
        self.client_id=client_id
        self.client_secret=client_secret
        self.url = url
        client_credentials = ClientCredential(client_id,client_secret)
        ctx = ClientContext(url).with_credentials(client_credentials)
        print("Connection Was succesfully Established")
        return ctx

    def print_progress(self,items_read):
        print("Items read: {0}".format(items_read))

    def enum_items(self,target_list):
        items = target_list.items.top(1000)  # .top(1220)
        items.page_loaded += self.print_progress  # page load event
        ctx = self.connet_sharepoint(self.client_id,self.client_secret,self.url)
        ctx.load(items)
        ctx.execute_query()
        output = pd.DataFrame()
        for index, item in enumerate(items):
            #print(item.properties)
            a = item.properties
            output = output.append(a, ignore_index=True)
            #print("{0}: {1}".format(index, item.properties['Color']))
        output.columns= output.columns.str.lower()
        output = output.loc[:,~output.columns.duplicated()]
        #del output['ID']
        #output.to_csv('data.csv',index=False)
        return output

    def sql_query(self,output,query):
        #q1 = """SELECT * FROM output where "Color" = 'Red'"""
        q1 = query
        d = self.cursor.execute(q1)
        for row in d:
            print(row)
  

    def return_list(self,query):
        ctx = self.connet_sharepoint(self.client_id,self.client_secret,self.url)
        ccc_list = ctx.web.lists.get_by_title(self.title)
        opt = self.enum_items(ccc_list)
        return self.sql_query(opt,query)
    
    


        
   


