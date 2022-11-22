# https: // leetcode.com/problems/keys-and -rooms/description/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited = set()
        current_room = 0
        keys = [0]

        while len(keys) != 0:
            current_room = keys.pop(0)
            if current_room not in visited:
                keys += rooms[current_room]
                visited.add(current_room)

        return True if len(visited) == len(rooms) else False


# to go into the while loop, set keys with start room
# in the loop, visit rooms, add new gathered key in the the queue and
# add visted rooms to visited, and move to new room with new key
# if the room is already visited, directly move to next room with new key
