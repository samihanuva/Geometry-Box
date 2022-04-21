def work():
    import pygame
    import time
    import random
    import pygame.freetype
    pygame.freetype.init()
    pygame.init()
    import sympy
    from sympy import solve, Poly, Eq, Function, exp, root
    from sympy import symbols, Eq, solve, sympify
    from sympy.parsing.sympy_parser import parse_expr
    import math

    display_width = 1200
    display_height = 800
    increment_line = 25
    main_line_width = 5
    number_per_line = 1
    middle = display_width / 2
    left_edge = -(display_width / increment_line)
    up_edge = -(display_height / increment_line)
    increment_per_iterate = ((number_per_line / increment_line) * 10) / 2
    equation_number = 1
    list_of_points = []
    list_of_points_2 = []
    start_1 = (left_edge) * number_per_line
    start_2 = (up_edge) * number_per_line
    graph_start_left = round((-number_per_line * (display_width / (2 * increment_line))))
    graph_start_up = round(-(-number_per_line * (display_height / (2 * increment_line))))

    def text_objects(msg, color, sizi):
        font = pygame.font.Font("ka1.ttf", sizi)
        textSurface = font.render(msg, True, color)
        return textSurface, textSurface.get_rect()

    def message_to_screen(msg, color, x_position, y_position, size):
        textSurf, textRect = text_objects(msg, color, size)
        textRect.center = (x_position, y_position)
        gameDisplay.blit(textSurf, textRect)

    gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)

    white = (255, 255, 255)
    black = (0, 0, 0)
    blue = (0, 0, 255)
    red = (255, 0, 0)

    def draw_graph():
        start = display_width / 2
        start_count = 0

        for x in range(600, display_width, increment_line):

            if (x == 600):
                pygame.draw.line(gameDisplay, red, (x, 0), (x, display_height), main_line_width)

            else:

                pygame.draw.line(gameDisplay, black, (x, 0), (x, display_height))

            message_to_screen(str(start_count), blue, x, 400 + 10, 10)
            start_count += number_per_line

        start_count = 0 - number_per_line
        for x in range(600 - increment_line, 0, -increment_line):
            pygame.draw.line(gameDisplay, black, (x, 0), (x, display_height))
            message_to_screen(str(start_count), blue, x, 400 + 10, 10)
            start_count -= number_per_line

        start_count = 0
        for x in range(400, display_height, increment_line):
            if (x == 400):
                pygame.draw.line(gameDisplay, red, (0, x), (display_width, x), main_line_width)
            else:
                pygame.draw.line(gameDisplay, black, (0, x), (display_width, x))
                message_to_screen(str(start_count), blue, 600 + 10, x, 10)

            start_count -= number_per_line

        start_count = 0 + number_per_line
        for x in range(400 - increment_line, 0, -increment_line):
            pygame.draw.line(gameDisplay, black, (0, x), (display_width, x))
            message_to_screen(str(start_count), blue, 600 + 10, x, 10)
            start_count += number_per_line

    def arrange_equation(lala):
        one = ""
        two = ""
        three = ""
        flag = 0

        for i in range(len(lala)):
            if lala[i] == '=':
                flag = 1
                continue

            if (flag == 0):
                if (lala[i] == 'y'):
                    one += "(-y)"
                elif (lala[i] == '^'):
                    one += '**'
                else:
                    one += lala[i]

            else:
                if (lala[i] == 'y'):
                    two += "(-y)"
                elif (lala[i] == '^'):
                    two += '**'
                else:
                    two += lala[i]

        three += one + '-' + '(' + two + ')'
        return three

    print(graph_start_up)

    def solve_geometry(dd):
        x, y = symbols('x y')

        dd = arrange_equation(dd)
        # eq1 = Eq( x + y**2  , 10 ) # y er age for some unknown reason - boshate hoe, or else kaj kore na :3
        ii = dd
        eq1 = Eq(parse_expr(ii), 0)

        from_left = graph_start_left
        from_up = graph_start_up

        eq2 = Eq(x, from_left)
        eq3 = Eq(y, from_up)

        add = increment_per_iterate
        right_limit = -from_left
        down_limit = -from_up

        while (True):

            if (from_left > right_limit):
                break

            if (abs(from_left) >= 0 and abs(from_left) <= 0.001):
                from_left += add
                eq2 = Eq(x, round(from_left, 3))
                print("lol")
                continue

            # print(eq1)
            # print(eq2)
            sol = solve((eq1, eq2), (x, y))
            print(eq1)
            print(eq2)
            print(sol)

            # print(sol)

            flag = 0

            print(type(sol))

            if (type(sol) == dict):
                flag = 1
                print(flag)
                # pygame.draw.circle(gameDisplay, red, (1200 + (sol[x] * increment_line) / number_per_line,
                #                                       400 + (sol[y] * increment_line) / number_per_line), 5)
                if (len(sol) == 1):
                    from_left += add
                    eq2 = Eq(x, round(from_left, 3))
                    continue

                list_of_points.append([600 + ((sol[x]) * increment_line) / number_per_line,
                                       400 + ((sol[y]) * increment_line) / number_per_line])
                print("tulululu")

            from_left += add
            eq2 = Eq(x, round(from_left, 3))
            print(flag)

            if (flag == 1):
                continue
            for p in range(0, len(sol), 1):
                print(flag)
                val = complex(sol[p][1])
                if (val.imag == 0):
                    print("yes")
                    # pygame.draw.circle(gameDisplay, red, ( 1200+ (sol[p][0]*increment_line)/number_per_line ,400+ (  sol[p][1]*increment_line )/number_per_line), 5  )

                    list_of_points.append([600 + (sol[p][0] * increment_line) / number_per_line,
                                           400 + (sol[p][1] * increment_line) / number_per_line])


                else:
                    print("no")

        while (True):

            if (from_up < (down_limit)):
                break
            # print(eq1)
            # print(eq2)

            if (abs(from_up) >= 0 and abs(from_up) <= 0.001):
                from_up -= add
                eq3 = Eq(y, round(from_up, 3))
                print("lol")
                continue

            sol = solve((eq1, eq3), (x, y))
            print(eq1)
            print(eq3)
            print(sol)

            # print(sol)

            flag = 0

            if (type(sol) == dict):
                flag = 1
                # pygame.draw.circle(gameDisplay, red, (1200 + (sol[x] * increment_line) / number_per_line,
                #                                       400 + (sol[y] * increment_line) / number_per_line), 5)
                if (len(sol) == 1):
                    from_up -= add
                    eq3 = Eq(y, round(from_up, 3))
                    continue

                list_of_points_2.append([600 + ((sol[x]) * increment_line) / number_per_line,
                                         400 + ((sol[y]) * increment_line) / number_per_line])

            from_up -= add
            eq3 = Eq(y, round(from_up, 3))

            if (flag == 1):
                continue
            for p in range(0, len(sol), 1):

                val = complex(sol[p][0])
                if (val.imag == 0):
                    print("yes")
                    # pygame.draw.circle(gameDisplay, red, ( 1200+ (sol[p][0]*increment_line)/number_per_line ,400+ (  sol[p][1]*increment_line )/number_per_line), 5  )
                    list_of_points_2.append([600 + (sol[p][0] * increment_line) / number_per_line,
                                             400 + (sol[p][1] * increment_line) / number_per_line])


                else:
                    print("no")

    def draw_geometry():
        for i in range(len(list_of_points)):
            print(list_of_points[i])
            print(list_of_points[i][0])
            print(list_of_points[i][1])
            pygame.draw.circle(gameDisplay, red, (list_of_points[i][0], list_of_points[i][1]), 5)

        for i in range(len(list_of_points_2)):
            print(list_of_points_2[i])
            print(list_of_points_2[i][0])
            print(list_of_points_2[i][1])
            pygame.draw.circle(gameDisplay, red, (list_of_points_2[i][0], list_of_points_2[i][1]), 5)

    def adjust_point(val):
        nonlocal number_per_line
        if (number_per_line + val >= 1 and number_per_line + val <= 20):
            prev = number_per_line
            number_per_line += val

            global graph_start_left
            graph_start_left = round((-number_per_line * (display_width / (2 * increment_line))))
            global graph_start_up
            graph_start_up = round(-(-number_per_line * (display_height / (2 * increment_line))))
            print("cutush")

            for pp in range(len(list_of_points)):
                # list_of_points[pp]=(list_of_points[pp]*number_per_line)/prev
                list_of_points[pp][0] = ((list_of_points[pp][0] - 600) * (prev / increment_line))
                list_of_points[pp][0] = 600 + (list_of_points[pp][0] * increment_line) / number_per_line
                list_of_points[pp][1] = ((list_of_points[pp][1] - 400) * (prev / increment_line))
                list_of_points[pp][1] = 400 + ((list_of_points[pp][1]) * increment_line) / number_per_line

            for pp in range(len(list_of_points_2)):
                # list_of_points_2[pp]=(list_of_points_2[pp]*number_per_line)/prev
                # list_of_points_2[pp]=float(1)
                list_of_points_2[pp][0] = ((list_of_points_2[pp][0] - 600) * (prev / increment_line))
                list_of_points_2[pp][0] = 600 + (list_of_points_2[pp][0] * increment_line) / number_per_line
                list_of_points_2[pp][1] = ((list_of_points_2[pp][1] - 400) * (prev / increment_line))
                list_of_points_2[pp][1] = 400 + ((list_of_points_2[pp][1]) * increment_line) / number_per_line

    def gameloop():
        font = pygame.font.Font("Wishleman.ttf", 30)
        gameexit = 1
        input_box_1 = pygame.Rect(10, 10, 1, 32)  # this is for giving the input equation
        input_box_2 = pygame.Rect(10, 45, 1, 32)  # This is for the mouse Location
        input_box_3 = pygame.Rect(1160, 10, 1, 32)  # for zoom in
        input_box_4 = pygame.Rect(50, 80, 1, 32)  # for zoom out

        active_1 = False
        text_1 = ""  # this is for the equation
        text_2 = ""  # this is for the mouse location
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        button_color_1 = color_inactive

        # solve_geometry("x + 5")
        while (gameexit):
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    gameexit = 0
                    break

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if input_box_1.collidepoint(event.pos):
                        # Toggle the active variable.
                        active_1 = not active_1
                        color = color_active

                    if input_box_3.collidepoint(event.pos):
                        import main
                        main.go()

                    if input_box_4.collidepoint(event.pos):
                        adjust_point(1)

                if event.type == pygame.KEYDOWN:

                    if active_1:
                        if event.key == pygame.K_RETURN:
                            if active_1 == True:
                                # print(text_1)
                                # size_of_list = int(text_1)
                                # number_flag = 1
                                active_1 = False
                                color = color_inactive
                                op = text_1
                                text_1 = ""
                                solve_geometry(str(op))


                        elif event.key == pygame.K_BACKSPACE:
                            if active_1 == True:
                                text_1 = text_1[:-1]
                        else:
                            if active_1 == True:
                                text_1 += event.unicode
                                print(text_1)
                                # if int(text_1) > 20:
                                # text_1 = text_1[:-1]

            mouse = pygame.mouse.get_pos()
            mouse_text_x = str(round((-number_per_line * (display_width / (2 * increment_line)) + (
                        (mouse[0]) * number_per_line) / increment_line), 2))
            mouse_text_y = str(round(-(-number_per_line * (display_height / (2 * increment_line)) + (
                        (mouse[1]) * number_per_line) / increment_line), 2))
            text_2 = mouse_text_x + ' , ' + mouse_text_y

            gameDisplay.fill(white)
            draw_geometry()

            draw_graph()

            zoom_in_color = color_inactive
            zoom_out_color = color_inactive

            input_box_1.w = 500
            input_box_2.w = 170
            input_box_3.w = 40
            input_box_4.w = 40

            if (mouse[0] >= input_box_3.x and mouse[0] <= input_box_3.x + input_box_3.w and mouse[
                1] >= input_box_3.y and mouse[1] <= input_box_3.y + 32):
                zoom_in_color = red

            if (mouse[0] >= input_box_4.x and mouse[0] <= input_box_4.x + input_box_4.w and mouse[
                1] >= input_box_4.y and mouse[1] <= input_box_4.y + 32):
                zoom_out_color = red

            txt_surface = font.render(text_1, True, color_active)
            txt_surface_2 = font.render(text_2, True, color_active)
            txt_surface_3 = font.render("X", True, zoom_in_color)
            #txt_surface_4 = font.render("-", True, zoom_out_color)

            gameDisplay.blit(txt_surface, (input_box_1.x + 35, input_box_1.y))
            gameDisplay.blit(txt_surface_2, (input_box_2.x + 10, input_box_2.y))
            gameDisplay.blit(txt_surface_3, (input_box_3.x + 10, input_box_3.y))
            #gameDisplay.blit(txt_surface_4, (input_box_4.x + 10, input_box_4.y))

            pygame.draw.rect(gameDisplay, color, input_box_1, 5)
            pygame.draw.rect(gameDisplay, color_active, input_box_2, 5)
            pygame.draw.rect(gameDisplay, color_active, input_box_3, 5)
            #pygame.draw.rect(gameDisplay, color_active, input_box_4, 5)

            # solve_geometry()

            pygame.display.update()

    gameloop()