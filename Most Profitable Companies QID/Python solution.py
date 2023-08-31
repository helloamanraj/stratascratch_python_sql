# Import your libraries
import pandas as pd

# Start writing code
df = forbes_global_2010_2014
df[['company','profits']].sort_values('profits', ascending = False).head(3)