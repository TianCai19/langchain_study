# LangChain 学习项目 🚀

> 个人学习 LangChain 和 LangGraph 的实践记录，基于 [LangGraph 官方教程](https://langchain-ai.github.io/langgraph/#get-started) 的中文翻译版本和适合国内环境的配置。

## 📖 项目简介

这个项目是我学习 LangChain 生态系统的个人实践记录。基于 [LangGraph 官方教程](https://langchain-ai.github.io/langgraph/#get-started)，我将英文教程翻译成中文，并针对国内开发环境进行了优化配置，主要是为了：

- 📚 **学习记录**：记录自己的学习进度，增强学习的成就感和持续动力
- 🌏 **本土化适配**：解决国内开发者在使用 LangChain 时遇到的网络和 API 访问问题
- 🎯 **实践导向**：通过动手实践来深入理解 LangChain 的核心概念
- 🔄 **自我反馈**：通过翻译和修改代码来验证自己的理解程度

## 🎯 主要特色

### 🌟 中文化内容
- 将英文官方教程完整翻译成中文
- 保留关键技术术语的英文原文，确保准确性
- 添加更详细的中文注释和说明

### 🛠 国内环境优化
- **OpenRouter 集成**：使用 [OpenRouter](https://openrouter.ai/) 替代直接调用 OpenAI API
- **网络访问优化**：解决国内网络环境下的 API 访问问题
- **多模型支持**：通过 OpenRouter 访问多种 LLM 模型（GPT-4、Claude、Llama 等）

### 📊 学习进度追踪
- [x] **00: 基础 Chatbot** - LangGraph 入门教程
- [x] **01: Tool-calling Chatbot** - 集成外部工具
- [ ] **02: Memory-enabled Chatbot** - 添加记忆功能
- [ ] **03: Multi-agent System** - 多智能体协作
- [ ] **04: Custom Workflows** - 自定义工作流

## 📁 项目结构

```
langchain_study/
├── README.md                               # 项目介绍（本文件）
├── .env.example                            # 环境变量配置模板
├── .gitignore                              # Git 忽略文件配置
├── 00_basic_chatbot_tutorial.ipynb        # 00: 基础 Chatbot 教程
├── 01_tool_calling_chatbot_tutorial.ipynb # 01: Tool-calling 教程
├── notebooks/                              # 更多教程 Notebooks
│   ├── 02_memory_chatbot.ipynb            # 02: Memory 功能教程
│   └── 03_multi_agent_system.ipynb       # 03: 多智能体教程
└── docs/                                   # 学习笔记和文档
    ├── concepts.md                         # 核心概念笔记
    ├── troubleshooting.md                 # 常见问题解决
    └── resources.md                        # 学习资源整理
```

## 🚀 快速开始

### 环境准备

1. **安装依赖**
```bash
pip install -U langgraph langsmith langchain[openai] langchain-tavily python-dotenv
```

2. **获取 API Keys**
   - **OpenRouter API Key**: 访问 [OpenRouter](https://openrouter.ai/) 注册账户并获取 API Key（格式：`sk-or-...`）
   - **Tavily API Key**: 访问 [Tavily](https://tavily.com/) 注册账户并获取搜索引擎 API Key

3. **配置环境变量**
```bash
# 方法一：使用 .env 文件（推荐）
cp .env.example .env
# 然后编辑 .env 文件，填入您的实际 API Keys

# 方法二：直接在代码中设置（不推荐用于生产环境）
# 教程中的代码会自动处理环境变量配置
```

### 运行教程

1. 打开 `00_basic_chatbot_tutorial.ipynb`（基础教程）
2. 或打开 `01_tool_calling_chatbot_tutorial.ipynb`（工具调用教程）
3. 按步骤执行每个单元格
3. 体验从零构建 LangGraph Chatbot 的全过程

## 🔧 配置说明

### OpenRouter 集成优势

- ✅ **统一接口**：一个 API Key 访问多个 AI 模型
- ✅ **网络友好**：解决国内访问 OpenAI 的网络问题
- ✅ **成本优化**：竞争性定价，支持多种付费方式
- ✅ **模型丰富**：支持 GPT、Claude、Llama、Gemini 等主流模型

### 支持的模型示例

```python
# GPT-4o
llm = init_chat_model("openai:openai/gpt-4o", base_url="https://openrouter.ai/api/v1")

# Claude 3.5 Sonnet
llm = init_chat_model("openai:anthropic/claude-3.5-sonnet", base_url="https://openrouter.ai/api/v1")

# Llama 3.1 405B
llm = init_chat_model("openai:meta-llama/llama-3.1-405b-instruct", base_url="https://openrouter.ai/api/v1")
```

## 📈 学习心得

### 已完成的模块

#### 00. 基础 Chatbot (✅ 已完成)
- **原教程**：[Build a Basic Chatbot](https://langchain-ai.github.io/langgraph/tutorials/get-started/1-build-basic-chatbot)
- **中文版本**：`00_basic_chatbot_tutorial.ipynb`
- **核心概念**：StateGraph、State Management、Nodes、Edges
- **实践收获**：理解了 LangGraph 的基本架构和数据流
- **本土化改进**：
  - 完整的中文注释和说明
  - OpenRouter API 集成配置
  - 适合国内网络环境的解决方案
- **技术要点**：
  - `add_messages` reducer 的作用机制
  - Graph 编译和执行流程
  - 多模型支持配置

#### 01. Tool-calling Chatbot (✅ 已完成)
- **原教程**：[Add Tools](https://langchain-ai.github.io/langgraph/tutorials/introduction/)
- **中文版本**：`01_tool_calling_chatbot_tutorial.ipynb`
- **核心概念**：Tool Integration、Tool Calling、Conditional Edges、ToolNode
- **实践收获**：掌握了如何为聊天机器人集成外部工具能力
- **本土化改进**：
  - Tavily Search API 集成和配置说明
  - OpenRouter 多模型支持示例
  - 完整的中文注释和调试信息
- **技术要点**：
  - `bind_tools()` 方法的使用
  - 条件边的路由逻辑
  - 预构建组件 vs 自定义组件
  - 工具调用的错误处理

### 学习反思

通过这个项目，我深刻体会到：

1. **理论与实践结合**：单纯看文档和真正动手写代码是完全不同的体验
2. **本土化的重要性**：解决网络和 API 访问问题大大提升了学习效率
3. **中文翻译的价值**：在翻译过程中会强迫自己真正理解每个概念
4. **进度可视化**：看到自己完成的 ✅ 给了很大的成就感和继续学习的动力

## 🎯 下一步计划

- [x] **工具集成**：为 Chatbot 添加网络搜索、计算器等工具
- [ ] **记忆功能**：实现对话历史记忆和上下文理解
- [ ] **多智能体**：构建多个 AI Agent 协作的系统
- [ ] **RAG 系统**：结合检索增强生成技术
- [ ] **生产部署**：将学习成果部署到实际应用中

## 🤝 贡献与反馈

这是一个个人学习项目，如果您也在学习 LangChain，欢迎：

- 🌟 **Star** 这个项目，给我继续学习的动力
- 🐛 **Issues** 反馈问题或建议
- 💡 **Discussions** 分享您的学习心得
- 🔄 **Fork** 创建您自己的学习版本

## 📚 参考资源

### 官方资源
- [LangGraph 官方教程](https://langchain-ai.github.io/langgraph/#get-started) - 本项目的原始教程来源
- [LangChain 官方文档](https://python.langchain.com/)
- [OpenRouter API 文档](https://openrouter.ai/docs)
- [LangSmith 调试工具](https://smith.langchain.com/)

### 教程对照
| 原版教程 | 中文版本 | 状态 |
|---------|---------|------|
| [Build a Basic Chatbot](https://langchain-ai.github.io/langgraph/tutorials/introduction/) | `00_basic_chatbot_tutorial.ipynb` | ✅ 已完成 |
| [Add Tools](https://langchain-ai.github.io/langgraph/tutorials/introduction/) | `01_tool_calling_chatbot_tutorial.ipynb` | ✅ 已完成 |
| Memory-enabled Chatbot | `02_memory_chatbot.ipynb` | 🚧 计划中 |
| Multi-agent System | `03_multi_agent_system.ipynb` | 🚧 计划中 |

## 📄 许可证

本项目基于 MIT 许可证开源，主要用于学习和交流目的。

---

⭐ **如果这个项目对您的学习有帮助，请给个 Star 支持一下！**

> 学习之路漫漫，与君共勉。每一行代码都是成长的见证。🌱
