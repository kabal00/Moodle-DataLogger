from spidev import SpiDev

class MCP3202:
    def __init__(self, bus = 0, device = 0):
        self.bus, self.device = bus, device
        self.spi = SpiDev()
        self.open()

    def open(self):
        self.spi.open(self.bus, self.device)
        self.spi.max_speed_hz =1000000
        self.spi.mode = 0b00
    
    def read(self, channel = 0):
        self.spi.max_speed_hz =1000000
        self.spi.mode = 0b00
        adc = self.spi.xfer2([1, (0b10100000 + (channel<<6)), 0])
        data = (((adc[1] & 0b1111) << 8) + adc[2])*3.3/4096
        return data
            
    def close(self):
        self.spi.close()
