# class Review:

#     def __init__(
#         self,
#         review_id=None,
#         employee_id=None,
#         review_date=None,
#         performance_rating=None,
#         reviewer_id=None,
#         comments=None
#     ):

#         self.review_id = review_id
#         self.employee_id = employee_id
#         self.review_date = review_date
#         self.performance_rating = performance_rating
#         self.reviewer_id = reviewer_id
#         self.comments = comments

#     def to_dict(self):

#         return self.__dict__.copy()

from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Review:

    review_id: Optional[int] = None

    employee_id: int = 0

    review_date: Optional[date] = None

    performance_rating: int = 3

    reviewer_id: Optional[int] = None

    comments: str = ""