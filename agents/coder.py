from llm.openai_client import ask_gpt
import re

class CoderAgent:
    def run(self, plan: dict):
        print("\n[Coder] GPT 生成代码...")

        prompt = f"""
根据以下文件列表生成完整C++代码项目：

{plan}

要求：
1. 每个文件用如下格式输出：
=== filename ===
<code>

2. 可编译运行
"""

        result = ask_gpt("你是C++专家", prompt)

        return self.parse_files(result)

    def parse_files(self, text: str):
        files = {}
        pattern = r"=== (.*?) ===\n(.*?)(?=\n===|\Z)"
        matches = re.findall(pattern, text, re.S)

        for name, content in matches:
            files[name.strip()] = content.strip()

        return files
