# SAST MCP 测试指南

本目录包含SAST（静态应用安全测试）解析器的完整测试套件。

## 快速开始

### 运行全部测试
```bash
# 运行所有测试（推荐）
uv run pytest tests/ -v

# 或者逐个运行
uv run python tests/test_moan_parser.py
uv run python tests/test_qianxin_conversion.py
uv run python tests/test_qianxin_parser.py
uv run pytest tests/test_sast_mcp.py -v
```

### 环境要求
- Python 3.10+
- uv 包管理器
- 所需依赖：`uv sync`

## 目录结构

```
tests/                              # 测试代码目录
├── test_moan_parser.py             # 默安解析器测试
├── test_qianxin_conversion.py      # 奇安信转换功能测试
├── test_qianxin_parser.py          # 奇安信解析器测试
├── test_sast_mcp.py                # MCP服务器综合测试（pytest）
└── README.md                       # 本文件

test_data/                          # 测试数据目录（独立）
├── moan/                           # 默安测试数据
│   ├── 默安-sast报告-acepilot-server.docx
│   └── .scanissuefix/             # 生成的JSON文件
├── qianxin/                        # 奇安信测试数据
│   ├── 奇安信-sast报告-webgoat.docx
│   └── .scanissuefix/             # 生成的JSON文件
└── README.md                       # 测试数据说明
```

## 测试内容说明

### 🔥 核心功能测试

#### `test_moan_parser.py` - 默安解析器
- **测试范围**: 完整的默安SAST报告处理流程
- **数据来源**: `test_data/moan/默安-sast报告-acepilot-server.docx`
- **验证内容**:
  - docx → JSON 转换
  - 3个漏洞类型解析
  - JSON结构完整性验证
  - CSV报告生成

#### `test_qianxin_conversion.py` - 奇安信转换功能
- **测试范围**: 大规模数据处理能力
- **数据来源**: `test_data/qianxin/奇安信-sast报告-webgoat.docx`
- **验证内容**:
  - **155种**不同漏洞类型解析
  - **634个**具体缺陷提取
  - XML内容完整提取（含软换行）
  - 统计报告准确性

#### `test_qianxin_parser.py` - 奇安信解析器核心
- **测试范围**: 解析器选择和检测机制
- **验证内容**:
  - 多厂商格式自动检测
  - 解析器优先级机制
  - XML内容提取验证

#### `test_sast_mcp.py` - MCP服务器综合测试
- **测试范围**: 端到端系统集成（pytest框架）
- **验证内容**:
  - 解析器工厂注册机制
  - 完整的转换流程
  - 错误处理和边界条件
  - 路径安全验证

## 运行方式详解

### 🚀 推荐运行方式

```bash
# 1. 完整测试套件（最全面）
uv run pytest tests/ -v

# 2. 指定测试文件
uv run pytest tests/test_sast_mcp.py -v

# 3. 测试特定功能
uv run pytest tests/test_sast_mcp.py::TestSASTMCPServer::test_convert_sast_docx_to_json_success -v
```

### 📋 独立功能测试

```bash
# 默安解析器完整流程（3个漏洞）
uv run python tests/test_moan_parser.py

# 奇安信大数据测试（155种漏洞，634个缺陷）
uv run python tests/test_qianxin_conversion.py

# 解析器选择机制测试
uv run python tests/test_qianxin_parser.py
```

### 🔍 调试和详细输出

```bash
# 详细输出模式
uv run pytest tests/ -v -s

# 只运行失败的测试
uv run pytest tests/ --lf

# 显示最慢的10个测试
uv run pytest tests/ --durations=10
```

## 测试结果解读

### ✅ 成功指标
- **默安**: 3个JSON文件生成，包含完整漏洞信息
- **奇安信**: 155个JSON文件生成，634个缺陷全部提取
- **CSV报告**: 正确生成修复状态报告
- **解析器选择**: 正确识别文档厂商格式

### ⚠️ 常见问题
1. **编码错误**: 确保系统支持UTF-8编码
2. **文件锁定**: Word文档被占用时关闭相关程序
3. **路径问题**: 确保工作目录在项目根目录

## 数据文件说明

### 测试数据特点
- **默安文档**: 包含"四、漏洞详情"和"六、代码规范风险详情"
- **奇安信文档**: 包含"1、检测概要"和"2、详细信息"，数据量大

### 生成文件
测试运行后会在相应目录下生成：
- `*_new.json`: 新解析的漏洞数据
- `*_finished.json`: 模拟修复完成的数据
- `sast_fix_report.csv`: 修复状态统计报告

## 故障排除

### 常见错误及解决方案

```bash
# 清理Python缓存
find . -name "__pycache__" -type d -exec rm -rf {} +

# 重新安装依赖
uv sync --reinstall

# 检查测试数据文件
ls -la test_data/*/
```

### 性能优化
- 解析器使用文档缓存，避免重复读取大文件
- 测试完成后自动清理缓存，防止内存泄漏

## 开发者说明

### 添加新测试
1. 在`tests/`目录下创建`test_*.py`文件
2. 使用pytest装饰器和断言
3. 测试数据放入`test_data/`相应目录

### 测试最佳实践
- 每个测试方法只测试一个功能点
- 使用临时目录避免测试间相互影响
- 清理测试生成的文件，保持环境整洁