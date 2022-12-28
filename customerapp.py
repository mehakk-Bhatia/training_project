from flask import *
from customer import Customer
from Databasehelper import DataBaseHelper

app = Flask("CustomerManagementApp", template_folder="cms")
db_helper = DataBaseHelper()

@app.route("/")
def index():
    # return "Welcome to CMS App"
    return render_template("index.html")


@app.route("/add")
def add():
    # return "Welcome to CMS App"
    return render_template("add-customer.html")


@app.route("/view")
def view():
    # return "Welcome to CMS App"
    cref = Customer()
    sql = cref.select_sql()
    rows = db_helper.read(sql)
    return render_template("view-customers.html", result=rows)


@app.route("/delete/<id>")
def delete_customer_from_db(id):
    cref = Customer(id=id)
    sql = cref.delete_sql()
    db_helper.write(sql)
    return render_template("success.html", message="Customer with ID "+id+" Deleted Successfully..")


@app.route("/update-customer/<id>")
def update_customer(id):
    cref = Customer(id=id)
    sql = cref.select_sql_where()
    rows = db_helper.read(sql)
    return render_template("update-customer.html", row=rows[0])

@app.route("/update-customer-in-db/<id>", methods=["POST"])
def update_customer_in_db(id):
    cref = Customer(
        id=id,
        name=request.form["name"],
        phone=request.form["phone"],
        email=request.form["email"],
        remarks=request.form["remarks"]
    )

    if len(cref.name) == 0:
        return render_template("error.html", message="Name cannot be Empty...")

    print(vars(cref))
    sql = cref.update_sql()
    db_helper.write(sql)

    return render_template("success.html", message=cref.name + " Updated Successfully...")


@app.route("/save-customer", methods=["POST"])
def save_customer_in_db():
    cref = Customer(name=request.form["name"],
                    phone=request.form["phone"],
                    email=request.form["email"],
                    remarks=request.form["remarks"])

    if len(cref.name) == 0:
        return render_template("error.html" , message="Name cannot be Empty..." )

    print(vars(cref))
    sql = cref.insert_sql()
    db_helper.write(sql)
    # return cref.name+" Inserted Successfully..."
    return render_template("success.html" , message=cref.name+" Inserted Successfully..." )


def main():
    app.run()


if __name__ == "__main__":
    main()
