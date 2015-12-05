#Assignment 1. File createFeatureVectors.py
#Student 1 Name: <Qiuxin Sheng of 1st group member>
#Student 2 Name: <Jiaying He of 2nd group member>
#<Student 1> and <Student 2> attest that this assignment was done by them two and reflects their original work and based on their understanding of the concepts. Both students have equally contributed to the solution of this assignment.
import os
import string
import sys

# cleanup method cleans up the intext string of punctuation, numbers
# and stop words etc. and returns a lowercase string
def cleanup(intext):
   for mark in string.whitespace:
       intext = intext.replace(mark, " ")

   intext = intext.replace("!", " ExclamationMark ")
   intext = intext.replace("?", " QuestionMark ")

   #get rid of the messy code
   ilist = intext.split()
   for char in ilist:
       if not char.isalpha():
           intext = intext.replace(char, "")
           #print char
   intext = ' '.join(ilist)

   #remove punctuations
   for mark in string.punctuation:
       intext = intext.replace(mark, "")
   # #intext = [c for c in intext if c in string.letters]

   intext = intext.lower()

   #remove stop words
   for word in ['<br />', ' a ', ' able ', ' about ', 'an ', ' am ', ' an ', ' and ', ' are ', 
                ' as ', ' at ', ' be ', ' by ', ' for ', ' from ', ' he ', ' her ', 
                ' hers ', ' him ', ' his ', ' in ', ' is ', ' it ', ' its ', ' of ', 
                ' on ', ' or ', ' since ', ' than ', ' that ', ' the ', ' their ', 
                ' them ', ' then ', ' there ', ' these ',  ' this ', ' to ']:
       intext = intext.replace(word," ")

   #remove numbers
   for num in string.digits:
       intext = intext.replace(num, "")

   #get rid of the messy code
   ilist = intext.split()
   for char in ilist:
       if not char.isalpha():
           intext = intext.replace(char, "")
           #print char
   intext = ' '.join(ilist)
   #print(intext)
   return intext

def directory2features(dirName, vocabfilename):
   #open and read the vocabfilename
   allFiles = os.listdir(dirName)

   #put each word in vocabfile as an element in a list
   vocab = open(vocabfilename, 'r')
   vocabString = vocab.read()
   vlist = vocabString.split()
   vocab.close()

   fvectorName = "fvectors_" + dirName + ".txt"
   featureVectorFile = open(fvectorName, 'w')

   for f in allFiles:
       #extract label from the file name, f
       fvector = {}
       firstSplit = f.split(".")
       secSplit = firstSplit[0].split("_")
       #print(secSplit[1])
       #save the review rating
       if len(secSplit) > 1:
           featureVectorFile.write("%s " % secSplit[1])
           #open file in read format
           path = dirName + "/" + f
           file = open(path, 'r')
           #read file as a string
           content = file.read()
           #clean up the string
           content = cleanup(content)

           wordlist = content.split()
           uniquewords = list(set(wordlist))
           for w in uniquewords:
               fvector[vlist.index(w)] = wordlist.count(w)
           for key in sorted(fvector.iterkeys()):
               featureVectorFile.write("%s:%s " % (key, fvector[key]))
           featureVectorFile.write('\n')
           file.close()
   #close file
   featureVectorFile.close()
   return

def directory2Vocab(dirName):
   #start with an empty set
   vSet = set()
   #open a new file vocab.txt in the w mode
   vocabfile = open("Vocab.txt", 'w')

   allFiles = os.listdir(dirName)
   for f in allFiles:
       #open file in read format
       path = dirName + "/" + f
       myfile = open(path, 'r')
       #read file as a string
       filecontent = myfile.read()
       ###############################################################debug
       #print(filecontent)
       #clean up the string by calling cleanup method
       cleanedContent = cleanup(filecontent)
       #split the cleaned strings into words in a list
       words = cleanedContent.split()
       #add the set made from word list into the vSet
       vSet = vSet | set(words)
       myfile.close()

   #write vSet content to vocab file
   vlist = list(vSet)
   for w in vlist:
       vocabfile.write(w + '\n')
   vocabfile.close()
   return

def createFeatureVectors(dirName):
   directory2Vocab(dirName)
   directory2features(dirName, "Vocab.txt")
   return

#####################################################################################              
#if __name__ == "__main__":
   #createFeatureVectors(sys.argv[1])
createFeatureVectors("MovieReviews")