import datetime
import time


def rec(name):

    
    f = open(f"members/{name}.txt","a+")

    date = datetime.date.today()
    time = datetime.datetime.now().strftime("%I:%M:%S %p")

    
    f.write(f"{date} {time}\n")
    f.close()



if __name__ == '__main__':
    rec("test")
    



