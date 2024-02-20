from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass

class Truck(Transport):
    def deliver(self):
        return "Deliver by land"

class Ship(Transport):
    def deliver(self):
        return "Deliver by sea"

class Logistic(ABC):
    @abstractmethod
    def create_transport(self):
        pass

    def plan_delivery(self):
        transport = self.create_transport()
        return transport.deliver()

class RoadLogistic(Logistic):
    def create_transport(self):
        return Truck()

class SeaLogistic(Logistic):
    def create_transport(self):
        return Ship()

def client_code(logistic):
    print(logistic.plan_delivery())

if __name__ == "__main__":
    road_logistic = RoadLogistic()
    sea_logistic = SeaLogistic()

    print("Client: RoadLogistic is working")
    client_code(road_logistic)

    print("\nClient: Sea Logistic is working")
    client_code(sea_logistic)