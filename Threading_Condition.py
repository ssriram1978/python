import logging
import threading
import time
import queue

class threaded_queue:
    def __init(self):
        self.condition = threading.Condition()
        self.q = queue.Queue()
        self.time_to_exit = 0
        self.start()

    def start(self):
        for index in range(10):
            thread_name = "c" + str(index)
            c = threading.Thread(name=thread_name,
                                 target=self.consumer,
                                 args=(self.condition,))
            c.start()

        for index in range(3):
            time.sleep(2)
            p = threading.Thread(name='p',
                                 target=self.producer,
                                 args=(self.condition,))
            p.start()
        #terminate all consumer threads.
        self.time_to_exit = 1

    def consumer(self,cond):
        """wait for the condition and use the resource"""
        logging.debug('Starting consumer thread')
        while self.time_to_exit == 0 :
            with cond:
                cond.wait()
                print()
                logging.debug('Resource (%d) is available to consumer' %(self.q.get()))

    def producer(self,cond):
        """set up the resource to be used by the consumer"""
        logging.debug('Starting producer thread')
        with cond:
            logging.debug('Making resource available')
            for i in range(10):
                self.q.put(i)
            cond.notifyAll()

logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s (%(threadName)-2s) %(message)s',
        )
th_q = threaded_queue()

