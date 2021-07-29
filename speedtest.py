import speedtest

s=speedtest.speedtest()

option=int(input("what do you want:"
                 "1:-upload speed"
                 "2:-download speed"
                 "3:-ping"))
if option==1:
    print(s.upload())
elif option==2:
    print(s.download())
elif option==3:
    s=[]
    s.get_server(s)
    print(s.result.ping)

else:
    print("invalid output")