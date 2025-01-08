'''
 Sistema de Vendas
Crie um sistema de vendas que permita aos usuários cadastrar produtos, realizar vendas, calcular o total de vendas e gerar relatórios de vendas. 
Implemente classes como Product (representando um produto), Sale (representando uma venda) e SalesReport (representando um relatório de vendas).
'''

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Sale:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append({"product": product, "quantity": quantity})

    def total_price(self):
        total = 0
        for item in self.items:
            total += item["product"].price * item["quantity"]
        return total

class SalesReport:
    def __init__(self):
        self.sales = []

    def add_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        total = 0
        for sale in self.sales:
            total += sale.total_price()
        return total

# Exemplo de uso:
product1 = Product("Laptop", 1500)
product2 = Product("Smartphone", 800)
sale1 = Sale()
sale1.add_item(product1, 2)
sale2 = Sale()
sale2.add_item(product2, 1)
sales_report = SalesReport()
sales_report.add_sale(sale1)
sales_report.add_sale(sale2)
print("Total de vendas:", sales_report.total_sales())
