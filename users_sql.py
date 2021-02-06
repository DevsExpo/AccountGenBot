#    Copyright (C) Midhun KM 2020-2021
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from sqlalchemy import Column, String, UnicodeText, Integer
from sql_main import BASE, SESSION


class Stark(BASE):
    __tablename__ = "stark"
    user_id = Column(Integer, primary_key=True)
    usage_number = Column(Integer, default=0)

    def __init__(self, user_id, usage_number):
        self.user_id = user_id
        self.usage_number = usage_number


Stark.__table__.create(checkfirst=True)

def add_new_user(user_id: int, usage_number: int):
    tracker_adder = Stark(int(user_id), int(usage_number))
    SESSION.add(tracker_adder)
    SESSION.commit()

def get_user_info(user_id: int):
    try:
        s__ = SESSION.query(Stark).get(int(user_id))
        return int(s__.usage_number), int(s__.user_id)
    finally:
        SESSION.close()
        
def is_user_in_db(user_id: int):
    try:
        s__ = SESSION.query(Stark).get(int(user_id))
        if s__:
            return int(s__.usage_number)
    finally:
        SESSION.close()
        
        
def get_all_users_id():
    stark = [r.user_id for r in SESSION.query(Stark).all()]
    SESSION.close()
    return stark

def get_all_users():
    s = SESSION.query(Stark).all()
    SESSION.close()
    return s


def rm_user(user_id: int):
    warner = SESSION.query(Stark).get(int(user_id))
    if warner:
        SESSION.delete(warner)
        SESSION.commit()

def update_user_usage(user_id:int, usage_number: int):
    row = SESSION.query(Stark).get(user_id)
    row.usage_number += int(usage_number)
    # commit the changes to the DB
    SESSION.commit()
