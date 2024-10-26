try:
    s=open(file='file_1.txt')
    r=s.read()
    print(r)
    s2=open(file='file_2.txt')
    r2=s2.read()
    print(r2)
    s3=open(file='file_3.txt')
    r3=s3.read()
    print(r3)
except Exception as er:
    print("this is error",er)