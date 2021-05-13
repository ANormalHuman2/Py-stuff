print ("For all the codes type CODE")
def RPV():
    recpyrl=float(input("Base Length "))
    recpyrw=float(input("Base Width "))
    recpyrh=float(input("Height "))
    RPV=(recpyrl*recpyrw*recpyrh)/3
    print (RPV)
def RPSA():
    recpyrl=float(input("Base Length "))
    recpyrw=float(input("Base Width "))
    recpyrthl=float(input("Triangle Height On The Legth Side "))
    recpyrthw=float(input("Triangle Height On The Width Side "))
    recpyrsa=(recpyrl*recpyrw+recpyrthl*recpyrl+recpyrthw*recpyrw)
    print(recpyrsa)
def TPV():
    bw=float(input("Base Width "))
    bh=float(input("Base Height"))
    h=float(input("Height "))
    v=(1/3)*((bw*bh)/2)*h
    print (v)
def TPSA():
    bw=float(input("Base Width "))
    bh=float(input("Base Height"))
    tw=float(input("Side Width "))
    th=float(input("Side Height "))
    ssa=tw*th/2
    TPSA=ssa*3+bw*bh/2
    print (TPSA)
def CSA():
    print ("type r then l")
    r=float(input("r "))
    sl=float(input("l "))
    CSA=(3.14*r*r)+(3.14*sl*r)
    print(CSA)
def CSL():
    print ("Type r then SA")
    r=float(input("r "))
    CSA=float(input("SA "))
    sl=CSA/(3.14*r)-r
    round (sl)
    print (sl)
while True:
    print ("If lost type CODE")
    SAstart=input("Type here ---> ")
    if SAstart == "CODE":
        print ("For the volume of a rectangular pyramid type RPV.")
        print ("For the suface area of a rectangular pyramid type RPSA.")
        print ("For the volume of a triangular pyramid type TPV.")
        print ("For the suface srea of a triangular pyramid type TPSA.")
        print ("If you would like to find the surface area of A Cone type CSA.")
        print ("Or for the slant length of a cone the code is CSL")
    if SAstart == "RPV":
        RPV()
    if SAstart == "RPSA": 
        RPSA() 
    if SAstart == "TPV":
        TPV()
    if SAstart == "TPSA":
        TPSA()
    if SAstart == "CSA":
        CSA()
    if SAstart == "CSL":
        CSL()