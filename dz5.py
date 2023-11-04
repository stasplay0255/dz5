result = []


def divider(a, b):
    try:
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Both a and b should be numbers (int or float)")
        if b == 0:
            raise ValueError
        if a < b:
            raise ValueError
        if b > 100:
            raise IndexError
        return a / b
    except Exception as e:
        print(f"exception: {type(e).__name__}, {e}")
        return None


data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key in data:
    if isinstance(key, (int, float)) and isinstance(data[key], (int, float)):
        res = divider(key, data[key])
        result.append(res)
    else:
        print(f"skipped key: {key} and value: {data[key]} because they are not numbers")

print(result)
