'''
RAMPER
R - restate the problem
    there are n size array to represent miles 
    postiion and speed
        - a car cannot pass another car 
        - it can catch up and stay at the pace of the slowest speed
        - car fleet: single car or group of cars driving next to eachother
    if a car catches up to mile target that car or car fleets needs to be tracked and returned as the awsner 
A - ask any questions 
    how do we know when to add a car to our car fleet
    i'm thinking of using realy miles / hour to track 
    when we get to target but i feel that is overcomplication the solution
M - make an example 
    t = 12
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]
    walk thourgh solutin in head
P - pick a pattern
    tuple / stack ?
E - explain the plan
    traverse the cars 
    set the miles per hours per element in size n array
    10/2 = 5 
    so every second increament 5 miles per position 
    repeat this process and sort them in groups 
    when they overlap at any point? 

'''
def carFleet(target, position,speed):
    milesPerHour = []
    stack = []
    for p,s in zip(position,speed):
        milesPerHour.append((p,s))
milesPerHour = sorted(milesPerHour, key=lambda car: car[0], reverse=True)
    for pos,spd in milesPerHour:
        distance = (target - pos)
        time = (distance / spd)
        if not stack:
            stack.append(time)
        elif time > stack[-1]:
            stack.append(time)
        # or nothing 
        #else:
            #continue 
    return len(stack)

