import re
import pysubs2
# list of all the lines
lst = list() #src
# List of bionic lines
bioniclinelst = list()
#lst2 = list()
newbioniclinelst = list() #target

lst3 = list()


filename = input('Where is your subtitle file (with .txt extension!) located? ')
infile = open(filename, 'r')
lines = infile.readlines()

for line in lines:
    sline = line.strip()

    if re.search('^[0-9]+',sline) or len(sline)==0:
        continue
    lst.append(sline)
#print(lst)


infile.close()

infile = open(filename, 'r')
lines = infile.readlines()

for line in lines:
    line = line.strip()
    if re.search('^[0-9]+',line) or len(line)==0:
        continue
    #print(line)
    xline = line.split() #xline is a list of words in a line
    #print(xline
    for word in xline:
        #print(word)
        quotient = len(word) // 2
        if (len(word) % 2) == 0:
            numbold = quotient
        else:
            numbold = quotient + 1
        boldedpart = word[0:numbold]
        bionic = '<b>' + boldedpart + '</b>'
        #print(bionic)
        
        bionicword = word.replace(boldedpart, bionic)
        #print(bionicword)
        bioniclinelst.append(bionicword)
    bionicline = ' '.join(bioniclinelst)
    #print(bionicline)
    bioniclinelst = list()

    newbioniclinelst.append(bionicline)

    #print('Done!')
#print(newbioniclinelst)

replacements = {lst[i] : newbioniclinelst[i] for i in range(len(lst))}

with open(filename) as infile, open('subtitlefilenew.srt', 'w', encoding='utf-8') as outfile:
    for line in infile:
        for src, target in replacements.items():
            line = line.replace(src, target)
        outfile.write(line)

subs = pysubs2.load("subtitlefilenew.srt")
subs.save("modified_subtitles.ass")
with open("modified_subtitles.ass") as fp:
    fp.read()

stylereplacement = {'Style: Default,Arial,20.0,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,0,0,0,0,100.0,100.0,0.0,0.0,1,2.0,2.0,2,10,10,10,1' : 'Style: Default,Arial,20,&H00000000,&H0000000C,&H00ECECEC,&H00E7E7E7,0,0,0,0,100,100,0,0,3,1,1,2,10,10,10,1'}

with open('modified_subtitles.ass') as infile, open('modified_subtitlesnew.ass', 'w') as outfile:
    for line in infile:
        for src1, target1 in stylereplacement.items():
            line = line.replace(src1, target1)
        outfile.write(line)
print("modified_subtitlesnew.ass file is your bionic subtitle!")
