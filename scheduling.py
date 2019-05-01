import statistics as STAT

class RoundRobin:

    wait = [0]
    duration = [0]
    turnAroundT = [0]
    length = 0
    arrivalTime = []
    quanta = 2
    jobID = []

    def __init__(self, jobID, duration, arrivalTime):
        self.jobID = jobID
        self.duration = duration
        self.length = len(duration)
        self.wait = [0]*self.length
        self.turnAroundT = [0]*self.length
        self.arrivalTime = arrivalTime

        
    def findWaitingTime (self):
        cpy_duration = []
        
        for val in range(self.length):
            cpy_duration[val] = self.duration[val]
            
        time = 0
        while True:
            done = True
            
            for val in range(self.length):
                if cpy_duration[val] > 0:
                    done = False
                    if cpy_duration[val] > quanta:
                        time += quanta
                        cpy_duration[val] -= quanta
                else:
                    time = time + cpy_duration[val]
                    self.wait[val] = time - self.duration[val]
                    cpy_duration[val] = 0
            if done is True:
                break
            
    
        
    def findTurnAroundTime (self):
        for val in range(self.length):
            self.turnAroundT[val] = self.duration[val] + self.wait[val]
            


    def findAvgTime(self, process, n, burst, quanta):
        
        totalWait = 0
        totalTurnAroundTime = 0
        
        self.findWaitingTime(process, n, burst, wait, quanta)
        self.findTurnAroundTime(process, n, burst, wait, turnAroundT)
        print("Job ID \t\t Duration \t Arrival Time \t\t Waiting", 
		"Time \t Turn-Around Time \t Completion Time \n") 
        
      
        for i in range(self.length):

            totalWait += self.wait[i]
            totalTurnAroundTime += self.turnAroundT[i]
            completionTime = self.turnAroundT[i] + arrivalTime[i]

            print(" ", i + 1, "\t\t", self.duration[i], "\t\t", self.arrivalTime[i], 
			"\t\t", self.wait[i], "\t\t ", self.turnAroundT[i], "\t\t ", completionTime)
            
        print("Average Waiting Time = ", totalWait/n)
        print("Average turn around time = ", totalTurnAroundTime/n)

class FIFO:

    wait = [0]
    duration = [0]
    turnAroundT = [0]
    length = 0
    arrivalTime = []
    jobID = []

    def __init__(self, jobID, duration, arrivalTime):
        self.jobID = jobID
        self.duration = duration
        self.length = len(duration)
        self.wait = [0]*self.length
        self.turnAroundT = [0]*self.length
        self.arrivalTime = arrivalTime

    def findWaitingTime(self):

        buffer_time = [0] * self.length
        for i in range(1, self.length):
            buffer_time[i] = buffer_time[i - 1] + self.duration[i - 1]
            self.wait[i] = buffer_time[i - 1] + self.arrivalTime[i - 1]
            if self.wait[i] < 0:
                self.wait[i] = 0
    		
    def findTurnAroundTime(self):
    	for val in range(self.length):
        	self.turnAroundT[val] = self.duration[val] + self.wait[val]
    	
    def findAvgTime(self):

    	self.findWaitingTime()
    	self.findTurnAroundTime()    	
    	print("Job ID \t\t Duration \t Arrival Time \t\t Waiting", 
		"Time \t Turn-Around Time \t Completion Time \n") 
        for i in range(self.length):

            totalWait += self.wait[i]
            totalTurnAroundTime += self.turnAroundT[i]
            completionTime = self.turnAroundT[i] + arrivalTime[i]

            print(" ", i + 1, "\t\t", self.duration[i], "\t\t", self.arrivalTime[i], 
			"\t\t", self.wait[i], "\t\t ", self.turnAroundT[i], "\t\t ", completionTime)
            print("FIFO: Processes Burst time Waiting time Turn around time\nAverage waiting time: ", STAT.mean(self.wait), "\nAverage turn around time: ", STAT.mean(self.turnAroundT))


