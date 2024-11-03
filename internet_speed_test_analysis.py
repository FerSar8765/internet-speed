import pandas as pd
from ydata_profiling import ProfileReport

# df = pd.read_excel("results2024-10-24-1538.xlsx")

# df.info()
# print(df.describe())

# df = df.set_index("Date-time")

# df = df.drop(columns = ["Unnamed: 0"])

# print(df)

# print(f"The mean of Download Speed is {df["Download (Mb/s)"].mean():.2f} Mb/sec \n")    
# print(f"The mean of Upload Speed is {df["Upload (Mb/s)"].mean():.2f} Mb/sec\n")

# print(f"The median of Download Speed is {df["Download (Mb/s)"].median():.2f} Mb/sec \n")    
# print(f"The median of Upload Speed is {df["Upload (Mb/s)"].median():.2f} Mb/sec\n")

# print(f"The maximum of Download Speed is {df["Download (Mb/s)"].max():.2f} Mb/sec \n")    
# print(f"The maximum of Upload Speed is {df["Upload (Mb/s)"].max():.2f} Mb/sec\n")

# print(f"The minimum of Download Speed is {df["Download (Mb/s)"].min():.2f} Mb/sec \n")    
# print(f"The minimum of Upload Speed is {df["Upload (Mb/s)"].min():.2f} Mb/sec\n")

# print(df.sort_values(by = ["Upload (Mb/s)"], ascending=False))
# print(df.sort_values(by = ["Upload (Mb/s)"]))

# download_mean_value = df["Download (Mb/s)"].mean()
# mask = df["Download (Mb/s)"] > download_mean_value
# masked_df = df[mask]
# print(masked_df["Download (Mb/s)"])


# ...................................................................................................................
#                                  Group Results Analysis - for Presentation Assignment
# ...................................................................................................................

group_results_df = pd.read_excel("group_results.xlsx")
# profile = ProfileReport(group_results_df, title = "Internet Speed Report")
# profile.to_file('internet_speeds_teat.html')

# print(group_results_df.describe())

# .......................................... Download Speed ....................................................
# print("\nThe five statistic figure for Mean Download column are:\n")
# download_mean_df = group_results_df["Mean Download"] # isolating column "Mean Download" for using .describe()
# print(download_mean_df.describe()) # for calculating the statistic figures only on the column "Mean Download"


# The five statistic figure for Mean Download column are:

# count      9.000000
# mean      45.256322
# std       36.726081
# min        8.920000
# 25%       23.503100
# 50%       36.760000
# 75%       64.520000
# max      124.310000

print(f"\nThe lower_limit in mean download speeds equals to {23.5031 - (1.5 * (64.52 - 23.5031))} and minimum = 8.92\n")
print(f"The lower_limit in mean download speeds equals to {64.52 + (1.5 * (64.52 - 23.5031))} and maximum = 124.31\n")


# print(f"\nThe mean value among mean download speeds is {group_results_df["Mean Download"].mean():.2f} Mb/s")
# print(f"The median value among mean download speeds is {group_results_df["Mean Download"].median():.2f} Mb/s")
# print(f"The minimum value among mean download speeds is {group_results_df["Mean Download"].min():.2f} Mb/s")
# print(f"The maximum value among mean download speeds is {group_results_df["Mean Download"].max():.2f} Mb/s")
# print(f"The range vlue among mean download speeds is {(group_results_df["Mean Download"].max() - group_results_df["Mean Download"].min()):.2f} Mb/s\n")


# Calculating Lower and Upper limits for Group Mean Download Speeds


# Percentage Calculation for better comparison with national download speed
# def percent_function2(x):
#     return (x - 75) * 100 / 75

# group_results_df['Mean Download'] = group_results_df['Mean Download'].apply(percent_function2)
# download_mean_percent_df =  group_results_df['Mean Download']
# download_mean_percent_df.to_excel("download_mean_percent.xlsx")


# .......................... Upload Speed ..........................................
# upload_mean_df = group_results_df["Mean Upload"] # isolating column "Mean Upload" for using .describe()
# print("\nThe five statistic figure for Mean Upload column are:\n")
# print(upload_mean_df.describe()) # for calculating the statistic figures only on the column "Mean Upload"

# The five statistic figure for Mean Upload column are:

# count     9.000000
# mean     11.560689
# std       7.472080
# min       0.710000
# 25%       6.580200
# 50%      10.330000
# 75%      18.470000
# max      22.580000

print(f"\nThe lower_limit in mean upload speeds equals to {6.58 - (1.5 * (18.47 - 6.58))} and minimum = 0.71\n")
print(f"The lower_limit in mean upload speeds equals to {18.47 + (1.5 * (18.47 - 6.58))} and maximum = 22.58\n")


# print(f"\nThe mean value among mean upload speeds is {group_results_df["Mean Upload"].mean():.2f} Mb/s")
# print(f"The median value among mean upload speeds is {group_results_df["Mean Upload"].median():.2f} Mb/s")
# print(f"The minimum value among mean upload speeds is {group_results_df["Mean Upload"].min():.2f} Mb/s")
# print(f"The maximum value among mean upload speeds is {group_results_df["Mean Upload"].max():.2f} Mb/s")
# print(f"The range vlue among mean upload speeds is {(group_results_df["Mean Upload"].max() - group_results_df["Mean Upload"].min()):.2f} Mb/s\n")


# Percentage Calculation for better comparison with national upload speed
# def percent_function(x):
#     return (x - 15) * 100 / 15

# group_results_df['Mean Upload'] = group_results_df['Mean Upload'].apply(percent_function)
# upload_mean_percent_df =  group_results_df['Mean Upload']
# upload_mean_percent_df.to_excel("upload_mean_percent.xlsx")


