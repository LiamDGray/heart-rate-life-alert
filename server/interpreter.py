OVERDOSE_HEART_RATE = 80


def is_overdose(heart_rate):
    if heart_rate >= OVERDOSE_HEART_RATE:
        return True
    else:
        return False