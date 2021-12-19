import re


class TestIntroduction:
    def test_a(self):
        def solution(text: str):
            return True if re.search("0xB0", text) else False
        line1 = 'start address: 0xA0, func1 address: 0xC0'
        line2 = 'end address: 0xFF, func2 address: 0xB0'
        assert solution(line1) == False
        assert solution(line2) == True

    def test_b(self):
        def solution(text: str):
            return re.sub("5", "five", text)
        ip = 'They ate 5 apples and 5 oranges'
        assert solution(ip) == 'They ate five apples and five oranges'

    def test_c(self):
        def solution(text: str):
            return re.sub("5{1}", "five", text)
        ip = 'They ate 5 apples and 5 oranges'
        assert solution(ip) == 'They ate five apples and five oranges'

    def test_d(self):
        def solution(text: str):
            return [w for w in items if not re.search("e", w)]
        items = ['goal', 'new', 'user', 'sit', 'eat', 'dinner']
        assert solution(items) == ['goal', 'sit']

    def test_e(self):
        def solution(text: str):
            return re.sub("(?i)note", "X", text)
        ip = 'This note should not be NoTeD'
        assert solution(ip) == 'This X should not be XD'

    def test_f(self):
        def solution(text: str):
            return bool(re.search(b"at", text))
        ip = b'tiger imp goat'
        assert solution(ip) == True

    def test_g(self):
        def solution(text: str):
            result = []
            pat = re.compile("(?i)start")
            for line in para.split('\n'):
                if not pat.search(line):
                    result.append(line)
            return "\n".join(result)
        para = """
        good start
        Start working on that
        project you always wanted
        stars are shining brightly
        hi there
        start and try to
        finish the book
        bye
        """
        soln = """
        project you always wanted
        stars are shining brightly
        hi there
        finish the book
        bye
        """
        assert solution(para) == soln

    def test_h(self):
        def solution(text: str):
            return [w for w in items if re.search("(a|w)", w)]
        items = ['goal', 'new', 'user', 'sit', 'eat', 'dinner']
        assert solution(items) == ['goal', 'new', 'eat']

    def test_i(self):
        def solution(text: str):
            return [w for w in items if re.search("(?=.*e)(?=.*n)", w)]
        items = ['goal', 'new', 'user', 'sit', 'eat', 'dinner']
        assert solution(items) == ['new', 'dinner']

    def test_j(self):
        def solution(text: str):
            return re.sub("0xC0", "0x1F", re.sub("0xA0", "0x7F", text))
        ip = 'start address: 0xA0, func1 address: 0xC0'
        assert solution(ip) == 'start address: 0x7F, func1 address: 0x1F'


class TestAnchors:
    def test_a(self):
        def solution(text: str):
            return True
        line1 = ''
        assert solution(line1) == True

    def test_b(self):
        def solution(text: str):
            return True
        line1 = ''
        assert solution(line1) == True

    def test_c(self):
        def solution(text: str):
            return True
        line1 = ''
        assert solution(line1) == True

    def test_d(self):
        def solution(text: str):
            return True
        line1 = ''
        assert solution(line1) == True

    def test_e(self):
        def solution(text: str):
            return True
        line1 = ''
        assert solution(line1) == True

    def test_f(self):
        def solution(text: str):
            return True
        line1 = ''
        assert solution(line1) == True

    def test_g(self):
        def solution(text: str):
            return True
        line1 = ''
        assert solution(line1) == True

    def test_h(self):
        def solution(text: str):
            return True
        line1 = ''
        assert solution(line1) == True

    def test_i(self):
        def solution(text: str):
            return True
        line1 = ''
        assert solution(line1) == True

    def test_j(self):
        def solution(text: str):
            return True
        line1 = ''
        assert solution(line1) == True
