import pandas as pd
import csvtomd 

df = pd.read_csv('en_stopwords.csv', dtype=str)

# Format Table File names as links:
df['file'] = "[" + df['name'] + "]" + "(en/" + df['file'] + ")"
df['source'] = "[" + " ⇱ " + "]" + "(" + df['source_url'] + ")"

# Subset of columns:
df = df[['file','size','source','description']] #.to_csv(index=False)

# Format table for csvtomd
table = list()
table.append(list([row for row in df.columns]))
table.extend(list([list(row)[1:] for row in df.itertuples()]))
print(csvtomd.md_table(table))