class SJF: 

    jobID = [0]
    arrivalTime = [0]
    wait = [0]
    duration = [0]
    turnAroundT = [0]
    length = 0
    
    

    def __init__(self, jobID, duration, arrivalTime):
        processInfo = {}
        processInfo_order = {}
        jobID_order = []
        duration_order = []
        arrivalTime_order = []


        for i in range(len(duration)):
            processInfo[duration[i]] = [jobID[i], arrivalTime[i]]

        median = sorted(list(processInfo.keys()))
        for val in median:
            processInfo_order[val] = processInfo[val]

        #print("Sorted: ", processInfo_order)
        duration_order = list(processInfo_order.keys())
        for val in list(processInfo_order.values()):
            jobID_order.append(val[0])
            arrivalTime_order.append(val[1])


        self.jobID = jobID_order
        self.duration = duration_order
        self.length = len(duration_order)
        self.wait = [0]*self.length
        self.turnAroundT = [0]*self.length
        self.arrivalTime = arrivalTime_order
        

    #remember, you need to sort the list
    def findWaitingTime(self):
        buffer_time = [0] * self.length
        for i in range(1, self.length):
            buffer_time[i] = buffer_time[i - 1] + self.duration[i - 1]
            self.wait[i] = buffer_time[i - 1] + self.arrivalTime[i - 1]
            if self.wait[i] < 0:
                self.wait[i] = 0

    def findTurnAroundTime(self):
        for i in range(self.length):
            self.turnAroundT[i] = duration[i] + self.wait[i]

    def findAvgTime(self):
        totalWait = 0
        totalTurnAroundTime = 0
        self.findWaitingTime()
        self.findTurnAroundTime()
        print("Job ID \t\t Duration \t Arrival Time \t\t Waiting", 
		"Time \t Turn-Around Time \t Completion Time \n") 
        for i in range(self.length):

            totalWait += self.wait[i]
            totalTurnAroundTime += self.turnAroundT[i]
            completionTime = self.turnAroundT[i] + arrivalTime[i]

            print(" ", i + 1, "\t\t", self.duration[i], "\t\t", self.arrivalTime[i], 
			"\t\t", self.wait[i], "\t\t ", self.turnAroundT[i], "\t\t ", completionTime)

        print("SJF: Processes Burst time Waiting time Turn around time")
        print("Average waiting time: ", STAT.mean(self.wait))
        print("Average turn around time: ", STAT.mean(self.turnAroundT))

class BJF:

    jobID = [0]
    arrivalTime = [0]
    wait = [0]
    duration = [0]
    turnAroundT = [0]
    length = 0
    
    

    def __init__(self, jobID, duration, arrivalTime):
        processInfo = {}
        processInfo_order = {}
        jobID_order = []
        duration_order = []
        arrivalTime_order = []


        for i in range(len(duration)):
            processInfo[duration[i]] = [jobID[i], arrivalTime[i]]

        median = sorted(list(processInfo.keys()), reverse=True)
        for val in median:
            processInfo_order[val] = processInfo[val]

        #print("Sorted: ", processInfo_order)
        duration_order = list(processInfo_order.keys())
        for val in list(processInfo_order.values()):
            jobID_order.append(val[0])
            arrivalTime_order.append(val[1])


        self.jobID = jobID_order
        self.duration = duration_order
        self.length = len(duration_order)
        self.wait = [0]*self.length
        self.turnAroundT = [0]*self.length
        self.arrivalTime = arrivalTime_order
        

    #remember, you need to sort the list
    def findWaitingTime(self):
        buffer_time = [0] * self.length
        for i in range(1, self.length):
            buffer_time[i] = buffer_time[i - 1] + self.duration[i - 1]
            self.wait[i] = buffer_time[i - 1] + self.arrivalTime[i - 1]
            if self.wait[i] < 0:
                self.wait[i] = 0

    def findTurnAroundTime(self):
        for i in range(self.length):
            self.turnAroundT[i] = duration[i] + self.wait[i]

    def findAvgTime(self):
        totalWait = 0
        totalTurnAroundTime = 0
        self.findWaitingTime()
        self.findTurnAroundTime()
        print("Job ID \t\t Duration \t Arrival Time \t\t Waiting", 
		"Time \t Turn-Around Time \t Completion Time \n") 
        for i in range(self.length):

            totalWait += self.wait[i]
            totalTurnAroundTime += self.turnAroundT[i]
            completionTime = self.turnAroundT[i] + arrivalTime[i]

            print(" ", i + 1, "\t\t", self.duration[i], "\t\t", self.arrivalTime[i], 
			"\t\t", self.wait[i], "\t\t ", self.turnAroundT[i], "\t\t ", completionTime)

        print("SJF: Processes Burst time Waiting time Turn around time")
        print("Average waiting time: ", STAT.mean(self.wait))
        print("Average turn around time: ", STAT.mean(self.turnAroundT))

