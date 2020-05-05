
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob

def Eda():

    '''df=pd.read_csv('C://Users/Asus/Desktop/Datasets/covid_tweets.CSV')

    print(df.columns)

    print(df.shape)


    print(df.isnull().sum())


    #sns.heatmap(df.isnull())
    li=['country_code','place_type','place_full_name','reply_to_status_id', 'reply_to_user_id', 'reply_to_screen_name','account_lang']
    df.drop(li,inplace=True,axis=1)
    new_df=df
    print(new_df.isnull().sum())

    print(new_df.shape)

    #new_df['sentiment_df']=new_df['text'].apply(sentiments)
    #print(new_df['sentiment_df'][1])
    print(new_df.columns)'''

    senti_df=pd.read_csv('sentiments_data.csv')


    plt.show()

    positive=senti_df.sentiment_df.str.count('Positive').sum()
    negative = senti_df.sentiment_df.str.count('Negative').sum()
    neutral = senti_df.sentiment_df.str.count('Neutral').sum()

    labels = 'Positive', 'Negative', 'Neutral'
    sizes = [positive,negative,neutral]
    #only "explode" the 2nd slice (i.e. 'Hogs')





    fig1, ax1 = plt.subplots(1,2,squeeze=False)
    fig1.tight_layout()
    ax1[0,0].pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1[0,1].bar(labels,sizes,alpha=1)

    plt.show()




def sentiments(text):

    blob=TextBlob(text)
    if(blob.sentiment.polarity < 0):
        return "Negative"
    elif(blob.sentiment.polarity > 0):
        return "Positive"
    else:
        return ("Neutral")


    pass








if __name__ == '__main__':
    Eda()