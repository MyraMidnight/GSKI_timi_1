import time

def time_start():
    return time.time_ns()

def time_end(start_var):
    end_var = time.time_ns()
    diff_var = end_var - start_var
    print(diff_var, " nano seconds")
    seconds = diff_var/(10**9)
    minutes = seconds // 60
    print(seconds, " seconds")
    print(minutes, " minutes")


start = time_start()

my_var = 1
while my_var < 200:
    my_var += 1

time_end(start)






