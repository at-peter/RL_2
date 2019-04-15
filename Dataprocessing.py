import pandas as pd
import numpy as np 
import seaborn as sns
from matplotlib import pyplot as plt


def loadDataframe(Filename):
    '''

    '''
    data = pd.read_csv(str(Filename))
    return data


if __name__ == "__main__":
    df = loadDataframe('average_reward_2_0.5_2_15')
    print(df.columns)
    df.plot()
    # sns.scatterplot(x =df.index , y =  data = df)]
    plt.show()
    pass