# Python ternary — note: condition is in the MIDDLE
x = "even" if n % 2 == 0 else "odd"

# vs Go:  x := func() string { if n%2==0 { return "even" } return "odd" }()
# vs Java: String x = n%2==0 ? "even" : "odd";   ← more similar

# Pythonic: ternary for simple cases, never nest them
result = "high" if score > 90 else "mid" if score > 60 else "low"  # ok, but pushing it