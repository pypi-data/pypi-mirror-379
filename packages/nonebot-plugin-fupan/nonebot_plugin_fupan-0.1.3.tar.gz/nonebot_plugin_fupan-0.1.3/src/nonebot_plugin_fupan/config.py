from nonebot import get_driver, get_plugin_config
from pydantic import BaseModel
from typing import Optional, Dict


class Config(BaseModel):
    # Check-in configuration
    fupan_checkin_start_time: str = "15:00"  # Default start time for check-in
    fupan_checkin_end_time: str = "09:00"    # Default end time for check-in (next day)

    # Per-group time window configuration (group_id: {start_time, end_time})
    fupan_checkin_group_time_windows: Dict[str, Dict[str, str]] = {}

    # Per-user time window configuration (user_id: {start_time, end_time})
    fupan_checkin_user_time_windows: Dict[str, Dict[str, str]] = {}


# 配置加载
plugin_config: Config = get_plugin_config(Config)
global_config = get_driver().config

# 全局名称
NICKNAME: str = next(iter(global_config.nickname), "")