import csv
from collections import Counter
from random import randint
from math import sqrt

def look_up(bisac): #looking up what a specific BISAC means
    for x in L4:
        if bisac == x[0]:
            return x

def look_up2(bisac): #looking up the number of occurences of a specific BISAC in database
    for x in L7:
        if bisac == x[0]:
            return x[1]
        
def get_x(a,b,c): #example: if the tag is 'FIC019072' then you would use get_x('FIC','FIC019','FIC019072')
    #outputs the count of lvl1, lvl2, and lvl3 matches in both Peter's library and the Shelfie itself as a list
    acount = 0 #count of 'FIC' (lvl1) matches in lib
    bcount = 0 #count of 'FIC019' (lvl2) matches in lib
    ccount = 0 #count of 'FIC019072' (lvl3) matches in lib
    for x in L9:
        for y in x: #cycling through all bisacs in lib and increasing counts as necessary
            if y[:3] == a:
                acount = acount + 1
            if y[:6] == b:
                bcount = bcount + 1
            if y == c:
                ccount = ccount + 1
    a2count = 0 #exact same thing but in the Shelfie a.k.a 20 random books from Shelby's lib
    b2count = 0
    c2count = 0
    for x in L12:
        for y in x:
            if y[:3] == a:
                a2count = a2count + 1
            if y[:6] == b:
                b2count = b2count + 1
            if y == c:
                c2count = c2count + 1
    if b[3:6] == '000': #if there is no significant lvl2/lvl3 data then there should be no value assigned to a match
        bcount = 0 #example: 'FIC000000' matches with 'FIC000000' on all 3 lvls but should only increase the count for lvl1 because the others are insignificant
        b2count = 0
    if c[6:] == '000':
        ccount = 0
        c2count = 0
    return [acount,a2count,bcount,b2count,ccount,c2count] #list containing counts is returned

L1 = [] #rows from Peter's library sheet
L2 = [] #rows from L1 turned into lists

#Fun facts:

#L2[0][0] = title
#L2[0][1] = authors
#L2[0][2] = pages
#L2[0][3] = price
#L2[0][4] = currency
#L2[0][5] = subjects
#L2[0][6] = bisac

#this format holds true for all csv libraries turned into lists 

#502/549 books have bisac tags
#982 tags total

#235 books with 1 tag
#136 with 2
#78 with 3
#32 with 4
#21 with >4

with open('bisac.csv', newline ='') as csvfile:
    read = csv.reader(csvfile, delimiter=',')
    for row in read:
        L1.append('| '.join(row))

for x in L1:
    L2.append(x.split('| '))

L2.remove(L2[0])

L3 = [] #rows from BISAC sheet
L4 = [] #rows from L3 turned into lists, format is ['BISAC','Tag1','Tag2','Tag3','Tag4']

with open('bisac3.csv', newline ='') as csvfile:
    read = csv.reader(csvfile, delimiter=',')
    for row in read:
        L3.append('| '.join(row))

for x in L3:
    L4.append(x.split('| '))

L4.remove(L4[0])

L5 = [] #rows from shelby lib
L6 = [] #rows from L5 turned into lists

with open('shelby.csv', newline ='') as csvfile: #not needed until I decide to run random tests
    read = csv.reader(csvfile, delimiter=',')
    for row in read:
        L5.append('| '.join(row))

for x in L5:
    L6.append(x.split('| '))

L7 = [] #[All Bisacs, # of children]

child = open('data2.txt',"r")
lines = child.readlines()

for x in lines: #farms elements for L7 from data2.txt to save time
    rows = x.split("\n")
    n = rows[0].index(' ')
    rows[1] = int(rows[0][n:])
    rows[0] = rows[0][:n]
    L7.append(rows)

L8 = [['C Reference Manual (German)', 'HARBISON STEELE', '', '10.95', 'GBP', '', ''], ['Crystal Power', 'Michael G. Smith and Christine Snow', '', '14.5', 'CND', 'OCCULTISM', 'OCC016000'], ["Cunningham's Encyclopedia of Crystal, Gem and Metal Magic", 'Scott Cunningham', '288', '', '', 'CRYSTALS_FOLKLORE , GEMS_FOLKLORE', 'SOC011000'], ['Curing Everyday Ailments the Natural Way', "Reader's Digest Staff", '2384', '59.95', 'AUD', '', ''], ['Darkworld Detective', 'Michael Reaves and Copyright Paperback Collection (Library of Congress) Staff', '257', '', '', '', ''], ['Deep Future', 'Stephen Baxter', '224', '', '', 'COSMOLOGY , TWENTY-FIRST CENTURY', 'SCI015000 , SOC037000'], ['Deep Wizardry', 'Diane Duane', '256', '', '', '', ''], ['Desert Wildlife', 'Edmund C. Jaeger', '320', '', '', 'DESERT ANIMALS , ANIMAL BEHAVIOR , ZOOLOGY_MEXICO , ZOOLOGY_UNITED STATES', 'NAT037000 , SCI070000'], ['Dragons of Eden : Speculations on the Evolution of Human Intelligence', 'Carl Sagan', '288', '', '', 'FICTION_SCIENCE FICTION_GENERAL , INTELLECT , BRAIN , GENETIC PSYCHOLOGY', 'SCI029000 , FIC028000 , PSY000000 , MED057000'], ['Dreamcatcher', '', '150', '', '', '', ''], ['Dreamwalker : The Path of Sacred Power', 'Mary Summer Rain', '240', '', '', 'SPIRITUAL LIFE', 'REL062000'], ["Dr. Ecco's Cyberpuzzles : 36 Puzzles for Hackers and Other Mathematical Detectives", 'Dennis E. Shasha', '256', '', '', 'MATHEMATICAL RECREATIONS', 'MAT025000'], ["Earl Mindell's Herb Bible", 'Earl Mindell', '304', '', '', 'HERBS , HERBS_THERAPEUTIC USE', 'HEA011000 , GAR009000'], ['Ear, the Eye, and the Arm', 'Nancy Farmer', '295', '', '', "CHILDREN'S FICTION , ADVENTURE AND ADVENTURERS_FICTION", 'JUV001000 , JUV000000'], ['Elements of Feng Shui', "Man Ho Kwok and Joanne O'Brien", '', '', '', '', ''], ['Embedded Software Primer', 'David E. Simon', '448', '', '', 'COMPUTER SOFTWARE , SOFTWARE ENGINEERING', 'COM000000 , COM051230'], ['Emotional Intelligence : Why It Can Matter More Than IQ', 'Daniel Goleman', 'xiv, 352', '', '', 'EMOTIONS AND COGNITION , INTELLECT , SUCCESS_PSYCHOLOGICAL ASPECTS', 'PSY000000 , SEL027000 , PSY013000'], ['Ether Cosmic', 'Wilhelm Reich', '', '', '', 'LIFE (BIOLOGY) , ORGONOMY', 'SCI058000 , SCI008000'], ['Etheric Double', 'Arthur E. Powell', '140', '5.95', 'GBP', 'PSYCHOLOGY', 'PSY000000'], ['Feng Shui for You and Your Cat', 'Alison Daniels', '160', '', '', 'FENG SHUI', 'OCC037000']]
#L8 contains 20 random books from shelby's library (pregenerated)

