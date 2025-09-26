"""
Display message in separate process
"""
import multiprocessing as mp
import sys
import tkinter
import tkinter.ttk


class MessageGui(tkinter.Tk):
    """Simple gui for displaying a message"""

    def __init__(self, parent=None, msg=""):
        tkinter.Tk.__init__(self, parent)

        self.grid()
        self.resizable(False, False)

        self.parent = parent
        # Display window without decorations
        self.wm_attributes('-type', 'splash')

        self.frame = tkinter.ttk.Frame(self, padding=5, borderwidth=0)
        self.frame.grid()
        tkinter.ttk.Label(self.frame, text=msg, relief="ridge",
                          padding=10).grid()

        if 'linux' in sys.platform:
            style = tkinter.ttk.Style()
            style.theme_use('clam')

    def __call__(self):
        self.mainloop()


class Message(object):
    """Simple class for displaying a GUI message"""

    def __init__(self, msg):
        self.msg = msg
        self._process = None

    def show(self):
        """Spawn new process with tkinter window with a message"""

        self._process = mp.Process(target=_spawn, args=(self.msg, ))
        self._process.start()

    def close(self):
        """Terminate the process with gui"""
        if self._process:
            if self._process.is_alive():
                self._process.terminate()
            self._process.join()


def _spawn(msg):
    """Spawn gui for displaying message"""
    app = MessageGui(msg=msg)
    app()
