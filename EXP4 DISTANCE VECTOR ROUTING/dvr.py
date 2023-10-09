
class Router:
    
    def __init__(self, name):
        self.name = name
        self.distance_vector = {self.name: 0}
        self.neighbors = {}

    def add_neighbor(self, neighbor, cost):
        self.neighbors[neighbor] = cost
        self.distance_vector[neighbor] = cost

    def send_distance_vector(self):
        return {self.name: self.distance_vector}

    def receive_distance_vector(self, neighbor, received_vector):
        updated = False

        for _, table in received_vector.items():
            for destination, cost in table.items():
                total_cost = cost + self.neighbors.get(neighbor, 0)          #Bellman-Ford algorithm
                if self.update_distance_vector(destination, total_cost):
                    updated = True
                    print(f"{self.name}: Updated distance to {destination} via {neighbor} to {total_cost}")
        return updated

    def update_distance_vector(self, destination, new_distance):
        current_distance = self.distance_vector.get(destination, float('inf'))
        if new_distance < current_distance:
            self.distance_vector[destination] = new_distance
            return True
        return False
    
    
    
def print_network_state(routers):
        print("Initial Network State:")
        for router in routers:
            print(f"{router.name}: Neighbors - {router.neighbors}")    



def simulate_network():
    router_a = Router('A')
    router_b = Router('B')
    router_c = Router('C')

    router_a.add_neighbor('B', 1)
    router_a.add_neighbor('C', 2)
    router_b.add_neighbor('A', 1)
    router_b.add_neighbor('C', 5)
    router_c.add_neighbor('A', 2)
    router_c.add_neighbor('B', 5)

    routers = [router_a, router_b, router_c]
    
    print_network_state(routers)

    for _ in range(5):
        print("\n---- Simulation Step ----")
        updated_routers = []
        for router in routers:
            for neighbor, cost in router.neighbors.items():
                neighbor_router = next(r for r in routers if r.name == neighbor)
                updated = neighbor_router.receive_distance_vector(router.name, router.send_distance_vector())
                if updated:
                    updated_routers.append(neighbor_router)

        print("\nRouting Tables:")
        for router in routers:
            print(f"{router.name}: {router.distance_vector}")

        if not updated_routers:
            print("\n Convergence reached. No updates in this iteration. \n")
            break

simulate_network()
