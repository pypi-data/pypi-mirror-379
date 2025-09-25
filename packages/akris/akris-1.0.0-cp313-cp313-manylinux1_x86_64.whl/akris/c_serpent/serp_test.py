#!/usr/bin/env python3

# import os
# import ctypes
# from serpent import serpent_init, serpent_cbc_ciph, serpent_cbc_deciph
#
# SERPENT_KEYSIZE = 32
# MAX_MESSAGE_LENGTH = 428
# EXPANDED_KEYSIZE = 528
#
#
# def _pad(text, size):
#     return text.ljust(size, b"\x00")
#
# cipher_key = os.urandom(SERPENT_KEYSIZE)
# expanded_key = ctypes.create_string_buffer(EXPANDED_KEYSIZE)
# serpent_init(ctypes.byref(expanded_key), cipher_key, SERPENT_KEYSIZE)
# print(len(expanded_key.raw))
# print(expanded_key.raw)
# python_byte_string = _pad(b"Hello, World! Testing.", MAX_MESSAGE_LENGTH)
# RED_SIZE = len(python_byte_string)
# # Create a ctypes byte string buffer of the same length as the Python byte string
# src = ctypes.create_string_buffer(RED_SIZE)
#
# # Set the value of the ctypes byte string using the Python byte string
# src.value = python_byte_string
#
# # Print the value of the ctypes byte string
# print(src.value)
# dst = ctypes.create_string_buffer(RED_SIZE)
# serpent_cbc_ciph(expanded_key,ctypes.byref(dst),src,RED_SIZE);
# deciph_dst = ctypes.create_string_buffer(RED_SIZE)
# serpent_cbc_deciph(expanded_key,ctypes.byref(deciph_dst),dst,RED_SIZE);
# decrypted_message = deciph_dst.value
# print(dst.raw)
# print(deciph_dst.raw)
