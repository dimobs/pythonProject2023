from abc import ABC, abstractmethod


class BaseWorker(ABC):

    @staticmethod
    @abstractmethod
    def work():
        ...

class Worker(BaseWorker):

    @staticmethod
    def work():
        print("I am working!!")


class SuperWorker(BaseWorker):

    @staticmethod
    def work():
        print("I ama super working!!")


class UltimateWorker(BaseWorker):

    @staticmethod
    def work():
        print("working 24/7")


class Manager:
    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        if not isinstance(worker, BaseWorker):
            raise AssertionError(f"worker must be a subclass of BaseWorker")

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
try:
    manager.set_worker(super_worker)
except AssertionError:
    print("manager fails to support super_worker....")