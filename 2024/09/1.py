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
    
    
print_disk(disk)

head = 0
tail = len(disk) - 1

while head < tail:
    free_id,free_len = disk[head]
    file_id,file_len = disk[tail] 

    if file_id == -1:
        tail -= 1
        continue
    if free_id != -1:
        head += 1
        continue
    
    print("todo: [head=%d]=%s , [tail=%d]=%s" % (head, disk[head], tail, disk[tail]))
    
    if free_len > file_len:
        disk[tail] = (-1, file_len)
        disk[head] = (-1, free_len-file_len)
        disk.insert(head,(file_id, file_len))
    elif free_len < file_len: ## free_len < file_len
        disk[head] = (file_id, free_len)
        disk[tail] = (file_id, file_len - free_len)
        disk.insert(tail+1, (-1, free_len))
    else: ## EQUAL
        disk[head] = (file_id, free_len)
        disk[tail] = (-1, file_len)
    
        
print_disk(disk)
    

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
        
            

