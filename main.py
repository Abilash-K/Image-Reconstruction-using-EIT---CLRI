from tkinter import *
from sympy import Point, Polygon, Line
import math


window = Tk()

window.geometry("600x400")
window.title("Polygon Simulation")

canvas = Canvas(width=400, height=400)

canvas.pack()

canvas.create_oval(0, 0, 400, 400, fill="purple")

polygon_points = [[224.2356,196.2049],[222.2607,211.2406],[215.6908,226.3429],[203.1994,237.7227],[189.7210,239.4222],[176.7850,231.9500],[168.8122,219.7678],[164.5375,203.4922],[164.7001,187.6920],[168.3534,173.7151],[176.4413,160.6113],[186.5356,153.4606],[195.4196,151.9446]]
canvas.create_polygon(polygon_points, outline='gray',
                      fill='gray', width=2)



# This function gets the coordinates of the mouse pointert and helps to place the electrode
# def motion(event):
#     x, y = event.x, event.y
#     print('{}, {}'.format(x, y))
# window.bind('<Motion>', motion)


# 52,72 TL
topleft_electrode_X = 29
topleft_electrode_Y = 80
def topleft_electrode(pointX,pointY):
    x = pointX
    y = pointY
    y1 = pointY + 500
    canvas.create_rectangle(x,y,x+15,y+12, fill="grey",width=2)
    for i in range(4):
        canvas.create_line(x,y,x+500,y1)
        y1 += 50





#  366,89     TR
topright_electrode_X = 355
topright_electrode_Y = 80
tre_ray = 370
def topright_electrode(pointX,pointY,ray):
    x = pointX
    y = pointY
    y1 = pointY + 200

    canvas.create_rectangle(x,y,x+15,y+12, fill="grey",width=2)
    # canvas.create_line(line_pt, y, x - 500, y +200)
    # canvas.create_line(line_pt, y, x - 500, y +250)
    # canvas.create_line(line_pt, y, x - 500, y +300)
    # canvas.create_line(line_pt, y, x - 500, y +350)
    for i in range(4):
        canvas.create_line(ray,y,x-500,y1)
        y1 += 50


#   35,315    BL
bottomleft_electrode_X = 73
bottomleft_electrode_Y = 357
ble_ray = 74
def bottomleft_electrode(pointX,pointY,ray):
    x = pointX
    y = pointY
    y1 = pointY - 500
    canvas.create_rectangle(x,y,x+15,y+12, fill="grey",width=2)
    # canvas.create_line(line_pt, y+10, x + 500, y - 500)
    # canvas.create_line(line_pt, y+10, x + 500, y - 550)
    # canvas.create_line(line_pt, y+10, x + 500, y - 600)
    # canvas.create_line(line_pt, y+10, x + 500, y - 650)
    for i in range(4):
        canvas.create_line(ray,y+10,x+500,y1)
        y1 -= 50


#   348,351    BR
bottomright_electrode_X = 314
bottomright_electrode_Y = 357
bre_ray = 330
def bottomright_electrode(pointX,pointY,ray):
    x = pointX
    y = pointY
    y1 = pointY - 500
    canvas.create_rectangle(x,y,x+15,y+12, fill="grey",width=2)
    # canvas.create_line(line_pt, y+13, x - 500, y -500)
    # canvas.create_line(line_pt, y+13, x - 500, y -550)
    # canvas.create_line(line_pt, y+13, x - 500, y -600)
    # canvas.create_line(line_pt, y+13, x - 500, y -650)
    for i in range(4):
        canvas.create_line(ray, y+13, x-500,y1)
        y1 -= 50

