class ArgumentsModel:
    def __init__(self, help=False, new=None, get=None, update=None, upload=False, error=None):
        self.help = help
        self.new = new or {
            "username": None,
            "type": None,
            "seed": None,
            "domain": None,
            "extra_id": None,  
            "password": None   
        }
        self.get = get or {"username": None, "all": None, "domain": None}
        self.update = update or {
            "username": None,
            "type": None,
            "seed": None,
            "domain": None
        }
        self.upload = upload
        self.error = error

    def __repr__(self):
        return (f"ArgumentsModel(help={self.help}, new={self.new}, get={self.get}, "
                f"update={self.update}, upload={self.upload}, error={self.error})")