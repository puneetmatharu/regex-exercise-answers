import re
from typing import List


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
        def solution(items: List[str]):
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
        def solution(items: List[str]):
            return [w for w in items if re.search("(a|w)", w)]
        items = ['goal', 'new', 'user', 'sit', 'eat', 'dinner']
        assert solution(items) == ['goal', 'new', 'eat']

    def test_i(self):
        def solution(items: List[str]):
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
            pat = re.compile("^be")
            return bool(pat.search(text))
        line1 = 'be nice'
        line2 = '"best!"'
        line3 = 'better?'
        line4 = 'oh no\nbear spotted'
        assert solution(line1) == True
        assert solution(line2) == False
        assert solution(line3) == True
        assert solution(line4) == False

    def test_b(self):
        def solution(text: str):
            return re.sub(r"\bred\b", "brown", text)
        words = 'bred red spread credible'
        assert solution(words) == 'bred brown spread credible'

    def test_c(self):
        def solution(words: List[str]):
            return [w for w in words if re.search(r"\B42\B", w)]
        words = ['hi42bye', 'nice1423', 'bad42', 'cool_42a', 'fake4b']
        assert solution(words) == ['hi42bye', 'nice1423', 'cool_42a']

    def test_d(self):
        def solution(items: List[str]):
            return [e for e in items if re.search(r"(\Aden|ly\Z)", e)]
        items = ['lovely', '1\ndentist', '2 lonely', 'eden', 'fly\n', 'dent']
        assert solution(items) == ['lovely', '2 lonely', 'dent']

    def test_e(self):
        def solution(text: str):
            return re.sub(r"(?m)^mall\b", "1234", text)
        para = """\
        \nball fall wall tall\
        \nmall call ball pall\
        \nwall mall ball fall\
        \nmallet wallet malls"""
        soln = """\
        \nball fall wall tall\
        \n1234 call ball pall\
        \nwall mall ball fall\
        \nmallet wallet malls"""
        assert solution(para) == soln

    def test_f(self):
        def solution(items: List[str]):
            return [e for e in items if re.search(r"(?m)(^den|ly$)", e)]
        items = ['lovely', '1\ndentist',
                 '2 lonely', 'eden', 'fly\nfar', 'dent']
        assert solution(items) == [
            'lovely', '1\ndentist', '2 lonely', 'fly\nfar', 'dent']

    def test_g(self):
        def solution(items: List[str]):
            return [e for e in items if re.search(r"(?i)\A12\nthree\Z", e)]
        items = ['12\nthree\n', '12\nThree', '12\nthree\n4', '12\nthree']
        assert solution(items) == ['12\nThree', '12\nthree']

    def test_h(self):
        def solution(items: List[str]):
            return [re.sub(r"^hand\B", "X", e) for e in items]
        items = ['handed', 'hand', 'handy', 'unhanded', 'handle', 'hand-2']
        assert solution(items) == ['Xed', 'hand',
                                   'Xy', 'unhanded', 'Xle', 'hand-2']

    def test_i(self):
        def solution(items: List[str]):
            return [re.sub("e", "X", e) for e in items if re.search(r"\Ah", e)]
        items = ['handed', 'hand', 'handy', 'unhanded', 'handle', 'hand-2']
        assert solution(items) == ['handXd', 'hand',
                                   'handy', 'handlX', 'hand-2']


