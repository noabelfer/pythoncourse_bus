1.	Write a function that receives a directory path, searches there for csv files, 
    and if csv files exist - return the following data for each: filename, amount of columns, 
    amount of rows. You can assume that all the csv files are in the correct format.
Make sure you handle properly a case in which the provided path does not exist. In addition, 
    you should take into account that there can be inner folders with files and you should find 
    them all. Test your code with this folder.
Hint: check out os.walk function to iterate directory.
 
2.	Write a function that receives a csv file with AAPL stock prices between 1980 and 2022, 
    and creates a new csv file that stores average, max and min prices and volumes per year. 
    The new file should have the following columns:
Year,  Avg Price, Min Price, Max Price, Avg Volume, Min Volume, Max Volume
Hint: use csv.DictReader to easily access fields in a csv file.


