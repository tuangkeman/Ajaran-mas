#no 1
import re

def sorting_string(stript):
    besar = "".join(re.findall(r"[A-Z]", stript))
    kecil = "".join(re.findall(r"[a-z]", stript))
    angka = "".join(re.findall(r"\d", stript))
    
    return f"{kecil}{besar}{angka}"

if _name_ == "_main_":
    stript = str(input())
    print(sorting_string(stript))

#soal no. 2

import re

def findPhoneNumber(text):
    pola = r"\b\d{4}-\d{4}-\d{4}\b"
    
    semuanomor = list(dict.fromkeys(re.findall(pola, text)))
    jumlah = len(semuanomor)
    
    print("=============================================")
    print(f"Total Phone Number Prof Wisnu : {jumlah}")
    
    if jumlah == 0:
        print("List Phone Number : Nomor is not define")
    elif jumlah == 1:
        print(f"List Phone Number : {semuanomor[0]}")
    elif jumlah == 2:
        print(f"List Phone Number : {semuanomor[0]} and {semuanomor[1]}")
    else:
        awal = ", ".join(semuanomor[:-1])
        print(f"List Phone Number : {awal}, and {semuanomor[-1]}")
        
    print("=============================================")
if __name__ == "__main__":
    text = str(input())
    findPhoneNumber(text)

#soal no. 3
import re
def ekstrakStr(teks):
    digits = re.findall(r'\d', teks)
    odd_numbers = []
    even_numbers = []
    
    for d in digits:
        num = int(d)
        if num % 2 != 0:
            odd_numbers.append(num + 9)
        else:
            even_numbers.append(num + 7)
    
    odd_numbers.sort()
    even_numbers.sort()
    
    print("=========================")
    print(f" ODD NUMBER : {' '.join(map(str, odd_numbers))}")
    print(f" EVEN NUMBER : {' '.join(map(str, even_numbers))}")
    print("=========================")

if __name__ == "__main__":
    strinput = str(input())
    ekstrakStr(strinput)