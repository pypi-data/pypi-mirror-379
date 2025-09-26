# mcp_filesystem

一个可配置的MCP服务器，用于文件系统操作，支持stdio、streamable-http和SSE传输协议。

## 功能特性

- 完整的文件系统操作（创建、读取、更新、删除文件和目录）
- 跨平台支持（Windows、Linux、macOS）
- 可配置的传输协议（stdio、streamable-http、SSE）
- 无第三方依赖（仅使用Python标准库）
- 深度适配uv工具，简化安装和使用

## 快速开始

### 安装uv

```bash
# Linux/macOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 安装mcp-filesystem

```bash
# 使用uv直接从PyPI安装
uv tool install mcp-filesystem

# 或者从源码安装
git clone https://github.com/yangjiacheng1996/mcp_filesystem.git
cd mcp_filesystem
uv sync
```

### 使用方法

#### 使用stdio传输协议（由MCP客户端自动管理）
stdio传输协议不需要手动启动服务器。MCP客户端（如Cherry Studio）会在需要时自动启动和管理服务器进程。

**配置方式（在MCP客户端中配置）：**
- 类型: stdio
- 命令: mcp-filesystem  
- 参数: `--stdio`
- 举例：安装Chatbox，创建自定义MCP，填入命令：D:/mcp_filesystem/.venv/Scripts/mcp-filesystem  --stdio

**注意：** 以下命令仅用于测试和调试目的，会启动一个前台进程占用命令行：
```bash
mcp-filesystem --stdio
```

#### 使用streamable-http传输协议
```bash
mcp-filesystem --streamable-http --host 0.0.0.0 --port 8000
```

#### 使用SSE传输协议
```bash
mcp-filesystem --sse --host 0.0.0.0 --port 8000
```

### 命令行参数说明

- `--config`: 配置文件路径（默认：自动查找config.toml）
- `--stdio`: 使用stdio传输协议
- `--streamable-http`: 使用streamable-http传输协议  
- `--sse`: 使用SSE传输协议
- `--host`: HTTP服务器主机地址（默认：从配置文件或0.0.0.0）
- `--port`: HTTP服务器端口（默认：从配置文件或8000）

## 传输协议

### 1. **stdio**
- 通过标准输入输出与MCP客户端通信
- 适用于本地集成和命令行工具
- 最简单的配置方式

### 2. **streamable-http**
- 通过HTTP流式传输协议通信
- 服务器监听: http://127.0.0.1:8000/mcp
- 适用于需要双向流式通信的场景

### 3. **SSE** (Server-Sent Events)
- 使用服务器发送事件协议
- 服务器监听: http://127.0.0.1:8000/sse
- 适用于需要实时事件推送的场景

## 在Cherry Studio中配置

### 对于stdio类型（推荐配置）:
- 类型: stdio
- 命令: mcp-filesystem
- 参数: `--stdio`

**注意：** 这是正确的配置方式，Cherry Studio会在需要时自动启动和管理服务器进程，无需手动运行命令。

### 对于streamable-http类型:
- 类型: streamable-http
- URL: http://127.0.0.1:8000/mcp

### 对于SSE类型:
- 类型: sse
- URL: http://127.0.0.1:8000/sse

## 开发指南

### 从源码开发

```bash
# 克隆项目
git clone https://github.com/yangjiacheng1996/mcp_filesystem.git
cd mcp_filesystem

# 安装依赖
uv sync

# 运行测试
uv run test

# 运行开发服务器
uv run dev
```

### 可用脚本

- `uv run test`: 运行测试套件
- `uv run test-cov`: 运行测试并生成覆盖率报告
- `uv run dev`: 启动开发服务器（stdio模式）

## Python版本要求

当前支持 Python >= 3.11

## 项目结构

```
mcp_filesystem/
├── src/
│   └── mcp_filesystem/
│       ├── __init__.py          # 主程序入口
│       ├── system_information.py
│       ├── path_exist.py
│       ├── directory_*.py       # 各种目录操作模块
│       └── file_*.py           # 各种文件操作模块
├── tests/                       # 测试文件
├── docs/                       # 文档
├── pyproject.toml              # 项目配置
├── config.toml                 # 服务器配置
├── uv.lock                     # uv依赖锁文件
└── README.md                   # 项目说明
```

## 发布到PyPI

项目已配置为可发布到PyPI:

```bash
# 构建包
uv build

# 发布到PyPI
uv publish --token <你的PyPI账号token>
```

## 故障排除

### 常见问题

1. **权限错误**: 确保有足够的权限访问目标文件和目录
2. **端口冲突**: 如果端口被占用，尝试使用不同的端口号
3. **依赖问题**: 使用 `uv sync` 重新同步依赖

### 获取帮助

- 查看项目文档: [docs/](docs/)
- 提交问题: [GitHub Issues](https://github.com/yangjiacheng1996/mcp_filesystem/issues)
- 联系维护者: yangjiacheng1996@outlook.com

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 贡献

欢迎贡献代码！请阅读贡献指南并提交Pull Request。

## 更新日志

### v0.3.0
- 添加SSE传输协议支持
- 优化项目结构以支持PyPI打包
- 深度适配uv工具
- 更新文档和配置

### v0.2.0
- 初始版本发布
- 支持stdio和streamable-http传输协议
- 完整的文件系统操作功能
