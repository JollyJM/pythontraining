trainees = ["Jhon",[2,["James","Mary"]]]
print(trainees[1][1][0])
#3
trainees.append("56")
print(trainees)
#4
trainees_new = trainees[1][1]
trainees_new.insert(1,"Mike")
print(trainees)
#5
trainees[1][0] = 8
print(trainees)
#6
del trainees[0]
print(trainees)
#6
trainees_del = trainees[0][1]
del trainees_del[2]
print(trainees)
#7
print(len(trainees))
