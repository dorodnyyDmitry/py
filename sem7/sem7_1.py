import matplotlib.pyplot as plt
import matplotlib.patches as ptc
import matplotlib.path as pth
import numpy as np

fig, ax = plt.subplots(1,3, figsize = (25,5))

flatten = lambda l: [item for sublist in l for item in sublist]

def draw_all(objects, fig):
    list(map(lambda x: x.draw(fig), objects))

def check_all(objects, points):
    print(*flatten(list(map(lambda x: list(map(lambda y: str(x.name) + ' does ' + ' not ' * (bool(x.contains(y))==False) + ' contain ' + str(y.name), points)), objects))), sep = '\n')


xlist = np.linspace(-4, 4, 1000)
ylist = np.linspace(-4, 4, 1000)
X, Y = np.meshgrid(xlist, ylist)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.name = 'Point_' + str(x) + '_' + str(y)

    def draw(self, i):
        ax[i].scatter(self.x,self.y, color = 'k', zorder = 100)


class Shape(Point):
    def __init__(self, xs, ys):
        super().__init__(xs, ys)
        self.name = 'Shape_' + str(xs) + '_' + str(ys)
    def draw(self, i):
        ax[i].plot([*self.x, self.x[0]], [*self.y, self.y[0]], marker = 'x', zorder = 100)

    def contains(self, point):
        polygon = [[self.x[i], self.y[i]] for i in range(len(self.x))]
        path = ptc.Polygon(polygon)
        return path.contains_point((point.x, point.y))

class Square(Shape):
    def __init__(self, x, y, size):
        super().__init__(x,y)
        self.size = size
        self.name = 'Square_'+str(x)+'_'+str(y)

    def draw(self, i):
        ax[i].add_patch(ptc.Rectangle((self.x, self.y),self.size,self.size, zorder = 0))

    def contains(self, point):
        return ((point.x >= self.x) and (point.x <= (self.x+self.size)) and (point.y >= self.y) and (point.y <= (self.y+self.size)))


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x,y)
        self.radius = radius
        self.name = 'Circle_'+str(x)+'_'+str(y)

    def draw(self, i):
        ax[i].add_patch(ptc.Circle((self.x, self.y),self.radius, zorder = 0))

    def contains(self, point):
        return ((point.x-self.x)**2 + (point.y-self.y)**2)**0.5 <= self.radius

class Union(Shape):
    def __init__(self, figs):
        self.figs = figs
        #self.pts = ones(X.shape)

    def contains(self, point):
        return any([figure.contains(point) for figure in self.figs])

    def draw(self, i):
        draw_all(self.figs, i)

class Intersection(Shape):
    def __init__(self, figs):
        self.figs = figs

    def contains(self, point):
        return all([figure.contains(point) for figure in self.figs])

    def draw(self):
        #mask = np.ones(X.shape)
        ptsx = []
        ptsy = []
        for x in xlist:
            for y in ylist:
                if all([fig.contains(Point(x,y)) for fig in self.figs]):
                #if fig.contains(Point(x,y)):
                    ptsx.append(x)
                    ptsy.append(y)
        #path = ptc.Polygon(pts, closed = True)
        ax[2].scatter(ptsx, ptsy)



point0, point1, point2 = Point(-5,3), Point(10, 10), Point(1,1)
square0, square1 = Square(0, 0, 2), Square(-6, 4, 4)
circle0, circle1 = Circle(7, 7, 6), Circle(-9,-7, 3)

draw_all([point0, point1, point2, square0, square1, circle0, circle1], 1)
check_all([square0, square1, circle0, circle1], [point0, point1, point2])


pt = Point(9,9)
pt.draw(0)
shap = Shape([1,6,2], [2, -3, 3])
shap.draw(0)

uni = Union([Circle(1,-9,3), Square(2,-8,4)])
#uni.draw(2)

xx = ptc.Circle((0,0), radius = 500)
yy = ptc.Circle((0,0), radius = 1)
x = xx.get_path()
y = yy.get_path()

#ax.add_patch()

#print(x.to_polygons()[0])
#ax.plot(xs, ys)
#print(*list(x.iter_segments(clip = (-0.1, -0.1, 0.1, 0.1))), sep = '\n')
#print(z.to_polygons())


zxc = Square(0,0,4)
xcv = Circle(0,0,2)
vbs = Circle(0, 2.5, 2)
kys = Intersection([zxc,xcv, vbs])
kys.draw()

for i in range(3):
    ax[i].set_xlim(-10, 10)
    ax[i].set_ylim(-10, 10)





#plt.xticks(np.arange(-10, 10, step=1))
#plt.yticks(np.arange(-10, 10, step=1))
#ax.set_aspect(aspect = 'equal')
plt.show()
