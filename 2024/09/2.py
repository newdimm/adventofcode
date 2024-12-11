#!/bin/python3
import sys

fname = "1.txt"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fname = sys.argv[1]
        
    
id = 0
disk = []
is_free_space = False

with open(fname) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        for l in line:
            n = int(l)
            if is_free_space:
                disk.append((-1, n))
            else:
                disk.append((id, n))
                id += 1
                
            is_free_space = not is_free_space
            
            
def print_disk(disk):
    str = ""
    for (id,len) in disk:
        if id == -1:
            str += "." * len
        else:
            str += ("%d"%id) * len
    
    print(str)
    
    
def update_queues(queues, position, length, tail):
    #print(queues)
    
    for q in queues:
        index = 0
        while index < len(q):
            if q[index] > tail:
                del q[index]
                continue
            elif q[index] >= position:
                q[index] += 1
            index += 1
            
        
    q = queues[length]
    index = 0
    while index < len(q):
        if q[index] >= position:
            break
        index += 1
    q.insert(index, position)
    
def rebuild_queues(queues, disk, tail):
    for i in range(len(queues)):
        queues[i] = []
        
    for index in range(tail + 1):
        file_id, file_len = disk[index]
    
        if file_id != -1:
            continue
        queues[file_len].append(index)

def get_min(queues, length):
    q_index = None
    head = None
    for index in range(length, len(queues)):
        if queues[index]:
            q_first = queues[index][0]
            if q_index is None or head > q_first: 
                q_index = index
                head = q_first
                
    if q_index is not None:
        return queues[q_index].pop(0)
    else:
        return -1
    
#print_disk(disk)

tail = len(disk) - 1

#print_disk(disk)
free_queues=[]
for i in range(10):
    free_queues.append([])

rebuild_queues(free_queues, disk, tail)

while tail > 0:
    file_id,file_len = disk[tail] 

    if file_id == -1:
        tail -= 1
        continue
    
    #print("placing [tail=%d]=(%d,%d)" % (tail, file_id, file_len))

    head = get_min(free_queues, file_len)
            
    if head < 0:
        #print("not found")
        #ignore=input("press enter")
        tail -= 1
        continue
        
    free_id,free_len = disk[head]
    
    if free_id != -1 or free_len < file_len:
        print("error!!! poped (%d, %d) for (%d, %d)" % (free_id, free_len, file_id, file_len))
        break
    
    for check in range(head):
        check_id, check_len = disk[check]
        if check_id == -1 and check_len >= file_len:
            print("error!!! poped [%d](%d, %d) for (%d, %d)" % (head, free_id, free_len, file_id, file_len))
            print("COULD not find [%d]=(%d,%d)" % (check, check_id, check_len))
    
    #print("found at [head=%d]=(%d,%d)" % (head, free_id, free_len))

    if free_len == file_len:
        disk[head] = (file_id, free_len)
        disk[tail] = (-1, file_len)
    else: # free_len > file_len:
        disk[tail] = (-1, file_len)
        disk[head] = (file_id, file_len)
        
        new_free_len = free_len - file_len
        disk.insert(head+1, (-1, new_free_len))
        
        #update_queues(free_queues, head + 1, new_free_len, tail - 1)
        rebuild_queues(free_queues, disk, tail)
    
    #print_disk(disk)
    #ignore=input("press enter")

print("do checksum")
    

csum = 0
position = 0
for file_id,file_len in disk:
    if file_id == -1:
        position += file_len
        continue
    while file_len:
        csum += position * file_id
        position += 1
        file_len -= 1
        
print("csum=%d" % csum)

            

