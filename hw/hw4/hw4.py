#Quankang Wang,CIT590 HW4
#finished all by myself
#UID:54162826.

import csv
import math
from random import shuffle
import copy

def read_cities(file_name):
    reader = csv.reader(open(file_name,"r"), delimiter='\t')
    file_=[]
    for i in reader:
        file_.append((i[0],i[1],float(i[2]),float(i[3])))
    return file_

def print_cities(road_map):
    print("road_map:")
    for i in road_map:
        print(i[0],i[1],"%.2f %.2f"%(i[2],i[3]))

def compute_total_distance(road_map):
    sum= 0 
    for i in range(0,len(road_map)-1):
        sum+= math.sqrt((road_map[i][2]-road_map[i+1][2])**2+(road_map[i][3]-road_map[i+1][3])**2)
    sum+= math.sqrt((road_map[0][2]-road_map[len(road_map)-1][2])**2+(road_map[0][3]-road_map[len(road_map)-1][3])**2)
    return sum

def swap_cities(road_map, index1, index2):
    #print(road_map)
    new_road_map=road_map
    new_road_map[index1],new_road_map[index2]=road_map[index2],road_map[index1]
    return (road_map,compute_total_distance(new_road_map))#(new_road_map, new_total_distance)

def the_gradient(road_map):
    temp_list=[]
    for index1 in range(0,len(road_map)-1):
        for index2 in range(index1+1,len(road_map)):
            temp_dis= swap_cities(road_map,index1,index2)[1]
            temp_list.append([index1,index2,temp_dis])
    temp_list=sorted(temp_list,key=lambda x: x[2])
    if compute_total_distance(road_map) < temp_list[0][2]:
        return []
    else:
        return temp_list[0]

def find_best_cycle(road_map):
    for i in range(50):
        temp=the_gradient(road_map)
        if temp != []:
            road_map=swap_cities(road_map,the_gradient(road_map)[0],the_gradient(road_map)[1])[0]
        else:
            break
    return road_map

def print_map(road_map):
    for i in range(len(road_map)-1):
        print(road_map[i][0],road_map[i][1],"%.2f"%(math.sqrt((road_map[i][2]-road_map[i+1][2])**2+(road_map[i][3]-road_map[i+1][3])**2)))
    print("to the origin porint","%.2f"%(math.sqrt((road_map[0][2]-road_map[len(road_map)-1][2])**2+(road_map[len(road_map)-1][3]-road_map[0][3])**2)))
    print("total cost:",compute_total_distance(road_map))    

def main():
    road_map=read_cities('city-data.txt')
    #times = int(3) # times for do it 
    best_total=[]
    best_map=[]
    i_best=0
    i=0
    
    for i in range(3):
        shuffle(road_map)
        temp_map=find_best_cycle(road_map)
        temp_dis=compute_total_distance(temp_map)
        best_total.append(temp_dis)
        if best_total[i] <= min(best_total):
            best_map = temp_map
            i_best = i
    
    print("three cycles:",best_total,"\n============",i,"road map is shortes=========")
    print_map(best_map)
    # '''
    # shuffle(road_map)
    # print(compute_total_distance(find_best_cycle(road_map)))
    print(road_map)

'''
Reads in and prints out the city data. Repeat the following procedure 3 times: randomly
shuffle the starting city list and find the “best” cycle. After the three iterations, print the 
total distance of each of your three best cycles as well as the actual road_map that
achieved the shortest distance of the three.
'''

if __name__ == "__main__":
    main()
