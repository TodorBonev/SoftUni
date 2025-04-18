class Inventory:

    def __init__(self, __capacity):
        self.__capacity = __capacity
        self.left_capacity = __capacity
        self.items = []

    def add_item(self, item):
        if self.left_capacity == 0:
            return "not enough room in the inventory"
        else:
            self.left_capacity -= 1
            self.items.append(item)

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.left_capacity}"