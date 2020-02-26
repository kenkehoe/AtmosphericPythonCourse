#! /usr/bin/env python3

from multiprocessing import Process, Pool, cpu_count, current_process
import numpy as np
import time
import sys

# https://pymotw.com/2/multiprocessing/basics.html

def some_function(wait=0):
    # Wait for 5 seconds
    time.sleep(wait)
    print(f"Waited {wait} seconds to finish")


if True:
    jobs_2_run = [1, 1, 1, 1]
    print(f"\nLooping over {len(jobs_2_run)} jobs one at a time.")
    start = time.time()
    for ii in jobs_2_run:
        some_function(ii)
    print(f"Job took {time.time()-start} to complete.")

    jobs = []
    print(f"\nLooping over {len(jobs_2_run)} jobs {len(jobs_2_run)} at a time.")
    start = time.time()
    for ii in jobs_2_run:
        p = Process(target=some_function, args=(ii,))
        jobs.append(p)
        p.start()
    print('Notice this statement is printed right away and before the jobs are completed, '
          'but the print statement is after the jobs are set to run. The code after is '
          'set to run without waiting.')
    p.join()
    print(f"Job took {time.time()-start} to complete.")


if False:
    data = (['a', '2'], ['b', '4'], ['c', '1'], ['d', '0'],
            ['e', '1'], ['f', '3'], ['g', '2'], ['h', '3'])

    def mp_worker( input_tuple):
        inputs, the_time = input_tuple
        print(f"Starting processs {inputs}\tWaiting {the_time} seconds")
        time.sleep(int(the_time))
        print(f"\tProcess {inputs}\tDONE")

    cpu_utilize = cpu_count()
    print(f'\nNumber of CPUs used {cpu_utilize}.\n')
    jobs = []
    for ii in data:
        p = Process(target=mp_worker, args=(ii, ))
        jobs.append(p)
        p.start()

if False:
    data = (['a', '2'], ['b', '4'], ['c', '1'], ['d', '0'],
            ['e', '1'], ['f', '3'], ['g', '2'], ['h', '3'])

    def mp_worker( input_tuple):
        inputs, the_time = input_tuple
        print(f"Starting processs {inputs}\tWaiting {the_time} seconds")
        time.sleep(int(the_time))
        print(f"\tProcess {inputs}\tDONE")

    cpu_utilize = cpu_count() // 2  # Set number of CPUS to half with int division.
    # Can set a higher number but it will just stay at number of CPUs.
#    cpu_utilize = cpu_count() * 2  
    print(f'\nNumber of CPUs used {cpu_utilize}.\n')
    def mp_handler():
        p = Pool(cpu_utilize)
        p.map(mp_worker, data)

    mp_handler()


if False:
    def worker():
        name = current_process().name
        print(name, 'Starting')
        time.sleep(2)
        print(name, 'Exiting')

    def my_service():
        name = current_process().name
        print(name, 'Starting')
        time.sleep(3)
        print(name, 'Exiting')

    service = Process(name='my_service', target=my_service)
    worker_1 = Process(name='worker 1', target=worker)
    worker_2 = Process(target=worker) # use default name

    worker_1.start()
    worker_2.start()
    service.start()


if False:
    def daemon():
        p = current_process()
        print('Starting:', p.name, p.pid)
        sys.stdout.flush()
        time.sleep(2)
        print('Exiting :', p.name, p.pid)
        sys.stdout.flush()

    def non_daemon():
        p = current_process()
        print('Starting:', p.name, p.pid)
        sys.stdout.flush()
        print('Exiting :', p.name, p.pid)
        sys.stdout.flush()

    d = Process(name='daemon', target=daemon)
    d.daemon = True

    n = Process(name='non-daemon', target=non_daemon)
    n.daemon = False

    # User this to start the processing
    if True:
        d.start()
        time.sleep(1)  # Wait one second to show difference in completion times
        n.start()

    # If we want the main process to wait until the daemon has finished used join()
    # method.
    elif False:
        d.start()
        n.start()

        d.join()
        n.join()

    # We can tell it how long to wait for daemon process. If the daemon process takes
    # longer than that number of seconds the main process will terminate and kill the
    # daemon process
    elif False:
        d.start()
        n.start()

        d.join(1)
        print('d.is_alive()', d.is_alive())
        n.join()

if False:

    cpu_utilize = cpu_count()
    p = Pool(processes=cpu_utilize)  # Define number of CPUs to use

    jobs_2_run = list(range(0, cpu_utilize,))
    jobs_2_run.reverse()
    print(jobs_2_run)
    p.map(some_function, jobs_2_run)

#cpu_utilize = 32

#if cpu_utilize > cpu_count():
#    cpu_utilize = int(cpu_count())

#print(cpu_utilize)

#number_jobs_2_run = 10

#pool = Pool(processes=int(cpu_utilize))  # Define number of CPUs to use




#with Pool(1) as p:
#    p.map(some_function, jobs_2_run)


#waits = [1 for ii in range(number_jobs_2_run)]
#return_values = pool.starmap(waits)

#return_error = pool.starmap(
#            process_data, product(
#                process_list, [dq_proc_mod_base],
#                [run_id], [args], [data_path], [make_metrics],
#                [make_plots], [process_db_write], [plot_db_write],
#                [make_thumbnail]))

