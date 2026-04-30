from agents.planner import PlannerAgent
from agents.coder import CoderAgent
from agents.debugger import DebuggerAgent
from agents.fixer import FixerAgent
from utils.file_utils import write_files
from utils.compiler import compile_project

MAX_RETRY = 3

def main():
    request = "写一个带类的C++程序，打印Hello，并故意加入一个小错误"

    planner = PlannerAgent()
    coder = CoderAgent()
    debugger = DebuggerAgent()
    fixer = FixerAgent()

    plan = planner.run(request)
    files = coder.run(plan)

    for i in range(MAX_RETRY):
        print(f"\n=== 第 {i+1} 轮编译 ===")

        write_files(files)

        success, log = compile_project()

        if success:
            print("\n🎉 编译成功！")
            break

        print("\n❌ 编译失败:\n", log)

        analysis = debugger.run(log)
        print("\n🧠 错误分析:\n", analysis)

        files = fixer.run(files, log)

    else:
        print("\n🚫 修复失败，达到最大次数")

if __name__ == "__main__":
    main()
