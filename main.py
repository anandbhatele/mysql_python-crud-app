from fastapi import FastAPI,Depends,HTTPException
from schema import UserCreate,UserUpdate
from mysession import sessionlocal
from sqlalchemy.orm import Session
from create_table import User

def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()

app=FastAPI()


#insert data
@app.post("/users",status_code=201)
def create_user(user:UserCreate,db:Session=Depends(get_db)):
    new_row=User(name=user.name,email=user.email)
    data=db.query(User).filter(User.email==user.email).first()
    if data:
        raise HTTPException(status_code=400, detail="Email already exists")
    
    try:
        db.add(new_row)
        db.commit()
        print("Data insert.....")
    except:
        print("Error..")


#fetch all data
@app.get("/users",status_code=200)
def get_users(db:Session=Depends(get_db)):
    return db.query(User).all()


#fetch one row
@app.get("/users/{user_id}",status_code=200)
def get_user(user_id:int,db:Session=Depends(get_db)):
    user=db.query(User).filter(User.id==user_id).first()
    if user is None:
        raise HTTPException(status_code=404,detail="User Not Found")
    return user



#update(put) data
@app.put("/users/{user_id}",status_code=200)
def update_user(user_id:int,user:UserUpdate,db:Session=Depends(get_db)):
    data=db.query(User).filter(User.id==user_id).first()
    if data is None:
        raise HTTPException(status_code=404,detail="User Not Found")
    data.name=user.name
    data.email=user.email
    db.commit()


#delete data
@app.delete("/users/{user_id}",status_code=200)
def delete_user(user_id:int,db:Session=Depends(get_db)):
    data=db.query(User).filter(User.id==user_id).first()
    if data is None:
        raise HTTPException(status_code=404,detail="User Not Found")
    db.delete(data)
    db.commit()


#update(patch)
@app.patch("/users/{user_id}",status_code=200)
def patch_user(user_id:int,user:UserUpdate,db:Session=Depends(get_db)):
    data=db.query(User).filter(User.id==user_id).first()
    if data is None:
        raise HTTPException(status_code=404,detail="User Not Found")
    update_data=user.dict(exclude_unset=True,exclude_none=True)
    for key , values in update_data.items():
        setattr(data,key,values)
    db.commit()




