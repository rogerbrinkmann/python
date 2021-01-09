from dataclasses import dataclass, field, asdict, make_dataclass


@dataclass
class InventoryItem:
    """Class for keeping track of an item in inventory."""

    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand


Pdu = make_dataclass("Pdu", [("signal1",str, "s1"), ("signal2", str, "s2")], init=True)       

p = Pdu()
