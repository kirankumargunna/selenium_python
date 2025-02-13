import sys
import cProfile
import pstats
import time

sys.set_int_max_str_digits(1000000)
def add(x,y):
    resulting_sum=0
    resulting_sum+=x
    resulting_sum+=y
    return resulting_sum
def fact(n):
    result=1
    for i in range(n):
        result*=i+1
    return result

def do_stuff():
    result=[]
    for i in range(10000):
        result.append(i**2)
    return result

def waste_time():
    time.sleep(5)
    print("hello")


if __name__=="__main__":
    with cProfile.Profile() as profile:
        print(add(100000,1234))
        print(fact(12345))
        print(do_stuff())
        waste_time()


# before printing the results we can also sort them using pstats 

        results=pstats.Stats(profile)
        results.sort_stats(pstats.SortKey.TIME)
        results.print_stats()
        results.dump_stats("result.prof")