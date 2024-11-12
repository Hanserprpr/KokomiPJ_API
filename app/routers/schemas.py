from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional

class RegionList(str, Enum):
    asia = "asia"
    eu = "eu"
    na = "na"
    ru = "ru"
    cn = "cn"

class LanguageList(str, Enum):
    cn = 'cn'
    en = 'en'
    ja = 'ja'
    ru = 'ru'

class UserInfoModel(BaseModel):
    account_id: int
    is_active: int
    active_level: int
    is_public: int
    total_battles: int
    last_battle_time: int

class UserBasicModel(BaseModel):
    account_id: int = Field(..., description='用户id')
    region_id: int = Field(..., description='服务器id')
    nickname: str = Field(..., description='用户名称')

class UserRecentModel(BaseModel):
    account_id: int = Field(..., description='用户id')
    region_id: int = Field(..., description='服务器id')
    recent_class: Optional[int] = Field(None, description='需要更新的字段')
    last_query_time: Optional[int] = Field(None, description='需要更新的字段')
    last_write_time: Optional[int] = Field(None, description='需要更新的字段')
    last_update_time: Optional[int] = Field(None, description='需要更新的字段')


