import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data_company1 = pd.read_csv('AA Historical Data.csv')
data_company2 = pd.read_csv('GM Historical Data.csv')
data_company3 = pd.read_csv('MSFT Historical Data.csv')

plt.figure(figsize=(50, 15))
plt.subplot(3, 1, 1)
plt.plot(data_company1['Date'], data_company1['Price'], color='blue')
plt.title('Company 1 Stock Price')
plt.xlabel('Year')
plt.ylabel('Price')

plt.subplot(3, 1, 2)
plt.plot(data_company2['Date'], data_company2['Price'], color='blue')
plt.title('Company 2 Stock Price')
plt.xlabel('Year')
plt.ylabel('Price')

plt.subplot(3, 1, 3)
plt.plot(data_company3['Date'], data_company3['Price'], color='blue')
plt.title('Company 3 Stock Price')
plt.xlabel('Year')
plt.ylabel('Price')
plt.tight_layout()
plt.show()
