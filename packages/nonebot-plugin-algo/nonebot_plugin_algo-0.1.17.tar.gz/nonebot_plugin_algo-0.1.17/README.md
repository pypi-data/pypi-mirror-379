<div align="center">
  <a href="https://v2.nonebot.dev/store">
    <img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo">
  </a>
  <br>
  <p>
    <img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText">
  </p>
</div>

<div align="center">

# 🏆 算法比赛助手

_✨ 基于 NoneBot2 的算法比赛查询与订阅助手 ✨_

<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/Tabris-ZX/nonebot-plugin-algo.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-algo">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-algo.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="python">
<a href="https://github.com/nonebot/nonebot2">
    <img src="https://img.shields.io/badge/nonebot-2.4.3+-red.svg" alt="nonebot2">
</a>

</div>

## 📖 简介

基于 **NoneBot2** 与 **clist.by API** 开发的智能算法比赛助手插件。

🎯 **核心功能**：

- 🔍 **智能查询**：今日/近期比赛、平台筛选、题目检索
- 🔔 **订阅提醒**：个性化比赛提醒，支持群聊/私聊
- 💾 **持久化存储**：订阅数据本地保存，重启不丢失
- 🌐 **多平台支持**：涵盖 Codeforces、AtCoder、洛谷等主流平台

## ✨ 功能特性

### 🔍 基础查询功能

| 命令                     | 功能              | 示例            |
| ------------------------ | ----------------- | --------------- |
| `近期比赛` / `近期`  | 查询近期比赛      | `近期比赛`    |
| `今日比赛` / `今日`  | 查询今日比赛      | `今日比赛`    |
| `比赛 [平台id] [天数]` | 条件检索比赛      | `比赛 163 10` |
| `题目 [比赛id]`        | 查询比赛题目      | `题目 123456` |
| `clt` / `/官网`      | clist.by 官网链接 | `clt`         |

