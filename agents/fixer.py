from llm.openai_client import ask_gpt
import re

class FixerAgent:
    def run(self, files: dict, error_log: str):
        print("\n[Fixer] GPT 修复代码...")

        prompt = f"""
下面是C++项目代码和错误日志，请修复：

错误：
{error_log}

代码：
{files}

返回完整修复后的文件，格式：
=== filename ===
code
"""

        result = ask_gpt("你是C++修复专家", prompt)

        return self.parse_files(result)

    def parse_files(self, text):
        files = {}
        pattern = r"=== (.*?) ===\n(.*?)(?=\n===|\Z)"
        matches = re.findall(pattern, text, re.S)

        for name, content in matches:
            files[name.strip()] = content.strip()

        return files
