import numpy as np
from numpy.polynomial import Polynomial as P
import timeit
from random import randint
#function to convert a hexadecimal string to a binary one

#sbox (for encrrption)
sbox =  [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67,
            0x2b, 0xfe, 0xd7, 0xab, 0x76, 0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59,
            0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0, 0xb7,
            0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1,
            0x71, 0xd8, 0x31, 0x15, 0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05,
            0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75, 0x09, 0x83,
            0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29,
            0xe3, 0x2f, 0x84, 0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b,
            0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf, 0xd0, 0xef, 0xaa,
            0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c,
            0x9f, 0xa8, 0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc,
            0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2, 0xcd, 0x0c, 0x13, 0xec,
            0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19,
            0x73, 0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee,
            0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb, 0xe0, 0x32, 0x3a, 0x0a, 0x49,
            0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
            0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4,
            0xea, 0x65, 0x7a, 0xae, 0x08, 0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6,
            0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a, 0x70,
            0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9,
            0x86, 0xc1, 0x1d, 0x9e, 0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e,
            0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf, 0x8c, 0xa1,
            0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0,
            0x54, 0xbb, 0x16]


#rsbox (for decryption)
rsbox = [0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3,
            0x9e, 0x81, 0xf3, 0xd7, 0xfb , 0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f,
            0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb , 0x54,
            0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b,
            0x42, 0xfa, 0xc3, 0x4e , 0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24,
            0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25 , 0x72, 0xf8,
            0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d,
            0x65, 0xb6, 0x92 , 0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda,
            0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84 , 0x90, 0xd8, 0xab,
            0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3,
            0x45, 0x06 , 0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1,
            0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b , 0x3a, 0x91, 0x11, 0x41,
            0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6,
            0x73 , 0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9,
            0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e , 0x47, 0xf1, 0x1a, 0x71, 0x1d,
            0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b ,
            0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0,
            0xfe, 0x78, 0xcd, 0x5a, 0xf4 , 0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07,
            0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f , 0x60,
            0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f,
            0x93, 0xc9, 0x9c, 0xef , 0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5,
            0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61 , 0x17, 0x2b,
            0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55,
            0x21, 0x0c, 0x7d]

#---------------------------matrix constants for encryption and decryption----------------------
mat_enc = [['02','03','01','01'],
           ['01','02','03','01'],
           ['01','01','02','03'],
           ['03','01','01','02']]

mat_dec = [['0e','0b', '0d', '09'],
           ['09','0e', '0b', '0d'],
           ['0d','09', '0e', '0b'],
           ['0b','0d', '09', '0e']]




#function to convert a hexadecimal string to a binary one
def to_binary(hex_num):
  bin_num = bin(int(hex_num, 16))[2:]
  #print(bin_num)
  count = len(str(hex_num))*4
  out = bin_num.zfill(count)
  return out


#function to convert a binary string to a hexadecimal one

def to_hex(bin_num):
  if len(str(bin_num))%4 != 0:
     new_len = len(str(bin_num))+(len(str(bin_num))%4)
     bin_num = bin_num.zfill(new_len)
  
  hex_num = hex(int(bin_num, 2))[2:]
  return hex_num

#function to sub bytes
def sub_bytes(hex_num, sbox):
  first = int(hex_num[0], 16)
  second = int(hex_num[1], 16)
  #how to access in 1d array?
  res = str(hex(sbox[(16*first)+second]))[2:]
  if len(res)==1:
    return '0'+res
  return res


#function to left shift word by 'byts' bytes
def left_shift_word(w, byts):
  #assuming that the word is in hex
  return w[(byts):]+w[:(byts)]

print(left_shift_word(['a6','ef', 'ef', 'ef'],3))

#function to right shift word by 'times' bytes
def right_shift_word(w, times):
  #assuming that the word is in hex
  return w[len(w)-(times):]+w[:len(w)-(times)]

print(right_shift_word(['a6', 'ef', 'ef', 'ef'],2))


def xor(hex1,hex2,string=False):  
    hex1 = ''.join(hex1)
    hex2 = ''.join(hex2)

    bin1 = to_binary(hex1)
    bin2 = to_binary(hex2)
    
    res = int(bin1,2) ^ int(bin2, 2)
    res  = str(hex(res))[2:]
    #print('res', res)

    if len(res)%len(hex1)!=0:
      for i in range(len(hex1)-((len(res)%len(hex1)))):
        res = '0'+res

    if string==False:
      res_list = [res[i:i+2] for i in range(0,len(res),2)]
      return res_list
    else:
      return res


#------------------------------------key expansion------------------------------------------------

