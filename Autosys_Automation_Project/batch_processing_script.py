

account = ''

a = open("customer_ids.txt","r")

print(a)

c = a.count(str()) + 1
print(c)
a = a.replace("\n",'","')
q = '"'
new_customer_ids = q + a + q
print(a)


file = open("customer_ids.txt", "r")


#Inserts customer_ids into the query
sql_query = 'select * from TABLE where COLUMN in (QUERY);'
final_query = sql_query.replace("QUERY", new_customer_ids, 1)
print(final_query)
