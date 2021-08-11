import sys, time
from daemonize import Daemon

class MyDaemon(Daemon):
    def run(self):
        count = 0
        while True:
            time.sleep(3)
            open("~/fun.txt", 'a+').write(f"Freedom {count}\n")
            count += 1

if __name__ == "__main__":
    daemon = MyDaemon('/tmp/daemon-example.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print(f"Usage: {sys.argv[0]} start|stop|restart")
        sys.exit(2)
