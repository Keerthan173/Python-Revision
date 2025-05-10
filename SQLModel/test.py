# from typing import Optional
# from sqlmodel import SQLModel,Field,create_engine,Session

# class Product(SQLModel,table=True):
#     id:int|None =Field(default=None,primary_key=True)
#     name:str =Field(index=True)
#     description:str|None=None
#     price:float
#     quantity:int =Field(default=0)
    
# sqlite_file_name = "database1.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"

# engine = create_engine(sqlite_url, echo=True)

# def create_db():
#     SQLModel.metadata.create_all(engine)
    
# def add_product(name: str, description: Optional[str], price: float, quantity: int = 0):
#     new_product = Product(
#         name=name,
#         description=description,
#         price=price,
#         quantity=quantity
#     )
    
#     with Session(engine) as session:
#         session.add(new_product)
#         session.commit()
#         session.refresh(new_product)
        
#         print("\nProduct added successfully!")
#         print("Product details:")
#         print(f"ID: {new_product.id}")
#         print(f"Name: {new_product.name}")
#         print(f"Description: {new_product.description}")
#         print(f"Price: ${new_product.price:.2f}")
#         print(f"Quantity: {new_product.quantity}")
        
#         return new_product

# def main():
#     # create_db()
#     # print("Database and tables created successfully!")
    
#     add_product(
#         name="Wireless Mouse",
#         description="Ergonomic wireless mouse with 2.4GHz connectivity",
#         price=24.99,
#         quantity=50
#     )

# if __name__ == "__main__":
#     main()



from sqlmodel import SQLModel, Field, create_engine, Session, select
from typing import Optional

# Define the Product model
class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: Optional[str] = None
    price: float
    quantity: int = Field(default=0)

# Create the SQLite engine
engine = create_engine("sqlite:///inventory.db", echo=True)

# Create the Product table
SQLModel.metadata.create_all(engine)

# Add a product
def add_product(name: str, description: Optional[str], price: float, quantity: int):
    new_product = Product(name=name, description=description, price=price, quantity=quantity)
    with Session(engine) as session:
        session.add(new_product)
        session.commit()
        session.refresh(new_product)
    print(f"Product added: ID={new_product.id}, Name={new_product.name}, Price={new_product.price}, Quantity={new_product.quantity}")

# List all products
def list_all_products():
    with Session(engine) as session:
        products = session.exec(select(Product)).all()
        if not products:
            print("No products found.")
            return
        for product in products:
            print(f"ID={product.id}, Name={product.name}, Price={product.price}, Quantity={product.quantity}, Description={product.description}")

# Find a product by name
def find_product_by_name(name: str):
    with Session(engine) as session:
        statement = select(Product).where(Product.name == name)
        product = session.exec(statement).first()
        if product:
            print(f"Product found: ID={product.id}, Name={product.name}, Price={product.price}, Quantity={product.quantity}, Description={product.description}")
        else:
            print(f"Product with name '{name}' not found.")

# Update a product's quantity
def update_product_quantity(name: str, new_quantity: int):
    with Session(engine) as session:
        statement = select(Product).where(Product.name == name)
        product = session.exec(statement).first()
        if product:
            product.quantity = new_quantity
            session.add(product)
            session.commit()
            print(f"Updated quantity of '{name}' to {new_quantity}.")
        else:
            print(f"Product with name '{name}' not found.")

# Delete a product
def delete_product(name: str):
    with Session(engine) as session:
        statement = select(Product).where(Product.name == name)
        product = session.exec(statement).first()
        if product:
            session.delete(product)
            session.commit()
            print(f"Product '{product.name}' has been deleted.")
        else:
            print(f"Product with name '{name}' not found.")

# Main demonstration
if __name__ == "__main__":
    add_product("Laptop", "Gaming laptop", 1500.00, 10)
    add_product("Mouse", "Wireless mouse", 25.50, 50)
    add_product("Keyboard", "Mechanical keyboard", 80.00, 30)

    print("\nAll Products:")
    list_all_products()

    print("\nFind 'Mouse':")
    find_product_by_name("Mouse")

    print("\nUpdate quantity of 'Keyboard' to 45:")
    update_product_quantity("Keyboard", 45)

    print("\nAll Products after update:")
    list_all_products()

    print("\nDelete 'Laptop':")
    delete_product("Laptop")

    print("\nAll Products after deletion:")
    list_all_products()
    