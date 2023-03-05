from peewee import *

db = SqliteDatabase('database/db.db')

class BaseModel(Model):
    class Meta:
        database = db
    
class UserProfile(BaseModel):
    avatar_path = TextField()
class User(BaseModel):
    username = TextField()
    password = TextField()
    user_profile = ForeignKeyField(UserProfile)
    
db.create_tables([User, UserProfile])
