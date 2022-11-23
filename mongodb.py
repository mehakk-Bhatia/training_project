import pymongo


class Customer:

    def __init__(self, name=None, phone=None, email=None, age=None, gender=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.age = age
        self.gender = gender


class MongoDBHelper:

    def __init__(self):
        client = pymongo.MongoClient(
            "mongodb+srv://atpl:atpl@cluster0.eh8zx.gcp.mongodb.net/?retryWrites=true&w=majority")
        
        self.db = client['gw2022pd1']
      
        self.collection = self.db['customers']

    def insert(self, document):
        result = self.collection.insert_one(document)
       
        print("Inserted Data:", result.inserted_id)

    def fetch(self):
        rows = []
        documents = self.collection.find()
        print(documents, type(documents))
        for document in documents:
            print(document, type(document))
            rows.append(document)
      
        return rows

    def fetch_selected(self, query):
        rows = []
        documents = self.collection.find(query)
        print(documents, type(documents))
        for document in documents:
            print(document, type(document))
            rows.append(document)


        return rows[0]



    def delete(self, query):
        result = self.collection.delete_one(query)
        print(result.deleted_count)

    def update(self, document, query):
        update_query = {"$set": document}
        result = self.collection.update_one(query, update_query)
        print(result.modified_count)


def main():
    db_helper = MongoDBHelper()

    customer1 = Customer(name="Shawn", phone="7777755555",
                         email="shawn@example.com", age=23, gender="male")
    customer1.subjects = [
        {
            "name": "Physics",
            "marks": 90
        },
        {
            "name": "Maths",
            "marks": 90
        }
    ]

  
    db_helper.fetch()


if __name__ == "__main__":
    main()
