class ArgumentsModel:
    def __init__(self, help=False, new=None, get=None, update=None, upload=False, error=None):
        self.help = help
        self.new = new or {"username": None, "type": None, "seed": None, "domain": None}
        self.get = get or {"username": None, "all": None, "domain": None}
        self.update = update or {"username": None, "type": None, "seed": None, "domain": None} 
        self.upload = upload
        self.error = error
