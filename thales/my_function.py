import time

def print_time_list_creation(
    append_time:float,
    list_comp_time:float,
    range_time:float):
    
    print(f'append_time={append_time}')
    print(f'list_comp_time={list_comp_time}')
    print(f'range_time={range_time}')

def evaluate_time_list_creation(n : int): # did you know you can type in python?
    begin_append=time.time()
    empty=[]
    for i in range(n):
        empty.append(n)
    total_append=time.time()-begin_append

    begin_list_comp=time.time()
    empty=[i for i in range(n)]
    total_list_comp=time.time()-begin_list_comp

    begin_range=time.time()
    empty=list(range(n))
    total_range=time.time()-begin_range

    print_time_list_creation(total_append,total_list_comp,total_range)

evaluate_time_list_creation(10000000)
# results for 10000000
# append_time=1.1212551593780518
# list_comp_time=0.6875247955322266
# range_time=0.9541969299316406

        