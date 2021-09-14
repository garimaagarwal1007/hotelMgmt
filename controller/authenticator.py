import jwt
import uvicorn
from fastapi import FastAPI, Depends, HTTPException,status
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from passlib.hash import bcrypt

from tortoise import fields
from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model
SECRET_KEY='hotelmgmntsecretekey'
class User(Model):
    id=fields.IntField(pk=True)
    username = fields.CharField(50,unique=True)
    password_hash = fields.CharField(128)




    def verify_password(self,password):
        return bcrypt.verify(password,self.password_hash)





outh2_scheme = OAuth2PasswordBearer(tokenUrl='token')

app = FastAPI()


async  def authentic_user(username, password):
     user = await User.get(username=username)
     if not user:
         return False
     if not user.verify_password(password):
         return False
     return user


@app.post('/token')
async def generate_token(form_data:OAuth2PasswordRequestForm=Depends()):
    user = await authentic_user(form_data.username,form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='invalid username or password')
    user_json= await UserIn_Pydantic.from_tortoise_orm(user)
    token=jwt.encode(user_json.dict(),SECRET_KEY)
    return {'access_token':token,'token_type':'bearer'}

@app.get('/')
async def index(token: str= Depends(outh2_scheme)):
    return {'token_value': token}
#
user_pydantic = pydantic_model_creator(User,name='User')
UserIn_Pydantic = pydantic_model_creator(User,name='UserIn',exclude_readonly=True)

@app.post('/create_users',response_model=UserIn_Pydantic)
async def create_user(user:UserIn_Pydantic):
    user_obj= User(username=user.username,password_hash=bcrypt.hash(user.password_hash))
    await user_obj.save()
    return await UserIn_Pydantic.from_tortoise_orm(user_obj)


async def get_current_user(token:str =Depends(outh2_scheme)):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=['HS256'])
        user=await User.get(username=payload.get('username'))
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='invalid username or password')
    return await user_pydantic.from_tortoise_orm(user)


@app.get('/user/reveal',response_model=user_pydantic)
async def get_user(user:user_pydantic=Depends(get_current_user)):
    return user


register_tortoise(
    app,
    db_url='sqlite://db.sqlite3',
    modules={'models':['__main__']},
    generate_schemas=True,
    add_exception_handlers=True

)




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5732)