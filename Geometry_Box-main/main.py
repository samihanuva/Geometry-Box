
def pp():
    # from tkinter import *
    from tkinter.ttk import Scale
    from tkinter import colorchooser, filedialog, messagebox, LabelFrame, Button, RIDGE, VERTICAL, Canvas, GROOVE, Tk
    from tkinter.font import Font
    # from PIL import image
    # import pil.ImageGrab as ImageGrab
    class Paint():
        def __init__(self, root):

            self.root = root
            self.root.title("Paint")
            self.root.geometry("1540x860")
            # self.root.geometry("800x520")
            self.root.configure(background='white')
            self.root.resizable(0, 0)

            # imp things
            self.pen_color = "black"
            self.eraser_color = "white"
            # self.myFont = font.Font(family='Courier')

            # trying lines###
            # self.my_canvas=Canvas(root, width=200, height=300, bg="black")
            # self.my_canvas.pack(pady=20)
            # self.my_canvas.create_line(0,100,300,100,fill="red")

            self.color_frame = LabelFrame(self.root, text='COLOR', font=('MS serif', 11, 'bold'), bd=5, relief=RIDGE,
                                          bg="white", fg="gray")
            self.color_frame.place(x=0, y=30, width=70, height=185)
            colors = ['#ff0000', '#ff6600', '#99ff33', '#00ffff', '#ff99ff', '#ffffff', '#800000', '#ffff00', '#006600',
                      '#000099', '#6600cc', '#000000']
            i = j = 0
            for color in colors:
                Button(self.color_frame, bg=color, bd=2, relief=RIDGE, width=3,
                       command=lambda col=color: self.select_color(col)).grid(row=i, column=j)
                i += 1
                if i == 6:
                    i = 0
                    j = 1
            self.pen_button = Button(self.root, text="Draw", font=('MS serif', 12, 'bold'), bd=4, bg='#ffffcc',
                                     fg='#cc9900', command=self.ink, width=6, relief=RIDGE)
            self.pen_button.place(x=0, y=240)

            self.eraser_button = Button(self.root, text="Erase", font=('MS serif', 12, 'bold'), bd=4, bg='#ccffff',
                                        fg='#000066', command=self.eraser, width=6, relief=RIDGE)
            self.eraser_button.place(x=0, y=290)

            self.canvas_color_button = Button(self.root, text="Canvas", font=('MS serif', 12, 'bold'), fg='#993366',
                                              bd=4, bg='#ffcccc', command=self.canvas_color, width=6, relief=RIDGE)
            self.canvas_color_button.place(x=0, y=340)

            self.clear_button = Button(self.root, text="Clear", font=('MS serif', 12, 'bold'), bd=4, bg='#ccff99',
                                       fg='#006600', command=lambda: self.canvas.delete("all"), width=6, relief=RIDGE)
            self.clear_button.place(x=0, y=390)

            # activebackground='#000000'

            # self.save_button = Button(self.root,text="Save",font= ('MS serif',10,'bold'),fg='#006600',bd=4,bg='#ccff99',command=None,width=6,relief=RIDGE)
            # self.save_button = Button(self.root,text="Save",font= ('MS serif',10,'bold'),fg='#006600',bd=4,bg='#ccff99',command=None,width=6,relief=RIDGE)
            # self.save_button.place(x=0,y=277)

            # self.canvas_line_button = Button(self.root,text="Line",font=('MS serif',10,'bold'),fg='#600080',bd=4,bg='#ffccff',command=self.line_draw,width=6,relief=RIDGE)
            # self.canvas_line_button.place(x=0,y=307)

            # self.canvas_sqare_button = Button(self.root,text="Sqare",font=('Fixedsys',10,'bold'),fg='#993366',bd=4,bg='#ffff99',command=self.sqare_draw,width=3,relief=RIDGE)
            # self.canvas_sqare_button.place(x=40,y=315)

            # creating a scale for pen and eraser resizable

            self.pen_size_scale_frame = LabelFrame(self.root, text="SIZE", bd=5, bg='white', fg='gray',
                                                   font=('MS serif', 12, 'bold'), relief=RIDGE)
            self.pen_size_scale_frame.place(x=0, y=450, height=230, width=70)

            self.pen_size = Scale(self.pen_size_scale_frame, orient=VERTICAL, from_=80, to=0, length=200)
            self.pen_size.set(1)
            self.pen_size.grid(row=0, column=1, padx=15)

            # creating canvas_color_button
            self.canvas = Canvas(self.root, bg='white', bd=5, relief=GROOVE, height=770, width=1400)
            self.canvas.place(x=80, y=10)

            # bind the canvas with mouse drag
            self.canvas.bind("<B1-Motion>", self.paint)
            # func defined here

        def paint(self, event):

            x1, y1 = (event.x - 2), (event.y - 2)
            x2, y2 = (event.x + 2), (event.y + 2)

            self.canvas.create_oval(x1, y1, x2, y2, fill=self.pen_color, outline=self.pen_color,
                                    width=self.pen_size.get())

        def select_color(self, col):
            self.pen_color = col

        # eraser func
        def eraser(self):
            self.pen_color = self.eraser_color

        def ink(self):
            self.pen_color = "black"

        def canvas_color(self):
            color = colorchooser.askcolor()
            # print(color[1])
            self.canvas.configure(background=color[1])
            self.eraser_color = color[1]

        def line_draw(self):
            self.canvas.create_line(210, 250, 500, 250, fill=self.pen_color)

            # self.canvas.bind("B2-Motion",self.sqare_again)

        #    def sqare_again(self,paint):
        # width=100

        def sqare_draw(self):
            self.canvas.create_rectangle(250, 150, 400, 300, outline=self.pen_color)
            # (x1,y1 top left) (x2,y2 bottom right)
            # w = 600
            # h = 400
            # x = w//2
            # y = h//2

    # self.canvas.bind("<B1-Motion>",self.sqare_draw)

    # oval oval
    # def oval_draw(self):
    # self.canvas.create_oval(50,150,250,50,outline=self.pen_color)

    # def save(self):
    # try:
    # file = asksaveasfilename(defaultextension='.jpg')
    # x = self.root.winfo_rootx() + self.canvas.winfo_x()
    # y = self.root.winfo_rooty() + self.canvas.winfo_y()
    ##y1 = y + self.canvas.winfo_height()
    # ImageGrab.grab().crop((x,y,x1,y1)).save(filename)
    # messagebox.showinfo('paint says','image is saved as ' + str(filename))

    # except:
    # messagebox.showerror("paint says","unable to save image,\n some thing went wrong")

    if __name__ == "__main__":
        root = Tk()
        # text = Text(root)
        # myFont = Font(family="Times New Roman", size=12)
        # text.configure(font=myFont)
        p = Paint(root)
        # def left(self,event):
        #    x_1 = event.x-10
        #    y_1 = y-0
        #    self.canvas.move(my_rectangle, event.x, event.y)
        # def right(self,event):
        #    x_1 = event.x+10
        #    y_1 =y+ 0
        #    self.canvas.move(my_rectangle, event.x, event.y)

        # def up(self,event):
        #    x_1 = event.x-10
        #    y_1 = event.y-0
        #    self.canvas.move(my_rectangle, event.x, event.y)

        # def down(self,event):
        # x_1 = event.x-0
        # y_1 = event.y-10
        # self.canvas.move(my_rectangle, event.x, event.y)

        # root.bind("<left>",left)
        # root.bind("<Right>",right)
        # root.bind("<Up>",up)
        # root.bind("<Down>",down)
        # root.bind("<Left>", left)
        # root.bind("<Right>", right)
        # root.bind("<Up>", up)
        # root.bind("<Down>", down)

        root.mainloop()


