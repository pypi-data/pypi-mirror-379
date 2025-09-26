# 测试数据目录

本目录包含SAST解析器的测试数据文件。

## 目录结构

```
test_data/
├── moan/                           # 默安SAST报告测试数据
│   ├── 默安-sast报告-acepilot-server.docx
│   └── .scanissuefix/             # 测试生成的JSON文件（运行时创建）
└── qianxin/                       # 奇安信SAST报告测试数据
    ├── 奇安信-sast报告-webgoat.docx
    └── .scanissuefix/             # 测试生成的JSON文件（运行时创建）
```

## 文件说明

### MoAn格式测试数据
- **默安-sast报告-acepilot-server.docx**: 默安科技SAST报告样本
  - 包含"四、漏洞详情"和"六、代码规范风险详情"章节
  - 用于测试MoAn解析器的功能

### QiAnXin格式测试数据
- **奇安信-sast报告-webgoat.docx**: 奇安信SAST报告样本
  - 包含"1、检测概要"和"2、详细信息"章节
  - 包含155种不同漏洞类型，634个具体缺陷
  - 用于测试QiAnXin解析器的XML内容提取功能

## 使用说明

测试运行时会在相应目录下创建`.scanissuefix`子目录，包含解析生成的JSON文件：
- `*_new.json`: 新解析的漏洞数据
- `*_finished.json`: 处理完成的漏洞数据（用于CSV报告生成）

## 注意事项

1. `.scanissuefix`目录及其内容为测试运行时动态生成，不应提交到版本控制
2. 测试数据文件包含真实的漏洞报告信息，仅用于开发和测试目的
3. 修改测试数据文件时，请确保相应的测试用例仍能正常运行