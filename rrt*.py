import math
import random
import matplotlib.pyplot as plt


class RRTStar:
    def __init__(self):
        self.start = (1, 1)
        self.end = (30, 30)
        self.obstacle_1 = (12, 5)
        self.obstacle_2 = (5, 12)
        self.obstacle_1_r = 8
        self.obstacle_2_r = 8
        self.search_radius = 2
        self.search_step = 0.1
        self.vertex_list = []


    def __is_vertex_inside_obstacle(self, point):
        if ((point[0] - self.obstacle_1[0])**2 +  (point[1] - self.obstacle_1[1])**2) < self.obstacle_1_r**2:
            return True
        if ((point[0] - self.obstacle_2[0])**2 +  (point[1] - self.obstacle_2[1])**2) <self.obstacle_2_r**2:
            return True
        return False

    def __is_line_touched_obstacle(self, vertex_1, vertex_2):
        """calculate a point to a line formula: ax+by+c/sqrt(a2+b2)
        """
        slope = (vertex_2[1] - vertex_1[1]) / (vertex_2[0] - vertex_1[0])
        slice = vertex_1[1] - vertex_1[0] * slope
        distance_to_obstacle_1_center = abs(slope(self.obstacle_1[0]) + self.obstacle_1[1] + slice) / math.sqrt(slope** + 1)
        distance_to_obstacle_2_center = abs(slope(self.obstacle_2[0]) + self.obstacle_2[1] + slice) / math.sqrt(slope** + 1)
        if distance_to_obstacle_1_center < self.obstacle_1_r**2 or distance_to_obstacle_2_center < self.obstacle_2**2:
            return True
        return False

    def __find_new_waypoint(self, point):
        x = random.uniform(point[0] + 1, 300)
        y = random.uniform(point[1] + 1, 300)
        return [x, y]

    def __calculate_edge_length(self, vertex_1, vertex_2):
        return math.sqrt((vertex_2[0] - vertex_1[0])**2 + (vertex_2[1] - vertex_1[1])**2)

    def __get_nearest_vertex(self, new_vertex):
        # distance_list = [(abs(new_vertex[0] - v[0]) + (new_vertex[1] - v[1])) for v in self.vertex_list]
        # nearest_vertex = distance_list[distance_list.index(min(distance_list))]
        min_distance = new_vertex[0] + new_vertex[1]
        for v in self.vertex_list:
            distance = abs(new_vertex[0] - v[0]) + abs(new_vertex[1] - v[1])
            if distance < min_distance and not self.__is_line_touched_obstacle(new_vertex, v):
                min_distance = distance
                nearest_vertex = v
        return nearest_vertex
    
    def execute(self):
        while True:
            new_vertex = self.__find_new_waypoint(self.start)
            if self.__is_vertex_inside_obstacle(new_vertex):
                continue
            nearest_vertex = self.__get_nearest_vertex(new_vertex)

