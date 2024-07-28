def security(fn):
    print("Security Check ")
    return fn

@security
def order():
    print("Oder Processing ")

@security
def sale():
    print("Sale Processing ")
    
order()