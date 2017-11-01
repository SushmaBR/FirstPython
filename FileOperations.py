text="this is demo text"
saveFile=open('demo.txt','w')
saveFile.write(text)
saveFile.close()

readFile=open('demo.txt','r')
print(readFile.read())
readFile.close()

appendFile=open('demo.txt','a')
appendFile.write(". this is a demo again.")
appendFile.close()

openFile=open('demo.txt','r')
print(openFile.read())
openFile.close()