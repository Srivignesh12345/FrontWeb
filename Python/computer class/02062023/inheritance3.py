class college:
    def name(self):
        print("sri eshwar")
class clgname(college):
    def name1(self):
        print("ksr college")
class clglocation(college):
    def name2(self):
        print("coimbatore")
class placement(clgname,clglocation,college):
    def name3(self):
        print("vv good")
p=placement()
p.name1()
p.name()
p.name2()
p.name()
