def multiple_returns(sentence):
    len_of_sent = len(sentence)
    first_char = sentence[0] if len_of_sent > 0 else None
    return len_of_sent, first_char
