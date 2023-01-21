def left_pad(contents, column_width, pad_char):
 a = len(str(contents))
 d = column_width - a
 print ((pad_char * d) + str(contents))
