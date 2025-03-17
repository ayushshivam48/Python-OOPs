class Account:
    def __init__ (self, acc_no, acc_pass):
        self.acc_no = acc_no    #public
        self.__acc_pass = acc_pass  #private
        
    def reset_pass(self):
        print(self.__acc_pass)    #accessed inside the class
        

acc1 = Account("12345", "abcde")

print(acc1.acc_no)
print(acc1.reset_pass())

#Note :- anything start with double-underscore'__' is a private data