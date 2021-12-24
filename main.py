import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import serial

def get_next_line(s :serial) -> str:
  raw_line = s.readline().decode('utf-8')
  raw_line = raw_line.replace('\0', '')
  raw_line = raw_line.strip('\r\n')
  return raw_line

ser = serial.Serial("/dev/cu.usbserial-110", 921600, timeout=None)

while True:
  if (get_next_line(ser) == 'IMGSTART'):
    img_pix_data = get_next_line(ser)
    img_pix_chain = [int(i) for i in img_pix_data.split(',')]
    img_data = np.array(img_pix_chain).reshape(3, 60, 60).transpose(1, 2, 0)
    plt.imshow(img_data)
  plt.pause(.01)