from flask import Flask, request, jsonify
import psycopg2
import json

app = Flask("bank_web_app")

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="bank",
    user="postgres",
    password="2222")

#get account by id
@app.route("/api/v1/customers/<int:customer_id>", methods=['GET'])
def get_customer(customer_id):
    print(f"called /customers/customer_id/{customer_id}")
    with conn:
        with conn.cursor() as cur:
            sql = "SELECT * FROM customers WHERE id = %s"
            cur.execute(sql, (customer_id,))
            result = cur.fetchone()
            if result:
                ret_data = {
                    'id': result[0],
                    'passport_num': result[1],
                    'name': result[2],
                    'address': result[3]
                }
                return jsonify(ret_data)
            else:
                return app.response_class(
                    status=404
                )

#Get customers - all or allow filtering by passport_num, name and/or address
@app.route("/api/v1/customers", methods=['get'])
def get_accounts():
    print(f"called /customers")
    with conn:
        with conn.cursor() as cur:
            # get all:
            if len(request.args) == 0:
                sql = "SELECT * FROM customers"
            #filtering:
            if len(request.args) > 0:
                new_data = request.form
                updates_str_list = []
                for field in new_data:
                    updates_str_list.append(f"{field}=%s")
                values_list = []
                for arg in request.args:
                    updates_str_list.append(f"{arg} ilike %s")
                    values = request.args.get(arg)
                    values_list.append(values)
                sql = f"select * from customers where {(' and '.join(updates_str_list))}"
            cur.execute(sql, tuple(values_list))
            result = cur.fetchall()

            if result:
                ret_data = {
                    'total customers': len(result),
                    'customers': []}
                for r in result:
                    ret_data_customers = {'id': r[0],
                                  'passport_num': r[1],
                                  'name': r[2],
                                  'address': r[3]
                                  }
                    ret_data['customers'].append(ret_data_customers)
                return jsonify(ret_data)
            else:
                return app.response_class(status=404)


if __name__ == '__main__':
    app.run(debug=True)