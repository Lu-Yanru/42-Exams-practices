def validate_parentheses(s: str) -> bool:
    reference = {
    	"[": "]",
    	"(": ")",
    	"{": "}"
    }
    start = 0
    end = len(s) - 1
    while start < len(s) // 2:
        if reference[s[start]] != s[end]:
            return False
        start += 1
        end -= 1
    return True


print(validate_parentheses("[]"))
print(validate_parentheses("([{}])"))
print(validate_parentheses("[(])"))
