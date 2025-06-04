import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

my_email = 'wishtoinvest@gmail.com'
# password = 'technocrat$4'
password = 'xaepcteelgwppybw'
server = 'smtp.gmail.com'
port = 587

connection = smtplib.SMTP(server, port)
connection.ehlo()
connection.starttls()
connection.login(my_email, password)



STOCK_NAME_1 = "AAPL"
COMPANY_NAME_1 = "Apple Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
# STOCK_API_KEY = 'B4898TGPS3Z4D8G9'
STOCK_API_KEY = "VVU23NZ6JMH6LQCV"
NEWS_API_KEY = '3efa5392192a46f4a0e75ebab789e4cf'

STOCK_NAME = input('Enter a Stock Name Please: ')
COMPANY_NAME = input('Enter a Company Name Please: ')
if STOCK_NAME == 'APPL':
    STOCK_NAME = STOCK_NAME_1
    COMPANY_NAME = COMPANY_NAME_1

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def getStockNews():
    paramaters = {
        'function': 'TIME_SERIES_DAILY_ADJUSTED',
        'symbol': STOCK_NAME,
        'apikey': STOCK_API_KEY
    }

    response = requests.get(STOCK_ENDPOINT, params=paramaters)
    data = response.json()['Time Series (Daily)']
    data_list = [value for item,value in data.items()]
    ycp = float(data_list[0]['4. close'])
    dbyp = float(data_list[1]['4. close'])
    tdbtdbyp = float(data_list[2]['4. close'])
    print(ycp)
    print(dbyp)

    pd = round(abs(ycp - dbyp), 2)
    print(pd)

    #4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
    percent = round((pd/ycp) * 100, 3)
    print(f'{percent}%')
    # 5. - If TODO4 percentage is greater than 5 then print("Get News").
    if percent > 5:
        params = {
            'qIntitle': COMPANY_NAME,
            'apikey': NEWS_API_KEY,
        }
        r = requests.get(NEWS_ENDPOINT, params=params)
        articles = r.json()['articles']

    #7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
        top_3_articles = [articles[num] for num in range(0, 1)]
        print(top_3_articles)

        ## STEP 3: Use twilio.com/docs/sms/quickstart/python
        #to send a separate message with each article's title and description to your phone number. 

    #TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension. 

    if ycp - dbyp < 0:
        symbol = '🔻'
    else:
        symbol = '🔺'
        

    for article in top_3_articles:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = f'{STOCK_NAME}: {symbol}{percent}'
        msg["From"] = my_email
        msg["To"] = "wishtoinvest@gmail.com"
        msg.attach(MIMEText(f"\nHeadline: {article['title']}\nBreif Description{article['description']} \n\n", 'plain'))
        
        connection.sendmail(
            my_email, 
            'wishtoinvest@yahoo.com',
            msg.as_string()
            )


    connection.close()


getStockNews()


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

