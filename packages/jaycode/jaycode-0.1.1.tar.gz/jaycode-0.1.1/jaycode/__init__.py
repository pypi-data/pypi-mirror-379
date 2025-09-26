from .ssh import SSHNamespace as SSH
from .db import DBNamespace as DB
from .file import FileNamespace as File

class Core:
    def __init__(self):
        self.SSH = SSH(self)
        self.DB = DB(self)
        self.File = File(self)

init = Core