testline=[(330,370),(-170,-143)]
def export_csv():
    # creating points using Point()
    p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13 = map(Point, polygon_points,)
    # creating polygons using Polygon()
    poly1 = Polygon(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13)

    #BOTTOM_RIGHT_ELECTRODE
    BOTTOM_RIGHT_ELECTRODE = []
    bre_Y1 = bottomright_electrode_Y - 500
    BRE_Y0 = bottomright_electrode_Y + 13
    for i in range(4):
        p14 , p15 = map(Point,[(bre_ray,BRE_Y0),(-186,bre_Y1)])
        bre_Y1 -= 50
        poly2 = Line(p14,p15)
        isIntersection = poly1.intersection(poly2)
        point1 = isIntersection[0].evalf()
        point2= isIntersection[1].evalf()
        final_distance = math.dist(point1,point2)
        BOTTOM_RIGHT_ELECTRODE.extend([(point1,point2,final_distance)])
    print(BOTTOM_RIGHT_ELECTRODE)

    #BOTTOM_LEFT_ELECTRODE
    BOTTOM_LEFT_ELECTRODE = []
    ble_Y1 = bottomleft_electrode_Y - 500
    BLE_Y0 = bottomright_electrode_Y + 10
    for i in range(4):
        p14 , p15 = map(Point,[(ble_ray,BLE_Y0),(573,ble_Y1)])
        bre_Y1 -= 50
        poly2 = Line(p14,p15)
        isIntersection = poly1.intersection(poly2)

        point1 = isIntersection[0].evalf()
        point2= isIntersection[1].evalf()
        final_distance = math.dist(point1,point2)
        BOTTOM_LEFT_ELECTRODE.extend([(point1,point2,final_distance)])
    print(BOTTOM_LEFT_ELECTRODE)

    # TOP_RIGHT_ELECTRODE
    TOP_RIGHT_ELECTRODE = []
    TRe_Y1 = topright_electrode_Y + 200
    for i in range(4):
        p14, p15 = map(Point, [(tre_ray, topright_electrode_Y), (-145, TRe_Y1)])
        TRe_Y1 += 50
        poly2 = Line(p14, p15)
        isIntersection = poly1.intersection(poly2)
        if (isIntersection):
            point1 = isIntersection[0].evalf()
            point2 = isIntersection[1].evalf()
            final_distance = math.dist(point1, point2)
            TOP_RIGHT_ELECTRODE.extend([(point1, point2, final_distance)])
    print(TOP_RIGHT_ELECTRODE)

    # TOP_LEFT_ELECTRODE
    TOP_LEFT_ELECTRODE = []
    Tle_Y1 = topleft_electrode_Y + 500
    for i in range(4):
        p14, p15 = map(Point, [(topleft_electrode_X, topleft_electrode_Y), (529, Tle_Y1)])
        Tle_Y1 += 50
        poly2 = Line(p14, p15)
        isIntersection = poly1.intersection(poly2)
        if (isIntersection):
            point1 = isIntersection[0].evalf()
            point2 = isIntersection[1].evalf()
            final_distance = math.dist(point1, point2)
            TOP_LEFT_ELECTRODE.extend([(point1, point2, final_distance)])
    print(TOP_LEFT_ELECTRODE)

    # p14, p15 = map(Point, testline)
    # poly2 = Line(p14, p15)

    # isIntersection = poly1.intersection(poly2)
    # point1 = isIntersection[0]
    # point2= isIntersection[1]
    # # segmentof = Segment(pointX,pointY)
    # # lengthof=segmentof.length
    # print(math.dist(point1,point2))
    # # print(pointX,pointY)



turn_on = Button(window, text="Export",command=export_csv)
turn_on.place(x = 512 , y = 212)

#186.97
# Testing purpose!
# canvas.create_line([(164.57,200.26),(201.30,237.96)], fill='red', width=2)


topleft_electrode(topleft_electrode_X,topleft_electrode_Y)
topright_electrode(topright_electrode_X,topleft_electrode_Y,tre_ray)
bottomleft_electrode(bottomleft_electrode_X,bottomleft_electrode_Y,ble_ray)
bottomright_electrode(bottomright_electrode_X,bottomright_electrode_Y,bre_ray)


window.mainloop()
