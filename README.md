# 📚 LeetCode Solutions

This repository contains my solutions to problems from [LeetCode](https://leetcode.com/). All solutions are kept in a single Jupyter Notebook file: **`solution.ipynb`**.

## 📂 Structure

Every problem is added as a separate section inside `solution.ipynb`, following a consistent format:

- Problem number and title
- Solution code

## 🗂️ Notebook Format

```markdown
## [Problem No]. Problem Title

# Solution code
```
```

### Example Entry

## 1. Two Sum

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
```

## 🚀 Technologies Used

- Python 3
- Jupyter Notebook