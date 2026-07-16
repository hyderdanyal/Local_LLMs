import io
import sys

old_stdout = sys.stdout
sys.stdout = buffer = io.StringIO()

code="""
import random
print(random.randint(1, 10))
print("Welcome to the Snake Game!")
"""

try:
    exec(code)
except Exception as e:
    print(f"Error executing generated code: {e}")

sys.stdout = old_stdout
output = buffer.getvalue()
print("Output from the generated code:")
print(output)