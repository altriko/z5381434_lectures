""" lec_avgs_example.py

Companion codes lecture
"""
import pandas as pd

# ----------------------------------------------------------------------------
#   The dates and prices lists
# ----------------------------------------------------------------------------
dates = [
  '2020-01-02',
  '2020-01-03',
  '2020-01-06',
  '2020-01-07',
  '2020-01-08',
  '2020-01-09',
  '2020-01-10',
  '2020-01-13',
  '2020-01-14',
  '2020-01-15',
  ]

# Close price
prices = [
  7.1600,
  7.1900,
  7.0000,
  7.1000,
  6.8600,
  6.9500,
  7.0000,
  7.0200,
  7.1100,
  7.0400,
  ]

# ----------------------------------------------------------------------------
#   Indexing using lists
# ----------------------------------------------------------------------------

# The `start` variable will hold the first index in the slice and the `end`
# variable will hold the last index in the slice. Remember that the `index`
# list method will return the position of the element in the list, starting at
# 0. In this case, `start` will be set to 2 and `end` will be set to 6.

# Remember to uncomment the statements below and complete the part with '?'
start  = dates.index('2020-01-06')
end  = dates.index('2020-01-10')
print(start, end)

# Now, slice the `prices` list.
# Remember that slices do not include endpoints
prcs_w1  = prices[start:end+1]

# Finally, calculate the average of the prices in the slice
avgprc  = sum(prcs_w1) / len(prcs_w1)
# print(avgprc)


# ----------------------------------------------------------------------------
#   Indexing using dictionaries
# ----------------------------------------------------------------------------
prc_dic = {
  '2020-01-02': 7.1600,
  '2020-01-03': 7.1900,
  '2020-01-06': 7.0000,
  '2020-01-07': 7.1000,
  '2020-01-08': 6.8600,
  '2020-01-09': 6.9500,
  '2020-01-10': 7.0000,
  '2020-01-13': 7.0200,
  '2020-01-14': 7.1100,
  '2020-01-15': 7.0400,
  }

# Get the price on '2020-01-13', in this case, 7.02
x  = prc_dic['2020-01-13']
# print(f'The price on 2020-01-13 is {x}')


# Try the following... it will not work because we cannot slice dictionaries
#prc_dic['2020-01-02':'2020-01-13']          # Raises Exception



# ----------------------------------------------------------------------------
#   Create a Series instance
# ----------------------------------------------------------------------------
# Create a series object
ser  = pd.Series(data = prices, index= dates)
print(ser)

# Select Qantas price on '2020-01-02' ($7.16) using ...
print(ser['2020-01-02'])
# ... the `prices` list
prc0  = '?'
#print(prc0)

# ... the `ser` series
prc1  = '?'
#print(prc1)

# ----------------------------------------------------------------------------
#   Slicing series
# ----------------------------------------------------------------------------
# Unlike dictionaries, you can slice a series
prcs  = '?'
#print(prcs)

# ----------------------------------------------------------------------------
#   Accessing the underlying array
# ----------------------------------------------------------------------------

# Use `.array` to get the underlying data array
ary  = '?'
#print(ary)

# Like any instance, you can get its type (i.e., the class used to create the
# instance)
#print(type(ser.array))

# Use the `index` attribute to get the index from a series
the_index  = '?'
#print(the_index)

# Like any instance, you can get its type (i.e., the class used to create the
# instance).
#print('The type of `the_index` is', type(the_index))

# ----------------------------------------------------------------------------
#   Changing the index by assignment
# ----------------------------------------------------------------------------

# The old index is:
#
# Index(['2020-01-02', '2020-01-03', '2020-01-06', '2020-01-07', '2020-01-08',
#    '2020-01-09', '2020-01-10', '2020-01-13', '2020-01-14', '2020-01-15'],
#   dtype='object')

# Replace the existing index with another with different values
# Note the -4 and 1000
#ser.index = [0, 1, 2, 3, -4, 5, 6, 7, 8, 1000]

# The new index is:
# Int64Index([0, 1, 2, 3, -4, 5, 6, 7, 8, 1000], dtype='int64')


# ----------------------------------------------------------------------------
#   Selecting obs using the new index
# ----------------------------------------------------------------------------
# Lets see how the series looks like
#print(ser)

# This will return 7.04
x  = '?'
#print(x)

# Compare the following cases:
# 1. This will return the element associated with the index label -4
#    (or 6.86)
#print(ser[-4])

# 2. This will return the fourth element from the end of the **list** `prices`
#    (or 7.00)
#print(prices[-4])