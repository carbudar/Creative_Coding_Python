import random

rectangles = []

def setup():
    size(400, 500)
    background(0)  # Black frame
    initialize_rectangles() #function for all the rectangles

def draw():
    draw_rectangles()

def initialize_rectangles():
    global rectangles #rectangle in global scope
    rectangles = [ #r,g,b,x,y,w,h
        [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 30, 30, 30, 80],  # Yellow square to left
        [(255, 255, 255), 30, 110, 30, 330],  # White middle left
        [(255, 255, 255), 30, 440, 30, 30],  # White bottom left
        [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 60, 440, 220, 30],  # Yellow bottom middle
        [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 280, 440, 90, 30],  # Grey bottom right
        [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 280, 360, 60, 80],  # Grey bottom right 2
        [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 340, 360, 30, 80],  # Grey bottom right 3
        [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 170, 360, 110, 80],  # Blue bottom middle
        [(255, 255, 255), 60, 290, 110, 150],  # White left middle
        [(255, 255, 255), 60, 260, 110, 30],  # Small white left middle
        [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 60, 110, 110, 150],  # Blue middle left 2
        [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 60, 30, 110, 80],  # Red top left 2
        [(255, 255, 255), 170, 30, 70, 80],  # White middle top
        [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 170, 110, 70, 150],  # Black middle top
        [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 170, 260, 70, 100],  # Red middle bottom
        [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 240, 260, 100, 100],  # Red right bottom
        [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 340, 200, 30, 160],  # Black middle right
        [(255, 255, 255), 240, 200, 100, 60],  # White middle right
        [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 240, 70, 130, 130],  # Yellow top right
        [(255, 255, 255), 240, 30, 130, 40],  # White top right
    ]

def draw_rectangles():
    fill(255)
    rect(20, 20, 360, 460)  # Frame inside
    
    stroke(0)
    stroke_weight(6)
    
    #loop through the rectangles and the color
    for i, ((r, g, b), x, y, w, h) in enumerate(rectangles): 
        if x <= mouse_x <= x + w and y <= mouse_y <= y + h: #mouse x mouse y hover effect
            r, g, b = max(r - 100, 0), max(g - 100, 0), max(b - 100, 0)  # Darken color when hovered
        fill(r, g, b)
        rect(x, y, w, h)

run_sketch()
