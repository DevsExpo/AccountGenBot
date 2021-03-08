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

from bot import mongo_client

m_s = mongo_client['accountgenbot']
sud = m_s['users']
shd = m_s['hits']

def add_user_to_db(user, no):
    stark = sud.find_one({"user": user})
    if stark:
        no2 = stark['no'] + 1
        sud.update_one(
            {"user": user}, {"$set": {"no": no2}}
        )
    else:
        sud.insert_one({'user': user, 'no': no})
       
def get_user_limit(user):
    meisnub = sud.find_one({"user": user})
    if meisnub:
        return meisnub['no']
    else:
        return 0
    
def get_all_users():
    ujwal = sud.find()
    if ujwal:
        return list(ujwal)
    else:
        return None
    
def add_hits_to_db(hit):
    ujwal = shd.find_one({"hit": hit})
    if not ujwal:
        shd.insert_one({'hit': hit})
        
def rm_all_hits():
    ujwal = shd.delete_many()
    
def rm_hit(hit):
    meisnub = shd.delete_one({"hit": hit})
    
def hit_exists(hit):
    ujwal = shd.find_one({'hit': hit})
    if ujwal:
        return True
    else:
        return False
