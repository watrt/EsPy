from machine import Pin, SPI
ili = ILI9163_SPI(128, 160, spi, res=Pin(27), dc=Pin(26), cs=Pin(4))



#测试中文