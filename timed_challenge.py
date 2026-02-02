"""
Timed Challenge — Group 3: Pointer-Based Traversal
Question 9: Insert After Value

Insert a new value immediately after the first occurrence of a target.
Example:
Input: [A, B, C], Insert "X" after "B"
Output: [A, B, X, C]
"""

def insert_after_value(lst, target, new_value):
    """
    Inserts new_value immediately after the first occurrence of target.
    Returns a new list. Raises TypeError with a specific message if:
    - input is not a list, or
    - target is not found in the list.
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")

    result = []
    inserted = False

    for item in lst:
        result.append(item)
        if item == target and not inserted:
            result.append(new_value)
            inserted = True

    if not inserted:
        # target not found — include actual list in the message
        raise TypeError(f"{lst} (target not found)")

    return result



# ------------------ TEST CASES ------------------

print(insert_after_value(["A", "B", "C"], "B", "X"))
# Expected: ["A", "B", "X", "C"]

try:
    print(insert_after_value([], "B", "X"))
except Exception as e:
    print(e)
# Expected: [] (target not found)  ← as an error message, not a returned list

print(insert_after_value(["A", "B", "B", "C"], "B", "X"))
# Expected: ["A", "B", "X", "B", "C"]

try:
    print(insert_after_value(["A", "C", "D"], "B", "X"))
except Exception as e:
    print(e)
# Expected: ['A', 'C', 'D'] (target not found)

try:
    print(insert_after_value("not a list", "B", "X"))
except Exception as e:
    print(e)
# Expected: Input must be a list.

'''
For this timed challenge, I chose to use a simple Python list as the primary data structure. The problem requires inserting a value immediately after the first occurrence of a target, which maps naturally to sequential traversal. Lists support ordered iteration and allow appending in O(1) time, which makes them a practical fit for reconstructing the sequence. Although inserting into the middle of a list is O(n), the problem only requires a single pass and insertion, so the overall runtime remains linear.

The 30‑minute time limit influenced my decision to avoid more complex pointer‑based structures such as linked lists. While a linked list could theoretically offer O(1) insertion once the node is found, implementing a full class under time pressure introduces unnecessary overhead and increases the risk of bugs. Given the constraints, prioritizing correctness and clarity over the theoretical was a better choice.

I also chose to rebuild the list rather than modify it in place. This approach is simpler, avoids index‑shifting pitfalls, and ensures predictable behavior even when the target appears multiple times. I also added defensive checks for invalid input types and tested edge cases such as empty lists and missing targets. These trade‑offs allowed me to deliver a clean, reliable solution within the allotted time while still demonstrating thoughtful design decisions.
'''
