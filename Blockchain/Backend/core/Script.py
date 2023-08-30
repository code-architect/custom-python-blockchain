class Script:
    def __init__(self, cmds=None):
        if cmds is None:
            self.cmds = []
        else:
            self.cmds = cmds

    @classmethod
    def p2pkh_script(cls, h160):
        """Takes a hash160 and returns the p2 public key hash ScriptPubKey"""
        return Script([0x76, 0xA9, h160, 0x88, 0xAC])
