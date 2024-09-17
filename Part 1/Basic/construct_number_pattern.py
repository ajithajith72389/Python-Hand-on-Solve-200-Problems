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

for  no_rows in range(1, no_rows + 1):
    for _ in range(no_rows):
        print(no_rows, end="")
    print()
