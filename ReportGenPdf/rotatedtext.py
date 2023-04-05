from reportlab.platypus.flowables import Flowable

class vT(Flowable):
    '''Rotates and vertically centers a text in a table cell.'''
    def __init__(self, text):
        Flowable.__init__(self)
        max_width=165
        self.text = text
        self.max_width = max_width
    
    def draw(self):
        canvas = self.canv
        canvas.rotate(90)
        fs = canvas._fontsize
        lines = self.text.split('\n')  # split the text into lines
        total_height = fs * len(lines)  # calculate total height of text
        y = (-total_height / 2)*.7# calculate starting y-coordinate for vertically centerin
        for line in lines:
            # draw each line of text
            x=(165-len(line)*4.4)/2
            canvas.drawString(x, y, line[:self.max_width])
            y -= fs  # move to the next line
        self.width, self.height = total_height, self.max_width
    
    def wrap(self, aW, aH):
        canv = self.canv
        fn, fs = canv._fontname, canv._fontsize
        lines = self.text.split('\n')
        return fs * len(lines), self.max_width
