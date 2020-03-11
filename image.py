#SPECIAL THANKS TO IAN WILLIAMS FOR HELPING ME WITH SOME DEBUGGING, PRAISE PROGRAMMER JESUS, PEACE BE UPON HIM
#<3 IW
import math

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):

    point = 0
    for row in m2:
        #get a copy of the next point
        tmp = row[:]

        for r in range(4):
            m2[point][r] = (m1[0][r] * tmp[0] +
                            m1[1][r] * tmp[1] +
                            m1[2][r] * tmp[2] +
                            m1[3][r] * tmp[3])
        point+= 1

def ident( matrix ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            if r == c:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

def make_bezier():
    pass

def make_hermite():
    pass

def generate_curve_coefs( p0, p1, p2, p3, t ):
    pass


def make_translate( x, y, z ):
    t = new_matrix()
    ident(t)
    t[3][0] = x
    t[3][1] = y
    t[3][2] = z
    return t

def make_scale( x, y, z ):
    t = new_matrix()
    ident(t)
    t[0][0] = x
    t[1][1] = y
    t[2][2] = z
    return t

def make_rotX( theta ):
    t = new_matrix()
    ident(t)
    t[1][1] = math.cos(theta)
    t[2][1] = -1 * math.sin(theta)
    t[1][2] = math.sin(theta)
    t[2][2] = math.cos(theta)
    return t

def make_rotY( theta ):
    t = new_matrix()
    ident(t)
    t[0][0] = math.cos(theta)
    t[0][2] = -1 * math.sin(theta)
    t[2][0] = math.sin(theta)
    t[2][2] = math.cos(theta)
    return t

def make_rotZ( theta ):
    t = new_matrix()
    ident(t)
    t[0][0] = math.cos(theta)
    t[1][0] = -1 * math.sin(theta)
    t[0][1] = math.sin(theta)
    t[1][1] = math.cos(theta)
    return t

def circle_point(x, y, theta, r):
    xn = x + (r * math.cos(theta))
    yn = y + (r * math.sin(theta))
    return [xn, yn]

class picture:
    def __init__(self, n, w, h):
        self.name = n
        self.width, self.height = (w, h)
        self.pixels = [[[0, 0, 0] for i in range(self.width)] for j in range(self.height)]
        self.four_identity = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        self.edge_matrix = [[], [], [], []]
        self.transformation_matrix = ident(new_matrix())

    def plot(self, x, y, color):
        if x < 0 or y < 0 or x >= self.width or y >= self.height:#out of bounds
            return
        self.pixels[self.height - y - 1][x] = color #Flip for humans

    def draw_line(self, x0, y0, x1, y1, color ):
        #swap points if going right -> left
        if x0 > x1:
            xt = x0
            yt = y0
            x0 = x1
            y0 = y1
            x1 = xt
            y1 = yt

        x = x0
        y = y0
        A = 2 * (y1 - y0)
        B = -2 * (x1 - x0)

        #octants 1 and 8
        if ( abs(x1-x0) >= abs(y1 - y0) ):

            #octant 1
            if A > 0:
                d = A + B/2

                while x < x1:
                    self.plot(x, y, color)

                    if d > 0:
                        y+= 1
                        d+= B
                    x+= 1
                    d+= A
                #end octant 1 while
                self.plot(x1, y1, color)
            #end octant 1

            #octant 8
            else:
                d = A - B/2

                while x < x1:
                    self.plot(x, y, color)
                    if d < 0:
                        y-= 1
                        d-= B
                    x+= 1
                    d+= A
                #end octant 8 while
                self.plot(x1, y1, color)
            #end octant 8
        #end octants 1 and 8

        #octants 2 and 7
        else:
            #octant 2
            if A > 0:
                d = A/2 + B

                while y < y1:
                    self.plot(x, y, color)
                    if d < 0:
                        x+= 1
                        d+= A
                    y+= 1
                    d+= B
                #end octant 2 while
                self.plot(x1, y1, color)
            #end octant 2

            #octant 7
            else:
                d = A/2 - B;

                while y > y1:
                    self.plot(x, y, color)
                    if d > 0:
                        x+= 1
                        d+= A
                    y-= 1
                    d-= B
                #end octant 7 while
                self.plot(x1, y1, color)

    def display_edge_matrix(self):
        for i in self.edge_matrix:
            print(i)

    def add_3d_point(self, x, y, z):
        self.edge_matrix[0].append(x)
        self.edge_matrix[1].append(y)
        self.edge_matrix[2].append(z)
        self.edge_matrix[3].append(1)

    def add_edge(self, x0, y0, z0, x1, y1, z1):
        self.add_3d_point(x0,y0,z0)
        self.add_3d_point(x1,y1,z1)


    def add_circle(self, points, cx, cy, cz, r, step ):
        centx = cx
        centy = cy
        theta = 0
        while(theta != 360):
            secondpoints = circle_point(centx, centy, step, r)
            add_edge(centx, centy, 1, secondpoints[0], secondpoints[1], 1)
            centx = secondpoints[0]
            centy = secondpoints[1]
            theta += step


    def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):


    def draw_lines( matrix, screen, color ):
        if len(matrix) < 2:
            print('Need at least 2 points to draw')
            return

        point = 0
        while point < len(matrix) - 1:
            draw_line( int(matrix[point][0]),
                int(matrix[point][1]),
                int(matrix[point+1][0]),
                int(matrix[point+1][1]),
                screen, color)
            point+= 2

