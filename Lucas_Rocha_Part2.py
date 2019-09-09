from pathlib import Path
import time as t


print('\n* Configuration of System and Paths')
basepath = Path('.')
output_file = basepath / 'documents' / 'Lucas_Rocha_Part2_Answers.txt'
print('  - Outputs path : ', output_file)

with open(output_file, 'w+') as ffile:
    ffile.write("---------------------------------------------------------------------------------------------------------------------- \n\n")
    ffile.write('                 Information about the Block awarded named as CNH-R01-L01-A7 \n\n\n')

    ffile.write('ITEM 5:	What company operates this block? \n')
    ffile.write('ANSWER: The block is operated by Talos Energy Offshore Mexico 7 in a shared production mode which \n')
    ffile.write('includes Sierra Oil and Gas and Premier Oil.\n\n')

    ffile.write('ITEM 6:	What is the area of this block in km2? \n')
    ffile.write('ANSWER: The surface area is around 464.799 km2, as described in file CNH-R01-L01-A7-2015.pdf (Page 76, Attachment 1)\n\n')

    ffile.write('ITEM 7:	What are the signature date and expiry date associated with this block? \n')
    ffile.write('ANSWER: The document was signed on November 17, 2015. The expiry date of exploration will be 30 years\n')
    ffile.write('after the signature date, so it will expire by November 17, 2045. \n\n')

    ffile.write('ITEM 8:	Find 3 Articles relevant to the operating company with respect to this block. \n')
    ffile.write('ANSWER: * 1) https://www.wsj.com/articles/mexico-awards-first-oil-block-in-historic-auction-1436978568 \n')
    ffile.write('        * 2) https://www.oedigital.com/news/451293-mexico-s-round-one-phase-two-a-success \n')
    ffile.write('        * 3) https://www.nsenergybusiness.com/projects/zama-oil-field-gulf-of-mexico/ \n\n')

    ffile.write('ITEM 9:	What is the name of the discovery (field) being developed on this block? \n')
    ffile.write("ANSWER: It's called Zama Field, and is located near Tabasco City in the Gulf of Mexico. \n\n")
    ffile.write("----------------------------------------------------------------------------------------------------------------------")

print('\n* Answers has been provided.')
print('\n* Closing App')
t.sleep(20)
