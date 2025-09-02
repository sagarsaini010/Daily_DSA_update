def pattern1(n):

# * * * * * 
# * * * * * 
# * * * * *
# * * * * *
# * * * * *

    for i in range(n):
        for j in range(n):
            print("*",end=" ")
        print("")    
def pattern2(n):
# * 
# * * 
# * * *
# * * * *
# * * * * *


    for i in range(n):
        for j in range(i+1):
            print("*",end=" ")
        print("")    
def pattern3(n):

# * * * * * 
# * * * * 
# * * *
# * *
# *


    for i in range(n):
        for j in range(n-i):
            print("*",end=" ")
        print("")    
def pattern4(n):
# *****
#  ****
#   ***
#    **
#     *

    for i in range(n):
        for j in range(i):
            print(" ",end="")
        for k in range(n-i):
            print("*",end="")    
        print("")
def pattern5(n):
# 1
# 12
# 123
# 1234
# 12345

    for i in range(n):
        for j in range(i+1):
            print(j+1,end="")
        print("")    
def pattern6(n):

# 1
# 22
# 333
# 4444
# 55555

    for i in range(n):
        for j in range(i+1):
            print(i+1,end="")
        print("")    
def pattern7(n):

# 12345
# 1234
# 123
# 12
# 1

    for i in range(n):
        for j in range(n-i):
            print(j+1,end="")
        print("")    
def pattern8(n):

#     *
#    ***
#   *****
#  *******
# *********

    for i in range(n):
        for j in range(n-(i+1)):
            print(" ",end="")
        for k in range(2*i+1):
            print("*",end="")
        print("")    
def pattern9(n):

# *********
#  *******
#   *****
#    ***
#     *

    for i in range(n):
        for k in  range(i):
            print(" ",end="") 
        for j in range(2*n-(2*i+1)):
            print("*",end="")
       
        print("")        
def pattern10(n):


#     *
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *



    for i in range(n):
        for j in range(n-(i+1)):
            print(" ",end="")
        for k in range(2*i+1):
            print("*",end="")
        print("")    
    for x in range(n):  
        for l in range(x):
            print(" ",end="")        
        for m in range(2*n-(2*x+1)):
            print("*",end="")
           
        print("")
def pattern11(n):

# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *


    for i in range(2*n):
        start = i
        if i>n:
            start=2*n-i
        for j in range(start):
            print("*",end="")
        print("")    
def pattern12(n):

# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1

    for i in range(n):
        value = 1
        if i%2!=0:
            value =0
        for j in range(i+1):
            print(value,end=" ")
            value = 1-value
        print("")         
def pattern13(n):

# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321

    for i in range(n):
        num=i+1
        for j in range(i+1):
            print(j+1,end="")
        for k in range(2*n-(2*(i+1))):
            print(" ",end="")
        for l in range(i+1):
            print(num,end="")
            num= num-1        
        print("")    
def pattern14(n):

# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15 

    value = 1
    for i in  range(n):
        for j in range(i+1):
            print(value,end=" ")
            value= value+1
        print("")
def pattern15(n):

# A
# AB
# ABC
# ABCD
# ABCDE

    for j in range(n):
        for i in range(j+1):
            print(chr(65+i),end="")
        print("")
def pattern16(n):

# A B C D E 
# A B C D 
# A B C 
# A B 
# A 

    for i in range(n):
        for j in range(n-i):
            print(chr(65+j),end=" ")
        print("")    
def pattern17(n):

# A 
# B B 
# C C C 
# D D D D 
# E E E E E 


    for i in range(n):
        for j in range(i+1):
            print(chr(65+i),end=" ")
        print("")    
def pattern18(n):

#     A
#    ABA
#   ABCBA
#  ABCDCBA
# ABCDEDCBA


  
    for i in range(n):
        num =0
        for j in range(n-(i+1)):
            print(" ",end="")
        for k in range(1,2*(i+1)):
            print(chr(65+num),end="")
            if k <(2*i+1)/2:
                num +=1
            else:
                num -=1
        print('')
def pattern19(n):

# E 
# D E 
# C D E
# B C D E
# A B C D E


    for i in range(n):
        num = n-i-1
        for j in range(i+1):
            print(chr(65+(num)),end=" ")
            num +=1

        print('')  
def pattern20(n):


# * * * * * * * * * * 
# * * * *     * * * * 
# * * *         * * *
# * *             * *
# *                 *
# *                 *
# * *             * *
# * * *         * * *
# * * * *     * * * *
# * * * * * * * * * *



    for i in range(n):
        # stars
        for j in range(n-i):
            print("*",end=" ")
        # space
        for k in range(2*i):
            print(" ",end=" ")
 
        # stars
        for l in range(n-i):
            print("*",end=" ")
        print("")
    for a in range(n):
        #stars
        for b in range(a+1):
            print("*",end=" ")

        #space
        for c in range(2*n-(2*a+2)):
            print(" ",end=" ")



        #stars
        for d in range(a+1):
            print("*",end=" ")

        print('')
def pattern21(n):
    for i in range(n*2-1):
        start = i+1
        if i>=n:
            start = 2*n-i-1
        for j in range(start):
            print("*",end=" ")

        if i<n:
            spa=2*n-(2*i+2)
        else:
            spa = 2*i-(2*n-2)
        for k in range(spa):
            print(" ",end=" ")

        star = i+1
        if i>=n:
            star = 2*n-i-1
        for l in range(star):
            print("*",end=" ")

        
        print("")
def pattern22(n):

# *****
# *   *
# *   *
# *   *
# *****


    for i in range(n):
        for j in range(n):
            if i==0 or j==0 or i==n-1 or j==n-1:
                print("*",end="")
            else:
                print(" ",end="")
               
        print("")
def pattern23(n):
    for i in range(2*n-1):
        for j in range(2*n-1):
            if i==0 or j==0 or i==2*n-2 or j ==2*n-2:
                print(n-1,end="")
            else:
                print(" ",end="")
        print("")



pattern11(4)


            