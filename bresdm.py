import pandas as pd

# 列出你的所有CSV文件，以及对应的年份
files_and_years = [
    ("https://raw.githubusercontent.com/ZoeyW99/bres/main/2007.csv", "2007"),
    ("https://raw.githubusercontent.com/ZoeyW99/bres/main/2008.csv", "2008"),
    ("https://raw.githubusercontent.com/ZoeyW99/bres/main/2009.csv", "2009"),
    ("https://raw.githubusercontent.com/ZoeyW99/bres/main/2010.csv", "2010"),
    ("https://raw.githubusercontent.com/ZoeyW99/bres/main/2011.csv", "2011"),
    ("https://raw.githubusercontent.com/ZoeyW99/bres/main/2012.csv", "2012"),
    ("https://raw.githubusercontent.com/ZoeyW99/bres/main/2013.csv", "2013"),
    ("https://raw.githubusercontent.com/ZoeyW99/bres/main/2014.csv", "2014"),
    ("https://raw.githubusercontent.com/ZoeyW99/bres/main/2015.csv", "2015"),
    ("https://raw.githubusercontent.com/ZoeyW99/bres/main/2016.csv", "2015"),
    ("https://raw.githubusercontent.com/ZoeyW99/bres/main/2017.csv", "2017"),
    ("https://raw.githubusercontent.com/ZoeyW99/bres/main/2018.csv", "2018"),

]

# 读取第一个CSV文件
df_all = pd.read_csv(files_and_years[0][0])

# 为了区分不同年份的数据，我们可以重命名数据列
for col in df_all.columns:
    if col not in ['Code']:  # We keep 'State' and 'County' columns the same
        df_all.rename(columns={col: col+'_'+files_and_years[0][1]}, inplace=True)

# 遍历剩余的文件和年份
for file, year in files_and_years[1:]:
    # 读取CSV文件
    df = pd.read_csv(file)
    
    # 重命名数据列
    for col in df.columns:
        if col not in ['Code']:
            df.rename(columns={col: col+'_'+year}, inplace=True)
    
    # 将这个数据框添加到总的数据框中
    df_all = pd.merge(df_all, df, on=['Code'])  # We merge on both 'State' and 'County'

# 保存合并后的数据到新的CSV文件
df_all.to_csv("/Users/zoeyw/Desktop/bres1.csv", index=False)