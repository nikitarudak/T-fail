file_read=open("TextFile1.txt","r",encoding="utf-8-sig")
text=file_read.read()
print(text)
file_read.close()
file_write=open("TextFile1.txt","a",encoding="utf-8-sig")
text=input("Mis tekst on vaja lisada: ")
file_write.write("\n"+text)
file_write.close()
with open("TextFile1.txt","r",encoding="utf-8-sig") as reader:
    print(reader.read())
with open("NewFile2.txt","x") as f:
    for i in range(5):
        text=input("Mis tekst on vaja lisada: ")
        f.write("\n"+text)
with open("NewFile2.txt","r") as f:
    print(f.read())