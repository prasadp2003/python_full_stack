import re
from typing import List, Tuple

EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
PHONE_RE = re.compile(r"(?:(?:\+?\d{1,3}[-.\s]?)?(?:\(?\d{1,4}\)?[-.\s]?){1,4}\d{1,4})")
DATE_RE = re.compile(
    r"\b(?:(?:\d{4}[-/.]\d{1,2}[-/.]\d{1,2})|(?:\d{1,2}[-/.]\d{1,2}[-/.]\d{4})|"
    r"(?:\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*\s+\d{4})|"
    r"(?:(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*\s+\d{1,2},\s*\d{4}))\b",
    re.IGNORECASE
)

def extract_all(text: str) -> Tuple[List[str], List[str], List[str]]:
    emails = [m.group(0) for m in EMAIL_RE.finditer(text)]
    phones = [m.group(0) for m in PHONE_RE.finditer(text)]
    dates  = [m.group(0) for m in DATE_RE.finditer(text)]
    return emails, phones, dates

# Example usage
if __name__ == "__main__":
    sample = """
    Contact: Alice <alice.smith+work@example.co.uk>, Bob at bob@example.com.
    Call +91 98765 43210 or (020) 7946 0958 or 123-456-7890.
    Important dates: 2024-07-01, 01/07/2024, July 1, 2024 and 1 Jul 2024.
    """
    e,p,d = extract_all(sample)
    print("Emails:", e)
    print("Phones:", p)
    print("Dates:", d)
