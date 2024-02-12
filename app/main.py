from typing import List


class Cargo:
    def __init__(
            self,
            weight: int
    ) -> None:
        self.weight = weight


class BaseRobot(Cargo):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: List[int] = None
    ) -> None:
        super().__init__(weight)
        self.name = name
        self.coords = coords
        if self.coords is None:
            self.coords = [0, 0]

    def go_forward(
            self,
            step: int = 1
    ) -> None:
        for i in range(step):
            self.coords[1] += 1

    def go_back(self, step: int = 1) -> None:
        for i in range(step):
            self.coords[1] -= 1

    def go_right(self, step: int = 1) -> None:
        for i in range(step):
            self.coords[0] += 1

    def go_left(self, step: int = 1) -> None:
        for i in range(step):
            self.coords[0] -= 1

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):

    def __init__(
            self,
            name: str,
            weight: int,
            coords: List[int] = None
    ) -> None:
        super().__init__(name, weight, coords)

        if self.coords is None or len(self.coords) == 2:
            self.coords = [0, 0, 0]

    def go_up(self, step: int = 1) -> None:
        for i in range(step):
            self.coords[2] += 1

    def go_down(self, step: int = 1) -> None:
        for i in range(step):
            self.coords[2] -= 1


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: List[int] = None,
            max_load_weight: int = 0,
            current_load: Cargo = None
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        if self.current_load is not None:
            self.current_load = None
