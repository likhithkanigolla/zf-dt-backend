from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from modules import database
from backend.routes.subscription_routes import router as subscription_router
from routes.calculate_routes import router as calculate_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database connection initialization
db = database.Database()

# Include routers from different modules
app.include_router(subscription_router, prefix="", tags=["Subscriptions"])
app.include_router(calculate_router, prefix="", tags=["CalculationModels"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=1629)
