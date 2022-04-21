def work():
    import pygame
    #import Main_Menu

    #from pygame.locals import *
    import math
    from shapely.geometry import Point, Polygon
    import pygame_widgets as pw

    from functools import reduce
    import operator
    import math
    import pygame.gfxdraw






    # --- constants --- (UPPER_CASE names)
    pygame.init()
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 800
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)

    FPS = 30
    COLOR_INACTIVE = pygame.Color('lightskyblue3')
    COLOR_ACTIVE = pygame.Color('dodgerblue2')
    FONT = pygame.font.Font('Wishleman.ttf', 12)
    increment_line = 25
    npl = 1
    perspective = (SCREEN_WIDTH/2) / ((increment_line - 1) * npl)


    pi = 3.141592653

    class rectangle_draw:
        def __init__(self, x, y, width, height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.fill = 1
            self.box1_rec = InputBox(10, 100, 50, 32)
            self.box2_rec = InputBox(70, 100, 50, 32)
            self.box3_rec = InputBox(10, 150, 50, 32)
            self.box4_rec = InputBox(70, 150, 50, 32)
            self.boxes_rec = [input_box1_circle, input_box2_circle, input_box3_circle, input_box4_rec]
            self.rec_fill = button((255, 255, 255), 10, 200, 60, 32, 'Fill')
            self.rec_back = button((255, 255, 255), 10, 250, 60, 32, 'Back')
            self.rec_delete = button((255, 255, 255), 10, 300, 60, 32, 'Delete')

        def draw(self):
            # self.box1_circle.change_text()
            self.box1_rec.txt_surface = FONT.render(str  (  round((self.x - 600) * npl / increment_line, 2) ), True, BLUE)
            self.box1_rec.draw(screen)

            # self.box2_circle.change_text()
            self.box2_rec.txt_surface = FONT.render(
                str(  round((SCREEN_HEIGHT - self.y - 400) * npl / increment_line, 2)  ), True, BLUE)
            self.box2_rec.draw(screen)
            # self.box3_circle.change_text()
            self.box3_rec.txt_surface = FONT.render(str(  round(self.width / perspective, 2)  ), True, BLUE)
            self.box3_rec.draw(screen)
            self.box4_rec.txt_surface = FONT.render(str( round( self.height / perspective, 2) ), True, BLUE)
            self.box4_rec.draw(screen)
            self.rec_fill.draw(screen, (0, 0, 0))
            self.rec_back.draw(screen, (0, 0, 0))
            self.rec_delete.draw(screen, (0, 0, 0))
            message_for_rec()

        def adjust(self, prev):
            tempi1=((self.x - 600) * prev / increment_line)
            self.x= 600 + ((tempi1) * increment_line) / npl
            tempi2 = (SCREEN_HEIGHT - self.y - 400) * prev / increment_line
            self.y = SCREEN_HEIGHT - (400 + ((tempi2) * increment_line) / npl)
            tempi3= self.width / ( (SCREEN_WIDTH/2) / ((increment_line - 1) * prev) )
            self.width =  tempi3 * perspective
            tempi4 = self.height / ( (SCREEN_WIDTH/2) / ((increment_line - 1) * prev) )
            self.height = tempi4 * perspective









    class circle_draw:
        def __init__(self, x, y, r):
            self.x = x
            self.y = y
            self.r = r
            self.width = 1
            self.box1_circle = InputBox(10, 100, 50, 32)
            self.box2_circle = InputBox(70, 100, 50, 32)
            self.box3_circle = InputBox(10, 150, 50, 32)
            self.boxes_circle = [input_box1_circle, input_box2_circle, input_box3_circle]
            self.circle_fill = button((255, 255, 255), 10, 200, 60, 32, 'Fill')
            self.circle_back = button((255, 255, 255), 10, 250, 60, 32, 'Back')
            self.circle_delete = button((255, 255, 255), 10, 300, 60, 32, 'Delete')

        def draw(self):
            # self.box1_circle.change_text()
            self.box1_circle.txt_surface = FONT.render(str( round( (self.x - 600) * npl / increment_line , 2) ), True,
                                                       BLUE)
            self.box1_circle.draw(screen)
            # self.box2_circle.change_text()
            self.box2_circle.txt_surface = FONT.render(
                str( round( (SCREEN_HEIGHT - self.y - 400) * npl / increment_line, 2)  ), True, BLUE)
            self.box2_circle.draw(screen)
            # self.box3_circle.change_text()
            self.box3_circle.txt_surface = FONT.render(str( round( self.r / perspective, 2)  ), True, BLUE)
            self.box3_circle.draw(screen)
            self.circle_fill.draw(screen, (0, 0, 0))
            self.circle_back.draw(screen, (0, 0, 0))
            self.circle_delete.draw(screen, (0, 0, 0))
            # print("kaka")

            message_for_circle()

            for event in pygame.event.get():
                # if (self.circle_fill.isOver(pygame.mouse.get_pos())):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # pos = pygame.mouse.get_pos()
                    if (self.circle_fill.isOver(pygame.mouse.get_pos())):
                        # print("pp")
                        if (self.width == 1):
                            self.width = 0
                        else:
                            self.width = 1

                # list_of_rectangles.append(circ_1)


        def adjust(self, prev):
            tempi1 = ((self.x - 600) * prev / increment_line)
            self.x = 600 + ((tempi1) * increment_line) / npl
            tempi2 = (SCREEN_HEIGHT - self.y - 400) * prev / increment_line
            self.y = SCREEN_HEIGHT - (400 + ((tempi2) * increment_line) / npl)
            tempi3 = self.r / ((SCREEN_WIDTH / 2) / ((increment_line - 1) * prev))
            self.r = tempi3 * perspective



    class line_draw:
        def __init__(self, x1, y1, x2, y2):
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2
            self.pt1_selected=0
            self.pt2_selected=0

            if (x2 - x1 == 0):
                self.dhal = math.trunc(round((y2 - y1) / 0.0000000001))

            elif (y2 - y1 == 0):
                self.dhal = math.trunc(round(0.0000000001 / (x2 - x1)))
            else:
                self.dhal = math.trunc(round((y2 - y1) / (x2 - x1)))

            # print(self.dhal)

            # self.dhal= math.trunc( round((y2-y1)/(x2-x1)))
            self.c = math.trunc(round(y1 - (self.dhal * x1)))
            self.box1_line = InputBox(10, 100, 50, 32)
            self.box2_line = InputBox(70, 100, 50, 32)
            self.box3_line = InputBox(10, 150, 50, 32)
            self.box4_line = InputBox(70, 150, 50, 32)
            self.boxes_line = [input_box1_line, input_box2_line, input_box3_line, input_box4_line]
            # self.circle_fill = button((255, 255, 255), 10, 200, 60, 32, 'Fill')
            self.line_back = button((255, 255, 255), 10, 200, 60, 32, 'Back')
            self.line_delete = button((255, 255, 255), 10, 250, 60, 32, 'Delete')
            self.line_pt1 = button((255, 255, 255), 10, 300, 60, 32, 'Pt1')
            self.line_pt2 = button((255, 255, 255), 70, 300, 60, 32, 'Pt2')


        def draw(self):
            # self.box1_circle.change_text()
            self.box1_line.txt_surface = FONT.render(str( round( (self.x1 - 600) * npl / increment_line , 2) ), True,
                                                     BLUE)
            self.box1_line.draw(screen)
            # self.box2_circle.change_text()
            self.box2_line.txt_surface = FONT.render(
                str( round( (SCREEN_HEIGHT - self.y1 - 400) * npl / increment_line, 2)   ), True, BLUE)
            self.box2_line.draw(screen)
            # self.box3_circle.change_text()
            self.box3_line.txt_surface = FONT.render(str( round( (self.x2 - 600) * npl / increment_line, 2)  ), True,
                                                     BLUE)
            self.box3_line.draw(screen)
            self.box4_line.txt_surface = FONT.render(
                str( round((SCREEN_HEIGHT - self.y2 - 400) * npl / increment_line, 2) ), True, BLUE)
            self.box4_line.draw(screen)
            # self.circle_fill.draw(screen, (0, 0, 0))
            self.line_back.draw(screen, (0, 0, 0))
            self.line_delete.draw(screen, (0, 0, 0))
            self.line_pt1.draw(screen, (0, 0, 0)  )
            self.line_pt2.draw(screen, (0, 0, 0))

            message_for_line()

        def adjust(self, prev):
            tempi1 = ((self.x1 - 600) * prev / increment_line)
            self.x1 = 600 + ((tempi1) * increment_line) / npl
            tempi2 = (SCREEN_HEIGHT - self.y1 - 400) * prev / increment_line
            self.y1 = SCREEN_HEIGHT - (400 + ((tempi2) * increment_line) / npl)
            tempi3 = ((self.x2 - 600) * prev / increment_line)
            self.x2 = 600 + ((tempi3) * increment_line) / npl
            tempi4 = (SCREEN_HEIGHT - self.y2 - 400) * prev / increment_line
            self.y2 = SCREEN_HEIGHT - (400 + ((tempi4) * increment_line) / npl)




    class arc_draw:
        def __init__(self, x, y, start, end, r):
            self.x = x
            self.y = y
            self.r = r
            self.start = start
            self.end = end
            self.box1_arc = InputBox(10, 100, 50, 32)
            self.box2_arc = InputBox(70, 100, 50, 32)
            self.box3_arc = InputBox(10, 150, 50, 32)
            self.box4_arc = InputBox(70, 150, 50, 32)
            self.box5_arc = InputBox(10, 200, 50, 32)
            self.arc_delete = button((255, 255, 255), 10, 250, 60, 32, 'Delete')

            # self.boxes_arc = [input_box1_arc, input_box2_arc, input_box3_arc, input_box4_arc, input_box5_arc]

        def draw(self):
            # self.box1_circle.change_text()
            self.box1_arc.txt_surface = FONT.render(str(  round( (self.x - 600) * npl / increment_line, 2)  ), True, BLUE)
            self.box1_arc.draw(screen)
            # self.box2_circle.change_text()
            self.box2_arc.txt_surface = FONT.render(
                str(  round((SCREEN_HEIGHT - self.y - 400) * npl / increment_line, 2)), True, BLUE)
            self.box2_arc.draw(screen)
            # self.box3_circle.change_text()
            self.box3_arc.txt_surface = FONT.render(str( round( float(self.start * (180 / pi)), 2)  ), True, BLUE)
            self.box3_arc.draw(screen)
            self.box4_arc.txt_surface = FONT.render(str( round( float(self.end * (180 / pi)), 2) ), True, BLUE)
            self.box4_arc.draw(screen)
            self.box5_arc.txt_surface = FONT.render(str( round(  self.r / perspective , 2) ), True, BLUE)
            self.box5_arc.draw(screen)
            self.arc_delete.draw(screen, (0, 0, 0))
            message_for_arc()

            # self.circle_fill.draw(screen, (0, 0, 0))
            # self.arc_back.draw(screen, (0, 0, 0))

        def adjust(self, prev):
            tempi1 = ((self.x - 600) * prev / increment_line)
            self.x = 600 + ((tempi1) * increment_line) / npl
            tempi2 = (SCREEN_HEIGHT - self.y - 400) * prev / increment_line
            self.y = SCREEN_HEIGHT - (400 + ((tempi2) * increment_line) / npl)
            tempi3 = self.r / ((SCREEN_WIDTH / 2) / ((increment_line - 1) * prev))
            self.r = tempi3 * perspective

    class polygon_draw:
        def __init__(self, list_of_x, list_of_y):
            self.list_of_x = list_of_x[:]
            self.list_of_y = list_of_y[:]
            self.width = 1
            self.fill = 1
            self.poly_back = button((255, 255, 255), 10, 50, 60, 32, 'Back')
            self.poly_fill = button((255, 255, 255), 70, 50, 60, 32, 'Fill')
            self.poly_delete = button((255, 255, 255), 130, 50, 60, 32, 'Delete')
            coords = []

            for i in range(0, len(self.list_of_x)):
                oo = []
                oo.append(self.list_of_x[i])
                oo.append(self.list_of_y[i])
                coords.append(oo)

            center = tuple(
                map(operator.truediv, reduce(lambda x, y: map(operator.add, x, y), coords), [len(coords)] * 2))
            abar = (sorted(coords, key=lambda coord: (-135 - math.degrees(
                math.atan2(*tuple(map(operator.sub, coord, center))[::-1]))) % 360))

            self.list_of_x.clear()
            self.list_of_y.clear()
            print(abar)

            for i in range(0, len(abar)):
                self.list_of_x.append(abar[i][0])
                self.list_of_y.append(abar[i][1])

        def get_polygon(self):
            return_list = []
            for i in range(0, len(self.list_of_x)):
                temp_list = []
                temp_list.append(self.list_of_x[i])
                temp_list.append(self.list_of_y[i])
                return_list.append(temp_list)

            return return_list

        def draw(self):

            start = 100
            self.poly_back.draw(screen, (0, 0, 0))
            self.poly_fill.draw(screen, (0, 0, 0))
            self.poly_delete.draw(screen, (0, 0, 0))
            follow=1

            for i in range(0, len(self.list_of_x)):
                temp_box_1 = InputBox(10, start, 50, 32)
                temp_box_2 = InputBox(70, start, 50, 32)
                message_to_screen( "X"+str(follow), RED, 20, start+40, 10 )
                message_to_screen("Y"+str(follow), RED, 80, start + 40, 10)
                follow+=1


                start += 50
                temp_box_1.txt_surface = FONT.render(str( round( (self.list_of_x[i] - 600) * npl / increment_line, 2) ),
                                                     True, BLUE)
                temp_box_1.draw(screen)
                temp_box_2.txt_surface = FONT.render(
                    str(round((SCREEN_HEIGHT - self.list_of_y[i] - 400) * npl / increment_line, 2)), True, BLUE)
                temp_box_2.draw(screen)

        def adjust(self, prev):

            for i in range( len(self.list_of_x) ):
                tempi1 = ((self.list_of_x[i] - 600) * prev / increment_line)
                self.list_of_x[i]= 600 + ((tempi1) * increment_line) / npl
                tempi2 = (SCREEN_HEIGHT - self.list_of_y[i] - 400) * prev / increment_line
                self.list_of_y[i] = SCREEN_HEIGHT - (400 + ((tempi2) * increment_line) / npl)


    class InputBox:

        def __init__(self, x, y, w, h, text=''):
            self.rect = pygame.Rect(x, y, w, h)
            self.color = COLOR_INACTIVE
            self.text = text
            self.txt_surface = FONT.render(text, True, self.color)
            self.active = False
            self.pp = []  # These are only for polygon

        def handle_event(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if self.rect.collidepoint(event.pos):
                    # Toggle the active variable.
                    self.active = not self.active
                else:
                    self.active = False
                # Change the current color of the input box.
                self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
            if event.type == pygame.KEYDOWN:
                if self.active:
                    if event.key == pygame.K_RETURN:
                        self.pp.append(int(self.text))
                        print(self.text)
                        self.text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode
                    # Re-render the text.
                    self.txt_surface = FONT.render(self.text, True, self.color)

        def update(self):
            # Resize the box if the text is too long.
            width = max(50, self.txt_surface.get_width() + 10)
            self.rect.w = width

        def draw(self, screen):
            # Blit the text.
            screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
            # Blit the rect.
            pygame.draw.rect(screen, self.color, self.rect, 2)

        def change_text(self):
            self.text = ''

    def draw_rect_outline(surface, rect, color, width=1):
        x, y, w, h = rect
        width = max(width, 1)  # Draw at least one rect.
        width = min(min(width, w // 2), h // 2)  # Don't overdraw.

        # This draws several smaller outlines inside the first outline. Invert
        # the direction if it should grow outwards.
        for i in range(width):
            pygame.gfxdraw.rectangle(screen, (x + i, y + i, w - i * 2, h - i * 2), color)

    def text_objects(msg, color, sizi):
        font = pygame.font.Font("ka1.ttf", sizi)
        textSurface = font.render(msg, True, color)
        return textSurface, textSurface.get_rect()

    def message_to_screen(msg, color, x_position, y_position, size):
        textSurf, textRect = text_objects(msg, color, size)
        textRect.center = (x_position, y_position)
        screen.blit(textSurf, textRect)


    def label( msg, color, x_position, y_position, size, new_size):
        textSurf, textRect = text_objects(msg, color, size)
        textRect.center = (x_position, y_position)
        screen.blit(textSurf,new_size)


    def message_for_circle():
        message_to_screen("X", RED, message_boxes_circle[0][0], message_boxes_circle[0][1], 10)
        message_to_screen("Y", RED, message_boxes_circle[1][0], message_boxes_circle[1][1], 10)
        message_to_screen("Radius", RED, message_boxes_circle[2][0], message_boxes_circle[2][1], 10)


    def message_for_line():
        message_to_screen("X1", RED, message_boxes_line[0][0], message_boxes_line[0][1], 10)
        message_to_screen("Y1", RED, message_boxes_line[1][0], message_boxes_line[1][1], 10)
        message_to_screen("X2", RED, message_boxes_line[2][0], message_boxes_line[2][1], 10)
        message_to_screen("y2", RED, message_boxes_line[3][0], message_boxes_line[3][1], 10)

    def message_for_rec():
        message_to_screen("X1", RED, message_boxes_rec[0][0], message_boxes_rec[0][1], 10)
        message_to_screen("Y1", RED, message_boxes_rec[1][0], message_boxes_rec[1][1], 10)
        message_to_screen("WIDTH", RED, message_boxes_rec[2][0], message_boxes_rec[2][1], 10)
        message_to_screen("HEIGHT", RED, message_boxes_rec[3][0], message_boxes_rec[3][1], 10)

    def message_for_arc():
        message_to_screen("X", RED, message_boxes_arc[0][0], message_boxes_arc[0][1], 10)
        message_to_screen("Y", RED, message_boxes_arc[1][0], message_boxes_arc[1][1], 10)
        message_to_screen("THETA1", RED, message_boxes_arc[2][0], message_boxes_arc[2][1], 10)
        message_to_screen("THETA2", RED, message_boxes_arc[3][0], message_boxes_arc[3][1], 10)
        message_to_screen("RADIUS", RED, message_boxes_arc[4][0], message_boxes_arc[4][1], 10)


    def graph_draw():
        start_count = 0

        for x in range(int(SCREEN_WIDTH/2), SCREEN_WIDTH, increment_line):
            if (x == SCREEN_WIDTH/2):
                pygame.draw.line(screen, BLUE, (x, 0), (x, SCREEN_HEIGHT), 5)
            else:
                pygame.draw.line(screen, BLACK, (x, 0), (x, SCREEN_HEIGHT))

            message_to_screen(str(start_count), RED, x, SCREEN_HEIGHT/2 + 10, 10)
            start_count += npl

        start_count = 0 - npl
        for x in range( int(SCREEN_WIDTH/2) - increment_line, 0, -increment_line):
            pygame.draw.line(screen, BLACK, (x, 0), (x, SCREEN_HEIGHT))
            message_to_screen(str(start_count), RED, x, SCREEN_HEIGHT/2  + 10, 10)
            start_count -= npl

        start_count = 0
        for x in range(int(SCREEN_HEIGHT/2), SCREEN_HEIGHT, increment_line):
            if (x == SCREEN_HEIGHT/2):
                pygame.draw.line(screen, BLUE, (0, x), (SCREEN_WIDTH, x), 5)
            else:
                pygame.draw.line(screen, BLACK
                                 , (0, x), (SCREEN_WIDTH, x))
                message_to_screen(str(start_count), RED, SCREEN_WIDTH/2 + 10, x, 10)
                # message_to_screen(str(start_count), blue, 600 + 10, x, 10)
            start_count -= npl

        start_count = 0 + npl
        for x in range(int(SCREEN_HEIGHT/2) - increment_line, 0, -increment_line):
            pygame.draw.line(screen, BLACK, (0, x), (SCREEN_WIDTH, x))
            message_to_screen(str(start_count), RED, SCREEN_WIDTH/2 + 10, x, 10)
            start_count += npl

    class button():
        def __init__(self, color, x, y, width, height, text=''):
            self.color = color
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.text = text

        def draw(self, win, outline):
            # Call this method to draw the button on the screen
            if outline:
                draw_rect_outline(screen, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), (255, 0, 0), 1)

                # pygame.draw.rect(screen, (0, 100, 255), (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

            # pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

            if self.text != '':
                font = pygame.font.Font('Simple Story.ttf', 15)
                pos = pygame.mouse.get_pos()
                # print(pos[0])
                # print(pos[1])
                if (pos[0] >= self.x and pos[0] <= self.x + self.width and pos[1] >= self.y and pos[
                    1] <= self.y + self.height):
                    # print("asdhnjqwedwqe")
                    text = font.render(self.text, 1, (0, 255, 255))
                    win.blit(text, (
                        self.x + (self.width / 2 - text.get_width() / 2),
                        self.y + (self.height / 2 - text.get_height() / 2)))
                else:
                    text = font.render(self.text, 1, (RED))
                    win.blit(text, (
                        self.x + (self.width / 2 - text.get_width() / 2),
                        self.y + (self.height / 2 - text.get_height() / 2)))
                # text = font.render(self.text, 1, (RED))

        def isOver(self, pos):
            # Pos is the mouse position or a tuple of (x,y) coordinates
            if pos[0] > self.x and pos[0] < self.x + self.width:
                if pos[1] > self.y and pos[1] < self.y + self.height:
                    return True

            return False





    list_of_rectangles = []

    line_point_selected=0

    # rec_1=rectangle_draw(300, 134, 30, 30)
    # list_of_rectangles.append( rec_1 )
    # rec_2=rectangle_draw(200, 134, 30, 30)
    # list_of_rectangles.append( rec_2 )
    # rec_3=rectangle_draw(100, 134, 30, 30)
    # list_of_rectangles.append( rec_3  )
    # rec_4=rectangle_draw(50, 134, 30, 30)
    # list_of_rectangles.append( rec_4 )
    # circ_1=circle_draw(300,300,20)
    # list_of_rectangles.append( circ_1 )
    # line_1=line_draw( 40,20,100,20 )
    # list_of_rectangles.append( line_1 )
    # arc_1=arc_draw( 200,300, pi,2*pi , 100)
    # list_of_rectangles.append( arc_1)

    # pp1=[200,30,60]
    # pp2=[50,40,70]
    # poly= polygon_draw( pp1,pp2 )
    # list_of_rectangles.append( poly )

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
    current = -1
    selected = -1
    # - objects -

    rectangle = pygame.rect.Rect(260, 134, 60, 60)
    # print(rectangle.x)
    # print(rectangle.y)
    # This two are the corner values of the rectangle
    # this is the width of the rectangle
    # this is the height of the rectangle




    rectangle_draging = False

    clock = pygame.time.Clock()

    running = True

    # These are the primary buttons that needs to have
    endButton = button((255, 255, 255), 1150, 10, 40, 30, 'X')
    circleButton = button((255, 255, 255), 255, 10, 150, 30, 'Circle')
    lineButton = button((255, 255, 255), 405, 10, 150, 30, 'Line')
    recButton = button((255, 255, 255), 555, 10, 150, 30, 'Rectangle')
    arcButton = button((255, 255, 255), 705, 10, 150, 30, 'Arc')
    polyButton = button((255, 255, 255), 855, 10, 150, 30, 'Polygon')
    graphButton = button((255, 255, 255), 105, 10, 80, 30, 'Graph')
    plusButton=button((255, 255, 255), 10, 10, 30, 30, '-')
    minusButton =button((255, 255, 255), 45, 10, 30, 30, '+')
    graph_selected = 0

    # These are the buttons and textboxes for the Circle
    input_box1_circle = InputBox(10, 100, 50, 32)
    message_1_circle=(20, 140)
    input_box2_circle = InputBox(70, 100, 140, 32)
    message_2_circle = (80, 140)
    input_box3_circle = InputBox(10, 150, 140, 32)
    message_3_circle = (30, 190)
    input_boxes_circle = [input_box1_circle, input_box2_circle, input_box3_circle]
    message_boxes_circle=[message_1_circle, message_2_circle, message_3_circle  ]
    circle_input = button((255, 255, 255), 70, 150, 60, 32, 'Input')


    # These are the buttons and the textboxes for the Line
    input_box1_line = InputBox(10, 100, 50, 32)
    message_1_line = (20, 140)
    input_box2_line = InputBox(70, 100, 140, 32)
    message_2_line = (80, 140)
    input_box3_line = InputBox(10, 150, 140, 32)
    message_3_line = (20, 190)
    input_box4_line = InputBox(70, 150, 140, 32)
    message_4_line = (80, 190)
    input_boxes_line = [input_box1_line, input_box2_line, input_box3_line, input_box4_line]
    line_input = button((255, 255, 255), 10, 200, 60, 32, 'Input')
    message_boxes_line = [message_1_line, message_2_line, message_3_line, message_4_line]

    # These are the buttons and the textboxes for the rectangle
    input_box1_rec = InputBox(10, 100, 50, 32)
    message_1_rec = (20, 140)
    input_box2_rec = InputBox(70, 100, 140, 32)
    message_2_rec = (80, 140)
    input_box3_rec = InputBox(10, 150, 140, 32)
    message_3_rec = (30, 190)
    input_box4_rec = InputBox(70, 150, 140, 32)
    message_4_rec = (95, 190)
    input_boxes_rec = [input_box1_rec, input_box2_rec, input_box3_rec, input_box4_rec]
    rec_input = button((255, 255, 255), 10, 200, 60, 32, 'Input')
    rec_fill = button((255, 255, 255), 10, 250, 60, 32, 'Fill')
    message_boxes_rec = [message_1_rec, message_2_rec, message_3_rec, message_4_rec]

    # These are the buttons and the textboxes for the arc
    input_box1_arc = InputBox(10, 100, 50, 32)
    message_1_arc = (20, 140)
    input_box2_arc = InputBox(70, 100, 140, 32)
    message_2_arc = (80, 140)
    input_box3_arc = InputBox(10, 150, 140, 32)
    message_3_arc = (30, 190)
    input_box4_arc = InputBox(70, 150, 140, 32)
    message_4_arc = (90, 190)
    input_box5_arc = InputBox(10, 200, 140, 32)
    message_5_arc = (30, 240)
    message_boxes_arc = [message_1_arc, message_2_arc, message_3_arc, message_4_arc, message_5_arc]

    input_boxes_arc = [input_box1_arc, input_box2_arc, input_box3_arc, input_box4_arc, input_box5_arc]
    arc_input = button((255, 255, 255), 70, 200, 60, 32, 'Input')

    # These are the buttons and the textboxes for the polygon
    input_box1_poly = InputBox(10, 100, 50, 32)
    message_1_poly= (20, 140)
    input_box2_poly = InputBox(70, 100, 500, 32)
    message_2_poly = (80, 140)
    input_boxes_poly = [input_box1_poly, input_box2_poly]
    message_boxes_poly = [message_1_poly, message_2_poly]

    poly_input = button((255, 255, 255), 10, 150, 60, 32, 'Input')


    while running:
        #print(npl)
        # print(current)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if event.button == 1:
                    for x in range(0, len(list_of_rectangles)):
                        if (type(list_of_rectangles[x]) == (rectangle_draw)):
                            mouse_temp_x, mouse_temp_y = event.pos
                            # print(event.pos)
                            # print( list_of_rectangles[x].x )
                            # print( list_of_rectangles[x].width +  list_of_rectangles[x].x )
                            # print(list_of_rectangles[x].y)
                            # print(list_of_rectangles[x].height + list_of_rectangles[x].y)
                            if mouse_temp_x >= list_of_rectangles[x].x and \
                                    mouse_temp_x <= list_of_rectangles[x].width + list_of_rectangles[x].x and \
                                    mouse_temp_y >= list_of_rectangles[x].y and \
                                    mouse_temp_y <= list_of_rectangles[x].height + \
                                    list_of_rectangles[x].y:
                                # print("tf")
                                rectangle_draging = True
                                mouse_x, mouse_y = event.pos
                                offset_x = list_of_rectangles[x].x - mouse_x
                                offset_y = list_of_rectangles[x].y - mouse_y
                                current = x
                                selected = -1

                        if (type(list_of_rectangles[x]) == (circle_draw)):
                            mouse_temp_x, mouse_temp_y = event.pos

                            if mouse_temp_x >= list_of_rectangles[x].x - list_of_rectangles[x].r and \
                                    mouse_temp_x <= list_of_rectangles[x].x + list_of_rectangles[x].r and \
                                    mouse_temp_y >= list_of_rectangles[x].y - list_of_rectangles[x].r and \
                                    mouse_temp_y <= list_of_rectangles[x].y + list_of_rectangles[x].r and \
                                    ((list_of_rectangles[x].x - mouse_temp_x) ** 2 +
                                     (list_of_rectangles[x].y - mouse_temp_y) ** 2) ** .5 <= list_of_rectangles[x].r:

                                if (list_of_rectangles[x].width == 1):
                                    if (((list_of_rectangles[x].x - mouse_temp_x) ** 2 +
                                         (list_of_rectangles[x].y - mouse_temp_y) ** 2) ** .5 <= list_of_rectangles[
                                        x].r + 5 and
                                            ((list_of_rectangles[x].x - mouse_temp_x) ** 2 +
                                             (list_of_rectangles[x].y - mouse_temp_y) ** 2) ** .5 >= list_of_rectangles[
                                                x].r - 5
                                    ):
                                        rectangle_draging = True
                                        mouse_x, mouse_y = event.pos
                                        offset_x = list_of_rectangles[x].x - mouse_x
                                        offset_y = list_of_rectangles[x].y - mouse_y
                                        current = x
                                        selected = -1



                                else:
                                    rectangle_draging = True
                                    mouse_x, mouse_y = event.pos
                                    offset_x = list_of_rectangles[x].x - mouse_x
                                    offset_y = list_of_rectangles[x].y - mouse_y
                                    current = x
                                    selected = -1

                        if (type(list_of_rectangles[x]) == (line_draw)):
                            mouse_temp_x, mouse_temp_y = event.pos
                            temp_obj = list_of_rectangles[x]
                            if (list_of_rectangles[x].x2 - list_of_rectangles[x].x1 == 0):
                                if (mouse_temp_y >= min(list_of_rectangles[x].y1,
                                                        list_of_rectangles[x].y2) - 5 and mouse_temp_y <= max(
                                        list_of_rectangles[x].y1, list_of_rectangles[x].y2) + 5 and
                                        (mouse_temp_x >= list_of_rectangles[x].x1 - 5 and mouse_temp_x <=
                                         list_of_rectangles[x].x1 + 5)):
                                    #print("pupu")
                                    rectangle_draging = True
                                    mouse_x, mouse_y = event.pos

                                    if(line_point_selected==1):
                                        #print("dhet")
                                        offset_x = list_of_rectangles[x].x1 - mouse_x
                                        offset_y = list_of_rectangles[x].y1 - mouse_y

                                    elif (line_point_selected == 2):
                                        #print("dhet")
                                        offset_x = list_of_rectangles[x].x2 - mouse_x
                                        offset_y = list_of_rectangles[x].y2 - mouse_y

                                    else:
                                        #print("dhet")
                                        offset_x = list_of_rectangles[x].x1 - mouse_x
                                        offset_y = list_of_rectangles[x].y1 - mouse_y
                                        offset_x2 = list_of_rectangles[x].x2 - mouse_x
                                        offset_y2 = list_of_rectangles[x].y2 - mouse_y

                                    current = x
                                    selected = -1

                            elif (list_of_rectangles[x].y2 - list_of_rectangles[x].y1 == 0):
                                if (mouse_temp_x >= min(list_of_rectangles[x].x1,
                                                        list_of_rectangles[x].x2) - 5 and mouse_temp_x <= max(
                                        list_of_rectangles[x].x1, list_of_rectangles[x].x2) + 5 and
                                        (mouse_temp_y >= list_of_rectangles[x].y1 - 5 and mouse_temp_y <=
                                         list_of_rectangles[x].y1 + 5)):
                                    #print("pupu")
                                    rectangle_draging = True
                                    mouse_x, mouse_y = event.pos

                                    if(line_point_selected==1):
                                        #print("dhet")
                                        offset_x = list_of_rectangles[x].x1 - mouse_x
                                        offset_y = list_of_rectangles[x].y1 - mouse_y

                                    elif (line_point_selected == 2):
                                        #print("dhet")
                                        offset_x = list_of_rectangles[x].x2 - mouse_x
                                        offset_y = list_of_rectangles[x].y2 - mouse_y

                                    else:
                                        #print("dhet")
                                        offset_x = list_of_rectangles[x].x1 - mouse_x
                                        offset_y = list_of_rectangles[x].y1 - mouse_y
                                        offset_x2 = list_of_rectangles[x].x2 - mouse_x
                                        offset_y2 = list_of_rectangles[x].y2 - mouse_y

                                    current = x
                                    selected = -1




                            elif ( ( (round(mouse_temp_y - temp_obj.dhal * mouse_temp_x)) <= math.trunc(
                                    round(temp_obj.c))+10  or
                                 (round(mouse_temp_y - temp_obj.dhal * mouse_temp_x)) >= math.trunc(
                                        round(temp_obj.c)) - 10 ) and
                                  mouse_temp_y >= min(temp_obj.y1, temp_obj.y2)  and mouse_temp_y <= max(
                                        temp_obj.y1, temp_obj.y2)and
                                  mouse_temp_x >= min(temp_obj.x1, temp_obj.x2)  and mouse_temp_x <= max(
                                        temp_obj.x1,
                                        temp_obj.x2) ):
                                #print("pupu")
                                rectangle_draging = True
                                mouse_x, mouse_y = event.pos
                                if (line_point_selected == 1):
                                    #print("dhet")
                                    offset_x = list_of_rectangles[x].x1 - mouse_x
                                    offset_y = list_of_rectangles[x].y1 - mouse_y

                                elif (line_point_selected == 2):
                                    #print("dhet")
                                    offset_x = list_of_rectangles[x].x2 - mouse_x
                                    offset_y = list_of_rectangles[x].y2 - mouse_y

                                else:
                                    #print("dhet")
                                    offset_x = list_of_rectangles[x].x1 - mouse_x
                                    offset_y = list_of_rectangles[x].y1 - mouse_y
                                    offset_x2 = list_of_rectangles[x].x2 - mouse_x
                                    offset_y2 = list_of_rectangles[x].y2 - mouse_y

                                current = x
                                selected = -1

                        if (type(list_of_rectangles[x]) == (arc_draw)):
                            mouse_temp_x, mouse_temp_y = event.pos
                            temp_obj = list_of_rectangles[x]
                            cone = -((((math.atan(
                                (temp_obj.y - mouse_temp_y) / (temp_obj.x - mouse_temp_x + 000000000.1))))) * 180) / pi
                            if (cone < 0):
                                cone = 180 - abs(cone)

                            if (mouse_temp_y > temp_obj.y):
                                cone += 180

                            cone = (cone * pi) / 180

                            # print(temp_obj.y)
                            # print(mouse_temp_y)
                            # print(temp_obj.x)
                            # print(mouse_temp_x)
                            # print(cone)

                            if (mouse_temp_x >= temp_obj.x - temp_obj.r and
                                    mouse_temp_x <= temp_obj.x + temp_obj.r and
                                    mouse_temp_y >= temp_obj.y - temp_obj.r and
                                    mouse_temp_y <= temp_obj.y + temp_obj.r and
                                    cone >= temp_obj.start and
                                    cone <= temp_obj.end and
                                    ((mouse_temp_x - temp_obj.x) ** 2 + (
                                            mouse_temp_y - temp_obj.y) ** 2) ** 0.5 <= temp_obj.r + 5
                                    and ((mouse_temp_x - temp_obj.x) ** 2 + (
                                            mouse_temp_y - temp_obj.y) ** 2) ** 0.5 >= temp_obj.r - 5
                            ):
                                rectangle_draging = True
                                mouse_x, mouse_y = event.pos
                                offset_x = list_of_rectangles[x].x - mouse_x
                                offset_y = list_of_rectangles[x].y - mouse_y
                                current = x
                                selected = -1
                        if (type(list_of_rectangles[x]) == (polygon_draw)):
                            coords = list_of_rectangles[x].get_polygon()
                            poly = Polygon(coords)
                            mouse_temp_x, mouse_temp_y = event.pos
                            p1 = Point(mouse_temp_x, mouse_temp_y)

                            if (p1.within(poly)):
                                offset_x_list = []
                                offset_y_list = []
                                rectangle_draging = True
                                current = x
                                selected = -1
                                for i in range(len(coords)):
                                    offset_x_list.append(mouse_temp_x - coords[i][0])

                                for i in range(len(coords)):
                                    offset_y_list.append(mouse_temp_y - coords[i][1])

                if (current != -1):
                    if (type(list_of_rectangles[current]) == (circle_draw)):
                        if (list_of_rectangles[current].circle_fill.isOver(pygame.mouse.get_pos())):
                            if (list_of_rectangles[current].width == 0):
                                list_of_rectangles[current].width = 1
                            else:
                                list_of_rectangles[current].width = 0

                        if (list_of_rectangles[current].circle_back.isOver(pygame.mouse.get_pos())):
                            tempi = list_of_rectangles[current]
                            del list_of_rectangles[current]
                            list_of_rectangles.insert(0, tempi)
                            current = 0
                            #print("Backed")

                        if (list_of_rectangles[current].circle_delete.isOver(pygame.mouse.get_pos())):
                            del list_of_rectangles[current]
                            current = -1
                            continue


                    elif (type(list_of_rectangles[current]) == (line_draw)):
                        if (list_of_rectangles[current].line_back.isOver(pygame.mouse.get_pos())):
                            tempi = list_of_rectangles[current]
                            del list_of_rectangles[current]
                            list_of_rectangles.insert(0, tempi)
                            current = 0
                            #print("Backed")

                        if (list_of_rectangles[current].line_delete.isOver(pygame.mouse.get_pos())):
                            del list_of_rectangles[current]
                            current = -1
                            continue


                        if( list_of_rectangles[current].line_pt1.isOver(pygame.mouse.get_pos()) ):
                            if( list_of_rectangles[current].pt1_selected==0 ):
                                list_of_rectangles[current].pt1_selected=1
                                list_of_rectangles[current].pt2_selected = 0
                                line_point_selected=1
                            else:
                                list_of_rectangles[current].pt1_selected = 0
                                line_point_selected = 0

                        if (list_of_rectangles[current].line_pt2.isOver(pygame.mouse.get_pos())):
                            if (list_of_rectangles[current].pt2_selected == 0):
                                #print("poppop")
                                list_of_rectangles[current].pt2_selected = 1
                                list_of_rectangles[current].pt1_selected = 0
                                line_point_selected = 2
                            else:
                                list_of_rectangles[current].pt2_selected = 0
                                line_point_selected = 0








                    elif (type(list_of_rectangles[current]) == (rectangle_draw)):
                        if (list_of_rectangles[current].rec_back.isOver(pygame.mouse.get_pos())):
                            tempi = list_of_rectangles[current]
                            del list_of_rectangles[current]
                            list_of_rectangles.insert(0, tempi)
                            current = 0
                            #print("Backed")

                        if (list_of_rectangles[current].rec_fill.isOver(pygame.mouse.get_pos())):
                            if (list_of_rectangles[current].fill == 0):
                                list_of_rectangles[current].fill = 1
                            else:
                                list_of_rectangles[current].fill = 0

                        if (list_of_rectangles[current].rec_delete.isOver(pygame.mouse.get_pos())):
                            del list_of_rectangles[current]
                            current = -1
                            continue





                    elif (type(list_of_rectangles[current]) == (polygon_draw)):
                        if (list_of_rectangles[current].poly_back.isOver(pygame.mouse.get_pos())):
                            tempi = list_of_rectangles[current]
                            del list_of_rectangles[current]
                            list_of_rectangles.insert(0, tempi)
                            current = 0
                            #print("Backed")

                        if (list_of_rectangles[current].poly_fill.isOver(pygame.mouse.get_pos())):
                            if (list_of_rectangles[current].fill == 0):
                                list_of_rectangles[current].fill = 1
                            else:
                                list_of_rectangles[current].fill = 0

                        if (list_of_rectangles[current].poly_delete.isOver(pygame.mouse.get_pos())):
                            del list_of_rectangles[current]
                            current = -1
                            continue

                    elif (type(list_of_rectangles[current]) == (arc_draw)):
                        if (list_of_rectangles[current].arc_delete.isOver(pygame.mouse.get_pos())):
                            del list_of_rectangles[current]
                            current = -1
                            continue

                if circleButton.isOver(pos):
                    # print("clicked")
                    selected = 1
                    current = -1

                if lineButton.isOver(pos):
                    # print("clicked")
                    selected = 2
                    current = -1

                if recButton.isOver(pos):
                    # print("clicked")
                    selected = 3
                    current = -1

                if arcButton.isOver(pos):
                    # print("clicked")
                    selected = 4
                    current = -1

                if polyButton.isOver(pos):
                    # print("clicked")
                    selected = 5
                    current = -1

                if (graphButton.isOver(pos)):
                    if (graph_selected == 0):
                        graph_selected = 1
                        current = -1
                    else:
                        graph_selected = 0
                        current = -1
                    # current = -1

                if (endButton.isOver(pos)):
                    import main
                    running = False
                    main.go()
                    pygame.quit()
                    return


                if( plusButton.isOver(pos) ):

                    npl+=1
                    #increment_line+=1
                    perspective = (SCREEN_WIDTH / 2) / ((increment_line - 1) * npl)
                    for oop in list_of_rectangles:
                        oop.adjust(npl-1)


                    #increment_line+=1

                if (minusButton.isOver(pos)):
                    if(npl==1):
                        continue
                    npl -= 1
                    perspective = (SCREEN_WIDTH / 2) / ((increment_line - 1) * npl)
                    # increment_line+=1
                    for oop in list_of_rectangles:
                        oop.adjust(npl+1)




                if (selected == 1):
                    if (circle_input.isOver(pos)):
                        circ_1 = circle_draw(600 + (float(input_box1_circle.text) * increment_line) / npl,
                                             SCREEN_HEIGHT - (400 + (float(
                                                 input_box2_circle.text) * increment_line) / npl),
                                             perspective * float(input_box3_circle.text))
                        input_box1_circle.change_text()
                        input_box1_circle.txt_surface = FONT.render(input_box1_circle.text, True,
                                                                    input_box1_circle.color)
                        input_box2_circle.change_text()
                        input_box2_circle.txt_surface = FONT.render(input_box2_circle.text, True,
                                                                    input_box2_circle.color)
                        input_box3_circle.change_text()
                        input_box3_circle.txt_surface = FONT.render(input_box3_circle.text, True,
                                                                    input_box3_circle.color)
                        list_of_rectangles.append(circ_1)

                if (selected == 2):
                    if (line_input.isOver(pos)):
                        line_1 = line_draw(600 + (float(input_box1_line.text) * increment_line) / npl,
                                           SCREEN_HEIGHT - (400 + (
                                                       float(input_box2_line.text) * increment_line) / npl),
                                           600 + (float(input_box3_line.text) * increment_line) / npl,
                                           SCREEN_HEIGHT - (400 + (
                                                       float(input_box4_line.text) * increment_line) / npl))
                        input_box1_line.change_text()
                        input_box1_line.txt_surface = FONT.render(input_box1_line.text, True, input_box1_line.color)
                        input_box2_line.change_text()
                        input_box2_line.txt_surface = FONT.render(input_box2_line.text, True, input_box2_line.color)
                        input_box3_line.change_text()
                        input_box3_line.txt_surface = FONT.render(input_box3_line.text, True, input_box3_line.color)
                        input_box4_line.change_text()
                        input_box4_line.txt_surface = FONT.render(input_box4_line.text, True, input_box4_line.color)
                        list_of_rectangles.append(line_1)

                if (selected == 3):
                    if (rec_input.isOver(pos)):
                        rec_1 = rectangle_draw(600 + (int(input_box1_rec.text) * increment_line) / npl,
                                               SCREEN_HEIGHT - (400 + (int(
                                                   input_box2_rec.text) * increment_line) / npl),
                                               int(input_box3_rec.text) * perspective,
                                               int(input_box4_rec.text) * perspective)
                        input_box1_rec.change_text()
                        input_box1_rec.txt_surface = FONT.render(input_box1_rec.text, True, input_box1_rec.color)
                        input_box2_rec.change_text()
                        input_box2_rec.txt_surface = FONT.render(input_box2_rec.text, True, input_box2_rec.color)
                        input_box3_rec.change_text()
                        input_box3_rec.txt_surface = FONT.render(input_box3_rec.text, True, input_box3_rec.color)
                        input_box4_rec.change_text()
                        input_box4_rec.txt_surface = FONT.render(input_box4_rec.text, True, input_box4_rec.color)
                        list_of_rectangles.append(rec_1)

                if (selected == 4):
                    if (arc_input.isOver(pos)):
                        arc_1 = arc_draw(600 + (int(input_box1_arc.text) * increment_line) / npl,
                                         SCREEN_HEIGHT - (400 + (
                                                     int(input_box2_arc.text) * increment_line) / npl),
                                         round(float(input_box3_arc.text) * (pi / 180), 3),
                                         round(float(input_box4_arc.text) * (pi / 180), 3),
                                         int(input_box5_arc.text) * perspective)
                        input_box1_arc.change_text()
                        input_box1_arc.txt_surface = FONT.render(input_box1_arc.text, True, input_box1_arc.color)
                        input_box2_arc.change_text()
                        input_box2_arc.txt_surface = FONT.render(input_box2_arc.text, True, input_box2_arc.color)
                        input_box3_arc.change_text()
                        input_box3_arc.txt_surface = FONT.render(input_box3_arc.text, True, input_box3_arc.color)
                        input_box4_arc.change_text()
                        input_box4_arc.txt_surface = FONT.render(input_box4_arc.text, True, input_box4_arc.color)
                        input_box5_arc.change_text()
                        input_box5_arc.txt_surface = FONT.render(input_box5_arc.text, True, input_box5_arc.color)

                        list_of_rectangles.append(arc_1)

                if (selected == 5):
                    if (poly_input.isOver(pos)):

                        for i in range(0, len(input_box1_poly.pp)):
                            input_box1_poly.pp[i] = 600 + (input_box1_poly.pp[i] * increment_line) / npl

                        for i in range(0, len(input_box2_poly.pp)):
                            input_box2_poly.pp[i] = SCREEN_HEIGHT - (
                                        400 + (input_box2_poly.pp[i] * increment_line) / npl)

                        poly_1 = polygon_draw(input_box1_poly.pp, input_box2_poly.pp)
                        input_box1_poly.change_text()
                        input_box1_poly.txt_surface = FONT.render(input_box1_poly.text, True, input_box1_poly.color)
                        input_box2_poly.change_text()
                        input_box2_poly.txt_surface = FONT.render(input_box2_poly.text, True, input_box2_poly.color)
                        input_box1_poly.pp.clear()
                        input_box2_poly.pp.clear()

                        list_of_rectangles.append(poly_1)


            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    rectangle_draging = False

            elif event.type == pygame.MOUSEMOTION:
                if rectangle_draging:

                    if (type(list_of_rectangles[current]) == (line_draw) and line_point_selected==0):
                        mouse_x, mouse_y = event.pos
                        list_of_rectangles[current].x1 = mouse_x + offset_x
                        list_of_rectangles[current].y1 = mouse_y + offset_y
                        list_of_rectangles[current].x2 = mouse_x + offset_x2
                        list_of_rectangles[current].y2 = mouse_y + offset_y2

                        if ((list_of_rectangles[current].x2 - list_of_rectangles[current].x1) == 0):
                            list_of_rectangles[current].dhal = math.trunc(round(
                                (list_of_rectangles[current].y2 - list_of_rectangles[current].y1) / (
                                    0.000000001)))

                        else:
                            list_of_rectangles[current].dhal = math.trunc(round(
                                (list_of_rectangles[current].y2 - list_of_rectangles[current].y1) / (
                                            list_of_rectangles[current].x2 - list_of_rectangles[current].x1)))
                            list_of_rectangles[current].c = math.trunc(round(list_of_rectangles[current].y1 - (
                                        list_of_rectangles[current].dhal * list_of_rectangles[current].x1)))

                    if (type(list_of_rectangles[current]) == (polygon_draw)):
                        mouse_x, mouse_y = event.pos
                        temp_obj = list_of_rectangles[current]
                        for i in range(0, len(offset_x_list)):
                            temp_obj.list_of_x[i] = mouse_x - offset_x_list[i]

                        for i in range(0, len(offset_y_list)):
                            temp_obj.list_of_y[i] = mouse_y - offset_y_list[i]


                    elif( type(list_of_rectangles[current]) == (line_draw) and line_point_selected==1 ):
                        mouse_x, mouse_y = event.pos
                        list_of_rectangles[current].x1 = mouse_x + offset_x
                        list_of_rectangles[current].y1 = mouse_y + offset_y

                    elif (type(list_of_rectangles[current]) == (line_draw) and line_point_selected == 2):
                        mouse_x, mouse_y = event.pos
                        list_of_rectangles[current].x2 = mouse_x + offset_x
                        list_of_rectangles[current].y2 = mouse_y + offset_y
                        #print("ajsdhqwbe")


                    else:

                        mouse_x, mouse_y = event.pos
                        list_of_rectangles[current].x = mouse_x + offset_x
                        list_of_rectangles[current].y = mouse_y + offset_y

            if (selected == 1):
                for box in input_boxes_circle:
                    box.handle_event(event)
            if (selected == 2):
                for box in input_boxes_line:
                    box.handle_event(event)

            if (selected == 3):
                for box in input_boxes_rec:
                    box.handle_event(event)

            if (selected == 4):
                for box in input_boxes_arc:
                    box.handle_event(event)

            if (selected == 5):
                for box in input_boxes_poly:
                    box.handle_event(event)

        if (selected == 1):
            for box in input_boxes_circle:
                box.update()

        if (selected == 2):
            for box in input_boxes_line:
                box.update()

        if (selected == 3):
            for box in input_boxes_rec:
                box.update()

        if (selected == 4):
            for box in input_boxes_arc:
                box.update()

        if (selected == 5):
            for box in input_boxes_poly:
                box.update()

        screen.fill(WHITE)

        if (current != -1):
            list_of_rectangles[current].draw()

        for obj in list_of_rectangles:
            if (type(obj) == (rectangle_draw)):
                temp_rect = (obj.x, obj.y, obj.height, obj.width)
                pygame.draw.rect(screen, RED, temp_rect, obj.fill)



            elif (type(obj) == (circle_draw)):
                temp_rect = (obj.x, obj.y)
                # print(temp_rect)
                pygame.draw.circle(screen, RED, temp_rect, obj.r, obj.width)

            elif (type(obj) == (line_draw)):
                temp_rect = (obj.x1, obj.y1)
                pygame.draw.line(screen, RED, temp_rect, (obj.x2, obj.y2))
                if(obj.pt1_selected==1 ):
                    pygame.draw.circle(screen, RED, temp_rect, 5, 1)

                if(obj.pt2_selected==1 ):
                    pygame.draw.circle(screen, RED,   (obj.x2, obj.y2)  , 5, 1)



            elif (type(obj) == (arc_draw)):
                # temp_rect = (obj.x, obj.y1)
                pygame.draw.arc(screen, RED, [obj.x - obj.r, obj.y - obj.r, 2 * obj.r, 2 * obj.r], obj.start, obj.end)

            elif (type(obj) == (polygon_draw)):
                wow = []

                pygame.draw.polygon(screen, RED, obj.get_polygon(), obj.fill)

        if (graph_selected == 1):
            graph_draw()

        # This are all the basic buttons
        endButton.draw(screen, (0, 0, 0))
        circleButton.draw(screen, (0, 0, 0))
        lineButton.draw(screen, (0, 0, 0))
        recButton.draw(screen, (0, 0, 0))
        arcButton.draw(screen, (0, 0, 0))
        polyButton.draw(screen, (0, 0, 0))
        graphButton.draw(screen, (0, 0, 0))
        plusButton.draw(screen, (0,0,0))
        minusButton.draw(screen, (0, 0, 0))

        # These are buttons and text boxes for circle
        if (selected == 1):
            for box in input_boxes_circle:
                box.draw(screen)
            circle_input.draw(screen, (0, 0, 0))
            #message_to_screen(str(234324), RED, 50, 50, 50)

            message_for_circle()

        if (selected == 2):
            for box in input_boxes_line:
                box.draw(screen)
            line_input.draw(screen, (0, 0, 0))
            message_for_line()



        if (selected == 3):
            for box in input_boxes_rec:
                box.draw(screen)
            rec_input.draw(screen, (0, 0, 0))

            message_for_rec()


        if (selected == 4):
            for box in input_boxes_arc:
                box.draw(screen)
            arc_input.draw(screen, (0, 0, 0))

            message_for_arc()



        if (selected == 5):
            for box in input_boxes_poly:
                box.draw(screen)
            poly_input.draw(screen, (0, 0, 0))
            message_to_screen("X", RED, message_boxes_poly[0][0], message_boxes_poly[0][1], 10)
            message_to_screen("Y", RED, message_boxes_poly[1][0], message_boxes_poly[1][1], 10)

        # I have to use this using for loop
        # pygame.draw.rect(screen, RED, rectangle)

        pygame.display.flip()

        # - constant game speed / FPS -

        clock.tick(FPS)

    # - end -

    pygame.quit()