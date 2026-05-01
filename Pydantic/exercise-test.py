from pydantic import (
    BaseModel,
    field_validator,
    model_validator,
    ConfigDict,
    Field,
    AfterValidator,
    ValidationError,
)
from typing import Annotated

from datetime import datetime
import time

class Employee(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True
    )

    name: Annotated[str, Field(min_length=4)]
    age: Annotated[int, Field(gt=18)]
    job_title: str
    dob: str
    salary: str | None = None
    years_of_exp: str | None = None


    @field_validator("years_of_exp",mode="before")
    @classmethod
    def modify_yrs_of_exp(cls,val: str) -> int:
        return int(val)

    @field_validator("years_of_exp")
    @classmethod
    def validate_yrs(cls, val: int) -> str:
        if not val > 0:
            raise ValueError("Employee must have atleast 1 yr exp")
        return str(val)
    
    @model_validator(mode="after")
    def validate_dob(self):
        now_dt = datetime.now()
        conv = time.strptime(self.dob, "%d-%m-%Y")
        yr_cal = now_dt.year - conv.tm_year
        is_age_consider = now_dt.month > conv.tm_mday
        
        if is_age_consider:
            yr_cal-=1

        if self.age != yr_cal:
            raise ValueError("Age and DOB is not matching")
        return self
    

    
emp1 = Employee(
    name = "Hari_Krishnan",
    age=34,
    job_title="SWE",
    dob="21-09-1992"
)





now_dt = datetime.now()
conv = time.strptime('14-11-1998', "%d-%m-%Y")
yr_cal = now_dt.year - conv.tm_year
is_age_consider = now_dt.month > conv.tm_mday

age = 28      
if is_age_consider:
    yr_cal-=1
if age != yr_cal:
    raise ValueError("Age and DOB is not matching")
else:
    print(f'AGE: {age}')