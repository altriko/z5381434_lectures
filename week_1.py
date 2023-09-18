import yfinance

stock = "QAN.AX"
start = '2023-01-01'
end = None
df = yfinance.download(stock, start, end)
print(df)

