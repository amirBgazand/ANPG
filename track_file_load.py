# love you :) :)
import csv

import matplotlib.pyplot as plt 

DELTA_TIMESTAMP_MS = 100  # similar throughout the whole dataset


class MotionState:
    def __init__(self, time_stamp_ms):
        self.time_stamp_ms = time_stamp_ms
        self.x = None
        self.y = None

class Track:
    def __init__(self, id):
        self.track_id = id
        self.time_stamp_ms_first = None
        self.time_stamp_ms_last = None
        self.motion_states = dict()



class Key:
    track_id = "track_id"
    frame_id = "frame_id"
    time_stamp_ms = "timestamp_ms"
    agent_type = "agent_type"
    x = "x"
    y = "y"
    vx = "vx"
    vy = "vy"
    psi_rad = "psi_rad"
    length = "length"
    width = "width"


class KeyEnum:
    track_id = 0
    frame_id = 1
    time_stamp_ms = 2
    agent_type = 3
    x = 4
    y = 5
    vx = 6
    vy = 7
    psi_rad = 8
    length = 9
    width = 10




def read_tracks(filename):

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        track_dict = dict()
        track_id = None
        path=list()
        pathforid=dict()

        for i, row in enumerate(list(csv_reader)):
            
            if i == 0:
                # check first line with key names
                assert(row[KeyEnum.track_id] == Key.track_id)
                assert(row[KeyEnum.frame_id] == Key.frame_id)
                assert(row[KeyEnum.time_stamp_ms] == Key.time_stamp_ms)
                assert(row[KeyEnum.agent_type] == Key.agent_type)
                assert(row[KeyEnum.x] == Key.x)
                assert(row[KeyEnum.y] == Key.y)
                assert(row[KeyEnum.vx] == Key.vx)
                assert(row[KeyEnum.vy] == Key.vy)
                assert(row[KeyEnum.psi_rad] == Key.psi_rad)
                assert(row[KeyEnum.length] == Key.length)
                assert(row[KeyEnum.width] == Key.width)
                continue

            if int(row[KeyEnum.track_id]) != track_id:
                # new track
                track_id = int(row[KeyEnum.track_id])
                track = Track(track_id)
                track.time_stamp_ms_first = int(row[KeyEnum.time_stamp_ms])
                track.time_stamp_ms_last = int(row[KeyEnum.time_stamp_ms])
                track_dict[track_id] = track
                path=[]

            track = track_dict[track_id]
            track.time_stamp_ms_last = int(row[KeyEnum.time_stamp_ms])
            ms = MotionState(int(row[KeyEnum.time_stamp_ms]))
            ms.x = float(row[KeyEnum.x])
            ms.y = float(row[KeyEnum.y])
            path.append((ms.x,ms.y))
            
            track.motion_states[ms.time_stamp_ms] = ms
            
            pathforid[track_id]=path

        return pathforid



path_id=read_tracks('recorded_trackfiles/DR_USA_Intersection_MA/vehicle_tracks_000.csv')


# x=[]
# y=[]

# for g in range (30,32):
#     try:
#         x=[]
#         y=[]
#         for i in range (len(path_id[g])):
#             x.append(path_id[g][i][0])
#             y.append(path_id[g][i][1])
#         plt.figure(g)
#         plt.plot(x,y, label=str(g))
#         plt.xlim([950, 1100])
#         plt.ylim([950, 1100]) 
#     except:
#         pass    
    
# plt.show()

L=[]
D=[]
R=[]
U=[]
L_U=[]
L_R=[]
L_D=[]
D_L=[]
D_U=[]
D_R=[]
R_U=[]
R_L=[]
R_D=[]
U_D=[]
U_R=[]
U_L=[]
nothing=[]


for id in list(path_id.keys()) :
    for item in path_id[id] :
        if 992<=item[0]<=997 and 997<=item[1]<=1006 :
            L.append(id)
            break
        if 1026<=item[0]<=1037 and 980<=item[1]<=988 :
            D.append(id)
            break
        if 1038<=item[0]<=1044 and 1006<=item[1]<=1012 :
            R.append(id)
            break
        if 1004<=item[0]<=1021 and 1011<=item[1]<=1026 :
            U.append(id)
            break
        else :
            continue
    else :
        nothing.append(id)


for id in L :
    for item in path_id[id]:
        if 1021<=item[0]<=1035 and 1012<=item[1]<=1021 :
            L_U.append(id)
            break
        if 1043<=item[0]<=1050 and 997<=item[1]<=1006 :
            L_R.append(id)
            break
        if 1005<=item[0]<=1016 and 980<=item[1]<=989 :
            L_D.append(id)
            break

for id in D :
    for item in path_id[id]:
        if 1021<=item[0]<=1035 and 1012<=item[1]<=1021 :
            D_U.append(id)
            break
        if 1043<=item[0]<=1050 and 997<=item[1]<=1006 :
            D_R.append(id)
            break
        if 988<=item[0]<=1000 and 1006<=item[1]<=1010 :
            D_L.append(id)
            break

for id in R :
    for item in path_id[id]:
        if 1021<=item[0]<=1035 and 1012<=item[1]<=1021 :
            R_U.append(id)
            break
        if 1005<=item[0]<=1016 and 980<=item[1]<=989 :
            R_D.append(id)
            break
        if 988<=item[0]<=1000 and 1006<=item[1]<=1010 :
            R_L.append(id)
            break

for id in U :
    for item in path_id[id]:
        if 1005<=item[0]<=1016 and 978<=item[1]<=988 :
            U_D.append(id)
            break
        if 1043<=item[0]<=1050 and 997<=item[1]<=1006 :
            U_R.append(id)
            break
        if 998<=item[0]<=1000 and 1006<=item[1]<=1010 : 
            U_L.append(id)

print(U_D)
print(U_R)
print(U_L)
print(L_U)
print(L_R)
print(L_D)
print(D_L)
print(D_U)
print(D_R)
print(R_D)
print(nothing)



x=[]
y=[]
plt.figure()
for id in U_D :
    for i in range(len(path_id[id])):
        x.append(path_id[id][i][0])
        y.append(path_id[id][i][1])
    plt.plot(x,y)
    plt.xlim([950, 1100])
    plt.ylim([950, 1100])
plt.show()




# import glob

# for file in glob.glob('D:\\1-UNIVERSITY\\2-Niusha_Project\\Intersection\\ANPG\\recorded_trackfiles\\DR_USA_Intersection_MA\\v*.csv'):
#     print(file)