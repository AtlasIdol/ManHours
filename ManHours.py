import random, datetime

class Department:
    def __init__(self, rh, oh, u):
        self.rh = rh
        self.oh = oh
        self.u = u 
        self.th = self.getth()
        self.mhpu = self.getmphu()

    def getth(self):
        return self.rh + (self.oh * 1.5)

    def getmhpu(self):
        return self.th / self.u

departments = ['2031', '2029', '2030', '2080', '2120', '2140', '2105', '2090', '2114', '2118', '2113', '2085', '2023']
elements = ['rh', 'oh', 'u']
departmentstats = []

for department in departments:
    department = Department()

for department in departments:
    for elem in elements:
        departmentstats.append(department + elem)
       
for item in departmentstats:
    if 'rh' in item:
        item = input(f'Enter regular hours for department {item[:4]}: ')
    elif 'oh' in item:
        item = input(f'Enter the overtime hours for department {item[:4]}: ')
    elif 'u' in item:
        item = input(f'Enter the units for department {item[:4]}: ')
