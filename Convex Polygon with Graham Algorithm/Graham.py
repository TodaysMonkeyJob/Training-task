from math import atan2  # for computing polar angle
from random import randint  # for sorting and creating data pts

import shapely  # for checking intersection
from matplotlib import pyplot as plt  # for plotting
from shapely import geometry


class Line():
    def __init__(self):
        self.line_cor = []

    # Returns a list of (x,y) coordinates,
    # each x and y coordinate is writen by user
    def create_line_points(self, point=2):
        print("Enter coordinates of Line: ")
        self.line_cor = [[int(input("Point " + str(_) + " X: ")), int(input("Point " + str(_) + " Y: "))] \
                         for _ in range(point)]


class Polygon():

    def __init__(self):
        self.pts = []
        self.hull = []
        self.points = 0

    # Returns a list of (x,y) coordinates of length 'num_points',
    # each x and y coordinate is writen by user
    def create_points(self, ct):
        self.pts = [[int(input("\n" + "Point " + str(_) + " X: ")), int(input("Point " + str(_) + " Y: "))] \
                    for _ in range(ct)]

    # If Polygon is convex
    # Creates a scatter plot, input is a list of (x,y) coordinates.
    # The second input 'convex_hull' is another list of (x,y) coordinates
    # consisting of those points in 'coords' which make up the convex hull,
    # if not None, the elements of this list will be used to draw the outer
    # boundary (the convex hull surrounding the data points).
    def scatter_plot(self, coords, line_cor, convex_hull=None):
        hull = self.graham_scan(True)
        shapely_line = shapely.geometry.LineString(line_cor)
        shapely_poly = shapely.geometry.Polygon(hull)
        intersection_line = list(shapely_poly.intersection(shapely_line).coords)
        xs, ys = zip(*coords)  # unzip into x and y coord lists
        xl, yl = zip(*line_cor)
        xi, yi = zip(*intersection_line)

        fig, ax = plt.subplots()

        if convex_hull != None:
            # plot the convex hull boundary, extra iteration at
            # the end so that the bounding line wraps around
            for i in range(1, len(convex_hull) + 1):
                if i == len(convex_hull): i = 0  # wrap
                c0 = convex_hull[i - 1]
                c1 = convex_hull[i]
                ax.plot((c0[0], c1[0]), (c0[1], c1[1]), 'b', marker='o')
        ax.plot(xs[0], ys[0], 'b', marker='o', label="Polygon")
        ax.plot(xl, yl, 'r', marker='o', label="Line")
        ax.plot(xi, yi, 'y', marker='o', label="Intersection")
        ax.legend()
        fig.set_figheight(5)
        fig.set_figwidth(8)
        plt.show()

    # If polygon isn`t convex
    # Creates a scatter plot, input is a list of (x,y) coordinates.
    def simple_plot(self, coords, line_cor):
        shapely_line = shapely.geometry.LineString(line_cor)
        shapely_poly = shapely.geometry.Polygon(coords)
        intersection_line = list(shapely_poly.intersection(shapely_line).coords)
        xs, ys = zip(*coords)  # unzip into x and y coord lists
        xl, yl = zip(*line_cor)
        xi, yi = zip(*intersection_line)

        fig, ax = plt.subplots()
        ax.plot(xs, ys, 'b', marker='o', label="Polygon")
        ax.plot(xl, yl, 'r', marker='o', label="Line")
        ax.plot(xi, yi, 'y', marker='o', label="Intersection")
        ax.legend()
        fig.set_figheight(5)
        fig.set_figwidth(8)
        plt.show()

    # Returns the polar angle (radians) from p0 to p1.
    # If p1 is None, defaults to replacing it with the
    # global variable 'anchor', normally set in the
    # 'graham_scan' function.
    def polar_angle(self, p0, p1=None):
        if p1 == None: p1 = anchor
        y_span = p0[1] - p1[1]
        x_span = p0[0] - p1[0]
        return atan2(y_span, x_span)

    # Returns the euclidean distance from p0 to p1,
    # square root is not applied for sake of speed.
    # If p1 is None, defaults to replacing it with the
    # global variable 'anchor', normally set in the
    # 'graham_scan' function.
    def distance(self, p0, p1=None):
        if p1 == None: p1 = anchor
        y_span = p0[1] - p1[1]
        x_span = p0[0] - p1[0]
        return y_span ** 2 + x_span ** 2

    # Returns the determinant of the 3x3 matrix...
    # 	[p1(x) p1(y) 1]
    #	[p2(x) p2(y) 1]
    # 	[p3(x) p3(y) 1]
    # If >0 then counter-clockwise
    # If <0 then clockwise
    # If =0 then collinear
    def det(self, p1, p2, p3):
        return (p2[0] - p1[0]) * (p3[1] - p1[1]) \
               - (p2[1] - p1[1]) * (p3[0] - p1[0])

    # Sorts in order of increasing polar angle from 'anchor' point.
    # 'anchor' variable is assumed to be global, set from within 'graham_scan'.
    # For any values with equal polar angles, a second sort is applied to
    # ensure increasing distance from the 'anchor' point.
    def quicksort(self, a):
        if len(a) <= 1: return a
        smaller, equal, larger = [], [], []
        piv_ang = self.polar_angle(a[randint(0, len(a) - 1)])  # select random pivot
        for pt in a:
            pt_ang = self.polar_angle(pt)  # calculate current point angle
            if pt_ang < piv_ang:
                smaller.append(pt)
            elif pt_ang == piv_ang:
                equal.append(pt)
            else:
                larger.append(pt)
        return self.quicksort(smaller) \
               + sorted(equal, key=self.distance) \
               + self.quicksort(larger)

    # Returns the vertices comprising the boundaries of
    # convex hull containing all points in the input set.
    # The input 'points' is a list of (x,y) coordinates.
    # If 'show_progress' is set to True, the progress in
    # constructing the hull will be plotted on each iteration.
    def graham_scan(self, show_progress=False):
        global anchor  # to be set, (x,y) with smallest y value

        # Find the (x,y) point with the lowest y value,
        # along with its index in the 'points' list. If
        # there are multiple points with the same y value,
        # choose the one with smallest x.
        min_idx = None
        for i, (x, y) in enumerate(self.pts):
            if min_idx == None or y < self.pts[min_idx][1]:
                min_idx = i
            if y == self.pts[min_idx][1] and x < self.pts[min_idx][0]:
                min_idx = i

        # set the global variable 'anchor', used by the
        # 'polar_angle' and 'distance' functions
        anchor = self.pts[min_idx]

        # sort the points by polar angle then delete
        # the anchor from the sorted list
        sorted_pts = self.quicksort(self.pts)
        del sorted_pts[sorted_pts.index(anchor)]

        # anchor and point with smallest polar angle will always be on hull
        hull = [anchor, sorted_pts[0]]
        for s in sorted_pts[1:]:
            while self.det(hull[-2], hull[-1], s) <= 0:
                del hull[-1]  # backtrack
            # if len(hull)<2: break
            hull.append(s)
            if show_progress:
                pass
                # scatter_plot(points, hull)
        return hull

    # Check if Polygon is Convex
    def is_Convex(self, pts, hull):
        print("Is Convex") if len(pts) == len(hull) else print("Is not Convex ")

    # Check if Polygon is intersected by line
    # Work just with Polygon
    # Polygon created with 2 dots don`t work and cause error
    def is_Intersection(self, line_cor, pts, hull):
        shapely_line = shapely.geometry.LineString(line_cor)
        if len(pts) == len(hull):
            shapely_poly = shapely.geometry.Polygon(hull)
            intersection_line = list(shapely_poly.intersection(shapely_line).coords)
        else:
            shapely_poly = shapely.geometry.Polygon(pts)
            intersection_line = list(shapely_poly.intersection(shapely_line).coords)

        if len(intersection_line) == 0:
            print("Not Intersection")
            exit(0)
        elif len(intersection_line) == 1:
            print("Intersection")
        else:
            if line_cor[0] == intersection_line[0] and line_cor[1] == intersection_line[1] \
                    or line_cor[1] == intersection_line[0] and line_cor[0] == intersection_line[1]:
                print("Line in Polygon")
            elif line_cor[0] == intersection_line[0] or line_cor[1] == intersection_line[1] \
                    or line_cor[1] == intersection_line[0] or line_cor[0] == intersection_line[1]:
                print("Line cross Polygon but not intersection")
            else:
                print("Intersection")

    # Main function
    def on_going(self):
        line_par = Line()
        line_par.create_line_points()
        print(line_par.line_cor)
        self.points = int(input("\n" + "Enter count of Points: "))
        self.create_points(self.points)

        print("Points:", self.pts)
        self.hull = self.graham_scan(True)
        print("Graham:", self.hull)
        self.is_Convex(self.pts, self.hull)
        if len(self.pts) == len(self.hull):
            self.is_Intersection(line_par.line_cor, self.pts, self.hull)
            self.scatter_plot(self.pts, line_par.line_cor, self.hull)
        else:
            self.is_Intersection(line_par.line_cor, self.pts, self.hull)
            plot = self.pts[0]
            self.pts.append(plot)
            self.simple_plot(self.pts, line_par.line_cor)


if __name__ == '__main__':
    project = Polygon()
    project.on_going()
