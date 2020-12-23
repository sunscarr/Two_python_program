import re

def min_temp_spread(filename):
    smallest =10000
    with open(filename, 'r') as f:
        line = f.readline()
        while line!='':
            separation=(re.findall('[0-9]*\.?[0-9]+', line))
            if(len(separation)>10):
                minimum = (int(separation[1]) - int(separation[2]))
                if (minimum < smallest):
                    smallest = minimum
                    smallest_temp=separation[0]
            line=f.readline()
    print(smallest_temp)
            
def smallest_diff_goals(filename):
    smallest_difference=100000
    with open(filename, 'r') as f:
        line=f.readline()
        while line!="":
            separation=(re.findall('[0-9]+', line))
            if (len(separation)>7):
                minimum = abs(int(separation[-3]) - int(separation[-2]))
                if (minimum < smallest_difference):
                    smallest_difference = minimum
                    team=line.split()[1]

            line=f.readline()
    print(team)


min_temp_spread("w_data.dat")
smallest_diff_goals("soccer.dat")
