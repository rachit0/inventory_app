from django.db import models
from pymongo import MongoClient
class Supplier:
    def __init__(self,name,email,phone,address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
    
    
    
class Product:
    def __init__(self,name,description,category,price,stock_quantity,supplier)
    self.name = name
    self.description = description
    self.category = category
    self.price = price
    self.stock_quantity = stock_quantity
    self.supplier =supplier

class SaleOrder:
    def __init__(self,product_id,quantity,total_price,sale_date,status):
        self.product_id = product_id
        self.quantity = quantity
        self.total_price = total_price
        self.sale_date = sale_date
        self.status = status

class StockMovement:
    def __init__(self,product_id,quantity,movement_type,movement_date):
        self.product_id = product_id
        self.quantity = quantity
        self.movement_type = movement_type
        self.movement_date = movement_date

client = MongoClient("mongodb://localhost:27017/")
db = client['inventory_db']