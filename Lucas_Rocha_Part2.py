from pathlib import Path
import time as t


print('\n* Configuration of System and Paths')
basepath = Path('.')
output_file = basepath / 'documents' / 'Lucas_Rocha_Part2_Answers.txt'
print('  - Outputs path : ', output_file)

with open(output_file, 'w+') as ffile:
    ffile.write(" ------------------------ --------------------------------- \n\n")
    ffile.write('Contract information for the Block awarded in Round 01 named as CNH-R01-L01-A7 \n\n\n')

    ffile.write('ITEM 5:	What company operates this block? \n')
    ffile.write('ANSWER: Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum \n\n')

    ffile.write('ITEM 6:	What is the area of this block in km2? \n')
    ffile.write('ANSWER: Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum \n\n')

    ffile.write('ITEM 7:	What are the signature date and expiry date associated with this block? \n')
    ffile.write('ANSWER: The document was signed in November 17, 2015. The expiry date of explorarion will be 30 years\n')
    ffile.write('after the signature date, so it will expires by November 17, 2045. \n')

    ffile.write('ITEM 8:	Find 3 Articles relevant to the operating company with respect to this block. \n')
    ffile.write('ANSWER: Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum \n\n')

    ffile.write('ITEM 9:	What is the name of the discovery (field) being developed on this block? \n')
    ffile.write('ANSWER: Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum \n\n')

print('\n* Answers has been provided.')
print('\n* Closing App')
t.sleep(20)


'''


1.	In a web browser (suggest google chrome) navigate to the website for the Comisión Nacional de Hidrocarburos - Gobierno de México (CNH). View this site in Spanish.
2.	There have been a number of Licensing Rounds that have occurred in Mexico, beginning with Round 0 in 2014. Find the link on the website that pertains to licensing rounds. 
3.	Open the Rounds section of this website, and locate the link for the Administración de Contratos.
4.	Locate the contract information for the Block awarded in Round 01 named as CNH-R01-L01-A7. This award occurred in 2015.


Looking at the CNH website for this block:

5.	What company operates this block?
6.	What is the area of this block in km2? 
7.	What are the signature date and expiry date associated with this block?

Further Research about this block:

8.	Find 3 Articles relevant to the operating company with respect to this block. 
9.	What is the name of the discovery (field) being developed on this block?

'''
