from difflib import SequenceMatcher


# TODO: Check 'fuzzywuzzy' and 'rapidfuzz'
# libraries that wrap this 'difflib'
class TextComparator:
    """
    Class to warp functionality related to
    comparing texts.
    """

    @staticmethod
    def get_similarity(
        text_a: str,
        text_b : str
    ) -> float:
        """
        Get the similarity between the 'text_a' and
        the 'text_b' texts provided as a value in a
        [0.0, 1.0] range (where 1.0 means exactly the
        same texts).
        """
        return SequenceMatcher(None, text_a, text_b).ratio()
    
    @staticmethod
    def is_similar(
        text_a: str,
        text_b: str,
        similarity: float = 0.95
    ) -> bool:
        """
        Check if the 'text_a' provided is, at least,
        a 'similarity' similar to the also given
        'text_b'.

        The 'similarity' parameter must be a value
        in the [0.0, 1.0] range (where 1.0 means
        completely exact texts).
        """
        return TextComparator.get_similarity(
            text_a = text_a,
            text_b = text_b
        ) >= similarity

