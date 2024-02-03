class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.slots = [None] * capacity
        self.tickets = {}

    def park(self, car):
        slot = self.find_empty_slot()
        if slot is not None:
            self.slots[slot] = car
            ticket = ticket(car, slot)
            self.tickets[car.reg_no] = ticket
            return ticket
        else:
            return None

    def leave(self, reg_no):
        ticket = self.tickets.get(reg_no)
        if ticket is not None:
            self.slots[ticket.slot] = None
            del self.tickets[reg_no]
            return ticket
        else:
            return None

    def find_empty_slot(self):
        for i in range(self.capacity):
            if self.slots[i] is None:
                return i
        return None

    def find_reg_nos_by_color(self, color):
        reg_nos = []
        for car in self.tickets.keys():
            if car.color == color:
                reg_nos.append(car.reg_no)
        return reg_nos

    def find_slot_by_reg_no(self, reg_no):
        ticket = self.tickets.get(reg_no)
        if ticket is not None:
            return ticket.slot
        else:
            return None

    def find_slots_by_color(self, color):
        slots = []
        for ticket in self.tickets.values():
            if ticket.car.color == color:
                slots.append(ticket.slot)
        return slots