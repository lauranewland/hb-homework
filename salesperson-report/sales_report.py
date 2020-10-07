"""Generate sales report showing total melons each salesperson sold."""


salespeople = []
melons_sold = []

f = open('sales-report.txt')
for line in f: #loops through each line in the file
    line = line.rstrip() #strips out all all white space to the end of each line
    entries = line.split('|') #creates a list that is stored in entries that will be split by |

    salesperson = entries[0] #stores the word at zero index of each line
    melons = int(entries[2]) #takes the word at index 2 and converts it to an int and stores the value in melons

    if salesperson in salespeople: #loops through each Sales person and 
        position = salespeople.index(salesperson) #returns the position of the first occurances of the salesperson
        melons_sold[position] += melons # takes the number of melons sold at that position and addes it to melons 
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)


for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')


"""improvements would be to store everything in a dictionary. 
Key value would be the persons name and the value would be the number of melons. You would loop through to get the total number of melons"""
