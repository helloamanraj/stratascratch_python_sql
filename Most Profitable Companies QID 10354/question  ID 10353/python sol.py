# Import your libraries
import pandas as pd

# Start writing code
df  = pd.merge(worker, title, left_on = 'worker_id', right_on = 'worker_ref_id', how = 'inner')
df[df['salary'] == df['salary'].max()]['worker_title']