#!/bin/env python3

import serial

magic_cookie = (ord('B'), ord('A'), ord('L'))

with serial.Serial('/dev/ttyUSB0', 19200, timeout=1) as ser:
  buf = (ser.read(), ser.read(), ser.read())
  if (buf == magic_cookie) :
    print("Found Magic Cookie")
    num_circuits = ser.read() # num circuits
    for circuit in range(0, num_circuits):
      max_current = ser.read()  # max number of amps tested (ie 20)
      accumulator_msw_msb = ser.read()
      accumulator_msw_lsb = ser.read()
      accumulator_lsw_msb = ser.read()
      accumulator_lsw_lsb = ser.read()
      accumulator = (accumulator_msw_msb << 40) & (accumulator_msw_lsb << 32) & (accumulator_lsw_msb << 16) & accumulator_lsw_lsb
      mean_sqr = sqrt(accumulator)
      # convert from 0-1023 to amps, 511 = 0 amps, 1023 = 20 amps, 0 = -20 amps
      
  else :
    # didn't find our magic token, so read another byte and try again
    buf.pop(0)
    buf.append(ser.read()) 
