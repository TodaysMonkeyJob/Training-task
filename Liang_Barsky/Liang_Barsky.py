from tkinter import *


class windows_cutter:

    def __init__(self):
        self.my_canvas = None
        self.mouse_click_right = 0
        self.mouse_click_left = 0
        self.x_line_coor_min = 0
        self.x_line_coor_max = 0
        self.x_rect_coor_min = 0
        self.x_rect_coor_max = 0
        self.y_line_coor_min = 0
        self.y_line_coor_max = 0
        self.y_rect_coor_min = 0
        self.y_rect_coor_max = 0

    def draw_line(self, event):

        if self.mouse_click_left == 0:
            self.x_line_coor_min = event.x
            self.y_line_coor_min = event.y
            self.mouse_click_left = 1
            self.my_canvas.create_oval(self.x_line_coor_min - 1, self.y_line_coor_min - 1,
                                       (self.x_line_coor_min + 1), (self.y_line_coor_min + 1), outline="red", width=4)
        else:
            self.x_line_coor_max = event.x
            self.y_line_coor_max = event.y
            self.my_canvas.create_line(self.x_line_coor_min, self.y_line_coor_min,
                                       self.x_line_coor_max, self.y_line_coor_max, fill="red", width=5)
            self.Liang_Barsky()
            self.mouse_click_left = 0

    def draw_rectangle(self, event):
        self.my_canvas.create_rectangle(0, 0, 600, 600, fill="white")
        if self.mouse_click_right == 0:
            self.x_rect_coor_min = event.x
            self.y_rect_coor_min = event.y
            self.mouse_click_right = 1
            self.my_canvas.create_oval(self.x_rect_coor_min - 1, self.y_rect_coor_min - 1,
                                       (self.x_rect_coor_min + 1), (self.y_rect_coor_min + 1), outline="blue", width=4)
        else:
            self.x_rect_coor_max = event.x
            self.y_rect_coor_max = event.y
            self.my_canvas.create_rectangle(self.x_rect_coor_min, self.y_rect_coor_min,
                                            self.x_rect_coor_max, self.y_rect_coor_max, outline="blue", width=5)
            self.mouse_click_right = 0

    def Liang_Barsky(self):

        if self.x_rect_coor_min > self.x_rect_coor_max and self.y_rect_coor_min > self.y_rect_coor_max:
            self.x_rect_coor_min, self.x_rect_coor_max = self.x_rect_coor_max, self.x_rect_coor_min
            self.y_rect_coor_min, self.y_rect_coor_max = self.y_rect_coor_max, self.y_rect_coor_min

        if self.x_rect_coor_min > self.x_rect_coor_max:
            self.x_rect_coor_min, self.x_rect_coor_max = self.x_rect_coor_max, self.x_rect_coor_min

        if self.y_rect_coor_min > self.y_rect_coor_max:
            self.y_rect_coor_min, self.y_rect_coor_max = self.y_rect_coor_max, self.y_rect_coor_min

        p = [0] * 4
        q = [0] * 4
        dx = self.x_line_coor_max - self.x_line_coor_min
        dy = self.y_line_coor_max - self.y_line_coor_min
        tmin = 0
        tmax = 1
        p[0] = -(self.x_line_coor_max - self.x_line_coor_min)
        p[1] = (self.x_line_coor_max - self.x_line_coor_min)
        p[2] = -(self.y_line_coor_max - self.y_line_coor_min)
        p[3] = (self.y_line_coor_max - self.y_line_coor_min)
        q[0] = self.x_line_coor_min - self.x_rect_coor_min
        q[1] = self.x_rect_coor_max - self.x_line_coor_min
        q[2] = self.y_line_coor_min - self.y_rect_coor_min
        q[3] = self.y_rect_coor_max - self.y_line_coor_min

        for i in range(0, 4):

            if p[i] < 0:
                tmin = max(tmin, (q[i] / p[i]))

            elif p[i] > 0:
                tmax = min(tmax, (q[i] / p[i]))

            elif q[i] < 0:
                tmax = 0
                tmin = 1
                break
        if tmin < tmax:
            # print((self.x_line_coor_min + tmin * dx), (self.y_line_coor_min + tmin * dy),
            #     (self.x_line_coor_min + tmax * dx), (self.y_line_coor_min + tmax * dy))
            self.my_canvas.create_line((self.x_line_coor_min + tmin * dx), (self.y_line_coor_min + tmin * dy),
                                       (self.x_line_coor_min + tmax * dx), (self.y_line_coor_min + tmax * dy),
                                       fill='green', width=6)
        else:
            print("Line lies outside")

    def main(self):
        my_window = Tk()
        self.my_canvas = Canvas(my_window, width=600, height=600, background='white')
        self.my_canvas.grid(row=0, column=0)
        self.my_canvas.bind('<Button-1>', self.draw_line)
        self.my_canvas.bind('<Button-3>', self.draw_rectangle)
        my_window.mainloop()


if __name__ == '__main__':
    project = windows_cutter()
    project.main()
