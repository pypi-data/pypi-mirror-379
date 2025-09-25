class RtcController:   

    def __init__(self, serialPort, stream):
        self.transport = serialPort
        self.stream = stream

    def Write(self, rtc_timedate: bytes)->bool:
        count = len(rtc_timedate)
        # declare b9 array
        cmd = f"dim b9[{count}]"
        self.transport.WriteCommand(cmd)
        self.transport.ReadResponse()

        # write data to b9
        ret = self.stream.WriteBytes("b9",rtc_timedate)

        # write b9 to dmx
        self.transport.WriteCommand("RtcW(b9)")
        r,s = self.transport.ReadResponse()

        return r

    def Read(self, rtc_timedate: bytearray)->int:
        count = len(rtc_timedate)
        # declare b9 array
        cmd = f"dim b9[{count}]"
        self.transport.WriteCommand(cmd)
        self.transport.ReadResponse()

        cmd = f"RtcR(b9)"
        self.transport.WriteCommand(cmd)
        self.transport.ReadResponse()

        ret = self.stream.ReadBytes("b9",rtc_timedate)

        return ret    
        
        




       



