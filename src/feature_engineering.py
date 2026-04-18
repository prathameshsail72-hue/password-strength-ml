import math
from itertools import groupby

COMMON_PATTERNS = ["123", "abc", "password", "qwerty", "111", "000"]


def calculate_entropy(password):
    if len(password) == 0:
        return 0

    prob = [float(password.count(c)) / len(password) for c in set(password)]
    return -sum([p * math.log2(p) for p in prob])


def extract_features(password):
    features = {}

    features['length'] = len(password)

    features['num_lower'] = sum(c.islower() for c in password)
    features['num_upper'] = sum(c.isupper() for c in password)
    features['num_digits'] = sum(c.isdigit() for c in password)
    features['num_special'] = sum(not c.isalnum() for c in password)

    length = len(password) if len(password) > 0 else 1
    features['lower_ratio'] = features['num_lower'] / length
    features['upper_ratio'] = features['num_upper'] / length
    features['digit_ratio'] = features['num_digits'] / length
    features['special_ratio'] = features['num_special'] / length

    features['has_lower'] = int(features['num_lower'] > 0)
    features['has_upper'] = int(features['num_upper'] > 0)
    features['has_digit'] = int(features['num_digits'] > 0)
    features['has_special'] = int(features['num_special'] > 0)

    features['entropy'] = calculate_entropy(password)

    features['has_common_pattern'] = int(
        any(pattern in password.lower() for pattern in COMMON_PATTERNS)
    )

    features['max_repeat'] = max(
        [len(list(g)) for _, g in groupby(password)],
        default=1
    )

    return features


if __name__ == "__main__":
    print(extract_features("P@ssw0rd123"))