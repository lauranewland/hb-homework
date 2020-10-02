def file_parser(day,file_name):  #Defines the function
    print(day) #prints out the day being passed in
    the_file = open(file_name) #assigns open(file_name) to the variable the_file
    for line in the_file: #iterates over each line whithin the file 
        line = line.rstrip() #strips out any garbage at the end of each line
        words = line.split('|') #each line will be slit at the delimiter '|' creating a list that will be stored in the variable word 

        melon = words[0] #the element stored at index 0 will be assigned to the variable melon
        count = words[1]
        amount = words[2]

        print("Delivered {} {}s for total of ${}".format(count, melon, amount)) #prints out each line with the count, melon and amount
    the_file.close()


delivery_files = [['Day 1', 'um-deliveries-20140519.txt'], ['Day 2', 'um-deliveries-20140520.txt'], ['Day 3', 'um-deliveries-20140521.txt']]
for entry in delivery_files: #itirates over delivery files list
    file_parser(entry[0], entry[1]) #passes the elemets within each list into the file parser function 
    # file_parser(*entry) - esentually does what line 18 is doing however it automagically unpacks the list and passes in each vaule into the function