class TestAlternationAndGrouping:
    def test_a(self):
        def solution(items: List[str]):
            return [x for x in items if re.search(r"(\Aden|ly\Z)", x)]
        items = ['lovely', '1\ndentist', '2 lonely', 'eden', 'fly\n', 'dent']
        assert solution(items) == ['lovely', '2 lonely', 'dent']

    def test_b(self):
        def solution(items: List[str]):
            return [x for x in items if re.search(r"(?m)(^den|ly$)", x)]
        items = items = ['lovely', '1\ndentist',
                         '2 lonely', 'eden', 'fly\nfar', 'dent']
        assert solution(items) == [
            'lovely', '1\ndentist', '2 lonely', 'fly\nfar', 'dent']

    def test_c(self):
        def solution(line: str):
            pat = re.compile(r"re(mov||ceiv|fus)ed")
            return pat.sub('X', line)
        s1 = 'creed refuse removed read'
        s2 = 'refused reed redo received'
        assert solution(s1) == 'cX refuse X read'
        assert solution(s2) == 'X X redo X'

    def test_d(self):
        def solution(line: str):
            words = ['late', 'later', 'slated']
            # Match largest words first
            pat = re.compile("|".join(sorted(words, reverse=True)))
            return pat.sub('A', line)
        s1 = 'plate full of slate'
        s2 = "slated for later, don't be late"
        assert solution(s1) == 'pA full of sA'
        assert solution(s2) == "A for A, don't be A"

    def test_e(self):
        def solution(items: List[str]):
            words = ['late', 'later', 'slated']
            pat = re.compile('|'.join(words))
            return [x for x in items if pat.fullmatch(x)]
        items = ['slate', 'later', 'plate', 'late', 'slates', 'slated ']
        assert solution(items) == ['later', 'late']


class TestEscapingMetacharacters:
    def test_a(self):
        def solution(line: str):
            return re.sub(r"\(9-2\)\*", "3", line)
        str1 = '(9-2)*5+qty/3'
        str2 = '(qty+4)/2-(9-2)*5+pq/4'
        assert solution(str1) == '35+qty/3'
        assert solution(str2) == '(qty+4)/2-35+pq/4'

    def test_b(self):
        def solution(line: str):
            esc = re.escape(r"(4)\|")
            pat = re.compile(r"\A" + esc + r"|" + esc + r"\Z")
            return pat.sub("2", line)
        s1 = r'2.3/(4)\|6 foo 5.3-(4)\|'
        s2 = r'(4)\|42 - (4)\|3'
        s3 = 'two - (4)\\|\n'
        assert solution(s1) == '2.3/(4)\\|6 foo 5.3-2'
        assert solution(s2) == '242 - (4)\\|3'
        assert solution(s3) == 'two - (4)\\|\n'

    def test_c(self):
        def solution(line: str):
            items = ['a.b', '3+n', r'x\y\z', 'qty||price', '{n}']
            pat = re.compile('|'.join([re.escape(x) for x in items]))
            return pat.sub('X', line)
        s1 = '0a.bcd'
        s2 = 'E{n}AMPLE'
        s3 = r'43+n2 ax\y\ze'
        assert solution(s1) == '0Xcd'
        assert solution(s2) == 'EXAMPLE'
        assert solution(s3) == '4X2 aXe'

    def test_d(self):
        def solution(line: str):
            return re.sub("\b", " ", line)
        ip = '123\b456'
        assert solution(ip) == '123 456'

    def test_e(self):
        def solution(line: str):
            return re.sub(r"\\e", "e", line)
        ip = r'th\er\e ar\e common asp\ects among th\e alt\ernations'
        assert solution(
            ip) == 'there are common aspects among the alternations'

    def test_f(self):
        def solution(line: str):
            eqns = ['(a^b)', '(a/b)', '(a^b)+2']
            pat = re.compile("|".join([re.escape(x)
                             for x in sorted(eqns, reverse=True)]))
            return pat.sub("X", line)
        ip = '3-(a^b)+2*(a^b)-(a/b)+3'
        assert solution(ip) == '3-X*X-X+3'


