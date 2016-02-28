HEADERS = [
"WiringPi/wiringPi/wiringPi.h",
"WiringPi/wiringPi/wiringPiI2C.h",
"WiringPi/wiringPi/wiringPiSPI.h",
"WiringPi/wiringPi/wiringSerial.h",
"WiringPi/wiringPi/wiringShift.h",
"WiringPi/wiringPi/wpiExtensions.h",

"WiringPi/wiringPi/drcSerial.h",
"WiringPi/wiringPi/max31855.h",
"WiringPi/wiringPi/max5322.h",
"WiringPi/wiringPi/mcp23008.h",
"WiringPi/wiringPi/mcp23016.h",
"WiringPi/wiringPi/mcp23016reg.h",
"WiringPi/wiringPi/mcp23017.h",
"WiringPi/wiringPi/mcp23s08.h",
"WiringPi/wiringPi/mcp23s17.h",
"WiringPi/wiringPi/mcp23x0817.h",
"WiringPi/wiringPi/mcp23x08.h",
"WiringPi/wiringPi/mcp3002.h",
"WiringPi/wiringPi/mcp3004.h",
"WiringPi/wiringPi/mcp3422.h",
"WiringPi/wiringPi/mcp4802.h",
"WiringPi/wiringPi/pcf8574.h",
"WiringPi/wiringPi/pcf8591.h",
"WiringPi/wiringPi/sn3218.h",
"WiringPi/wiringPi/softPwm.h",
"WiringPi/wiringPi/softServo.h",
"WiringPi/wiringPi/softTone.h",
"WiringPi/wiringPi/sr595.h",

"WiringPi/devLib/ds1302.h",
"WiringPi/devLib/font.h",
"WiringPi/devLib/gertboard.h",
"WiringPi/devLib/lcd128x64.h",
"WiringPi/devLib/lcd.h",
"WiringPi/devLib/maxdetect.h",
"WiringPi/devLib/piFace.h",
"WiringPi/devLib/piGlow.h",
"WiringPi/devLib/piNes.h"
]
def is_c_decl(line):
    if "wiringPiISR" in line:
        return False
    for prefix in ['extern','void','int','uint8_t']:
        if line.startswith(prefix):
            return True

for file in HEADERS:
    print("\n// Header file {}".format(file))
    h = open(file).read().split('\n')
    extern = False
    cont = False
    if 'extern "C" {' not in h:
        extern = True
    for line in h:
        line = line.strip()
        if cont:
            print("\t{}".format(line))
            cont = ";" not in line
            continue
        if line.startswith('extern "C"'):
            extern = True
            continue
        if is_c_decl(line) and extern:
            print(line)
            cont = ";" not in line
