<div align="center">
    <a href="https://v2.nonebot.dev/store">
    <img src="https://raw.githubusercontent.com/fllesser/nonebot-plugin-template/refs/heads/resource/.docs/NoneBotPlugin.svg" width="310" alt="logo"></a>

## ✨ nonebot-plugin-fupan ✨

<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/zanderzhng/nonebot-plugin-fupan.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-fupan">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-fupan.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="python">
<a href="https://github.com/astral-sh/ruff">
    <img src="https://img.shields.io/badge/code%20style-ruff-black?style=flat-square&logo=ruff" alt="ruff">
</a>
<a href="https://github.com/astral-sh/uv">
    <img src="https://img.shields.io/badge/package%20manager-uv-black?style=flat-square&logo=uv" alt="uv">
</a>
<a href="https://results.pre-commit.ci/latest/github/zanderzhng/nonebot-plugin-fupan/master">
    <img src="https://results.pre-commit.ci/badge/github/zanderzhng/nonebot-plugin-fupan/master.svg" alt="pre-commit" />
</a>
</div>

## 📖 介绍

NoneBot 复盘打卡插件，用于帮助交易者进行每日复盘打卡。支持交易日判断、时间窗口控制、数据统计等功能。

## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-fupan --upgrade
使用 **pypi** 源安装

    nb plugin install nonebot-plugin-fupan --upgrade -i "https://pypi.org/simple"
使用**清华源**安装

    nb plugin install nonebot-plugin-fupan --upgrade -i "https://pypi.tuna.tsinghua.edu.cn/simple"


</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details open>
<summary>uv</summary>

    uv add nonebot-plugin-fupan
安装仓库 master 分支

    uv add git+https://github.com/zanderzhng/nonebot-plugin-fupan@master
</details>

<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-fupan
安装仓库 master 分支

    pdm add git+https://github.com/zanderzhng/nonebot-plugin-fupan@master
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-fupan
安装仓库 master 分支

    poetry add git+https://github.com/zanderzhng/nonebot-plugin-fupan@master
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_fupan"]

</details>

<details>
<summary>使用 nbr 安装(使用 uv 管理依赖可用)</summary>

[nbr](https://github.com/fllesser/nbr) 是一个基于 uv 的 nb-cli，可以方便地管理 nonebot2

    nbr plugin install nonebot-plugin-fupan
使用 **pypi** 源安装

    nbr plugin install nonebot-plugin-fupan -i "https://pypi.org/simple"
使用**清华源**安装

    nbr plugin install nonebot-plugin-fupan -i "https://pypi.tuna.tsinghua.edu.cn/simple"

</details>


## ⚙️ 配置

在 nonebot2 项目的`.env`文件中添加下表中的配置项

| 配置项  | 必填  | 默认值 |   说明   |
| :-----: | :---: | :----: | :------: |
| fupan_checkin_start_time | 否 | 15:00 | 打卡开始时间（交易日当天） |
| fupan_checkin_end_time | 否 | 09:00 | 打卡结束时间（下一交易日） |
| fupan_checkin_group_time_windows | 否 | {} | 群组特定时间窗口配置 |
| fupan_checkin_user_time_windows | 否 | {} | 用户特定时间窗口配置 |

### 高级配置示例

#### 群组特定时间窗口配置
```env
fupan_checkin_group_time_windows = {"123456": {"start_time": "16:00", "end_time": "08:00"}}
```

#### 用户特定时间窗口配置
```env
fupan_checkin_user_time_windows = {"user123": {"start_time": "17:00", "end_time": "07:00"}}
```

### 盘后时间窗口说明
盘后时间窗口定义为：T日收盘后到T+1交易日开盘前的时间段。默认配置为15:00至次日09:00。

## 🎉 使用
### 指令表
| 指令  | 权限  | 范围  |   说明   |
| :---: | :---: | :---: | :------: |
| 复盘/打卡/签到 | 群员  | 群聊/私聊  | 进行复盘打卡 |
| 复盘统计 | 群员  | 群聊/私聊  | 查看个人打卡统计 |
| 复盘排行 | 群员  | 群聊/私聊  | 查看打卡排行榜 |
| 复盘撤销/撤销复盘 | 群员  | 群聊/私聊  | 撤销最后一次打卡 |
| 复盘帮助 | 群员  | 群聊/私聊  | 查看帮助信息 |
| 复盘重置 | 超级用户  | 群聊/私聊  | 重置数据（私聊/群组） |

### 使用说明
1. 用户可以在交易日的盘后时间窗口内进行打卡（默认15:00至下一个交易日的09:00）
2. 非交易日（周末、节假日）会自动调整打卡时间窗口
3. 每个用户每次盘后只能打卡一次
4. 支持查看个人统计和群内排行榜（基于连续打卡次数）
5. 支持按群组或用户设置特定的时间窗口
6. 用户可以使用"复盘撤销"或"撤销复盘"命令撤销最后一次打卡记录
7. 群聊和私聊的数据完全分离，互不影响
8. 超级用户可以使用"复盘重置"命令重置数据：
   - `/复盘重置 私聊` - 重置所有私聊用户数据
   - `/复盘重置 当前群组` - 重置当前群组数据
   - `/复盘重置 群组<群号>` - 重置指定群组数据
9. 用户可以使用"复盘帮助"命令查看所有可用指令
10. 详细的打卡日志记录功能，包括时间戳、星期分布、交易日信息等统计信息
11. 连续打卡计数功能，追踪用户的连续交易日打卡记录

### 平台限制说明
由于官方QQ机器人的平台限制，用户昵称信息无法获取。昵称显示功能在其他Bot适配器上效果更佳。

### 🎨 效果图
如果有效果图的话