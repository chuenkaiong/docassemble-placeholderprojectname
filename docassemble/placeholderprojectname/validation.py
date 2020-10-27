import re
from docassemble.base.util import *

def check_nric(nric):
    nric = nric.upper()
    if is_valid_format(nric) and is_valid_checksum(nric):
        return True
    validation_error("You have entered in invalid NRIC. Please check again.")

def is_valid_format(nric):
    if len(nric) != 9:
        return False
    return bool(re.match(r"[STFG][0-9]{7}[A-Z]", nric))

def is_valid_checksum(nric):
    # set d0
    if nric[0] in "SF":
        d0 = 0
    else:
        d0 = 4

    # implement the dot product thing 
    d1_to_d7 = nric[1:8]
    num_arr = [2, 7, 6, 5, 4, 3, 2]
    checksum = 0
    for i in range(len(d1_to_d7)):
        checksum += int(d1_to_d7[i]) * num_arr[i]
    d = (d0 + checksum) % 11

    if nric[0] in "ST":
        check_char_list = "JZIHGFEDCBA"
    else:
        check_char_list = "XWUTRQPNMLK"

    # final comparison
    return nric[8] == check_char_list[d]
