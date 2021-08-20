import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn')
#dates = [
   # datetime(2019, 5, 24),datetime(2019, 5, 25),datetime(2019, 5, 26),datetime(2019, 5, 27),datetime(2019, 5, 28),datetime(2019, 5, 29),datetime(2019, 5, 30)]

#y = [0, 1, 3, 4, 6, 5, 7]

#plt.plot(dates,y)

#plt.gcf().autofmt_xdate() #gcf=get current figure

#date_format=mpl_dates.DateFormatter('%b %d,%Y') #(month date year(caps for yyyy))
#plt.gca().xaxis.set_major_formatter(date_format)



data = pd.read_csv('data.csv')

data['Date'] = pd.to_datetime(data['Date']) #converting date column to date time in the data
data.sort_values('Date', inplace=True) #sorting data inplace=true inplies that it modifies the data

price_date = data['Date']
price_close = data['Close']

plt.plot_date(price_date, price_close, linestyle='solid')

plt.gcf().autofmt_xdate()

plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.tight_layout()

plt.show()
