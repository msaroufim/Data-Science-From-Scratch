import gzip



#read a compressed file
f = gzip.open('file.txt.gz', 'rb')
file_content = f.read()
f.close()

#compress an existing file
f_in = open('file.txt', 'rb')
f_out = gzip.open('file.txt.gz', 'wb')
f_out.writelines(f_in)
f_out.close()
f_in.close()