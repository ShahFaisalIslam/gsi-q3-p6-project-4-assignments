import tkinter as tk

# Initialize canvas dimensions and colors
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
RECT_SIZE = 50
ERASER_SIZE = 30
BLUE = "blue"
WHITE = "white"

def create_canvas_grid(canvas):
    """Create a grid of blue rectangles on the canvas."""
    for x in range(0, CANVAS_WIDTH, RECT_SIZE):
        for y in range(0, CANVAS_HEIGHT, RECT_SIZE):
            canvas.create_rectangle(x, y, x + RECT_SIZE, y + RECT_SIZE, fill=BLUE, outline="black")

def erase(event):
    """Erase blue rectangles by setting them to white when the eraser is dragged over."""
    x1, y1 = event.x - ERASER_SIZE // 2, event.y - ERASER_SIZE // 2
    x2, y2 = event.x + ERASER_SIZE // 2, event.y + ERASER_SIZE // 2
    overlapping_items = canvas.find_overlapping(x1, y1, x2, y2)
    for item in overlapping_items:
        canvas.itemconfig(item, fill=WHITE)
    update_eraser(event)  # Move the eraser with the cursor

def update_eraser(event):
    """Update the position of the visible eraser."""
    x1, y1 = event.x - RECT_SIZE // 4, event.y - RECT_SIZE // 4
    x2, y2 = event.x + RECT_SIZE // 4, event.y + RECT_SIZE // 4
    canvas.coords(eraser_rectangle, x1, y1, x2, y2)

# Create the main application window
root = tk.Tk()
root.title("Erase Canvas")

# Create the canvas widget
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=WHITE)
canvas.pack()

# Draw the initial grid of blue rectangles
create_canvas_grid(canvas)

# Create a visible eraser as a rectangle
eraser_rectangle = canvas.create_rectangle(0, 0, RECT_SIZE // 2, RECT_SIZE // 2, outline="black", fill="", width=2)

# Bind the eraser functionality to mouse drag and motion events
canvas.bind("<B1-Motion>", erase)
canvas.bind("<Motion>", update_eraser)

# Run the application
root.mainloop()