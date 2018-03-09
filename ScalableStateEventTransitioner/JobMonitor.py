class JobMonitor:

    stop = False
    def __init__(self):
        print("Job Monitor")

    def monitor(self):
        character=input("Enter your choice: q-quit").strip()
        while character != 'q':
            character = input("Enter your choice: q-quit").strip()
            JobMonitor.stop=True

    @staticmethod
    def isActive():
        if JobMonitor.stop==False:
            return True
        else:
            return False