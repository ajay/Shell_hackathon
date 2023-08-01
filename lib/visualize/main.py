import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt



def load_data():
    df = pd.read_csv('dataset/Biomass_History.csv')
    return df
def visualize_data(data):
    for year in ['2010','2011','2012','2013','2014','2015','2016','2017']:
        visualize_data_of_year(data,year)

def visualize_data_of_year(data,year):
    print(year)
    sns.set(style="whitegrid")
    plt.stackplot(data["Index"],data[year],labels=['Biomass'],colors=['#FF0000'])
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Biomass Distribution for ' + year) 
    plt.savefig('dataset/' + "biomass-history-"+ year + '.png',dpi=1000)
    plt.show()
    plt.clf()




if(__name__ == '__main__'):
    data = load_data()
    df=pd.DataFrame(data)
    print(df)
    visualize_data(df)