class Catalogue:
    products = []

    def __init__(self, name):
        self.name = name

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        filtered_products = []
        for i in self.products:
            if i[0] == first_letter:
                filtered_products.append(i)
        return filtered_products

    def __repr__(self):
        result = ''
        result += f"Items in the {self.name} catalogue:\n"
        result += '\n'.join(sorted(self.products))
        return result