# Project: Information Extraction 
Project carried out in S1 of the section L3 ACAD A at USTHB, for the subject "Information Extraction".

## Author 
- **Name:** Lilia Mehamli 
- **Student ID:** 181831083114
- **Section:** ACAD A
- **Github Account:** cr105ph1nx

## Goal
The final goal is to create a dictionary of medical data using different language processing tools (Python, Unitex, Gramlab).

## Function
### server.py: 
- We have to load the project on localhost with WEBSERVER.

Setup: `webserver.py 8080`
### aspirer.py: 
- Using Web scraping with the python library beautifulsoup and from vidal.fr website, retrieve the names of drugs sorted by active substance from A to Z encoded in "UCS-2 LE BOM".
- Give the user the possibility of determining the interval of the pages to be processed in alphabetical order (ex: A-C, C-G or F-K).
- Analyze the output file containing the names of the drugs, then calculate the number of medical entities per active substance and for each letter of the alphabet.

Setup: `aspirer.py A-W 8080`
### enrichir.py: 
- Extend the output file containing the names of drugs, by analyzing a "corpus-medical.txt" file to add new drugs by trade name or by active substance, taking into account duplicates and sorting.

Setup: `enrichir.py corpus-medical.txt`
### posologie.grf:
- Build an extraction graph under Unitex in order to extract the occurrences of "treatment dosages" (a treatment dosage contains the name of the drug, the dose and the rate (or frequency).
### unitex.py:
- We have to create a unitex.py script in order to call UNITEX to use the graph.
- The file being very large, the dosages must be extracted using regular expressions and the system dictionary "Dela_fr.bin" provided by Unitex in order to be able to use lexical masks. 

Setup: `unitex.py`
### sqlite.py
- record the dosages contained in the file "concord.html" in the SQLite database named "extraction.db"

Setup: `sqlite.py`

## Ressources
- **Python**: beautifulsoup, urllib, regex, http, os, sqlite3
- **Unitex**
- **Database**: sqlite3