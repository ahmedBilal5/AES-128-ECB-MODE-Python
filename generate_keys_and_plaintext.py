#the code to generate test vectors
import random
def hex_number( count, padded=False ):
  # This currently generates a number of length count hex digits.
  # Pad on the left with 0's if padded is True:
  x = random.randint( 0, 16**count )
  hexdig = "%x" % x
  if padded:
    out = hexdig.zfill( count ) # pad with 0 if necessary
    return out
  else:
    return hexdig

def AESvectors( size, num, padded, filename):
# generate num vectors (one per line) of size at most count
# hex digits
    with open(filename, 'a') as key_file:   
        for i in range( num ):
            hex_num = hex_number( size, padded) 
            key_file.write(hex_num)
            key_file.write('\n')
            # Set the last param to True to pad all lines size hex digits.
            # The padding is only needed for lines that have leading 0's.

Keys = AESvectors(size=1000, num=6, padded=True, filename='plaintext.pt')
# with open('key_values.keys', 'a') as key_file:   
#     for key in Keys:
#         key_file.write(key)


