# Write a Python program to construct the following pattern, using a nested loop number.
# 1                                                                                                             
# 22                                                                                                            
# 333                                                                                                           
# 4444                                                                                                          
# 55555                                                                                                         
# 666666                                                                                                        
# 7777777                                                                                                       
# 88888888                                                                                                      
# 999999999  

no_rows = int(input("Enter  a number: "))

for  num in range(1, no_rows + 1):  # range(1, 4+1)
    for _ in range(num):    # range(0, 3)
        print(num, end="")
    print()
