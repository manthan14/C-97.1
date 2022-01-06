introString=input("Enter String")
charCount=0
wordCount=1
for i in introString:
    charCount=charCount+1   
    if i==' ':
        wordCount=wordCount+1
print("numberOfWords",wordCount)
print("numbersChar",charCount)        