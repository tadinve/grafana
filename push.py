from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
import random
import time


for _ in range(300):
    random_number = random.randint(1, 100)
    print(random_number)
    registry = CollectorRegistry()
    g = Gauge('C130', 'Altitude', registry=registry)

    g.set(random_number) 

    push_to_gateway('localhost:9091', job='C130', registry=registry)
    time.sleep(15) 