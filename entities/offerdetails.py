from DAO.db_util import insert
from DAO.db_conn import DAO
from flask import Blueprint,request
from fastapi import FastAPI,APIRouter
from pydantic import BaseModel
from typing import Optional

class Offer(BaseModel):
    offer_desc: str
    is_percent: Optional[int]=0
    offer_discount:int

offer_router=APIRouter()
@offer_router.post("/add_offer")
async def add_offer(data:Offer):
    query=insert(data)
    dao=DAO()
    result=dao.execute_non_execute(query)
    return result

# class OfferDetails:
#     def __init__(self):
#         self.offer_desc="Paytm offer"
#         self.is_percent=1
#         self.offer_discount=10