L9 = [] #list of book bisacs in peter's library in the format of [[Book 1 Bisac 1, Book 1 Bisac 2], [Book 2 Bisac 1], ...]
L10 = [] #list of book bisacs in L8/Shelfie, same format as L9

for x in L2:
    if x[6] != '':
        L9.append(x[6].split(' , '))

for x in L8:
    if x[6] != '':
        L10.append(x[6].split(' , '))

L11 = [] #unique BISACs from L10 in [0(score),'BISAC'] format

for x in L10:
    for y in x:
        if [0,y] not in L11:
            L11.append([0,y])

end = 0
while end != len(L10):
    for y in L10[end]:#cycling through all books in Shelfie
        L12 = L10[:] #L12 is a copy of L10
        a = L10[end].index(y)
        b = L10[end][a]
        c = L10[end]
        L12[end] = ['a'] #the book list from which the BISAC we are scoring is turned into ['a'] so that no points are score for the BISAC matching with itself
                         #or other BISACs in the same book
        counts = get_x(b[:3],b[:6],b)
        #example bisac = 'FIC019072'
        n = 1 #number of occurences of 'FIC000000' in database
        o = 1 #number of occurences of 'FIC019000' in database
        p = 1 #number of occurences of 'FIC019072' in database
        #these variables are default set to 1 to avoid 1/0 errors in case a tag not present in the database shows up
        for x in L7:
            if x[0] == b[:3]+'000000':
                n = n*x[1]
            elif x[0] == b[:6]+'000':
                o = o*x[1]
            elif x[0] == b:
                p = p*x[1]
        cst = (len(L2)/len(L8))/2 # cst = ((number of books in peter's library)/(number of books in Shelfie))/2
        #this shelfie:library balancing constant is related to how much we value interest (matches to library) compared to how much we value description (matches
        #within the Shelfie), right now interest is being valued twice as much
        for k in L11:
            if k[1] == b:
                l = (1/sqrt(n))*(counts[0]+cst*counts[1]) #score increase due to lvl1 matches in shelfie+lib
                m = (1/sqrt(o))*(counts[2]+cst*counts[3]) #same thing for lvl2
                q = (1/sqrt(p))*(counts[4]+cst*counts[5]) #same thing for lvl3
                r = 1 #over multiplier based on how many lvls of the BISAC contain info
                if b[6:] != '000': #all 3 lvls containing info = the score being multiplied by 4
                    r = 4
                elif b[3:6] != '000': #2 lvls containg info = the score being multiplied by 2
                    r = 2
                k[0] = k[0] + (l+m+q)*r #scores added
                print(l,m,q,r)
        print(b)
        print("Stats from Lib: #ofTags (Lvl 1) = ",n," Count (Lvl 1) = ",counts[0]," #ofTags (Lvl 2) = ",o," Count (Lvl 2) = ",counts[2]," #ofTags (Lvl 3) = ",p," Count (Lvl 3) = ",counts[4])
        print("Stats from Shelfie: #ofTags (Lvl 1) = ",n," Count (Lvl 1) = ",counts[1]," #ofTags (Lvl 2) = ",o," Count (Lvl 2) = ",counts[3]," #ofTags (Lvl 3) = ",p," Count (Lvl 3) = ",counts[5])
        print("Node Score =", (l+m+q)*r)
        print()
        L12[end] = c #resets L10 so that the book list turned into ['a'] is back to normal for the rest of the runs
    end = end + 1        

for x in L8: #prints all the BISACs+tag info from the shelfie
    y = x[6].split(' , ')
    for z in y:
        print(look_up(z))

L11.sort()
L13 = L11[-10:]
L13.reverse()
print()
print("Control")
with open("Results.txt", "a") as text_file:
    print(file = text_file)
    print("Control", file = text_file)
    print(file = text_file)
print()
for x in L13:
    with open("Results.txt", "a") as text_file: 
        print(x[0],look_up(x[1]))
        print(x[0],look_up(x[1]),file = text_file)

#top 10 tags + score + tag info are outputted to results.txt and screen
