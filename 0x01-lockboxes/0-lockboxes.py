#!/usr/bin/python3

def canUnlockAll(boxes):
    keys = set(boxes[0])
    checked_box = []
    box_len = len(boxes) - 1

    while len(keys) and box_len:
        key = next(iter(keys))
        if key in checked_box:
            keys.remove(key)
            continue

        if key < len(boxes):
            keys.update((boxes[key]))
            checked_box.append(key)
            box_len -= 1
            keys.remove(key)
    
    return box_len == 0
        

# print(canUnlockAll([[1], [2]]))