class LogicGate:
    def __init__(self, lbl):
        self.label = lbl
        self.output = None
    def get_label(self):
        return self.label
    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output

class BinaryGate(LogicGate):
    def __init__(self, lbl):
        LogicGate.__init__(self, lbl)
        self.pin_a = None
        self.pin_b = None
    def get_pin_a(self):
        return int(input(f"Enter pin A input (0 or 1) for gate {self.get_label()}: "))
    def get_pin_b(self):
        return int(input(f"Enter pin B input (0 or 1) for gate {self.get_label()}: "))
    def set_next_pin(self, source):
        if self.pin_a == None:
            self.pin_a = source
        else:
            if self.pin_b == None:
                self.pin_b = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")

class UnaryGate(LogicGate):
    def __init__(self, lbl):
        LogicGate.__init__(self, lbl)
        self.pin = None
    def get_pin(self):
        return int(input(f"Enter pin input (0 or 1) for gate {self.get_label()}: "))

class AndGate(BinaryGate):
    def __init__(self, lbl):
        BinaryGate.__init__(self, lbl)
    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self. get_pin_b()
        if a == 1 and b == 1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self, lbl):
        BinaryGate.__init__(self, lbl)
    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self. get_pin_b()
        if a == 1 or b == 1:
            return 1
        else:
            return 0

class NotGate(UnaryGate):
    def __init__(self, lbl):
        UnaryGate.__init__(self, lbl)
    def perform_gate_logic(self):
        a = self.get_pin()
        if a == 1:
            return 0
        else:
            return 1

class Connector:
    def __init__(self, fgate, tgate):
        self.from_gate = fgate
        self.to_gate = tgate
        tgate.set_next_pin(self)
    def get_from(self):
        return self.from_gate
    def get_to(self):
        return self.to_gate


g1 = AndGate("G1")
print(g1.get_output())

# g2 = OrGate("G2")
# print(g2.get_output())

# g3 = NotGate("G3")
# print(g3.get_output())
