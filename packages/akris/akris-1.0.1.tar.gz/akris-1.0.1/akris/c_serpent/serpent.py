import sys
import os
import ctypes

SERPENT_KEY_SIZE = 32
MAX_MESSAGE_LENGTH = 428
EXPANDED_KEY_SIZE = 528

try:
    package_path = os.path.dirname(os.path.abspath(__file__))
    lib = ctypes.cdll.LoadLibrary(os.path.join(package_path, "../../_serpent_cffi.abi3.so"))
except OSError:
    venv_site_packages_path = sys.path[4]
    lib = ctypes.cdll.LoadLibrary(os.path.join(venv_site_packages_path, "_serpent_cffi.cpython-310-x86_64-linux-gnu.so"))
serpent_init = lib.serpent_init
serpent_cbc_ciph = lib.serpent_cbc_ciph
serpent_cbc_deciph = lib.serpent_cbc_deciph

def expand_key(key):
    expanded_key = ctypes.create_string_buffer(EXPANDED_KEY_SIZE)
    serpent_init(ctypes.byref(expanded_key), key, SERPENT_KEY_SIZE)
    return expanded_key.raw

def encrypt(key, plaintext):
    expanded_key = expand_key(key)

    red_packet_size = len(plaintext)
    # Create a ctypes byte string buffer of the same length as the Python byte string
    c_plaintext = ctypes.create_string_buffer(red_packet_size)

    # Set the value of the ctypes byte string using the Python byte string
    c_plaintext.value = plaintext

    c_ciphertext = ctypes.create_string_buffer(red_packet_size)
    serpent_cbc_ciph(expanded_key, ctypes.byref(c_ciphertext), c_plaintext, red_packet_size)
    return c_ciphertext.raw

def decrypt(key, ciphertext):
    expanded_key = expand_key(key)
    red_packet_size = len(ciphertext)
    c_ciphertext = ctypes.create_string_buffer(ciphertext)
    c_plaintext = ctypes.create_string_buffer(red_packet_size)
    serpent_cbc_deciph(expanded_key,ctypes.byref(c_plaintext), c_ciphertext, red_packet_size);
    return c_plaintext.raw
