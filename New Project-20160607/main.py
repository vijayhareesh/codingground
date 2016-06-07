class vijay():
    numcount = 0
    total = 0
    def disp_msg(self):
        #print "hello world!"
        print "total numbers : " + str(self.numcount)
        print "total sum : " + str(self.total)
    def set_num(self,numb):
        self.num = numb
        self.numcount+=1
        self.total += self.num
    #def __init__(self):
        #self.numcount = 0
        #self.numcount+=1
        #self.num = numb
def main():
    a = vijay()
    a.set_num(4)
    a.set_num(7)
    a.set_num(10)
    a.disp_msg()

main()