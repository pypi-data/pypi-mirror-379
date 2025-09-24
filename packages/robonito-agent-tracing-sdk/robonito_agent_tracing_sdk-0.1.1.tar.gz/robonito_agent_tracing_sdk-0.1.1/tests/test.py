import unittest
from agent_tracing import tool_tracing

class TestModule1(unittest.TestCase):
    def test_func1(self):
        pass
        self.assertEqual(tool_tracing.add(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
