## 0. Creating DataFrames
### Problem: Contact List(Locating Contacts)
- You are given a dictionary that contains names and numbers of people.
- You need to create a DataFrame from the dictionary and add an index to it, which should be the name values.
- Then take a name from user input and output the row in the DataFrame, which corresponds to that row.

## 1. Indexing & Slicing
### Problem: Numbers and Ranks(Ranking Board)
- You are given a DataFrame that includes the names and ranks of people
- You need to take a rank as input and output the corresponding column from the DataFrame as a Series
- Note that the rank is an integer, so you need to convert the user input to an integer

## 2. Reading Data
### Problem: Cases and Deaths(December 31, 2020)
- You are working with 'ca-covid' CSV file that contains the COVID-19 infection data in California for the year 2020
- The file provides data on daily cases and deaths for the entire year
- Find and output the row that corresponds to December 31, 2020
 
## 3. Working with Data
### Problem: Day of The Week(weekdays)
- You continue working with COVID dataset for California
- Now, add the weekday names for each row as a new colum, named 'weekday'
- Then, output the last 7 days data of the dataset
- Do not set any index on the DataFrame

## 4. Grouping
### Problem: Number of Cases(Worst day)
- Given the COVID data, find the day with maximum cases in a given month
- Take a month name as input and output the row that corresponds to the day with the maximum number of cases in that month
- The output should be a DataFrame, which includes all the columns
