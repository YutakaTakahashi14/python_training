try :
    raise Exception("Hello,Error!")
except Exception as e:
    print(e)
finally :
    print("finally")