import csv
from collections import Counter
from random import randint
from math import sqrt

# In this experiment each BISAC contributes (0.5+0.5/n) to the total count where n is the number BISACs the book we are
# currently dealing with has, purpose is to make sure books with lots of BISACs don't crowd out books with less
# this is less oppressive than the 1/n experiment

def look_up(bisac):
    for x in L4:
        if bisac == x[0]:
            return x

def look_up2(bisac):
    for x in L7:
        if bisac == x[0]:
            return x[1]
        
def get_x(a,b,c):
    acount = 0
    for x in L9:
        for y in x:
            if y[:3] == a:
                acount = acount + (0.5+0.5/len(x))
    bcount = 0
    for x in L9:
        for y in x:
            if y[:6] == b:
                bcount = bcount + (0.5+0.5/len(x))
    ccount = 0
    for x in L9:
        for y in x:
            if y == c:
                ccount = ccount + (0.5+0.5/len(x))
    a2count = 0
    for x in L12:
        for y in x:
            if y[:3] == a:
                a2count = a2count + (0.5+0.5/len(x))
    b2count = 0
    for x in L12:
        for y in x:
            if y[:6] == b:
                b2count = b2count + (0.5+0.5/len(x))
    c2count = 0
    for x in L12:
        for y in x:
            if y == c:
                c2count = c2count + (0.5+0.5/len(x))
    if b[3:6] == '000':
        bcount = 0
        b2count = 0
    if c[6:] == '000':
        ccount = 0
        c2count = 0
    return [acount,a2count,bcount,b2count,ccount,c2count]

L1 = [] #rows from Peter's library sheet
L2 = [] #rows from L1 turned into lists

with open('bisac.csv', newline ='') as csvfile:
    read = csv.reader(csvfile, delimiter=',')
    for row in read:
        L1.append('| '.join(row))

for x in L1:
    L2.append(x.split('| '))

L2.remove(L2[0])

L3 = [] #rows from BISAC sheet
L4 = [] #rows from L3 turned into lists

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
#L8 contains 20 random books from shelby's library

L9 = [] #list of book bisacs in peter's library
L10 = [] #list of book bisacs in L8/Shelfie

for x in L2:
    if x[6] != '':
        L9.append(x[6].split(' , '))

for x in L8:
    if x[6] != '':
        L10.append(x[6].split(' , '))

L11 = [] #unique tags from L8 in [0(score),tag] format

for x in L10:
    for y in x:
        if [0,y] not in L11:
            L11.append([0,y])

end = 0
while end != len(L10):
    for y in L10[end]:
        L12 = L10[:]
        a = L10[end].index(y)
        b = L10[end][a]
        c = L10[end]
        L12[end] = ['a'] 
        scores = get_x(b[:3],b[:6],b)
        n = 1
        o = 1
        p = 1
        for x in L7:
            if x[0] == b[:3]+'000000':
                n = n*x[1]
            elif x[0] == b[:6]+'000':
                o = o*x[1]
            elif x[0] == b:
                p = p*x[1]
        cst = (len(L2)/len(L8))/2
        for k in L11:
            if k[1] == b:
                l = (1/sqrt(n))*(scores[0]+cst*scores[1])
                m = (1/sqrt(o))*(scores[2]+cst*scores[3])
                q = (1/sqrt(p))*(scores[4]+cst*scores[5])
                r = 1
                if b[6:] != '000':
                    r = 4
                elif b[3:6] != '000':
                    r = 2
                k[0] = k[0] + (l+m+q)*r
                print(l,m,q,r)
        print(b)
        print("Stats from Lib: #ofTags (Lvl 1) = ",n," Count (Lvl 1) = ",scores[0]," #ofTags (Lvl 2) = ",o," Count (Lvl 2) = ",scores[2]," #ofTags (Lvl 3) = ",p," Count (Lvl 3) = ",scores[4])
        print("Stats from Shelfie: #ofTags (Lvl 1) = ",n," Count (Lvl 1) = ",scores[1]," #ofTags (Lvl 2) = ",o," Count (Lvl 2) = ",scores[3]," #ofTags (Lvl 3) = ",p," Count (Lvl 3) = ",scores[5])
        print("Node Score =", (l+m+q)*r)
        print()
        L12[end] = c 
    end = end + 1        

for x in L8:
    y = x[6].split(' , ')
    for z in y:
        print(look_up(z))

L11.sort()
L13 = L11[-10:]
L13.reverse()
print()
print("Experiment 3: 0.5+0.5/n Count")
with open("Results.txt", "a") as text_file:
    print(file = text_file)
    print("Experiment 3: 0.5+0.5/n Count", file = text_file)
    print(file = text_file)
print()
for x in L13:
    with open("Results.txt", "a") as text_file: 
        print(x[0],look_up(x[1]))
        print(x[0],look_up(x[1]),file = text_file)
