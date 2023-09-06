# Import your libraries
import pandas as pd

# Start writing code
df1 = airbnb_hosts
df2 = airbnb_guests
df = df1.merge(df2, on=['nationality', 'gender'])[['host_id', 'guest_id']].drop_duplicates()