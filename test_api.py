import os
import getpass

# 🔄 尝试加载 .env 文件
print("🔍 检查 .env 文件...")
try:
    from dotenv import load_dotenv
    if load_dotenv():
        print("✅ .env 文件加载成功")
    else:
        print("📝 .env 文件不存在或为空")
except ImportError:
    print("💡 提示：安装 python-dotenv 可以自动加载 .env 文件")
    print("   pip install python-dotenv")

def _set_env(var: str):
    """智能地设置环境变量"""
    if os.environ.get(var):
        print(f"✅ {var} 已配置")
        return
    
    print(f"⚠️  {var} 未找到，请输入：")
    os.environ[var] = getpass.getpass(f"{var}: ")
    print(f"✅ {var} 设置完成")

# 检查并显示当前环境变量状态
print("\n🔍 检查环境变量状态:")
print(f"TAVILY_API_KEY: {'✅ 已设置' if os.environ.get('TAVILY_API_KEY') else '❌ 未设置'}")
print(f"OPENAI_API_KEY: {'✅ 已设置' if os.environ.get('OPENAI_API_KEY') else '❌ 未设置'}")

print("\n🔄 配置必要的环境变量...")

# 设置 Tavily API Key
_set_env("TAVILY_API_KEY")

# 设置 OpenRouter API Key
_set_env("OPENAI_API_KEY")

# 设置 OpenRouter 的 Base URL
os.environ["OPENAI_BASE_URL"] = "https://openrouter.ai/api/v1"

print("\n✅ 环境变量配置完成！")
print("🔗 使用 OpenRouter 作为 API 提供商")
print("🔍 使用 Tavily 作为搜索引擎")
print(f"📊 TAVILY_API_KEY: ...{os.environ.get('TAVILY_API_KEY', 'None')[-8:]}")
print(f"📊 OPENAI_API_KEY: ...{os.environ.get('OPENAI_API_KEY', 'None')[:]}")