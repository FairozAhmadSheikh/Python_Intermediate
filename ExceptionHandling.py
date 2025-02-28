# import sys
# while True:
#     try:
#         inp1=int(input("enter numerator : "))
#         inp2=int(input("enter denumerator : "))
#         div=inp1/inp2
#         print(div)
#         break
    # except ValueError:
    #     print("Not allow integers")
    # except ZeroDivisionError:
    #     print("Infity as Divided by zero")
    # other way

    # except(ValueError,ZeroDivisionError) as e :
    #     print(e)

    # other way 
    # except:
    #     a,b,c=sys.exc_info()
    #     print("exception Class : ",a)
    #     print("exception Message: ",b)
    #     print("Error in Line Number: ",c)



# Creating Custom Exceptional classes
class NegativeException(Exception):
    pass

while True:
    try:
        inp1=int(input("enter numerator : "))
        inp2=int(input("enter denumerator : "))
        if inp2<0 or inp1<0:
            raise NegativeException("Negative Numbers not allowed")
        div=inp1/inp2
        print(div)
        break
    except ValueError:
        print("Not allow integers")
    except ZeroDivisionError:
        print("Infity as Divided by zero")
    except NegativeException as e:
        print(e)