
def removeKDigits(num: str, k: int) -> str:
    numStack = []

    for digit in num:
        while k and numStack and numStack[-1] > digit:
            numStack.pop()
            k -= 1

        numStack.append(digit)

    finalstack = numStack[:-k] if k else numStack

    return "".join(finalstack).lstrip('0') or "0"

print(removeKDigits("1432219", 3))
