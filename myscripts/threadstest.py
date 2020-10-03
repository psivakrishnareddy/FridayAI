
# import time
# import reminder as srs


# def main():
#     print("Welcome Friday")
#     srs.remainder_init("siva", 0.1)
#     while True:
#         print("xx" + str(time.time()))
#         time.sleep(1)


# main()
import wikipedia
import time

from timeloop import Timeloop
from datetime import timedelta

tl = Timeloop()


@tl.job(interval=timedelta(seconds=0.1))
def sample_job_every_2s():

    print("2s job current time : {}".format(time.ctime()))


@tl.job(interval=timedelta(seconds=0.5))
def sample_job_every_5s():
    # for i in range(3):
    #     print("SIVAAA")
    #     time.sleep(2)
    print("5s job current time : {}".format(time.ctime()))


def main():
    tl.start(block=False)
    while True:
        print("ain task")
        time.sleep(1)


# main()
print(wikipedia.summary("Facebook", sentences=1))
