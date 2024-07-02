"""
WAP to create a decorator function which when applied to a function gives the execution time
of the function
"""
import time

def time_taken(func):
    def inner_fxn(*args,**kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        # return start
        return end-start
        # return end
        
    return inner_fxn

@time_taken
def long_loop():
    for i in range(100000000):
        pass

result=long_loop()
print(f"Taken time is: {result}")

# start = time.time()
# long_loop()
# end = time.time()

# print("Taken time is", end-start)