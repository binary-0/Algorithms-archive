numMeeting = int(input())

meetingList = []
curTime = 0
cnt = 0

for i in range(numMeeting):
    startEndList = list(map(int, input().split()))
    meetingList.append(startEndList)
    
meetingList.sort(key=lambda x: (x[1], x[0]))

for meeting in meetingList:
    if meeting[0] >= curTime:
        #start the meeting
        curTime = meeting[1]
        cnt += 1

print(cnt)