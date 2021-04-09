import re, sys, urllib.request
from string import ascii_uppercase

if __name__ == "__main__":
    if(len(sys.argv) < 2):
        print("Error: Missing argument...\nUsage: python enrichir.py [CORPUS FILE]\n")
    else:
        try:
            # Trying to open files with reading permission
            corpus = open(sys.argv[1], 'r') 
            dct = open('subst.dic', 'a+', encoding='utf-16')
            dct_enr = open('subst_enri.dic', 'w+', encoding='utf-16')
        except:
            print("Error: Permission denied...\n")
        else:
            # Initialize number of substances found in corpus-medical.txt
            cpt = 0    
            listCorpus = corpus.readlines()
            # Loop through each line of corpus file
            for line in listCorpus:
                sreg = re.search(r'''
                ^[-*]?\s?   # Starts with "* " or "- "
                (\w+)       # The substance wanted
                \s:?\s?     # subts :  (METOPROLOL : 1⁄2 le matin, 1⁄2 le soir)
                (\d+|,|\d+.\d)+     # "2" or "," or "1.1" ...etc.
                \s(mg|ml|µg|mcg|g|cp|amp|flacon).+    # measuring unit
                ''', line, re.VERBOSE | re.I)     
                # If substance found:
                if sreg:        
                    if sreg.group(1).lower() != 'intraveineuse' and sreg.group(1).lower() != 'eau' and sreg.group(1).lower() != 'puis': # Remove the words which unitex matched by mistake
                        dct_enr.write(sreg.group(1).lower()+',.N+subst\n')
                        # Write substace in both dictionaries
                        dct.write(sreg.group(1).lower()+',.N+subst\n')      
                        cpt+=1
                        # Displayig the substance with the value of counter
                        print(str(cpt)+" : "+sreg.group(1))        
            # Sorting and deletion of duplicates in subst.dic
            dct = open('subst.dic', 'r+', encoding='utf-16')
            tri = sorted(list(set(dct.readlines())))
            dct = open('subst.dic', 'w+', encoding='utf-16')
            for el in tri:
                # Recopy the sorted elements
                dct.write(el)         
             
            # Writing on file infos2.txt from corpus
            infos2 = open('infos2.txt', 'w+', encoding='utf-8')
            corpus = open(sys.argv[1], 'r+', encoding='utf-8') 
            listCorpus = corpus.readlines()
            # Calculate the number of substances per letter of the alphabet
            for letter in ascii_uppercase:       
                nbLettre=0
                for el in list(set(listCorpus)):
                    if letter == el[0].upper():
                        nbLettre+=1
                infos2.write('\t- Number of entries in '+letter+': '+str(nbLettre)+'\n')
            infos2.write('\n - Number of total entries: '+str(len(list(set(listCorpus)))))

            # Writing on file infos3.txt from subst_enri
            infos3 = open('infos3.txt', 'w+', encoding='utf-8')
            dct_enr = open('subst_enri.dic', 'r+', encoding='utf-16')
            listDctEnr = dct_enr.readlines()
            # Calculate the number of substances per letter of the alphabet
            for letter in ascii_uppercase:       
                nbLettre=0
                for el in list(set(listDctEnr)):
                    if letter == el[0].upper():
                        nbLettre+=1
                infos3.write('\t- Number of entries in '+letter+': '+str(nbLettre)+'\n')
            infos3.write('\n - Number of total entries: '+str(len(list(set(listDctEnr)))))

            
