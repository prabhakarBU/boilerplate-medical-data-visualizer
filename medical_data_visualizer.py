import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
bmi = (df['weight'])/((df['height']/100)**2)
#df['bmi'] = bmi;
df['overweight'] = np.where(bmi >= 25, 1, 0)

# 3
df['cholesterol'] = np.where(df['cholesterol'] > 1, 1, 0)
df['gluc'] = np.where(df['gluc'] > 1, 1, 0)


# 4
def draw_cat_plot():
    # 5
    df_cat = pd.DataFrame(data=pd.melt(df,id_vars='cardio',value_vars=['active','alco','cholesterol', 'gluc','overweight','smoke'  ]))
    
    # 6
    df_cat["total"] = 0
    df_cat = df_cat.groupby(["cardio", "variable", "value"])["total"].count().reset_index(name="total")
    
    # 7
    plot = sns.catplot(data=df_cat, kind="bar", x="variable", y="total", hue="value", col="cardio")
    plot.set_ylabels('total')
    
    # 8 
    fig = plot.fig


    # 9
    fig.savefig('catplot.png')
    return fig

# 10
def draw_heat_map():
    # 11
    df_heat = df.loc[(df['ap_lo'] <= df['ap_hi']) & 
                     (df['height'] >= df['height'].quantile(0.025)) & 
                     (df['height'] <= df['height'].quantile(0.975)) & 
                     (df['weight'] >= df['weight'].quantile(0.025)) & 
                     (df['weight'] <= df['weight'].quantile(0.975))]
    # 12
    corr = df_heat.corr()
    # 13
    mask = np.triu(corr)
    # 14
    fig, ax = plt.subplots(figsize=(16,9))
    # 15
    sns.heatmap(data=corr, mask=mask, annot=True, center=0, vmin=-0.12, vmax=0.28, fmt='0.1f', linewidths=0.2)


    # 16
    fig.savefig('heatmap.png')
    return fig