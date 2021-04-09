import urllib.request, re, sys, os
from http import server, HTTPStatus
from string import ascii_uppercase

if __name__ == "__main__":
    if(len(sys.argv) < 3):
        print("Error: Missing arguments...\nUsage: python aspirer.py [A-Z] [PORT NUMBER]\n")
    else:
        interval = sys.argv[1].upper()       # Interval
        port = sys.argv[2]               # Port

        if(not re.match(r'[A-Z]-[A-Z]', interval)):
            print("Error: The given interval isn't valid...")
        else:
            # Opening files
            infos = open('infos.txt', 'w+', encoding='utf-8')
            dct = open('subst.dic', 'w+', encoding='utf-16')
    
            # Start aspiration
            nbtotal = 0  # Initialize total number of entries
            for c in ascii_uppercase: # Loop through all uppercase letters
                if(c>=interval[0] and c<=interval[2]): # If c is in the given interval, handle case 
                    print("http://localhost:%s/vidal/vidal-Sommaires-Substances-%c.htm" %(port, c))
                    url = urllib.request.urlopen("http://localhost:%s/vidal/vidal-Sommaires-Substances-%c.htm" %(port, c))
                    res = url.read().decode('utf-8')
                    fin = re.findall(r'href="Substance/.*-.*.htm">(\w*)', res)
                    inf = ",.N+subst\n".join(fin)
                    for line in inf:
                        dct.write(line)
                    infos.write("\t- Number of entries in %c: %d\n" %(c, len(fin) ) )
                    nbtotal+=len(fin)
            # Display total number of entries
            infos.write("\n- Total number of entries: %d" %(nbtotal) )
            