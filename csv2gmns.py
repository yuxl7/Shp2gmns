import pandas as pd

link_csv_path = "results/link.csv"
node_csv_path = "results/node.csv"
mapping_csv_path = "cube_gmns_settings.csv"
link_gmns_csv_path = "results/link_gmns.csv"
node_gmns_csv_path = "results/node_gmns.csv"

link_df = pd.read_csv(link_csv_path)
node_df = pd.read_csv(node_csv_path)
mapping_df = pd.read_csv(mapping_csv_path)

link_mapping_df = mapping_df[mapping_df['section'].str.lower() == 'link']
node_mapping_df = mapping_df[mapping_df['section'].str.lower() == 'node']

link_mapping = dict(zip(link_mapping_df['csv_field_name'], link_mapping_df['gmns_field_name']))
node_mapping = dict(zip(node_mapping_df['csv_field_name'], node_mapping_df['gmns_field_name']))

link_df.rename(columns=link_mapping, inplace=True)
node_df.rename(columns=node_mapping, inplace=True)

link_gmns_columns = link_mapping_df['gmns_field_name'].tolist()
node_gmns_columns = node_mapping_df['gmns_field_name'].tolist()

for col in link_gmns_columns:
    if col not in link_df.columns:
        link_df[col] = None

for col in node_gmns_columns:
    if col not in node_df.columns:
        node_df[col] = None

link_df = link_df[link_gmns_columns]
node_df = node_df[node_gmns_columns]

link_df.to_csv(link_gmns_csv_path, index=False)
node_df.to_csv(node_gmns_csv_path, index=False)

print("GMNS 格式的 CSV 文件已成功生成。")