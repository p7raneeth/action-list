from fastapi import FastAPI
from app.routers import tasks, user

# Create FastAPI app
app = FastAPI(
    title="Task Management API",
    description="A simple task management API",
    version="1.0.0"
)

# Include the tasks router
app.include_router(tasks.router, prefix="/api/v1")
app.include_router(user.router, prefix="/api/v1")


# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Task Management API is running!"}

# Health check
@app.get("/health")
def health_check():
    return {"status": "healthy"}