def print_pic_ascii(g):
    s = ""
    for x in range(g.width):
        for y in range(g.height):
            n = g.pixels[x][y]
            s += str(n[0]) + " " + str(n[1]) + " " + str(n[2]) + "  "
        s += "\n"
    #print(s)
    return s

def ppm_save_ascii(g):
    n = str(g.name)
    f = open(n + ".ppm", "w")
    f.write("P3\n" + str(g.width) + " " + str(g.height) + "\n255\n")
    f.write(print_pic_ascii(g))
    f.close()
    print(n + '.ppm')

# def test(x, y, deltx, delty, y_int):
#     return (delty *  x) - (deltx *  y) + (deltx * y_int)

def add_line(g, startx, starty, endx, endy):
    g.pixels[startx][starty] = [0, 0, 0]
    g.pixels[endx][endy] = [0, 0, 0]
    if endx - startx == 0:
        drawline_straight(g, startx, starty, endy)
    else:
        slope = (endy - starty)/(endx - startx)
        if (0 <= abs(slope) and abs(slope) < 1):
            drawline_octant_1(g, startx, starty, endx, endy)
        elif (1 <= abs(slope)):
            drawline_octant_2(g, startx, starty, endx, endy)

#NEW MATRIX CODE BELOW
# example_matrix = [[25, 25, 0, 1], [50, 50, 0, 1], [25, 50, 0, 1], [50, 25, 0, 1]]

def display_matrix(x):
    for i in x:
        print(i)

def multiply_matrices(x,y):
#this function is meant to take in rectangular matrices and multiply them in order given
    #Python doesn't generate matrices like this: result = [len(y)][len(y[0])] IW
    result_matrix = [([0] * len(y[0])) for i in range(len(y))]#[len(y)][len(y[0])]
    print(result_matrix)
    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(y)):
                result_matrix[i][j] += x[i][k] * y[k][j]
    display_matrix(result_matrix)
    y = result_matrix #Alters the second matrix IW
    return result_matrix

ARG_COMMANDS = [ 'line', 'scale', 'move', 'rotate', 'save', 'bezier', 'hermite', 'circle' ]

def parse_file( fname, edges, transform, screen, color ):

    f = open(fname)
    lines = f.readlines()

    c = 0
    while c < len(lines):
        line = lines[c].strip()
        #print ':' + line + ':'

        if line in ARG_COMMANDS:
            c+= 1
            args = lines[c].strip().split(' ')

        if line == 'line':
            #print 'LINE\t' + str(args)

            add_edge( edges,
                      float(args[0]), float(args[1]), float(args[2]),
                      float(args[3]), float(args[4]), float(args[5]) )

        elif line == 'circle':
            pass

        elif line == 'bezier':
            pass

        elif line == 'hermite':
            pass

        elif line == 'scale':
            #print 'SCALE\t' + str(args)
            t = make_scale(float(args[0]), float(args[1]), float(args[2]))
            matrix_mult(t, transform)

        elif line == 'move':
            #print 'MOVE\t' + str(args)
            t = make_translate(float(args[0]), float(args[1]), float(args[2]))
            matrix_mult(t, transform)

        elif line == 'rotate':
            #print 'ROTATE\t' + str(args)
            theta = float(args[1]) * (math.pi / 180)

            if args[0] == 'x':
                t = make_rotX(theta)
            elif args[0] == 'y':
                t = make_rotY(theta)
            else:
                t = make_rotZ(theta)
            matrix_mult(t, transform)

        elif line == 'ident':
            ident(transform)

        elif line == 'apply':
            matrix_mult( transform, edges )

        elif line == 'display' or line == 'save':
            clear_screen(screen)
            draw_lines(edges, screen, color)

            if line == 'display':
                display(screen)
            else:
                save_extension(screen, args[0])

        c+= 1

#TEST CODE BELOW

#draw_line(self, x0, y0, x1, y1, color )
#add_edge(self, x0, y0, z0, x1, y1, z1)
#draw_edges(self, color)
parse_file( 'script', edges, transform, screen, color )

n = picture('image', 500, 500)

n.draw_edges([255, 255, 255])

ppm_save_ascii(n)