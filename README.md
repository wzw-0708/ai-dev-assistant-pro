# 🚀 AI Dev Assistant Pro

> 一个基于多 Agent 架构的自主 AI 系统，能够对 C++ 代码进行**生成、编译、调试并自动修复（Auto Fix）**，实现完整的软件开发闭环。

---

## ✨ 项目简介

AI Dev Assistant Pro 是一个轻量级的 AI 开发辅助系统，模拟“从需求到可运行程序”的完整流程。

系统支持：

1. 解析用户需求
2. 自动生成 C++ 代码
3. 调用 `g++` 进行真实编译
4. 分析编译错误
5. 自动修复代码
6. 循环执行直到成功

👉 实现了一个**可运行的 AI 自动编程闭环系统**

---

## 🧠 核心架构（多 Agent 协作）

本项目采用多 Agent 分工协作模式：

* **Planner Agent（规划器）**
  将用户自然语言需求拆解为结构化任务

* **Coder Agent（代码生成）**
  根据任务生成多文件 C++ 项目代码

* **Debugger Agent（调试分析）**
  分析编译错误日志，定位问题原因

* **Fixer Agent（自动修复）**
  基于错误分析结果修改代码并重试

---

## 🔁 执行流程（Auto Fix Loop）

```id="u0b3y8"
用户需求
   ↓
Planner Agent
   ↓
Coder Agent
   ↓
编译器（g++）
   ↓
Debugger Agent
   ↓
Fixer Agent
   ↺（自动修复循环）
```

---

## 🎬 示例（终端输出）

```id="l0m3vr"
第1轮 ❌ 编译失败
→ error: missing header file

AI 分析：
缺少 #include <iostream>

AI 修复：
补充头文件

第2轮 ✅ 编译成功 🎉
```

---

## 📌 输入 / 输出示例

**输入**

```id="2rj3jw"
写一个带类的 C++ 程序，并故意包含一个错误
```

**系统执行流程**

```id="d7l6tx"
生成代码 → 编译 → 报错 → 分析 → 修复 → 再编译 → 成功
```

---

## 📦 项目结构

```id="3m1c4n"
ai-dev-assistant-pro/
├── agents/
│   ├── planner.py
│   ├── coder.py
│   ├── debugger.py
│   └── fixer.py
├── llm/
│   └── openai_client.py
├── utils/
│   ├── compiler.py
│   └── file_utils.py
├── output/
├── main.py
├── requirements.txt
└── README.md
```

---

## 🚀 快速开始

### 1️⃣ 安装依赖

```bash id="m9k2pt"
pip install -r requirements.txt
```

### 2️⃣ 配置 API Key

```bash id="p1v8zn"
export OPENAI_API_KEY=你的API_KEY
```

（Windows 使用：`setx OPENAI_API_KEY xxx`）

### 3️⃣ 运行项目

```bash id="w5s8yc"
python main.py
```

---

## 🛠 运行环境

* Python 3.10+
* g++ 编译器
* OpenAI API Key
<img width="1106" height="459" alt="image" src="https://github.com/user-attachments/assets/2447d0c1-26c2-493d-a9a1-466e18e83101" />

---

## 🔥 核心亮点

* 多 Agent 协作架构（Planner / Coder / Debugger / Fixer）
* 自动调试闭环（Auto Fix Loop）
* GPT + 编译器工具真实联动（非模拟）
* 基于错误反馈的迭代修复能力
* 从需求到可执行程序的端到端流程

---

## 📈 本项目体现的能力

* 长链推理（Long Chain Reasoning）
* Agent 系统设计能力
* AI + 工具调用（Tool Use）融合
* 自主迭代与错误修复机制
* AI 编程系统的工程化实现

---

## 🛣 后续规划（Roadmap）

* [ ] 支持 CMake 多文件工程构建
* [ ] 支持 Qt GUI 项目生成
* [ ] 自动生成单元测试（Test Agent）
* [ ] Web 可视化界面（类似 Copilot Workspace）
* [ ] Git 集成（自动提交 / 版本管理）

---

## ⚠️ 注意事项

* 当前为简化原型系统（Prototype）
* 复杂项目可能需要额外依赖管理
* GPT 输出质量会影响修复成功率

---

## 📄 License

MIT License