> 💡 **平台ID说明**：163-洛谷，1-Codeforces，2-AtCoder 等，详见 [clist.by](https://clist.by/resources/)

### 🔔 订阅提醒功能 ⭐

| 命令                        | 功能             | 示例                          |
| --------------------------- | ---------------- | ----------------------------- |
| `订阅 -i [比赛id]`         | 通过ID订阅比赛   | `订阅 -i 123456`             |
| `订阅 -e [比赛名称]`       | 通过名称订阅比赛 | `订阅 -e "Codeforces Round"` |
| `取消订阅 [比赛id]`       | 取消指定订阅     | `取消订阅 123456`           |
| `订阅列表` / `我的订阅` | 查看订阅列表     | `订阅列表`                  |
| `清空订阅`                | 清空所有订阅     | `清空订阅`                  |

**🌟 订阅特色**：

- ✅ **智能匹配**：支持比赛ID和名称模糊匹配
- ⏰ **精准提醒**：比赛开始前自动提醒（默认30分钟前）
- 🔗 **一键直达**：提醒消息包含比赛直链
- 👥 **多场景**：群聊订阅群提醒，私聊订阅个人提醒

## 🎯 功能路线图

### ✅ 已完成功能

- [X] **取消订阅功能** - 支持取消特定比赛订阅
- [X] **订阅持久化存储** - 本地文件存储，重启不丢失
- [X] **便捷检索** - 支持中文名称模糊匹配
- [X] **多场景支持** - 群聊/私聊订阅分离
- [X] **智能提醒** - 自动定时提醒系统

### 🚧 开发中功能

- [ ] **批量订阅管理** - 一键管理多个订阅
- [ ] **自定义提醒时间** - 个性化提醒时间设置
- [ ] **比赛统计分析** - 参与度、难度统计

### 🔮 规划中功能

- [ ] **用户题单收藏** - 题目收藏和管理
- [ ] **个性化推荐** - 基于历史订阅的智能推荐
- [ ] **多语言支持** - 国际化界面
- [ ] **Web管理面板** - 可视化订阅管理

## 🚀 快速开始

### 📦 安装插件

<details>
<summary>🎯 方式一：使用 nb-cli（推荐）</summary>

```bash
nb plugin install nonebot-plugin-algo
```

</details>

<details>
<summary>📚 方式二：使用包管理器</summary>

```bash
# 使用 poetry（推荐）
poetry add nonebot-plugin-algo

# 使用 pip
pip install nonebot-plugin-algo
```

然后在 NoneBot 项目的 `pyproject.toml` 中启用插件：

```toml
[tool.nonebot]
plugins = ["nonebot_plugin_algo"]
```

</details>

### ⚙️ 配置设置

<details>
<summary>🔧 基础配置（可选）</summary>

在 `.env` 文件中添加配置：

```env
# clist.by API 凭据
algo_clist_username=your_username
algo_clist_api_key=your_api_key

# 查询配置
algo_days=7                    # 查询近期天数，默认 7
algo_limit=20                  # 返回数量上限，默认 20
algo_remind_pre=30             # 提醒提前时间（分钟），默认 30
algo_order_by=start            # 排序字段，默认 start
```

</details>

<details>
<summary>📋 配置项详解</summary>

| 配置项                  | 类型 | 默认值      | 说明                     |
| ----------------------- | ---- | ----------- | ------------------------ |
| `algo_days`           | int  | `7`       | 查询近期比赛的天数       |
| `algo_limit`          | int  | `20`      | 返回结果数量上限         |
| `algo_remind_pre`     | int  | `30`      | 订阅提醒提前时间（分钟） |
| `algo_clist_username` | str  | `""`      | clist.by 用户名（可选）  |
| `algo_clist_api_key`  | str  | `""`      | clist.by API Key（可选） |
| `algo_order_by`       | str  | `"start"` | 查询结果排序字段         |

> 💡 **提示**：请前往 [clist.by](https://clist.by/api/v4/doc/) 申请 API Key。

</details>

## 📖 使用示例

### 🔍 查询功能演示

```bash
# 基础查询
近期比赛          # 查询近期比赛
今日比赛          # 查询今日比赛
比赛 163 10       # 查询洛谷平台10天内的比赛
题目 123456       # 查询比赛ID为123456的题目
clt               # 获取clist.by官网链接
```

### 🔔 订阅功能演示

```bash
# 订阅操作
订阅 i 123456                    # 通过比赛ID订阅
订阅 e "Codeforces Round"        # 通过名称订阅
订阅列表                         # 查看订阅列表
取消订阅 123456                  # 取消指定订阅
清空订阅                         # 清空所有订阅
```

### 💡 使用技巧

<details>
<summary>🎯 订阅最佳实践</summary>

1. **精确订阅**：使用比赛ID订阅最准确
2. **模糊搜索**：比赛名称支持关键词匹配
3. **及时管理**：定期查看和清理过期订阅
4. **场景选择**：群聊订阅适合团队，私聊订阅适合个人

</details>

## 🏗️ 技术架构

<details>
<summary>🛠️ 技术特性</summary>

- ⚡ **异步处理**：基于 asyncio 的高性能异步 HTTP 请求
- 🔄 **智能重试**：网络请求失败时自动重试机制（最多3次）
- 🌍 **时区处理**：自动处理 UTC 时间转换本地时间
- 💾 **持久化存储**：订阅信息保存到 JSON 文件，重启后自动恢复
- ⏰ **精确定时**：基于 APScheduler 的毫秒级定时提醒
- 🎯 **代码优化**：DRY 原则，减少重复代码，提高可维护性

</details>

## 📄 开源协议

本项目基于 [MIT License](LICENSE) 开源协议。

## 🙏 特别感谢

- 🤖 [**NoneBot2**](https://github.com/nonebot/nonebot2) - 强大的 Python 机器人框架
- 🌐 [**clist.by**](https://clist.by/) - 提供丰富的算法比赛数据 API
- ⚡ [**Alconna**](https://github.com/ArcletProject/Alconna) - 优雅的命令解析库
- 📦 [**nonebot-plugin-localstore**](https://github.com/nonebot/plugin-localstore) - 本地存储解决方案

---

<div align="center">

### 🌟 如果这个项目对你有帮助，请给个 Star！

<!-- [![Star History Chart](https://api.star-history.com/svg?repos=Tabris-ZX/nonebot-plugin-algo&type=Date)](https://star-history.com/#Tabris-ZX/nonebot-plugin-algo&Date) -->

**让我们一起让算法竞赛变得更简单！** 

</div>
