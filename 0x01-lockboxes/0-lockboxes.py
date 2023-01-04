#!/usr/bin/python3
'''LockBoxes Challenge'''


def canUnlockAll(boxes):
    # Set up a set to track which boxes we have keys for
    keys = set()
    keys.add(0)
    
    # Set up a list to track the boxes we need to search for keys
    queue = [0]
    
    # While there are boxes in the queue
    while queue:
        # Take a box from the front of the queue
        box = queue.pop(0)
        
        # For each key in the current box
        for key in boxes[box]:
            # If the key is a valid box and we don't have a key for it yet
            if 0 <= key < len(boxes) and key not in keys:
                # Add the key to our set
                keys.add(key)
                # Add the box to the queue to search for more keys
                queue.append(key)
    
    # If we have a key for all boxes, return True
    return len(keys) == len(boxes)
