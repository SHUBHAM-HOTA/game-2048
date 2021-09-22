from tkinter import Frame, Label, CENTER
import game_logic
import game_constains as c

class game2048(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.grid()
        self.master.title("2048 by Shubham")
        self.master.bind("<Key>",self.key_pressed)
        self.commands = {c.KEY_UP: game_logic.move_up, c.KEY_DOWN: game_logic.move_down,
                        c.KEY_LEFT: game_logic.move_left, c.KEY_RIGHT: game_logic.move_right}

        self.grid_cells = []
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()

        self.mainloop()

    def init_grid(self):
        background = Frame(self, bg=c.BACKGROUND_COLOR_GAME, height=c.SIZE,
                           width=c.SIZE)
        background.grid()

        for i in range(c.GRID_LEN):
            grid_row = []
            for j in range(c.GRID_LEN):
                cell = Frame(background, bg=c.BACKGROUND_COLOR_CELL_EMPTY, height=100,width=100)
                           
                cell.grid(row=i, column=j, padx=c.GRID_PADDING, pady=c.GRID_PADDING)           
                
                t = Label(master=cell, text="",font=c.FONT,justify=CENTER,width=5,height=2)
                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)        

    def init_matrix(self):
        self.matrix = game_logic.start_game()
        game_logic.add_new_2(self.matrix)
        game_logic.add_new_2(self.matrix)

    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(text="", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                        
                else:
                    self.grid_cells[i][j].configure(text=str(
                        new_number), bg=c.BACKGROUND_COLOR_DICT[new_number],
                        fg=c.CELL_COLOR_DICT[new_number])
        self.update_idletasks()       


    def key_pressed(self, event):
        key = repr(event.char)
        if key in self.commands:
            self.matrix, changed = self.commands[repr(event.char)](self.matrix)
            if changed:
                game_logic.add_new_2(self.matrix)
                self.update_grid_cells()
                changed = False
                if game_logic.get_current_state(self.matrix) == 'WON':
                    self.grid_cells[1][1].configure(text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="Win!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                        
                if game_logic.get_current_state(self.matrix) == 'LOST':
                    self.grid_cells[1][1].configure(text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)   
                    self.grid_cells[1][2].configure(text="Lose!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                

gamegrid = game2048()                        
