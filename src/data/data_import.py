#Pour que python reconnaisse un dossier comme un module il faut ajouter en son sein un chicchier __init__.py 
#et également l'ajouter au PATH
import pandas as pd 
import sys

sys.path.insert(0, "/home/apprenant/Documents/simplon_dev/pyhon_sql/Foodflix")


#On peut ensuite importer le dossier comme un module

from src.utils.db_connect import db_connect, save_to_database, rename_cols 


# Connection with BDD version 1 (raw data lives there).

con = db_connect('./Data/raw_data/foodflix_v1.db')
cur = con.cursor()
cur.execute('pragma encoding=UTF8')


# Importing the data from the Data file

df = pd.read_csv('./Data/raw_data/foodflix_data.tsv', sep="\t")
df = df.sample(10000)

# Renaming all columns before stocking data into database

df.columns = rename_cols(df)


# Feeding the data into our first version database

save_to_database('./Data/raw_data/foodflix_v1.db','foodflix', df, False)
