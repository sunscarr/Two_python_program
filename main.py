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

# The way I wrote the second program was influenced by the first. The thought about writing the first program by just splitting the line and then getting the numbers to take the difference,
# but then I realized that some of the numbers had '*' in them so I decided to use regular expression to only take ints/floats digits from the lines. 
# My second program followed the same pattern where I only took digits using regular expression and found the difference. Therefore, it was influenced by the first.