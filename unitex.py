import os
from os import path

os.system("rd /s corpus-medical_snt")

if(not path.exists("corpus-medical_snt")):
    os.mkdir("corpus-medical_snt")

os.system("UnitexToolLogger Normalize corpus-medical.txt -r Norm.txt")
os.system("UnitexToolLogger Tokenize corpus-medical.snt -a Alphabet.txt")
os.system("UnitexToolLogger Compress subst.dic")
os.system("UnitexToolLogger Dico -t corpus-medical.snt -a Alphabet.txt subst.bin")
os.system("UnitexToolLogger Grf2Fst2 posologie.grf")
os.system("UnitexToolLogger Fst2Txt -t corpus-medical.snt -a Alphabet.txt -R Replace.fst2")
os.system("UnitexToolLogger Locate -t corpus-medical.snt -a Alphabet.txt -S -A --all posologie.fst2")
os.system("UnitexToolLogger Concord corpus-medical_snt/concord.ind -f \"Courrier new\" -s 12 -l 40 -r 55")