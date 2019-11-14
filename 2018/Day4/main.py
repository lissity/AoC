import datetime
import operator

def sort_input():
    file = open("input.txt", "r")
    list = []
    for line in file:
        ts = line[1:17]
        info = line[19:]
        tuple = (ts, info)
        list.append(tuple)
    list.sort(key=lambda tup: tup[0])
    file_sorted = open("sorted_input.txt", "w")
    for item in list:
        file_sorted.write(item[0] + ' ' + item[1])
    file_sorted.close()


#sort_input()

guards_sleep_time = dict()

file = open("Day4/sorted_input.txt", "r")
for line in file:
    current_command = line.split()[2]
    # Check who the current guard is and then move on to next line
    if current_command == "Guard":
        current_guard_id = line.split()[3]
        ts = line[0:16]
        last_ts = datetime.datetime.strptime(ts, "%Y-%m-%d %H:%M")
        if guards_sleep_time.get(current_guard_id) == None:
            guards_sleep_time[current_guard_id] = 0
    elif current_command == 'falls':
        current_ts = datetime.datetime.strptime(line[0:16], "%Y-%m-%d %H:%M")
        ts_delta = current_ts-last_ts
        wake_time = int(ts_delta.seconds/60)
        #print(wake_time)
        last_ts = current_ts
    elif current_command == 'wakes':
        current_ts = datetime.datetime.strptime(line[0:16], "%Y-%m-%d %H:%M")
        ts_delta = current_ts-last_ts
        sleep_time = int(ts_delta.seconds/60)
        #print("Sleep:" + str(sleep_time))
        guards_sleep_time[current_guard_id] += sleep_time
        last_ts = current_ts
file.close()

max_sleep = ("#-1", 0)
for x in guards_sleep_time:
    #print(str(x) + ": " + str(guards_sleep_time[x]))
    if guards_sleep_time[x] > max_sleep[1]:
        max_sleep = (x, guards_sleep_time[x])

print("Max sleep time: " + str(max_sleep))

# For Guard #3371
minutes = dict()
file = open("Day4/sorted_input.txt", "r")
mark_minutes = False
for line in file:
    current_command = line.split()[2]
    current_guard_id = line.split()[3]
    if(current_command=='Guard'):
        if (current_guard_id=='#3371'):
            mark_minutes = True
        else:
            mark_minutes = False
    elif(current_command == 'falls' and mark_minutes):
        last_ts = datetime.datetime.strptime(line[0:16], "%Y-%m-%d %H:%M")
    elif(current_command == 'wakes' and mark_minutes):
        current_ts = datetime.datetime.strptime(line[0:16], "%Y-%m-%d %H:%M")
        ts_delta = current_ts-last_ts
        #print(last_ts)
        #print(current_ts)
        sleep_time = int(ts_delta.seconds/60)
        #print(sleep_time)
        for i in range(last_ts.minute, current_ts.minute):
            if (minutes.get(i) == None):
                minutes[i] = 1;
            else:
                minutes[i] += 1;
file.close()
# Find the minute where Guard #3371 is asleep the most
print("Minute most asleep: " + str(max(minutes.items(), key=operator.itemgetter(1))[0]))

#For all guards:
file = open("Day4/sorted_input.txt", "r")
guard_dict = dict()
for line in file:
    current_command = line.split()[2]
    if(current_command=='Guard'):
        current_guard_id = line.split()[3]
        ts = line[0:16]
        last_ts = datetime.datetime.strptime(ts, "%Y-%m-%d %H:%M")
        if guard_dict.get(current_guard_id) == None:
            guard_dict[current_guard_id] = dict()
    elif(current_command == 'falls'):
        last_ts = datetime.datetime.strptime(line[0:16], "%Y-%m-%d %H:%M")
    elif(current_command == 'wakes'):
        current_ts = datetime.datetime.strptime(line[0:16], "%Y-%m-%d %H:%M")
        ts_delta = current_ts-last_ts
        sleep_time = int(ts_delta.seconds/60)
        for i in range(last_ts.minute, current_ts.minute):
            if (guard_dict[current_guard_id].get(i) == None):
                #minutes[i] = 1;
                guard_dict[current_guard_id][i] = 1;
            else:
                #minutes[i] += 1;
                guard_dict[current_guard_id][i] += 1;
new_dict = dict()
for x in guard_dict:
    #print(x + ': ' + str(guard_dict[x]))
    if(len(guard_dict[x]) != 0):
        #print(max(guard_dict[x].items(), key=operator.itemgetter(1))[0])
        new_dict[x] = max(guard_dict[x].items(), key=operator.itemgetter(1))[0]
#print(new_dict)
print('GuardID: ' + str(max(new_dict.items(), key=operator.itemgetter(1))[0]))
print('Minute: ' + str(new_dict['#1901']))
