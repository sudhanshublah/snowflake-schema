import snowflake.connector

# Gets the version
ctx = snowflake.connector.connect(
    user='<user>',
    password='<password>',
    account='kz41049.ap-south-1.aws'
    )
# cs = ctx.cursor().execute('CREATE DATABASE IF NOT EXISTS SCHEMACHANGE_DEMO')
# cs = ctx.cursor().execute('USE SCHEMA SCHEMACHANGE_DEMO.PUBLIC')
# cs = ctx.cursor().execute('')
# cs = ctx.cursor().execute('')
# cs = ctx.cursor().execute('')

sql_file = 'V1.1.1__initial_db_objects.sql'
with open('/home/ubuntu/snowflake/V1.1.1__initial_db_objects.sql', 'r', encoding='utf-8') as f:
    for cn in ctx.execute_stream(f):
        for rt in cn:
            print(rt)

ctx.close
print('done')
