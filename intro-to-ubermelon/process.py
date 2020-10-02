log_file = open("um-server-01.txt")


def sales_reports(log_file): #defines the sales_report function
    for line in log_file: #we are going to loop over each line within the text file
        line = line.rstrip() #takes each line and strips out the training chars
        day = line[0:3] #day will store the the chars that reside at index 0-3
        if day == "Mon": #We are looking for all instances where day has the value "Mon" stored
            print(line) #this will print all lines within the logfile that contain "Mon"


sales_reports(log_file)
