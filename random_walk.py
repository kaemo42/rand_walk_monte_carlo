import random


def random_walk_avg_distance(max_displacement, repetitions):
    """returns the average distance a point traveling around randomly can go before exceeding 4 units displacement from origin"""

    total_distance = 0


    for i in range(repetitions):

        x_distance, y_distance = 0, 0
        current_distance_travelled = 0
        current_displacement = 0


        while abs(current_displacement) <= max_displacement:

            (x_direction, y_direction) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
            
            x_distance += abs(x_direction)
            y_distance += abs(y_direction)

            current_displacement += x_direction
            current_displacement += y_direction

            current_distance_travelled = x_distance + y_distance


        total_distance += current_distance_travelled
    
    average_distance = total_distance / repetitions

    return average_distance


def random_walk_displacement(steps):
    """
    calculates the final displacement and coordinates after a random walk of distance (steps)
    returns {'coordinates': (x_displacement, y_displacement), 'displacement': displacement, 'distance': steps}"""

    x_displacement, y_displacement = 0, 0
    displacement = 0


    for i in range(steps):

        (x_direction, y_direction) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])

        x_displacement += x_direction
        y_displacement += y_direction


    displacement = abs(x_displacement) +  abs(y_displacement)

    return {'coordinates': (x_displacement, y_displacement), 'displacement': displacement, 'distance': steps}

        
for i in range(4, 31):
    tolls = 0

    for j in range(10000):
        trip_data = random_walk_displacement(i)

        if trip_data['displacement'] > 4:
            tolls += 1
        
    print('distance: ', i, ' probability less than 4: ', 1 - tolls / 10000)
        
        












