# from app.database import Base  # Import Base first
# from app.models.user import User  # Then import User
# from app.models.tasks import Task  # Then import Task

# # This ensures both models are registered with SQLAlchemy
# __all__ = ["Base", "User", "Task"]

from app.database import Base

# Import User FIRST, then Task
from app.models.user import User
from app.models.tasks import Task

# This is crucial - it registers both models
__all__ = ["Base", "User", "Task"]