class STCF:

    jobID = [0]
    arrivalTime = [0]
    wait = [0]
    duration = [0]
    turnAroundT = [0]
    length = 0
    
    def __init__(self, jobID, duration, arrivalTime):
        processInfo = {}
        processInfo_order = {}
        jobID_order = []
        duration_order = []
        arrivalTime_order = []


        for i in range(len(duration)):
            processInfo[duration[i]] = [jobID[i], arrivalTime[i]]

        median = sorted(list(processInfo.keys()))
        for val in median:
            processInfo_order[val] = processInfo[val]

        #print("Sorted: ", processInfo_order)
        duration_order = list(processInfo_order.keys())
        for val in list(processInfo_order.values()):
            jobID_order.append(val[0])
            arrivalTime_order.append(val[1])


        self.jobID = jobID_order
        self.duration = duration_order
        self.length = len(duration_order)
        self.wait = [0]*self.length
        self.turnAroundT = [0]*self.length
        self.arrivalTime = arrivalTime_order
        

    #remember, you need to sort the list
    def findWaitingTime(self):
        #self.wait[0] = 0
        '''
        for i in range(1, self.length):
            self.wait[i] = duration[i - 1] + self.wait[i - 1]
        '''
        temp = []
        INT_MAX = 999999999
        temp = self.duration
        complete, time, min, shortest, finish_time, check, = 0, 0, INT_MAX, 0, None, False
        while complete is not self.length:
            for j in range(self.length):
                if self.arrivalTime[j] <= time and temp[j] < min and temp[j] > 0:
                    min = temp[j]
                    shortest = j
                    check = True
            if check is False:
                time += 1
                continue
            
            temp[shortest] -= 1


            min = temp[shortest]
            if min is 0:
                min = INT_MAX

            if temp[shortest] is 0:
                complete += 1
                check = False
                finish_time = time + 1

                self.wait[shortest] = finish_time - duration[shortest] - arrivalTime[shortest]
                if self.wait[shortest] < 0:
                    self.wait[shortest] = 0
            
            time += 1
            
    def findTurnAroundTime(self):
        for i in range(self.length):
            self.turnAroundT[i] = duration[i] + self.wait[i]

    def findAvgTime(self):
        self.findWaitingTime()
        self.findTurnAroundTime()
        print("Job ID \t\t Duration \t Arrival Time \t\t Waiting", 
		"Time \t Turn-Around Time \t Completion Time \n") 
        for i in range(self.length):

            totalWait += self.wait[i]
            totalTurnAroundTime += self.turnAroundT[i]
            completionTime = self.turnAroundT[i] + arrivalTime[i]

            print(" ", i + 1, "\t\t", self.duration[i], "\t\t", self.arrivalTime[i], 
			"\t\t", self.wait[i], "\t\t ", self.turnAroundT[i], "\t\t ", completionTime)
        print("SJF: Processes Burst time Waiting time Turn around time")
        print("Average waiting time: ", STAT.mean(self.wait))
        print("Average turn around time: ", STAT.mean(self.turnAroundT))

def readFile(file):
    jobID = []
    arrivalTime = []
    duration = []
    f = open(file, "r")

    lines = iter(f.readlines())
    while True:
        try:
            line = next(lines).split('\t')
            if len(line) is 3:
                jobID.append(line[0])
                arrivalTime.append(line[1])
                duration.append(line[2].rstrip())
            else:
                print("More than 3 inputs in line! Please check file input!", line)
                exit()
            " do something with line"
        except StopIteration:
            break

    '''print("Job ID: ", jobID)
    print("Arrival Time: ", arrivalTime)
    print("Duration: ", duration)'''
    return [jobID, duration, arrivalTime]


jobID, duration, arrivalTime = readFile("/home/gauravkuppa24/jobs.dat")
jobID = list(map(int, jobID))
duration = list(map(int, duration))
arrivalTime = list(map(int, arrivalTime))



sjf = SJF(jobID, duration, arrivalTime)
sjf.findAvgTime()

      
		


