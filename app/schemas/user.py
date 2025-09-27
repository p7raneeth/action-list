from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from enum import Enum

class createUser(BaseModel):
    username : str
    password : str