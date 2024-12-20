import time

class Time :

    def Init() :
        t = time.time()
        Time.start = time.time()
        Time.current = Time.start
        Time.delta = 0

    def Update(FPSCAP=60) :
        t = time.time()
        Time.delta = t - Time.current
        if Time.delta < 1/FPSCAP :
            time.sleep(1/FPSCAP - Time.delta)
            Time.delta = 1/FPSCAP
            Time.current = time.time()
        else :
            Time.current = t

    def Elapsed() :
        return Time.current - Time.start()
