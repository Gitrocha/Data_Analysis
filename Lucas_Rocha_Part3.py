from pathlib import Path
import time as t


print('\n* Configuration of System and Paths')
basepath = Path('.')
output_file = basepath / 'documents' / 'Lucas_Rocha_Part3_Answers.txt'
print('  - Outputs path : ', output_file)

with open(output_file, 'w+') as ffile:
    ffile.write("---------------------------------------------------------------------------------------------------------------------- \n\n")
    ffile.write('                                        Data Integrity \n\n\n')

    ffile.write('The file "Argentina well data test 2019.csv" contains a sample of well attribute data for Argentina'
                ' wells. \n\n')
    ffile.write('QUESTION: What issues can you find with the data that would need to be addressed to ensure the integrity \n')
    ffile.write('of the data ahead of loading this into a database? \n\n')
    ffile.write('ANSWER: If aggregating data from more than one source or if the values have been manually updated by people,\n')
    ffile.write("it's important to certify that all values are consistent with the database datatypes expected. Also, it's\n")
    ffile.write('important to clean the data fields and remove duplicates.\n\n')
    ffile.write("        For example, The field 'well_number' has mixed types (string and integers) and should be treated.\n")
    ffile.write("If it's a large dataset, a good approach would be to create a unique integer index and an auxiliary dictionary\n")
    ffile.write("table to optimize queries.\n\n")
    ffile.write("        In the case of number fields such as latitude, longitude and depth it's also important to verify if\n")
    ffile.write("it contains only floats and integers and use some standardization rule to the number of digits and decimals\n")
    ffile.write("before inserting it into a database.\n\n")
    ffile.write("        For dates and texts, we should ensure that only valid date formats and right encoded characters are\n")
    ffile.write("being inserted into the database.\n\n")
    ffile.write("---------------------------------------------------------------------------------------------------------------------- \n\n")

print('\n* Answers has been provided.')
print('\n* Closing App')
t.sleep(20)
