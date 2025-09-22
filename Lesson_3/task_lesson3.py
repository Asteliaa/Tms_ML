from typing import List
from datetime import datetime, time


class Warehouse:
    def __init__(self, name: str, location: str, working_hours: tuple[time, time]):
        self.name = name
        self.location = location
        self.working_hours = working_hours  # (открытие, закрытие)

    def is_open(self, check_time: datetime) -> bool:
        start, end = self.working_hours
        return start <= check_time.time() <= end


class Transport:
    def __init__(self, t_type: str, capacity_t: float, capacity_m3: float,
                 speed_kmh: float, cost_per_km: float, allowed_cargo: List[str]):
        self.t_type = t_type
        self.capacity_t = capacity_t
        self.capacity_m3 = capacity_m3
        self.speed_kmh = speed_kmh
        self.cost_per_km = cost_per_km
        self.allowed_cargo = allowed_cargo  # ["normal", "fragile", "dangerous", "temperature"]


class Cargo:
    def __init__(self, name: str, weight_t: float, volume_m3: float, c_type: str, value: float = 1000.0):
        self.name = name
        self.weight_t = weight_t
        self.volume_m3 = volume_m3
        self.c_type = c_type  # normal, fragile, dangerous, temperature
        self.value = value  # стоимость груза для страховки


class RouteSegment:
    def __init__(self, from_wh: Warehouse, to_wh: Warehouse, distance_km: float, transport: Transport):
        self.from_wh = from_wh
        self.to_wh = to_wh
        self.distance_km = distance_km
        self.transport = transport

    def time_hours(self) -> float:
        return self.distance_km / self.transport.speed_kmh

    def cost(self) -> float:
        return self.distance_km * self.transport.cost_per_km


class Shipment:
    def __init__(self, cargos: List[Cargo], route_segments: List[RouteSegment]):
        self.cargos = cargos
        self.route_segments = route_segments

    def total_weight(self) -> float:
        return sum(c.weight_t for c in self.cargos)

    def total_volume(self) -> float:
        return sum(c.volume_m3 for c in self.cargos)

    def total_value(self) -> float:
        return sum(c.value for c in self.cargos)

    def validate(self) -> bool:
        for seg in self.route_segments:
            if self.total_weight() > seg.transport.capacity_t or self.total_volume() > seg.transport.capacity_m3:
                return False
            for cargo in self.cargos:
                if cargo.c_type not in seg.transport.allowed_cargo:
                    return False
        return True

    def calc_total_time(self) -> float:
        base_time = sum(seg.time_hours() for seg in self.route_segments)
        transfers = (len(self.route_segments) - 1) * 2
        return base_time + transfers

    def calc_total_cost(self) -> float:
        cost = sum(seg.cost() for seg in self.route_segments)
        for cargo in self.cargos:
            if cargo.c_type == "dangerous":
                cost *= 1.2
            elif cargo.c_type == "fragile":
                cost *= 1.1
            elif cargo.c_type == "temperature":
                cost += 200
        return cost


class Insurance:
    def __init__(self, rate: float = 0.02):
        self.rate = rate  

    def calc_insurance(self, shipment: Shipment) -> float:
        return shipment.total_value() * self.rate


class DeliveryManager:
    def __init__(self):
        self.shipments: List[Shipment] = []

    def add_shipment(self, shipment: Shipment):
        if shipment.validate():
            self.shipments.append(shipment)
            return True
        return False

    def total_revenue(self) -> float:
        return sum(s.calc_total_cost() for s in self.shipments)


if __name__ == "__main__":
    from datetime import time

    wh1 = Warehouse("Склад А", "Минск", (time(8, 0), time(20, 0)))
    wh2 = Warehouse("Склад Б", "Варшава", (time(7, 0), time(22, 0)))
    wh3 = Warehouse("Склад В", "Берлин", (time(6, 0), time(23, 0)))

    truck = Transport("Грузовик", 20, 60, 70, 1.2, ["normal", "fragile", "dangerous"])
    train = Transport("Поезд", 100, 300, 90, 0.8, ["normal", "dangerous", "temperature"])

    cargo1 = Cargo("Металл", 15, 30, "normal", value=5000)
    cargo2 = Cargo("Химия", 5, 10, "dangerous", value=12000)

    seg1 = RouteSegment(wh1, wh2, 550, truck)
    seg2 = RouteSegment(wh2, wh3, 800, train)

    shipment = Shipment([cargo1, cargo2], [seg1, seg2])

    manager = DeliveryManager()
    manager.add_shipment(shipment)

    insurance = Insurance(rate=0.03)

    print("Валидация маршрута:", shipment.validate())
    print("Время доставки (ч):", shipment.calc_total_time())
    print("Стоимость доставки ($):", shipment.calc_total_cost())
    print("Страховка ($):", insurance.calc_insurance(shipment))
    print("Суммарная выручка менеджера ($):", manager.total_revenue())
