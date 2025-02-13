import tkinter as tk


class Application(tk.Frame):
    def __init__(self, window_width, window_height, master=None):
        super().__init__(master)  # Call tk.Frame.__init__(master)
        self.master = master

        # Create a frame and place it in the window
        frame = tk.Frame(self.master, width=window_width, height=window_height)
        frame.pack()

        # Create a canvas and place it in the frame
        self.canvas = tk.Canvas(frame, bg='red')
        self.canvas.place(x=100, y=20, width=500, height=240)

        #self.canvas.bind("<ButtonPress-1>", self.mouse_left_button_press)
        #self.canvas.bind("<Motion>", self.mouse_move)
        #self.canvas.bind("<B1-Motion>", self.mouse_move_left_button_press)
        #self.canvas.bind("<ButtonRelease-1>", self.mouse_left_button_release)
        #self.canvas.bind("<Double-Button-1>", self.mouse_left_button_double_click)
        #self.canvas.bind("<Enter>", self.mouse_pointer_enter)
        self.canvas.bind("<Leave>", self.mouse_pointer_leave)

    def mouse_left_button_press(self, event):
        print("Mouse Left Button Pressed on the Canvas", event.x, " ", event.y)

    def mouse_move(self, event):
        print("Mouse Move", event.x, " ", event.y)

    def mouse_left_button_release(self, event):
        print("Mouse Left Button Released", event.x, " ", event.y)

    def mouse_left_button_double_click(self, event):
        print("Mouse Left Button Double Click", event.x, " ", event.y)

    def mouse_pointer_enter(self, event):
        print("Mouse Pointer Enter", event.x, " ", event.y)

    def mouse_pointer_leave(self, event):
        print("Mouse Pointer Leave", event.x, " ", event.y)

if __name__ == '__main__':
    master = tk.Tk()
    window_width = 700
    window_height = 300
    # Define window size
    master.geometry(str(window_width) + 'x' + str(window_height))
    app = Application(window_width, window_height, master=master)
    app.mainloop()
