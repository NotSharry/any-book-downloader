from libgen_api import LibgenSearch

import pandas as pd
print('EBooK Downloaded by ShaRrY')
print('Assistant:/enter the name of Book you want to Download')

BookData = input("Book Name:> ")

print("Searching For Book "+BookData)

class Book():

    

 pd.set_option("max_colwidth", None)

 s = LibgenSearch()

 results = s.search_title(BookData)

 # As the above output will be in JSON format so create a dataframe for the results

 # use json_normalize to create a dataframe using JSON value

 ne_af = LibgenSearch()

 result_df = pd.json_normalize(results)

 pd.set_option("display.max_rows",result_df.shape[0]+1)

 result_df.head(2).T 

 print(result_df)

 item_to_download = results[0]

 download_links = ne_af.resolve_download_links(item_to_download)

 links = pd.json_normalize(download_links)

 links.T
print('copy the first link ')

 print(links.T)
time.sleep(20000)
Book()

for i in range(1):

 

 try:

  Book()

 except:

  print("Failed to extract data")
