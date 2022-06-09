import magic
import glob
import hashlib

filenames = glob.glob("dokaz3/*")

for filename in filenames:
    # print(filename, magic.from_file(filename))
    print(filename, hashlib.md5(open(filename, 'rb').read()).hexdigest())
    print(filename, hashlib.sha1(open(filename, 'rb').read()).hexdigest())
    print(filename, hashlib.sha256(open(filename, 'rb').read()).hexdigest())

# print("Docx", hashlib.md5(open("test.docx", 'rb').read()).hexdigest())
# print("Jpg", hashlib.md5(open("test.jpg", 'rb').read()).hexdigest())

# print("Docx", hashlib.sha1(open("test.docx", 'rb').read()).hexdigest())
# print("Jpg", hashlib.sha1(open("test.jpg", 'rb').read()).hexdigest())