import string
import random
#Shift = random.randint(1,36)
#print(Shift)
MasterList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," ","0","1","2","3","4","5","6","7","8","9","~","`","!","@","#","$","%","^","&","*","(",")","-","_","=","+","[","]","{","}","|","'",'"',",",".","<",">","/","?",":",";"]
global shift
Shift = random.randint(0,len(MasterList))
print(Shift)
shift = Shift
f = open("Shift.txt","w")
f.write(str(shift))
f.close()
"""def Encryption(tbe,Shift,MasterList):
    MyList = list(tbe.strip(" "))
    EncryptedText=""
    for i in range(len(MyList)):
        CurrentPosition = MasterList.index(MyList[i])
        NewPosition = CurrentPosition + Shift
        if NewPosition < len(MasterList):
           encrypted_text = ''.join(MasterList[NewPosition])
           EncryptedText=EncryptedText+encrypted_text
        else:
           CurrentPosition = NewPosition - len(MasterList)
           encrypted_text = ''.join(MasterList[CurrentPosition])
           EncryptedText=EncryptedText+encrypted_text
    return EncryptedText"""


"""def Decryption(EncryptedText,Shift,MasterList):
    MyList = list(EncryptedText.strip(" "))
    DecryptedText=""
    for i in range(len(MyList)):
        CurrentPosition = MasterList.index(MyList[i])
        NewPosition = CurrentPosition - Shift
        if NewPosition < len(MasterList):
           encrypted_text = ''.join(MasterList[NewPosition])
           DecryptedText=DecryptedText+encrypted_text
        else:
           CurrentPosition = NewPosition - len(MasterList)
           encrypted_text = ''.join(MasterList[CurrentPosition])
           DecryptedText=DecryptedText+encrypted_text
    return DecryptedText"""
#print("\n"+"Encrypted text - "+EncryptedText+"\n")
#print("Decrypted text - "+DecryptedText)

#Ec=Encryption(tbe,Shift,MasterList)
#Dc=Decryption(Ec,Shift,MasterList)
#print(Ec)
#print("\n")
#print(b)