#Stock
STOCK = "TSLA"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_key='API KEY'

#News
COMPANY_NAME = "Tesla Inc"
NEWS_ENDPOINT='https://newsapi.org/docs/endpoints/everything'
NEWS_API_key='NEWS_API_KEY'

#




## STEP 1: Use https://newsapi.org/docs/endpoints/everything
import  requests
parameters={
    'function':'TIME_SERIES_DAILY'
    ,'symbol':STOCK,
    'apikey':STOCK_API_key
}
connection=requests.get(url=STOCK_ENDPOINT,params=parameters)
connection.raise_for_status()
data=connection.json()['Time Series (Daily)']

print(data)
#Yesterday
price_list=[price for price in data.values()]
yesterday=price_list[0]
yesterdays_closing_price=yesterday['4. close']

#Day Before Yesterday
day_before_yesterday=price_list[1]
day_before_yesterdays_closing_price=day_before_yesterday['4. close']


#Gap between them
diff=abs(float(yesterdays_closing_price)-float(day_before_yesterdays_closing_price))
if float(yesterdays_closing_price)>float(day_before_yesterdays_closing_price):
    sign="🔺"
else:
    sign="🔻"



#Percantage difference
percentage=(diff/float(yesterdays_closing_price))*100

#Get News
if percentage>5:
    ## STEP 2: Use https://newsapi.org/docs/endpoints/everything
    parameter = {
        'apikey': NEWS_API_key,
        'qInTitle': COMPANY_NAME
    }
    news = requests.get(url='https://newsapi.org/v2/everything', params=parameter)
    all_news = news.json()['articles']
    articles = all_news[0:3]

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    from twilio.rest import Client

    account_sid = 'account_sid'
    auth_token = 'auth_token'
    client = Client(account_sid, auth_token)
    for i in articles:
        message = client.messages.create(
            from_='+12185795372',
            body=f'{STOCK}-{percentage}{sign}\n{i['title']}\n{i['description']}',
            to='+48572629341'
        )
        print(message.status)
        print(message.sid)












