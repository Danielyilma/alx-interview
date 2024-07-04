#!/usr/bin/python3
'''implementation for the lockbox question'''


def canUnlockAll(boxes):
    '''locked boxes'''
    if not boxes:
        return False

    keys = set(boxes[0])
    checked_boxes = set([0])
    total_boxes = len(boxes)

    while keys:
        key = keys.pop()
        if key < total_boxes and key not in checked_boxes:
            checked_boxes.add(key)
            keys.update(boxes[key])

    return len(checked_boxes) == total_boxes

# def canUnlockAll(boxes):
#     '''
#     It addes the first box keys to a set(keys) and for each keys, it checkes
#     there is a box that can open it and  then it addes the keys in the opened
#     box to the set(keys) and repeates the process until all boxes are opened
#     or there is no key left
#     '''
#     keys = set(boxes[0])
#     checked_box = [0]
#     box_len = len(boxes) - 1

#     while len(keys) and box_len:
#         key = next(iter(keys))
#         if key in checked_box:
#             keys.remove(key)
#             continue

#         if key < len(boxes):
#             keys.update((boxes[key]))
#             checked_box.append(key)
#             box_len -= 1
#         keys.remove(key)

#     return box_len == 0
