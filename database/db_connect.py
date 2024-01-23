from sqlalchemy import create_engine,text
from dotenv import load_dotenv
import os

USERNAME = "hoteleyenadeem"
PASSWORD = "aCy0MFLVlDT7"
HOST = "ep-red-shape-a1vfs32k.ap-southeast-1.aws.neon.tech"
DATABASE = "university_db"

conn_str = f'postgresql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}?sslmode=require'
print (conn_str)
load_dotenv()
conn_str = os.getenv("DB_KEY")
print(conn_str)
engine = create_engine(conn_str, echo=True)



with engine.connect() as conn:
    result = conn.execute(text("select 'connected'"))
    print(result.all())