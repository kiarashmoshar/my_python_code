fw= open('sample.txt','w')
fw.write("hello\n")
fw.write("Hi\n")
fw.close()

fr= open('sample.txt','r')
text=fr.read()
print(text)
fr.close()