#how would one generate a round constant?
#lets see

def gen_rcon():
  std_pol = '00011011'
  rcon_list = ['00000001']
  for i in range(1, 8):
    rcon_list.append(rcon_list[i-1][1:]+rcon_list[i-1][:1]) #right shifting by 1
  for i in range(8, 10):
    rcon_list.append(std_pol[i-8:]+std_pol[:i-8]) #right shifting by 1
  for i in range(len(rcon_list)):
    rcon_list[i] = to_hex(rcon_list[i])
    if len(rcon_list[i])==1:
      rcon_list[i] = '0'+rcon_list[i]
  return rcon_list


def rcon_plus_zeroes(rcon_list):
  rcon_plus_zeroes = []
  for rcon in rcon_list:
    rcon_l = [rcon]
    for i in range(3):
      rcon_l.append('00')
    rcon_plus_zeroes.append(rcon_l)
  return rcon_plus_zeroes
  

#first of all we take the key and form the word array using the 16 byte (128-bit) key
def get_initial_word_array(key):
  init_indices = [0,2,4,6]
  w_arr = []
  for i in init_indices:
    w = []
    for j in range(0, 32, 8):
      w.append(key[i+j:i+j+2])
    w_arr.append(w)
  return w_arr

      
#only w3 will go to the g function
def g_func(w, rcon_key):
  l_shift_w = left_shift_word(w, 1)
  sub_w = [sub_bytes(x,sbox) for x in l_shift_w]
  xored_w = xor(sub_w, rcon_key)
  return xored_w


def next_key(w_arr, g_func_outp):
  next_key = []

  for i in range(len(w_arr)):
    if i == 0:
      xored = xor(w_arr[i], g_func_outp)
      next_key.append(xored)
    else:
      w = next_key[len(next_key)-1]
      next_key.append(xor(w, w_arr[i]))

  return next_key


#now finally we can write the whole key expansion function
def key_expansion(key):
  #keys = [[['54','68','61','74'],['73','20','6d','79'],['20','4b','75','6e'],['67','20','46','75']]]

  keys = [get_initial_word_array(key)]
  rcon_words =rcon_plus_zeroes(gen_rcon())
  #print(rcon_words)
  for i in range(10):
    #print(keys)
    w_arr = keys[len(keys)-1]
    #print(w_arr)
    g_func_outp = g_func(w_arr[3], rcon_words[i])
    next = next_key(w_arr, g_func_outp)
    keys.append(next)
  return keys



#----------------------------mix columns------------------------------------------------------

#function to multiply 2 polynomials and get a bit representation of the result
def multiply_pols(bin3, bin4):
  poly3 = P([int(dig) for dig in list(bin3[::-1])])
  poly4 = P([int(dig) for dig in list(bin4[::-1])])
  res_poly = poly3*poly4
  res = ''.join([str(int(dig)) for dig in list(res_poly)])[::-1]
  for i in range(len(res)):
    if (int(res[i])>1):
      coeff = int(res[i])
      if coeff%2==0:
        res=res[:i]+'0'+res[i+1:]
      else:
        res=res[:i]+'1'+res[i+1:]

  #res.replace()
  #res = '1'
  if len(res) < 8:
    needed_zeros = 8-len(res)
    for _ in range(needed_zeros):
      res = '0'+res

  #print('res: ', res)
  return(res)
  #there is at least 1 digit ahead of the 7th bit that needs to be transformed


#function to transform the bit representation from the last function so that it remains
#inside the galois field.

def put_within_galois_field(res):
  std_poly = '00011011' #the polynom used when powers exceed 7
  xtra_bits = len(res)-8 #the number of extra bits in result
  polynoms_to_xor = []
  if xtra_bits <= 4:
    for i in range(xtra_bits):
      if(res[i]=='1'):
        shift = (xtra_bits - i)-1
        polynom = std_poly[shift:] +std_poly[:shift]
        polynoms_to_xor.append(polynom)
  else:
    cant_shift_bits = xtra_bits-4
    #print('hello')
    #shift the maximum possible shift
    new_std_poly = std_poly[3:]+std_poly[:3]
    for _ in range(cant_shift_bits):
      new_std_poly = new_std_poly + '0'

    new_std_poly = put_within_galois_field(new_std_poly)
    polynoms_to_xor.append(new_std_poly)

  #print(polynoms_to_xor)
  new_res = res[xtra_bits:]
  #print(new_res)
  for polynom in polynoms_to_xor:
    new_res = int(new_res,2) ^ int(polynom, 2)
    new_res  = str(bin(new_res)[2:])
    if len(new_res) < 8:  #just adding the needed zeroes to the start
      needed_zeros = 8-len(new_res)
      for _ in range(needed_zeros):
        new_res = '0'+new_res
  return new_res