class TestDotMetacharacterAndQuantifiers:
    def test_a(self):
        def solution(line: str):
            return re.sub(r"42/+5", "8", line)
        ip = 'a+42//5-c pressure*3+42/5-14256'
        assert solution(ip) == 'a+8-c pressure*3+8-14256'

    def test_b(self):
        def solution(items: List[str]):
            return [x for x in items if re.search(r"^hand(.?|le)\Z", x)]
        items = ['handed', 'hand', 'handled',
                 'handy', 'unhand', 'hands', 'handle']
        assert solution(items) == ['hand', 'handy', 'hands', 'handle']

    def test_c(self):
        def solution(line: str):
            return re.split(r"42/{1,2}5", line)
        eqn1 = 'a+42//5-c'
        eqn2 = 'pressure*3+42/5-14256'
        eqn3 = 'r*42-5/3+42///5-42/53+a'
        assert solution(eqn1) == ['a+', '-c']
        assert solution(eqn2) == ['pressure*3+', '-14256']
        assert solution(eqn3) == ['r*42-5/3+42///5-', '3+a']

    def test_d(self):
        def solution(line: str):
            pat = re.compile(r"i.*")
            return pat.sub("", line)
        s1 = 'remove the special meaning of such constructs'
        s2 = 'characters while constructing'
        assert solution(s1) == 'remove the spec'
        assert solution(s2) == 'characters wh'

    def test_e(self):
        def solution(line: str):
            remove_parentheses = re.compile(r"\(.*?\)")
            return remove_parentheses.sub('', line)
        str1 = 'a+b(addition)'
        str2 = 'a/b(division) + c%d(#modulo)'
        str3 = 'Hi there(greeting). Nice day(a(b)'
        assert solution(str1) == 'a+b'
        assert solution(str2) == 'a/b + c%d'
        assert solution(str3) == 'Hi there. Nice day'

    def test_f(self):
        def solution(line: str):
            change = re.compile(r'inco|ink|ing|inter|int|ion|in')
            return change.sub('X', words)
        words = 'plink incoming tint winter in caution sentient'
        assert solution(words) == 'plX XmX tX wX X cautX sentient'

    def test_g(self):
        "'?' is same as {0,1}"
        "'*' is same as {0,}"
        "'+' is same as {1,}"

    def test_h(self):
        "Question: '(a*|b*)' is same as '(a | b)*'. True or False?"
        answer = False

    def test_i(self):
        def solution(line: str):
            pat = re.compile(r"(?i)(test)(.+)\Z")
            return pat.sub('', line)
        s1 = 'this is a Test'
        s2 = 'always test your RE for corner cases'
        s3 = 'a TEST of skill tests?'
        assert solution(s1) == "this is a Test"
        assert solution(s2) == "always "
        assert solution(s3) == "a "

    def test_j(self):
        def solution(words: List[str]):
            pats = (r"^s", r"e", r"t")
            return [w for w in words if all([re.search(p, w) for p in pats])]
        words = ['sequoia', 'subtle', 'exhibit',
                 'asset', 'sets', 'tests', 'site']
        assert solution(words) == ['subtle', 'sets', 'site']

    def test_k(self):
        def solution(words: List[str]):
            return [w for w in words if re.search(".{6,}", w)]
        words = ['sequoia', 'subtle', 'exhibit',
                 'asset', 'sets', 'tests', 'site']
        assert solution(words) == ['sequoia', 'subtle', 'exhibit']

    def test_l(self):
        def solution(words: List[str]):
            pat = re.compile(r"^(s|t)(.{,5})$")
            return [w for w in words if pat.search(w)]
        words = ['sequoia', 'subtle', 'exhibit',
                 'asset', 'sets', 'tests', 'site']
        assert solution(words) == ['subtle', 'sets', 'tests', 'site']

    def test_m(self):
        def solution(line: str):
            return re.sub(r'<.+?>', '', line)
        ip = 'a<apple> 1<> b<bye> 2<> c<cat>'
        # Not possible easily without character classes!
        assert solution(ip) != 'a 1<> b 2<> c'

    def test_n(self):
        def solution(line: str):
            pat = re.compile(r" +// +")
            return pat.split(line, maxsplit=1)
        s1 = 'go there  //   "this // that"'
        s2 = 'a//b // c//d e//f // 4//5'
        s3 = '42// hi//bye//see // carefully'
        assert solution(s1) == ['go there', '"this // that"']
        assert solution(s2) == ['a//b', 'c//d e//f // 4//5']
        assert solution(s3) == ['42// hi//bye//see', 'carefully']


if __name__ == "__main__":
    import pytest
    pytest.main(["-v", f"{__file__}"])
