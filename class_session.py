import time

class session():

    def __init__(self):
        self.__time = time.time()
    
    def get_time(self):
        curr_time = time.time() - self.__time
        return curr_time

    def end_timer(self):
        print(self.get_time())

            