#final function to multiply two functions inside the galois field
def multiply_within_galois_field(bin1, bin2):
  return put_within_galois_field(multiply_pols(bin1, bin2))

#function to mix-columns
def mix_cols(mat_con, state_arr):
  res_mat = []
  for i in range(len(mat_con)):
      temp_mat = []
      for j in range(len(mat_con)):
        sum = 0
        for k in range(len(mat_con)):
          #print(i,j,k)
          ans = to_hex(multiply_within_galois_field(to_binary(mat_con[i][k]), to_binary(state_arr[k][j])))
          #print(ans)
          sum = xor(str(sum), ans,string=True)
        temp_mat.append(sum)
      res_mat.append(temp_mat)
  return res_mat



#---------------------------shift rows---------------------------------------------------------
def shift_rows(state_arr, dir):
  shifted_state_arr = []
  if dir=='right':
    for i in range(len(state_arr)):
      shifted_state_arr.append(right_shift_word(state_arr[i],i))
  elif dir=='left':
    for i in range(len(state_arr)):
      shifted_state_arr.append(left_shift_word(state_arr[i],i))
  return shifted_state_arr


  #----------------FINAL AES-128 ENCRYPTION FUNCTION-----------------------------------------------



def AES_encryption(pt, all_keys, print=False):
  init_key = ''.join([j for sub in all_keys[0] for j in sub])
  state_arr = xor(pt, init_key)
  if print:
    print('after init round key: ', state_arr)
  for x in range(1, 11):
    #sub bytes
    for i in range(len(state_arr)):
      state_arr[i] = sub_bytes(state_arr[i], sbox)
    #print(state_arr)
    if print:
      print('after sub bytes: ', state_arr)

    #shift rows
    #first we make it into a  2d arr
    
    state_arr_2d = []
    for i in range(0,len(state_arr),4):
      state_arr_2d.append(state_arr[i:i+4])

    state_arr_2d = np.array(state_arr_2d).T.tolist()
    if print:
      print(state_arr_2d)  

    state_arr_2d = shift_rows(state_arr_2d, 'left')
    if print:
      print('after shift rows: ', state_arr_2d)

    #mixing columns
    if (x!=10):
      state_arr_2d = mix_cols(mat_enc, state_arr_2d)
    state_arr_2d = np.array(state_arr_2d).T.tolist()
    state_arr = [j for sub in state_arr_2d for j in sub]
    
    if print:
      print('after mix columns', state_arr)

    #add round key
    
    key = ''.join([j for sub in all_keys[x] for j in sub])
    state_arr = xor(state_arr, key)
    
    if print:
      print('after add round key', state_arr)

  ciphertext = "".join(state_arr)
  return ciphertext


#----------------FINAL AES-128 DECRYPTION FUNCTION-----------------------------------------------
def AES_decryption(ct, all_keys, print=False):
  last_key = ''.join([j for sub in all_keys[10] for j in sub])
  state_arr = xor(ct, last_key)
  if print:
    print('after init(last) round key: ', state_arr)
  
  for x in range(9,-1,-1):
    
    state_arr_2d = []
    for i in range(0,len(state_arr),4):
      state_arr_2d.append(state_arr[i:i+4])
    
    #transposing the state array
    state_arr_2d = np.array(state_arr_2d).T.tolist()

    if print:
      print(state_arr_2d)  

    if (x!=9):
      state_arr_2d = mix_cols(mat_dec, state_arr_2d)
      if print:
        print('after mix columns', state_arr)


    #shift rows
    #first we make it into a  2d arr
    state_arr_2d = shift_rows(state_arr_2d, 'right')
    if print:
      print('after shift rows: ', state_arr_2d)

        
    state_arr_2d = np.array(state_arr_2d).T.tolist()
    state_arr = [j for sub in state_arr_2d for j in sub]


    #sub bytes
    for i in range(len(state_arr)):
      state_arr[i] = sub_bytes(state_arr[i], rsbox)
    #print(state_arr)
    if print:
      print('after sub bytes: ', state_arr)

    #add round key
    
    key = ''.join([j for sub in all_keys[x] for j in sub])
    state_arr = xor(state_arr, key)
    if print:
      print('after add round key', state_arr)
  
  plaintext = "".join(state_arr)
  return plaintext



