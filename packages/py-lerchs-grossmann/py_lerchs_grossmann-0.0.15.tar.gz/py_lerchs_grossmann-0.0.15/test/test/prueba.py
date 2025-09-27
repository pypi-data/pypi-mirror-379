import py_lerchs_grossmann as plg
import pandas as pd
import pyarrow as pa

df_y = pd.read_csv("test/test/ModeloRecursos_edit.csv", engine="pyarrow")

print(df_y.head())

# df_arc = build_df_arc(df_y_original=df_y, block_size=20)
# df_arc.to_csv("df_arc.csv", index=False)

df_arc = pd.read_csv("test/test/df_arc.csv", engine="pyarrow")
print(df_arc.head())
df = plg.main(df_y, df_arc, False)
df.to_csv("test/test/df_x_x_ModeloRecursos.csv", index=False)
