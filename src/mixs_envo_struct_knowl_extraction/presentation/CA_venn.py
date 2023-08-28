import pandas as pd
from matplotlib import pyplot as plt
from matplotlib_venn import venn2


# a_var = "geo_loc_name"
# b_var = "lat_lon"

# Load the CSV data into a DataFrame
df = pd.read_csv('CA_geo_loc_name_vs_lat_lon.csv')

geo_loc_name_only = df[(df['geo_loc_name'] == True) & (df['lat_lon'] == False)].index
lat_lon_only = df[(df['geo_loc_name'] == False) & (df['lat_lon'] == True)].index
intersection = df[(df['geo_loc_name'] == True) & (df['lat_lon'] == True)].index

print(geo_loc_name_only)
print(lat_lon_only)
print(intersection)

geo_loc_name_only_len = len(geo_loc_name_only)
lat_lon_only_len = len(lat_lon_only)
intersection_len = len(intersection)

print(geo_loc_name_only_len)
print(lat_lon_only_len)
print(intersection_len)




# print(df)
# print(df.columns)
# print(df[a_var].value_counts(dropna=False))
# print(df[b_var].value_counts(dropna=False))
#
# a_true = df[df[a_var] == True].index
# b_true = df[df[b_var] == True].index
# a_false = df[df[a_var] == True].index
# b_false = df[df[b_var] == True].index
# # print(a_true)
# # print(type(a_true))
# # print(len(a_true))
# # print(b_true)
# # print(len(b_true))
# #
# # # Extract the sets of TRUE and FALSE values for columns "A" and "B"
# # true_in_A = set(df[df[a_var] == True].index)
# # true_in_B = set(df[df[b_var] == True].index)
# # false_in_A = set(df[df[a_var] == False].index)
# # false_in_B = set(df[df[b_var] == False].index)
# #
# # print(true_in_A)
#
# # Create the Venn diagram
# venn2(subsets=(
#     len(false_in_A - true_in_B),
#     len(false_in_B - true_in_A),
#     len(true_in_A & true_in_B)),
#     set_labels=(a_var, b_var)
# )

# venn2(subsets=(
# #     3, # As
# #     5, # Bs
# #     7), # intersection
# #     set_labels=("A", "B")
# # )

venn2(subsets=(
    geo_loc_name_only_len, # As
    lat_lon_only_len, # Bs
    intersection_len), # intersection
    set_labels=("'CA' or 'California'\nin geo_loc_name", "Shapefile analysis\nor geocoding of\nparsed lat_lon")
)

# Add title and display the Venn diagram
plt.title("Finding v6 Soil Biosamples from California")


plt.savefig('CA_v6_Soil_Biosamples.png', dpi=300, bbox_inches='tight')
plt.show()
