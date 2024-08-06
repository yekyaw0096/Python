def method():
    print("Version One")

def method(a):
    print("Version Two")

def method(a,b):
    print("Version Three")

#dynamic programming only recognize the last method of overwrite

method(1,21)