def go():
    import Daily_Geometry
    import Equation_Visualizer

    # string_test.work()

    import pygame
    import time
    import random
    import pygame.freetype
    pygame.freetype.init()

    pygame.init()

    display_width = 800
    display_height = 600

    gameDisplay = pygame.display.set_mode((display_width, display_height))

    playerImg = pygame.image.load('dp.png')
    playerImg = pygame.transform.scale(playerImg , (230, 150))
    playerX= 285
    playerY =50



    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 155, 0)
    blue = (0, 0, 255)
    light_blue = (0, 191, 255)
    light_green = (102, 255, 102)
    purple = (255, 0, 255)
    deep_red = (204, 0, 0)
    light_red = (255, 51, 51)
    deep_orange = (255, 128, 0)
    light_orange = (255, 178, 102)

    clock = pygame.time.Clock()

    def text_objects(msg, color, sizi):
        font = pygame.font.Font("Andromeda-Bold.otf", sizi)
        textSurface = font.render(msg, True, color)
        return textSurface, textSurface.get_rect()

    def message_to_screen(msg, color, y_displace=0, sizi=0):

        textSurf, textRect = text_objects(msg, color, sizi)
        textRect.center = (display_width / 2, display_height / 2 + y_displace)
        gameDisplay.blit(textSurf, textRect)

    def text_objects2(msg, color, sizi):
        font = pygame.font.Font("University.otf", sizi)
        textSurface = font.render(msg, True, red)
        return textSurface, textSurface.get_rect()

    def message_to_screen2(msg, color, y_displace=0, sizi=0):

        textSurf, textRect = text_objects2(msg, color, sizi)
        textRect.center = (display_width / 2, display_height / 2 + y_displace)
        gameDisplay.blit(textSurf, textRect)

    def text_objects3(msg, color, sizi):
        font = pygame.font.Font("University.otf", sizi)
        textSurface = font.render(msg, True, red)
        return textSurface, textSurface.get_rect()

    def message_to_screen3(msg, color, y_displace=0, sizi=0):

        textSurf, textRect = text_objects3(msg, color, sizi)
        textRect.center = (display_width / 2, display_height / 2 + y_displace)
        gameDisplay.blit(textSurf, textRect)

    def text_objects4(msg, color, sizi):
        font = pygame.font.Font("University.otf", sizi)
        textSurface = font.render(msg, True, red)
        return textSurface, textSurface.get_rect()

    def message_to_screen4(msg, color, y_displace=0, sizi=0):

        textSurf, textRect = text_objects4(msg, color, sizi)
        textRect.center = (display_width / 2, display_height / 2 + y_displace)
        gameDisplay.blit(textSurf, textRect)

    import pygame as pg

    def menu():
        intro = 1
        choice = 1
        while (intro):
            #print(choice)
            gameDisplay.fill( ( 246, 246, 246 )  )
            message_to_screen("GEOMETRY BOX", light_blue, -50, 70)
            message_to_screen2("Canvas", red, 30, 25)
            message_to_screen3("Daily Geometry", red, 80, 25)
            message_to_screen4("Equation Visualizer", red, 135, 25)
            if (choice == 1):
                pygame.draw.rect(gameDisplay, red, [display_width / 2 - 45, display_height / 2 + 50, 90, 5])
            elif (choice == 2):
                pygame.draw.rect(gameDisplay, red, [display_width / 2 - 120, display_height / 2 + 100, 240, 5])
            elif (choice == 3):
                pygame.draw.rect(gameDisplay, red, [display_width / 2 - 155, display_height / 2 + 155, 310, 5])


            gameDisplay.blit( playerImg, (playerX, playerY)  )
            pygame.display.update()
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    pygame.quit()
                    quit()
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_DOWN):
                        if (choice == 3):
                            choice = 1
                        else:
                            choice += 1
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_UP):
                        if (choice == 1):
                            choice = 3
                        else:
                            choice -= 1
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_RETURN):
                        if (choice == 3):
                            Equation_Visualizer.work()
                        elif (choice == 2):
                            Daily_Geometry.work()
                            menu()
                        elif (choice == 1):
                            pp()
                            menu()

    menu()


go()

