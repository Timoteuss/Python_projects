import psycopg2
import names
import random

conn = psycopg2.connect(dbname='qa_students_1',
                        user='qa_student_1_u_1',
                        password='123',
                        host='159.69.151.133',
                        port='5056')

cursor = conn.cursor()

# if conn:
#
#     print('Connected -- !')
#
#     select_query = 'select * from students;'
#
#     sql_select = '''select * from students'''
#
#     exeq_querry = cursor.execute(select_query)
#
#     f_query = cursor.fetchall()
#
#     print(f_query)
#     # print(cursor.description[1][0])
#
#     for i in f_query:
#
#         u_name = 'Name = ' + i[1]
#         u_email = 'Email = ' + i[2]
#         u_reg_time = 'Time = ' + str(i[4])
#         print(u_name, ';', u_email, ';', u_reg_time)
#
#     conn.commit()
#     conn.close()

# if conn:
#
#     print('Connected -- !')
#
#     create_query = 'create table users_python_23(' \
#                     'id serial primary key,' \
#                     'name varchar(40),' \
#                     'email varchar(100),' \
#                     'phone varchar(24),' \
#                     'country varchar(40),' \
#                     'city varchar(40),'\
#                     'salary int' \
#                     ')'
#     cursor.execute(create_query)
#     conn.commit()
#     conn.close()

# cities = ['Saint-Petersburg', 'Moscow', 'Tver', 'Yaroslavl', 'Kaliningrad', 'Vladivostok', 'Pskov', 'Novgorod', 'Luga']
#
# for i in range(20, 40):
#
#     if conn:
#
#         print('Connected -- !')
#
#         name = names.get_first_name(1)
#         email = name + str(i) + '@gmail.com'
#         phone = '+7(812)432-23-' + str(i)
#         country = 'Russia'
#         city = cities[random.randrange(0, len(cities), 1)]
#         salary = str(random.randrange(1000, 5000, 500))
#
#         q_values = "'" + name + "'" + ', ' + "'" + email + "'" + ', ' + "'"  + phone + "'" + ', ' + "'" + country + "'" + ', ' + "'" + city + "'" + ', ' + salary
#
#         print(q_values)
#
#         create_query = 'insert into public.users_python_23(name, email, phone, country, city, salary)' \
#                         'values(' + q_values + ')'
#
#         cursor.execute(create_query)
#         conn.commit()
# conn.close()

if conn:

    print('Connected -- !')

    select_query = 'select * from users_python_23;'

    sql_select = '''select * from students'''

    exeq_querry = cursor.execute(select_query)

    f_query = cursor.fetchall()

    print(f_query)
    # print(cursor.description[1][0])

    for i in f_query:

        u_name = 'Name = ' + i[1]
        u_email = 'Email = ' + i[2]
        u_phone = 'Phone = ' + i[3]
        u_country = 'Country = ' + str(i[4])
        u_city = 'City = ' + i[5]
        u_salary = 'Salary = ' + str(i[6])
        print(u_name, ';', u_email, ';', u_phone, ';', u_country, ';', u_city, ';', u_salary)

    conn.commit()
    conn.close()
