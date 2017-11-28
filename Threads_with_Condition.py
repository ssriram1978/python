import logging
import threading
import time
import queue

class threaded_queue:
    time_to_exit = 0
    condition = threading.Condition()
    q = queue.Queue()

    def __init__(self):
        logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s:(%(threadName)-2s):%(message)s')
        self.start()


    def start(self):
        for index in range(10):
            thread_name = "c" + str(index)
            c = threading.Thread(name=thread_name,
                                 target=threaded_queue.consumer,
                                 args=(threaded_queue.condition,
                                       threaded_queue.q))
            c.start()

        for index in range(10):
            p = threading.Thread(name='p',
                                 target=threaded_queue.producer,
                                 args=(threaded_queue.condition,
                                       threaded_queue.q))
            p.start()


        while threaded_queue.q.empty() == False:
            with threaded_queue.condition:
                threaded_queue.condition.notifyAll()
        #terminate all consumer threads.
        threaded_queue.time_to_exit = 1

    @staticmethod
    def consumer(cond,threadQ):
        """wait for the condition and use the resource"""
        logging.debug('Starting consumer thread')
        while threaded_queue.time_to_exit == 0 :
            with cond:
                cond.wait()
                print()
                logging.debug('Resource (%d) is consumed.' %(threadQ.get()))

    @staticmethod
    def producer(cond,threadQ):
        """set up the resource to be used by the consumer"""
        logging.debug('Starting producer thread')
        with cond:
            logging.debug('Making resource available')
            for i in range(10000):
                threadQ.put(i)
            cond.notifyAll()


th_q = threaded_queue()

