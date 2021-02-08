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





path_id=read_tracks('c:/arshad/final_project/dataset files/all mmb files/recorded_trackfiles/DR_USA_Intersection_MA/vehicle_tracks_000.csv')


x=[]
y=[]
for g in range (1,10):
    try:
        for i in range (len(path_id[g])):
            x.append(path_id[g][i][0])
            y.append(path_id[g][i][1])

        plt.plot(x,y)
        plt.xticks(range(950, 1100))  
        plt.yticks(range(950, 1060))  

        plt.show()
    except:
        pass    