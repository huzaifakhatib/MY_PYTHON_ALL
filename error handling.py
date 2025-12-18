#
# a = input("Enter number for table: ")
#
# print(f"Multiplication table of {a} is:")
#
# try:
#     num = int(a)  # convert once
#     for i in range(1, 11):
#         print(f"{num} X {i} = {num * i}")
#
# except Exception as e:
#     print("Error:", e)
#
# print("Some imp lines")


#finally
# try:
#         l=[1,4,5,6,7]
#         i=int(input("Enter number index: "))
#         print(l[i])
#
# except :
#         print(f"some error index {i} is not defined")
#
# finally:
#         print("finally")



# # Raising custom errors
# class myerror(Exception):
#     pass
# def check_number(num):
#     if num<0:
#         raise myerror("negative number")
#     return "number is valid"
#
# try:
#     k=int(input("enter number"))
#     print(check_number(k))
# except myerror as e:
#     print(e)