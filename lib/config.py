from micropython import const

# Gravity Expansion board for PICO[-W] - SPI0
SPI0_SCK  = const(18)
SPI0_MOSI = const(19)
SPI0_MISO = const(16)
SPI0_CS   = const(17)

# Gravity Expansion board for PICO[-W] - SPI1
SPI1_SCK  = const(14)
SPI1_MOSI = const(15)
SPI1_MISO = const(12)
SPI1_CS   = const(13)

# TFT - BLK/LED, RSET or DC pins connections
TFT_BLK0   = GPIO22 = const(22)
TFT_RESET0 = GPIO20 = const(20)
TFT_DC0    = GPIO21 = const(21)

# TFT - BLK/LED, RSET or DC pins connections
TFT_BLK1   = GPIO02 = const(2)
TFT_RESET1 = GPIO03 = const(3)
TFT_DC1    = GPIO12 = const(12)   # SPI1-MISO is not used!
