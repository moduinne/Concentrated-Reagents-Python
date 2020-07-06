import docx2txt


my_text = docx2txt.process("test.docx")
print (my_text.strip()[0:200])
    

