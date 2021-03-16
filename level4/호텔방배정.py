def Find(a, parent):
    c_list = [a]
    while a in parent.keys():
        a = parent[a]
        c_list.append(a)
    return a, c_list

def solution(k, room_number):
    room_info = {}
    
    answer = []
    for room in room_number:
        room -= 1
        room, c_list = Find(room,room_info)
        answer.append(room+1)
        
        next_room, _ = Find(room+1,room_info)
        for c in c_list:
            room_info[c] = next_room
        
    return answer
