#if we don't want to use the UI, then put the filename here.

from ocr import perform_ocr

perform_ocr("test.png")

import os
os.startfile("output.txt")