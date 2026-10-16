def countdown(n):
    # Execution pauses at each yield
    # and resumes from the SAME point
    while n > 0:
        yield n      # ← pauses here
        n -= 1
    # falling off the end raises StopIteration

gen = countdown(3)
# Nothing runs yet — generator is "suspended"