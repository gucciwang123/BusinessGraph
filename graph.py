import matplotlib.pyplot as plot

upper_bound = -1 #upper bound of values to be graphed; set to -1 to unbound
lower_bound = -1 #lower boundof values to be graphed; set to -1 to unbound
plot_limit = 500
plot_offset = 500

def deleteSegment(line): #input a char list
    while line[0] != '|' and len(line) >= 1:
        del line[0]
    del line[0]

def getSegment(line):
    string = ""
    i = 0
    while line[i] != '|' and len(line) > i:
        string += line[i]
        i += 1
    return string

file = open("file.txt", "r")

name = []
quanity = []

lines = file.readlines()
del lines[0]
del lines[-2]
del lines[-1]

file.close()

#parsing file
index = 1
for line in lines:
    line_list = list(line)
    deleteSegment(line_list)
    deleteSegment(line_list)

    name.append(str(index) + ":" + getSegment(line_list))
    index += 1

    deleteSegment(line_list)

    quanity.append(int(getSegment(line_list)))

#filtering data
indecies = []
#filter upper bound
for x in range(len(name)):
    if upper_bound == -1:
        break
    if quanity[x] >= upper_bound:
        indecies.append(x)

for index  in reversed(indecies):
    del name[index]
    del quanity[index]

#filter lower bound
for x in range(len(name)):
    if lower_bound == -1:
        break
    if quanity[x] <= lower_bound:
        indecies.append(x)

for index  in reversed(indecies):
    del name[index]
    del quanity[index]

print("Total points: " + str(len(name)))

if plot_offset >= len(name):
    print("Offset greater than size of filtered array.")
    exit(-1)
if plot_limit >= len(name) - plot_offset:
    plot_limit = len(name) - plot_offset

print("Plotted points: " + str(plot_limit))

print()
print("Starting plot")

#making plot
graph = plot.figure()
axis = graph.add_axes([0, 0, 1, 1])
axis.bar(name[plot_offset:plot_offset + plot_limit], quanity[plot_offset:plot_offset + plot_limit])
plot.show()

print("Ending plot")

