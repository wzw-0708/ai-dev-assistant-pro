from llm.openai_client import ask_gpt

class DebuggerAgent:
    def run(self, error_log: str):
        print("\n[Debugger] 分析错误...")

        prompt = f"""
以下是C++编译错误日志，请分析问题原因：

{error_log}

用简洁语言说明问题：
"""

        return ask_gpt("你是调试专家", prompt)
