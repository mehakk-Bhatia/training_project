class Customer:

    # Constructor
    def __init__(self, id=None, name=None, phone=None, email=None, created_on=None, remarks=None, points=None, type=None):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
        self.created_on = created_on
        self.remarks = remarks
        self.points = points
        self.type = type

    def insert_sql(self):
        return "insert into Customer (name, phone, email, remarks) " \
               "values " \
               "('{name}', '{phone}', '{email}', '{remarks}');".format_map(vars(self))

    def update_sql(self):
        query = "update Customer set name = '{name}', " \
               "phone='{phone}', email= '{email}' , remarks= '{remarks}' where id = {id}".format_map(vars(self))
        return query

    def delete_sql(self):
        return "delete from Customer where id = {}".format(self.id)

    def select_sql(self):
        return "select * from Customer"

    def select_sql_where(self):
        return "select * from Customer where id = {}".format(self.id)


c1 = Customer()
print(vars(c1))