if __name__== '__main__':
  
  print("Welcome to AES-128 bit (ECB Mode). Select an option:")
  print("1. Run AES with a plaintext and key")
  print("2. Run AES with timer to calculate execution time in MB/s")
  
  opt = int(input("Enter your option (number): "))
  if opt==1:
    
    pt = input("Enter plaintext: ")
    key = input("Enter key(Must be a 32-character hex string): ")
    while(len(key)!=32):
      key = input("Enter key(Must be a 32-character hex string): ")
    pad = False
    t_0 = timeit.default_timer()
    pt_blocks = []
    if(len(pt)%32==0):
      num_blocks = int(len(pt)/32)

    else:
      pad = True
      num_blocks = int(((len(pt)-(len(pt)%32))/32)+1)

    print(num_blocks)
    pad_bits = 0
    for i in range(0, 32*num_blocks, 32):
      if i != (32*num_blocks)-32:
        pt_blocks.append(pt[i:i+32])
      else:
        if pad:
          pt_blocks.append(pt[i:])
          
          while(len(pt_blocks[len(pt_blocks)-1]) != 32):
            pt_blocks[len(pt_blocks)-1] = pt_blocks[len(pt_blocks)-1]+'0' 
            pad_bits+=1

        else:
          pt_blocks.append(pt[i:i+32])

        # print(pt_blocks)
        # print(len(pt_blocks[len(pt_blocks)-1]))



    keys = key_expansion(key)
    ciphertext = []
    
    for pt_block in pt_blocks:
      ciphertext.append(AES_encryption(pt_block,keys, print=False))

    final_ciphertext = ''.join(ciphertext)
    print('ciphertext: ',final_ciphertext)

    decrypted_pt_blocks = []
    for cipher_block in ciphertext:
      decrypted_pt_blocks.append(AES_decryption(cipher_block,keys, print=False))
    
    final_plaintext = ''.join(decrypted_pt_blocks)
    print('final plaintext (with padding): ', final_plaintext)
    print('final plaintext (without padding)',final_plaintext[:len(final_plaintext)-pad_bits])
    t_1 = timeit.default_timer()
    elapsed_time = round((t_1 - t_0) * 10 ** 6, 3)
    print(f"Elapsed time: {elapsed_time} µs")
  elif opt==2:
    
    random_index = randint(0,3)
    p = ''
    k = ''
    with open('key_values.keys') as key_file:
      key = ''
      for i in range(random_index):
        #select a random key
        key = key_file.readline().strip()
      k = key


    with open('plaintext.pt') as pt_file:
      
  
      #select a random pt
      pt = ''
      for i in range(random_index):
        pt = pt_file.readline().strip()
      p = pt

    print('KEY: ', k)
    print('PLAINTEXT: ', p)

    pt = p
    key = k

    t_0 = timeit.default_timer()
    
    pad = False
    pt_blocks = []
    if(len(pt)%32==0):
      num_blocks = int(len(pt)/32)

    else:
      pad = True
      num_blocks = int(((len(pt)-(len(pt)%32))/32)+1)

    print(num_blocks)
    pad_bits = 0
    for i in range(0, 32*num_blocks, 32):
      if i != (32*num_blocks)-32:
        pt_blocks.append(pt[i:i+32])
      else:
        if pad:
          pt_blocks.append(pt[i:])
          
          while(len(pt_blocks[len(pt_blocks)-1]) != 32):
            pt_blocks[len(pt_blocks)-1] = pt_blocks[len(pt_blocks)-1]+'0' 
            pad_bits+=1

        else:
          pt_blocks.append(pt[i:i+32])

        # print(pt_blocks)
        # print(len(pt_blocks[len(pt_blocks)-1]))



    keys = key_expansion(key)
    ciphertext = []
    
    for pt_block in pt_blocks:
      ciphertext.append(AES_encryption(pt_block,keys, print=False))

    final_ciphertext = ''.join(ciphertext)
    print('ciphertext: ',final_ciphertext)

    decrypted_pt_blocks = []
    for cipher_block in ciphertext:
      decrypted_pt_blocks.append(AES_decryption(cipher_block,keys, print=False))
    
    final_plaintext = ''.join(decrypted_pt_blocks)
    print('final plaintext (with padding): ', final_plaintext)
    print('final plaintext (without padding)',final_plaintext[:len(final_plaintext)-pad_bits])

    t_1 = timeit.default_timer()
    elapsed_time = round((t_1 - t_0) * 10 ** 6, 3)
    print(f"Elapsed time: {elapsed_time} µs")
    print('Number of encrypted bytes: ', len(pt))
    print('Rate of encryption in MB/s: ', (len(pt)/1000000)/(elapsed_time/1000000))


    
      

    

    



  


    