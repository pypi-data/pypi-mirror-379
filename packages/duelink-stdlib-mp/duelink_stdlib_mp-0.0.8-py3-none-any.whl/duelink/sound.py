import duelink as DL

class SoundController:    
    def __init__(self, serialPort,stream):
        self.transport = serialPort
        self.stream = stream

    def Beep(self, pin, frequency, duration_ms):
        cmd = "beep({0}, {1}, {2})".format(pin, frequency, duration_ms)
        self.transport.WriteCommand(cmd)
        r,s = self.transport.ReadResponse()
        return r
        
    
    def MelodyPlay(self, pin, notes):
        #arr = ""
        #if isinstance(notes, (list)):
        #    arr = DL.build_floatarray(notes)
        #elif isinstance(notes, str):
        #    arr = notes
        #else:
        #   t = type(notes)
        #   raise Exception("Invalid notes type '{t}'")

        #self.transport.WriteCommand(f"melodyp({pin},{arr})")
        #r,s = self.transport.ReadResponse()
        #return r
        
        # use stream
        count = len(notes)
        # declare b9 array
        cmd = f"dim a9[{count}]"
        self.transport.WriteCommand(cmd)
        self.transport.ReadResponse()

        # write data to b9
        ret = self.stream.WriteFloats("a9",notes)

        # write b9 to dmx
        cmd = f"MelodyP({pin},a9)"
        self.transport.WriteCommand(cmd)
        r,s = self.transport.ReadResponse()
        return r
        
    def MelodyStop(self, pin):
        cmd = "MelodyS({0})".format(pin)
        self.transport.WriteCommand(cmd)
        r,s = self.transport.ReadResponse()
        return r
        


