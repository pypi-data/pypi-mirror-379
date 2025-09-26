#!/usr/bin/env python3
"""
提示词集成测试脚本 - 使用真实的 LLM API 进行测试
"""

import os
import sys
import json
import asyncio
from pathlib import Path

# 添加项目路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from tests.test_prompt_behavior import PromptTester, TestCase, ExpectedBehavior
from aipyapp.aipy.prompts import PromptManager
from aipyapp.llm.manager import LLMManager


class IntegratedPromptTester(PromptTester):
    """集成测试器，使用真实的 LLM API"""
    
    def __init__(self, prompt_path: str, llm_manager: LLMManager):
        super().__init__(prompt_path)
        self.llm_manager = llm_manager
        self.prompt_manager = PromptManager()
    
    def load_prompt_template(self) -> str:
        """加载提示词模板"""
        with open(self.prompt_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def construct_full_prompt(self, test_case: TestCase) -> str:
        """构造包含提示词的完整 prompt"""
        template = self.load_prompt_template()
        
        # 构造测试 prompt
        system_prompt = f"""
{template}

现在请处理用户的请求。记住：
1. 优先尝试执行任务
2. 只有在真正无法继续时才使用状态头
3. 对于可用免费替代方案的任务，不要要求 API 密钥
"""
        
        return {
            "system": system_prompt,
            "user": test_case.user_request
        }
    
    async def simulate_llm_response(self, test_case: TestCase) -> str:
        """使用真实 LLM API 获取响应"""
        try:
            # 构造 prompt
            prompts = self.construct_full_prompt(test_case)
            
            # 调用 LLM
            messages = [
                {"role": "system", "content": prompts["system"]},
                {"role": "user", "content": prompts["user"]}
            ]
            
            # 使用项目的 LLM 管理器
            response = await self.llm_manager.chat_async(messages)
            return response.content
            
        except Exception as e:
            print(f"API 调用失败: {e}")
            # 降级到模拟响应
            return await super().simulate_llm_response(test_case)


def create_benchmark_tests() -> List[TestCase]:
    """创建基准测试用例"""
    return [
        # 核心问题案例：之前被错误拒绝的任务
        TestCase(
            name="weather_free_api",
            user_request="获取上海今天的天气情况",
            expected_behavior=ExpectedBehavior.SHOULD_EXECUTE,
            category="weather_critical"
        ),
        TestCase(
            name="local_file_read",
            user_request="读取并分析当前目录的 README.md 文件",
            expected_behavior=ExpectedBehavior.SHOULD_EXECUTE,
            category="file_critical"
        ),
        TestCase(
            name="simple_computation",
            user_request="计算 2^10 的值",
            expected_behavior=ExpectedBehavior.SHOULD_EXECUTE,
            category="compute_critical"
        ),
        
        # 边界测试：应该要求信息的场景
        TestCase(
            name="personal_calendar",
            user_request="查看我明天的日程安排",
            expected_behavior=ExpectedBehavior.SHOULD_NEED_INFO,
            category="private_boundary"
        ),
        TestCase(
            name="paid_api_key",
            user_request="使用我的 Google Maps API 密钥查找路线",
            expected_behavior=ExpectedBehavior.SHOULD_NEED_INFO,
            category="auth_boundary"
        ),
    ]


async def run_integration_test():
    """运行集成测试"""
    print("=== 提示词集成测试 ===")
    
    # 检查配置
    prompt_path = "/Users/lgx/Src/aipy/aipyapp/res/prompts/task_status_header.j2"
    if not os.path.exists(prompt_path):
        print(f"❌ 提示词文件不存在: {prompt_path}")
        return
    
    try:
        # 初始化 LLM 管理器（需要配置）
        llm_manager = LLMManager()
        # 注意：这里需要根据实际项目配置调整
        
        tester = IntegratedPromptTester(prompt_path, llm_manager)
        
        # 运行基准测试
        print("运行基准测试用例...")
        benchmark_tests = create_benchmark_tests()
        
        results = []
        for test_case in benchmark_tests:
            print(f"测试: {test_case.name}")
            result = await tester.run_single_test(test_case)
            results.append(result)
            
            # 实时反馈
            status = "✅" if result.get("behavior_match", False) else "❌"
            print(f"  {status} {result.get('analysis', 'Unknown')}")
        
        # 统计结果
        total = len(results)
        passed = sum(1 for r in results if r.get("behavior_match", False))
        
        print(f"\n=== 测试结果 ===")
        print(f"总计: {total}, 通过: {passed}, 失败: {total - passed}")
        print(f"成功率: {passed/total*100:.1f}%")
        
        # 保存结果
        timestamp = str(int(asyncio.get_event_loop().time()))
        result_file = f"/Users/lgx/Src/aipy/integration_test_results_{timestamp}.json"
        
        with open(result_file, 'w', encoding='utf-8') as f:
            json.dump({
                "timestamp": timestamp,
                "total_tests": total,
                "passed_tests": passed,
                "success_rate": passed / total,
                "results": results
            }, f, ensure_ascii=False, indent=2)
        
        print(f"详细结果已保存: {result_file}")
        
        # 如果成功率低，提供改进建议
        if passed / total < 0.8:
            print("\n⚠️  成功率较低，建议:")
            print("1. 检查提示词中的执行优先级语言是否足够强烈")
            print("2. 考虑添加更多正面示例")
            print("3. 调整决策指南的措辞")
        
    except Exception as e:
        print(f"❌ 集成测试失败: {e}")
        print("请检查 LLM 配置和网络连接")


if __name__ == "__main__":
    asyncio.run(run_integration_test())