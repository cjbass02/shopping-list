import sqlite3

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('shopping_list.db')
        self.create_shopping_list_table()

    def __del__(self):
        self.conn.commit()
        self.conn.close()

    def create_shopping_list_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "ShoppingList" (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ItemName TEXT,
            Quantity INTEGER,
            Purchased BOOLEAN DEFAULT 0,
            CreatedOn DATE DEFAULT CURRENT_DATE
        );
        """
        self.conn.execute(query)

class ShoppingListModel:
    TABLENAME = "ShoppingList"

    def __init__(self):
        self.conn = sqlite3.connect('shopping_list.db')
        self.conn.row_factory = sqlite3.Row

    def __del__(self):
        self.conn.commit()
        self.conn.close()

    def get_by_id(self, _id):
        query = f"SELECT * FROM {self.TABLENAME} WHERE id={_id}"
        result = self.conn.execute(query).fetchone()
        return dict(result) if result else None

    def create(self, params):
        query = f'INSERT INTO {self.TABLENAME} (ItemName, Quantity, Purchased) VALUES ("{params.get("ItemName")}", {params.get("Quantity")}, {params.get("Purchased", 0)})'
        result = self.conn.execute(query)
        return self.get_by_id(result.lastrowid)

    def update(self, item_id, update_dict):
        set_query = ", ".join([f'{column} = "{value}"' for column, value in update_dict.items()])
        query = f"UPDATE {self.TABLENAME} SET {set_query} WHERE id = {item_id}"
        self.conn.execute(query)
        return self.get_by_id(item_id)

    def delete(self, item_id):
        query = f"DELETE FROM {self.TABLENAME} WHERE id = {item_id}"
        self.conn.execute(query)
        return self.list_items()

    def list_items(self):
        query = f"SELECT * FROM {self.TABLENAME}"
        result_set = self.conn.execute(query).fetchall()
        return [dict(row) for row in result_set]
