def mean(data):
    full = 0
    for i in data:
        full += i
    return full/len(data)

def mathRange(data):
    return data[len(data)-1]-data[0]

def median(data):
    if len(data)//2 == len(data)/2: #if its an even number of variables
        middleNum = len(data)//2
        return (data[middleNum] + data[middleNum+1])/2
    else:
        return data[middleNum]

def mad(data):
    variablity = []
    average = mean(data)
    for i in data:
        variablity.append(abs(average-i))
    return mean(variablity)
    
def mode(data):
    max = 0
    answer = []
    for i in data:
        if data.count(i) > max:
            answer.clear()
            answer.append(i)
            max = data.count(i)
        elif data.count(i) == max:
            if not i in answer:
                answer.append(i)
    return answer

data = []
rawData = input("Enter the data set: ").split(',')
for i in rawData:
    try:
        data.append(int(i))
    except:
        data.append(float(i))
data.sort()
print(data)

while True:
    inp = input("mean, range, mode, median, mad: ")
    inp = inp.lower()
    if inp == 'mean':
        print(mean(data))
    elif inp == 'range':
        print(mathRange(data))
    elif inp == 'mode':
        print(mode(data))
    elif inp == 'median':
        print(median(data))
    elif inp == 'mad':
        print(mad(data))