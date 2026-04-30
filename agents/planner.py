from llm.openai_client import ask_gpt
import json

class PlannerAgent:
    def run(self, request: str):
        print("\n[Planner] GPT 解析需求...")

        prompt = f"""
将以下需求拆解为C++项目文件结构，返回JSON：
需求：{request}

格式：
{{
  "files": ["main.cpp", "xxx.h"],
  "description": "..."
}}
"""

        result = ask_gpt("你是软件架构师", prompt)

        try:
            plan = json.loads(result)
        except:
            print("⚠ GPT 输出解析失败，使用默认方案")
            plan = {
                "files": ["main.cpp"],
                "description": request
            }

        print("[Planner] 结果:", plan)
        return plan
