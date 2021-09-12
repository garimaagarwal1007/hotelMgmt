from entities.offerdetails import offer_router
from fastapi import FastAPI

app = FastAPI(
    title="Hotel Management API"
)
app.include_router(offer_router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")