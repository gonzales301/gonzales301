""" 
 Draws the first scene on the canvas and outputs the first
 section of text for the story.
"""
def draw_circle(radius, color, x, y):
    circ=Circle(radius)
    circ.set_color(color)
    circ.set_position(x, y)
    add(circ)

    
def draw_scene1():
    print("This is scene 1")
    draw_circle(90, Color.yellow, 80,50)
    w = Text("HI I am Sun, where am I?")
    w.set_position(get_width() / 3 - w.get_width() / 3, get_height() / 3)
    add(w)

""" 
 Draws the second scene on the canvas and outputs the second
 section of text for the story.
"""
def draw_scene2():
    print("This is scene 2")
    draw_circle(90, Color.yellow, 80,50)
    draw_circle(50, Color.brown, 350,300)
    draw_circle(50, Color.red, 50,300)
    draw_circle(40, Color.blue, get_width()/2, get_height()/3.0)
    r = Text("Hello Sun, you are in space!")
    r.set_position(get_width() / 5 - r.get_width() / 4, get_height() / 2)
    add(r)

    

""" 
 Draws the third scene on the canvas and outputs the second
 section of text for the story.
"""
def draw_scene3():
    print("This is scene 3")

""" 
 Draws the fourth scene on the canvas and outputs the second
 section of text for the story.
"""
def draw_scene4():
    print("This is scene 4")
    draw_circle(90, Color.yellow, 80,50)
    draw_circle(50, Color.brown, 350,300)
    draw_circle(50, Color.red, 50,300)
    draw_circle(40, Color.blue, get_width()/2, get_height()/3.0)
    w = Text("Oh ok great, Goodbye!")
    w.set_position(get_width() / 3 - w.get_width() / 3, get_height() / 3)
    add(w)

"""
 This is set up code that makes the story advance from
 scene to scene. Feel free to check out this code and
 learn how it works!
 But be careful! If you modify this code the story might
 not work anymore.
"""

scene_counter = 0

# When this function is called the next scene is drawn.

def draw_next_screen(x, y):
    global scene_counter
    scene_counter += 1

    if scene_counter == 1:
        draw_scene1()
    elif scene_counter == 2:
        draw_scene2()
    elif scene_counter == 3:
        draw_scene3()
    else:
        draw_scene4()

welcome = Text("Click to Begin")
welcome.set_position(get_width() / 2 - welcome.get_width() / 2, get_height() / 2)
add(welcome)
add_mouse_click_handler(draw_next_screen)
