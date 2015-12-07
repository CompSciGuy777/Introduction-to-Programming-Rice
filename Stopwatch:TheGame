# template for "Stopwatch: The Game"
import simplegui

# define global variables
time = 0
total_stops = 0
successful_stops = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global time
    minutes = (t/600)
    seconds = (t/10)
    tenths = (((t%10)*10)/10)
    
    if time >= 600:
        seconds = (t % 600)/10
    else:
        pass
  
    return ("%s:%02d.%s" %(minutes, seconds, tenths))
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    global total_stops
    global successful_stops
    timer.stop()
    total_stops += 1
    
    if time % 10 == 0:
        successful_stops += 1
    
    else:
        pass
    

def reset():
    global time
    global total_stops
    global successful_stops
    timer.stop()
    time = 0
    total_stops = 0
    successful_stops = 0


# define event handler for timer with 0.1 sec interval
def time_handler():
    global time
    time += 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(str(format(time)),(125,160),40,'white')
    canvas.draw_text(str(successful_stops) + " / " + str(total_stops), (225,50),25,'green')
    
# create frame
frame = simplegui.create_frame("StopWatch",300,300,300)

# register event handlers
timer = simplegui.create_timer(100,time_handler)
start_button = frame.add_button("Start", start, 50)
stop_button = frame.add_button("Stop" , stop, 50)
reset_button = frame.add_button("Reset", reset, 50)
frame.set_draw_handler(draw_handler)

# start frame
frame.start()

# Please remember to review the grading rubric
