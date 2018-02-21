#!/usr/bin/python

def clean_assemly(program):
    if program in ['velvet', 'Velevet','MetaVelvet','Velveth','VELVET',
                   '~Velvet', ] :
        return 'velvet'

    if program in ['GATK', 'ATKv.'] :
        return 'GATK'

    if program in ['Edena', 'Edna'] :
        return 'Edna'

    if program in ['', '',''] :
        return ''


    if program in ['AMOS-Package', 'AMOS','AMOScmp'] :
        return 'AMOS'

    if program in ['allpaths-lg', 'Allpath-lg','Allpath-LG','vpAllpaths',
                   'AllPaths','ALLPATHS','allpaths'] :
        return 'Allpaths'
    if program in ['Indel_call_and_upgrade.pl', 'N/A','.v','2.6','454','454','454',
        '454','10/3/13','10/3/13','7/17/15','ay','de']:
        return "unknown"
    else:
        return program



with open("assemblerdata_09_17.csv", 'r') as f, open("cleaned_assemblers_09_17.csv",'w') as outf:
    for line in f:
        words=line.split(",")
        #todo: lines.rstrip("\n\r")
        print(clean_assemly(words[1].rstrip("\n\r")))

        taxid=words[0]
        assembly_program=clean_assemly(words[1].rstrip("\n\r"))
        outf.write(str(taxid)+ ','+str(assembly_program)+ "\n")


