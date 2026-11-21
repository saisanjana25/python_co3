# Q7 - Design a Contact-Merging Program

def normalise_phone(phone):
    digits = "".join(ch for ch in phone if ch.isdigit())
    if digits.startswith("91") and len(digits) == 12:
        digits = digits[2:]
    return digits


def normalise_name(name):
    return " ".join(name.lower().replace(".", "").split())


def merge_contacts(contact_lists):
    merged = {}
    for contacts in contact_lists:
        for c in contacts:
            numbers = c.get("phones", [])
            emails = c.get("emails", [])
            key = normalise_phone(numbers[0]) if numbers else None
            if not key:
                continue
            if key not in merged:
                merged[key] = {
                    "name": c.get("name", "").strip(),
                    "phones": set(),
                    "emails": set(),
                }
            merged[key]["phones"].update(normalise_phone(x) for x in numbers if x)
            merged[key]["emails"].update(x.strip().lower() for x in emails if x)
    return merged


if __name__ == "__main__":
    list_a = [
        {"name": "A. Kumar", "phones": ["+91 98765-43210"], "emails": ["akumar@example.com"]},
        {"name": "Priya S", "phones": ["9123456789"], "emails": ["priya@example.com"]},
    ]
    list_b = [
        {"name": "Arun Kumar", "phones": ["9876543210", "044-22334455"], "emails": ["arun.k@example.com"]},
    ]
    print(merge_contacts([list_a, list_b]))
