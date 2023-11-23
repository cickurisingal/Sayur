a=10

def first():
    #a=20
    def second():
        print(a)
    second()
first()
print(a)