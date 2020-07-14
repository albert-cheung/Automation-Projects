#Purpose of this query is to take a large number of queries and parse them out into digestable chunks.

lines = []

#Strips a list of customer_ids pasted individually on the .txt file
with open("customer_ids.txt") as file:
    for line in file:
        line = line.strip()
        lines.append("'" + line + "'")

lines_length = len(lines)


#Adds bracket to the string
def addBracket(string):
     return ('(' + string + ')');

# Turns list array into a string
myString = ",".join(lines);


#Function halflist will add queries into a SQL Query if there are less than 500 queries in the "in" parameter.
#Otherwise it will continue to divide the list in half and run the queries again.
def halflist(list):
    list_length = len(list)
    if (list_length < 500):
        myString = ",".join(list)
        mySQLQuery = "select * from TABLE where COLUMN in (QUERY);"
        myQueries = addBracket(myString)
        myFinalQuery = mySQLQuery.replace("QUERY", str(myString), 1)
        print(myFinalQuery)
    else:
        half = len(list)//2
        return halflist(list[:half]), halflist(list[half:])




