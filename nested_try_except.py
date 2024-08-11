try:
    print("Outer Block")
    try:
        print("10/10", 10/10)

    except:
        print("Inner  Exception")

    else: # OK case and then else case run
        print("Inner else")
    
    finally:
        print("Inner finally")    

except:
    print("Outer Exception")

finally:
    print("Outer finally")