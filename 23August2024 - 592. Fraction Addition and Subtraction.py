
class Solution:
    def fractionAddition(self, expression: str) -> str:
        def lcm(a, b):
            return a * b // gcd(a, b)
        
        # Parse the input string to extract fractions
        fractions = re.findall(r'[+-]?\d+/\d+', expression)
        
        # Initialize the numerator and denominator of the result
        numerator, denominator = 0, 1
        
        for fraction in fractions:
            num, denom = map(int, fraction.split('/'))
            # Find the common denominator
            common_denom = lcm(denominator, denom)
            # Adjust the numerators to the common denominator
            numerator = numerator * (common_denom // denominator) + num * (common_denom // denom)
            denominator = common_denom
        
        # Simplify the resulting fraction
        common_divisor = gcd(abs(numerator), denominator)
        numerator //= common_divisor
        denominator //= common_divisor
        
        return f"{numerator}/{denominator}"
    
# Time complexity: O(n)