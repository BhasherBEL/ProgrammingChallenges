class String:
    @staticmethod
    def levenshtein_distance(w1: str, w2: str) -> int:
        if len(w1) == 0 or len(w2) == 0:
            return max(len(w1), len(w2))

        if w1[0] == w2[0]:
            return String.levenshtein_distance(w1[1:], w2[1:])

        return 1 + min(
            String.levenshtein_distance(w1[1:], w2),
            String.levenshtein_distance(w1, w2[1:]),
            String.levenshtein_distance(w1[1:], w2[1:]),
        )

    @staticmethod
    def difference_count(w1: str, w2: str) -> int:
        return sum([l1 != l2 for l1, l2 in zip(w1, w2)]) + abs(len(w1) - len(w2))
