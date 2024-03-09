def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]

def assign_rooms(names):
    rooms = range(1,9)
    assignment = []
    for room in rooms:
        assignment.append(f"Hello, {names[room - 1]}! You'll be assigned to room {room}!")
    return assignment

def printer(names):
    for badges in batch_badge_creator(names):
        print(badges)

    for rooms in assign_rooms(names):
        print(rooms)
