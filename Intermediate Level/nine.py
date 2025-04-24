#GCD and LCM
# GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# LCM
def lcm(a, b):
    return a * b // gcd(a, b)

print("GCD:", gcd(12, 18))
print("LCM:", lcm(12, 18))
