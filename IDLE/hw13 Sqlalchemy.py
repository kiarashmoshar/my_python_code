import logging
logging.basicConfig(level=logging.DEBUG)
logging.getLogger('sqlalchemy.engine.base').setLevel(logging.DEBUG)
from sqlalchemy import *
engine = create_engine('sqlite:///')
connection = engine.connect()
result = connection.execute('select 2+2')
result.scalar()


metadata=MetaData()
table =Table('person',metadata,
             Column('id',Integer,primary_key=True),
             Column('name',String(25),nullable=False))
print(table.columns)
print(metadata.tables)

metadata.create_all(engine)

clause=table.insert()
print(clause)
engine.execute(clause,name='kia')

clause=table.select()
print clause
clause=clause.order_by(table.columns.name)
print clause

