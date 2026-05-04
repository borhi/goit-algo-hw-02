from queue import Queue
import uuid


class Request:
    def __init__(self, req_id, position):
        self.id = req_id
        self.position = position


class ServiceCenter:
    def __init__(self):
        self.requests = Queue()

    def generate_request(self, request):
        self.requests.put(request)

    def process_requests(self):
        while not self.requests.empty():
            current = self.requests.get()
            print(f"Обробляємо заявку #{current.id}, позиція: {current.position}")


if __name__ == "__main__":
    center = ServiceCenter()
    for i in range(5):
        center.generate_request(Request(f"REQ-{str(uuid.uuid4())}", i+1))
    center.process_requests()
