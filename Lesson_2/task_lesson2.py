from dataclasses import dataclass
from typing import List, Tuple, Optional

@dataclass
class Cargo:
    name: str
    weight: float
    volume: float

@dataclass
class Warehouse:
    name: str

@dataclass
class Transport:
    name: str
    speed: float
    cost_per_km: float
    max_weight: float
    max_volume: float

    def can_carry(self, cargo: Cargo) -> bool:
        return cargo.weight <= self.max_weight and cargo.volume <= self.max_volume

    def calc(self, distance: float, cargo: Cargo) -> Optional[Tuple[float, float]]:
        if not self.can_carry(cargo):
            return None
        time = distance / self.speed
        cost = distance * self.cost_per_km
        return time, cost

class LogisticsSystem:
    def __init__(self):
        self.transports: List[Transport] = []

    def add_transport(self, transport: Transport) -> None:
        self.transports.append(transport)

    def plan_route(
        self,
        cargo: Cargo,
        warehouses: List[Warehouse],
        distances: List[float]
    ) -> Tuple[List[Tuple[str, str, float, str, float, float]], float, float]:
        """
        warehouses: список складов [A, B, C]
        distances: список расстояний [100, 300] (A->B=100, B->C=300)
        """
        total_time = 0.0
        total_cost = 0.0
        route = []

        for i, dist in enumerate(distances):
            from_wh = warehouses[i]
            to_wh = warehouses[i + 1]

            best = None
            for t in self.transports:
                res = t.calc(dist, cargo)
                if res:
                    time, cost = res
                    if best is None or cost < best[2]:
                        best = (t.name, time, cost)

            if not best:
                raise ValueError(f"Нет транспорта для участка {from_wh.name}->{to_wh.name}")

            route.append((from_wh.name, to_wh.name, dist, best[0], best[1], best[2]))
            total_time += best[1]
            total_cost += best[2]

        return route, total_time, total_cost

# ===== пример использования =====
if __name__ == "__main__":
    # склады
    A = Warehouse("Минск")
    B = Warehouse("Москва")
    C = Warehouse("Казань")

    # транспорт
    truck = Transport("Грузовик", speed=70, cost_per_km=1.2, max_weight=20000, max_volume=60)
    plane = Transport("Самолёт", speed=800, cost_per_km=5.0, max_weight=10000, max_volume=200)

    # система
    system = LogisticsSystem()
    system.add_transport(truck)
    system.add_transport(plane)

    # груз
    cargo = Cargo("Бумага", weight=5000, volume=15)

    # маршрут: Минск -> Москва -> Казань
    warehouses = [A, B, C]
    distances = [700, 800]

    route, total_time, total_cost = system.plan_route(cargo, warehouses, distances)

    print("Маршрут:")
    for frm, to, dist, tr, time, cost in route:
        print(f" {frm} -> {to} ({dist} км): {tr}, {time:.1f} ч, {cost:.2f} у.е.")
    print(f"Итого: {total_time:.1f} ч, {total_cost:.2f} у.е.")
