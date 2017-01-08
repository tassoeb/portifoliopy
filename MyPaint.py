from Tkinter import *

#--Global variables, used to allow tools on the drawboard
flagline = 0

class TopBar:
	def __init__(self, root):
		self.root = root
		self.menu = Menu(root)
		self.menuFile = Menu(self.menu)
		self.menuEdit = Menu(self.menu)
		self.menuView = Menu(self.menu)
		self.menuImage = Menu(self.menu)
		self.menuOptions = Menu(self.menu)
		self.menuHelp = Menu(self.menu)
		self.menu.add_cascade(label = "File", menu = self.menuFile)
		self.menu.add_cascade(label = "Edit", menu = self.menuEdit)
		self.menu.add_cascade(label = "View", menu = self.menuView)
		self.menu.add_cascade(label = "Image", menu = self.menuImage)
		self.menu.add_cascade(label = "Options", menu = self.menuOptions)
		self.menu.add_cascade(label = "Help", menu = self.menuHelp)

  		self.menuFile.add_command(label="New")
		self.menuFile.add_command(label="Open")
		self.menuFile.add_command(label="Save")
		self.menuFile.add_command(label="Exit", command = self.exit)
		self.root.configure(menu = self.menu)

	def exit(self):
		self.root.destroy()

class Tools:
	def __init__(self,root):
		self.root = root
		self.frame = Frame(root)
		self.frame.grid(column=1,row=1,sticky=N+W)				
		
		#Buttons definitios
		self.star = Button(self.frame)
		self.star['text'] = 'Star'
		self.star.grid(column=1,row=1,sticky=N+E+S+W)	

		self.psquare = Button(self.frame)
		self.psquare['text'] = 'Psquare'
		self.psquare.grid(column=2,row=1,sticky=N+E+S+W)	

		self.eraser = Button(self.frame)
		self.eraser['text'] = 'Eraser'
		self.eraser.grid(column=1,row=2,sticky=N+E+S+W)	
	
		self.ink = Button(self.frame)
		self.ink['text'] = 'Ink'
		self.ink.grid(column=2,row=2,sticky=N+E+S+W)	

		self.drop = Button(self.frame)
		self.drop['text'] = 'Drop'
		self.drop.grid(column=1,row=3,sticky=N+E+S+W)	

		self.zoom = Button(self.frame)
		self.zoom['text'] = 'Zoom'
		self.zoom.grid(column=2,row=3,sticky=N+E+S+W)	

		self.img_pencil = PhotoImage(file='icons/pencil.png')
		self.pencil = Button(self.frame, command = self.btn_Pencil, image = self.img_pencil)	
		self.pencil.grid(column=1,row=4,sticky=N+E+S+W)	

		self.brush = Button(self.frame)
		self.brush['text'] = 'Brush'
		self.brush.grid(column=2,row=4,sticky=N+E+S+W)	

		self.spray = Button(self.frame)
		self.spray['text'] = 'Spray'
		self.spray.grid(column=1,row=5,sticky=N+E+S+W)	

		self.letter = Button(self.frame)
		self.letter['text'] = 'A'
		self.letter.grid(column=2,row=5,sticky=N+E+S+W)	

		self.line = Button(self.frame, command = self.btn_Line)
		self.line['text'] = 'Line'
		self.line.grid(column=1,row=6,sticky=N+E+S+W)	

		self.curve = Button(self.frame)
		self.curve['text'] = 'Curve'
		self.curve.grid(column=2,row=6,sticky=N+E+S+W)	

		self.square = Button(self.frame)
		self.square['text'] = 'Square'
		self.square.grid(column=1,row=7,sticky=N+E+S+W)		

		self.polygon = Button(self.frame)
		self.polygon['text'] = 'Polygon'
		self.polygon.grid(column=2,row=7,sticky=N+E+S+W)		

		self.circle = Button(self.frame)
		self.circle['text'] = 'Circle'
		self.circle.grid(column=1,row=8,sticky=N+E+S+W)	

		self.oval = Button(self.frame)
		self.oval['text'] = 'Oval'
		self.oval.grid(column=2,row=8,sticky=N+E+S+W)	

	def btn_Line(self):
		global flagline
		self.line['relief'] = RIDGE	
		self.pencil['relief'] = RAISED	
		flagline = 1		
	
	def btn_Pencil(self):
		global flagline
		self.pencil['relief'] = RIDGE	
		self.line['relief'] = RAISED	
		flagline = 0
class DrawBoard:	
	def __init__(self, root):
		self.canvas = Canvas(root, width=600, height=300, bg='white')
		self.canvas.grid(column=2,row=1)
	
		self.canvas.bind('<1>',self.drawLine)

	def drawLine(self,event):
		if flagline == 1:
			x_origin = self.canvas.winfo_rootx()
			y_origin = self.canvas.winfo_rooty()
			x_abs = self.canvas.winfo_pointerx()
			y_abs = self.canvas.winfo_pointery()
			try:
				P = (x_abs - x_origin, y_abs - y_origin)
				self.canvas.create_line(self.ultimo_P, P)
				self.ultimo_P = P
			except:
				self.ultimo_P=(x_abs - x_origin, y_abs - y_origin)	
root = Tk()
root.title('MyPaint')
root.geometry("600x300")
bar = TopBar(root)
tools = Tools(root)
draw = DrawBoard(root)
root.mainloop()
