#!/usr/bin/env python
import Queue
import threading
import urllib2
import time

from ProxyFinder import ProxyFinder

input_file = 'proxylist.txt'


queue = Queue.Queue()
output = []

class ThreadUrl(threading.Thread):
    """Threaded Url Grab"""
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            #grabs host from queue
            proxy_info = self.queue.get()

            try:
                proxy_handler = urllib2.ProxyHandler({'http':proxy_info})
                opener = urllib2.build_opener(proxy_handler)
                opener.addheaders = [('User-agent','Mozilla/5.0')]
                urllib2.install_opener(opener)
                req = urllib2.Request("http://www.google.fr")
                sock=urllib2.urlopen(req, timeout= 20)
                output.append(('good', proxy_info))
                print("Proxy: %s is working" % proxy_info)
            except urllib2.HTTPError, e:
                output.append(('bad', proxy_info))
                print('Proxy: %s, Error code: %d' % (proxy_info, e.code))
            except Exception, detail:
                output.append(('bad',proxy_info))
                print('Proxy: %s, Error : %s' % (proxy_info, detail))
            #signals to queue job is done
            self.queue.task_done()

start = time.time()
def main():

    """
    scrape freeproxylists for new proxylist
    :return:
    """
    proxyfinder = ProxyFinder()
    hosts = proxyfinder.find()

    """
    read proxies from file
    """
    #hosts = [host.strip() for host in open(input_file).readlines()]

    threads = len(hosts)
    #spawn a pool of threads, and pass them queue instance
    for i in range(threads):
        t = ThreadUrl(queue)
        t.setDaemon(True)
        t.start()

    #populate queue with data
    for host in hosts:
        queue.put(host)

    #wait on the queue until everything has been processed
    queue.join()

main()
print("proxy check stats")
print("-" * 20)
for proxy,host in output:
    print proxy,host

print "Elapsed Time: %s" % (time.time() - start)