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


class TestWorkingWithMatchedPortions:
    def test_a(self):
        def solution(line: str):
            pat = re.compile(r"is.*t")
            return pat.search(line).group()
        str1 = 'This the biggest fruit you have seen?'
        str2 = 'Your mission is to read and practice consistently'
        assert solution(str1) == 'is the biggest fruit'
        assert solution(str2) == 'ission is to read and practice consistent'

    def test_b(self):
        def solution(line: str):
            pat = re.compile(r"is|the|was|to")
            return pat.search(line).span()[0]
        s1 = 'match after the last newline character'
        s2 = 'and then you want to test'
        s3 = 'this is good bye then'
        s4 = 'who was there to see?'
        assert solution(s1) == 12
        assert solution(s2) == 4
        assert solution(s3) == 2
        assert solution(s4) == 4

    def test_c(self):
        def solution(line: str):
            pat = re.compile(r"is|the|was|to")
            *_, match = pat.finditer(line)
            return match.span()[0]
        s1 = 'match after the last newline character'
        s2 = 'and then you want to test'
        s3 = 'this is good bye then'
        s4 = 'who was there to see?'
        assert solution(s1) == 12
        assert solution(s2) == 18
        assert solution(s3) == 17
        assert solution(s4) == 14

    def test_d(self):
        def solution(line: str):
            return re.search(r":(.*)", line).group(1)
        ip = 'fruits:apple, mango, guava, blueberry'
        assert solution(ip) == 'apple, mango, guava, blueberry'

    def test_e(self):
        def solution(line: str):
            import math
            pat = re.compile(r"(.*-)(.*)")
            return pat.sub(lambda x: f"{x[1]}{math.log(float(x[2]))}", line)
        s1 = 'first-3.14'
        s2 = 'next-123'
        assert solution(s1) == 'first-1.144222799920162'
        assert solution(s2) == 'next-4.812184355372417'

    def test_f(self):
        def solution(line: str):
            word_map = {"par": "spar", "spare": "extra", "park": "garden"}
            pat = re.compile(r'spare|park|par')
            return pat.sub(lambda m: word_map[m[0]], line)
        str1 = 'apartment has a park'
        str2 = 'do you have a spare cable'
        str3 = 'write a parser'
        assert solution(str1) == 'aspartment has a garden'
        assert solution(str2) == 'do you have a extra cable'
        assert solution(str3) == 'write a sparser'

    def test_g(self):
        def solution(line: str):
            return re.findall(r"\((.*?)\)", line)
        ip = 'another (way) to reuse (portion) matched (by) capture groups'
        assert solution(ip) == ['way', 'portion', 'by']

    def test_h(self):
        def solution(line: str):
            return re.findall(r"<.+?>", line)
        ip = 'a<apple> 1<> b<bye> 2<> c<cat>'
        assert solution(ip) == ['<apple>', '<> b<bye>', '<> c<cat>']

    def test_i(self):
        def solution(line: str):
            pat = re.compile(r"(.+?),(.+?) ")
            return pat.findall(line)
        row1 = '-2,5 4,+3 +42,-53 4356246,-357532354 '
        row2 = '1.32,-3.14 634,5.63 63.3e3,9907809345343.235 '
        assert solution(row1) == [('-2', '5'), ('4', '+3'),
                                  ('+42', '-53'), ('4356246', '-357532354')]
        assert solution(row2) == [('1.32', '-3.14'),
                                  ('634', '5.63'), ('63.3e3', '9907809345343.235')]

    def test_j(self):
        def solution1(line: str):
            result = re.findall(r"(.+?),(.+?) ", line)
            sums = [sum(map(int, pair)) for pair in result]
            return sums

        def solution2(line: str):
            result = re.findall(r"(.+?),(.+?) ", line)
            sums = [sum(map(float, pair)) for pair in result]
            return sums
        row1 = '-2,5 4,+3 +42,-53 4356246,-357532354 '
        row2 = '1.32,-3.14 634,5.63 63.3e3,9907809345343.235 '
        assert solution1(row1) == [3, 7, -11, -353176108]
        assert solution2(row2) == [-1.82, 639.63, 9907809408643.234]

    def test_k(self):
        def solution(line: str):
            return re.split(r":.+?-(.+?);", line)
        ip = '42:no-output;1000:car-truck;SQEX49801'
        assert solution(ip) == ['42', 'output',
                                '1000', 'truck', 'SQEX49801']

    def test_l(self):
        def solution(words: List[str]):
            return [(w, w.count("t")) for w in words]
        words = ['sequoia', 'attest', 'tattletale', 'asset']
        assert solution(words) == [
            ('sequoia', 0), ('attest', 3), ('tattletale', 4), ('asset', 1)]

    def test_m(self):
        def solution(line: str):
            return [m.groups(default="NA") for m in re.finditer(r'(.{4})(..)?:', line)]
        ip = 'TWXA42:JWPA:NTED01:'
        assert solution(ip) == [('TWXA', '42'), ('JWPA', 'NA'), ('NTED', '01')]

    def test_n(self):
        def solution(line: str):
            pat = re.compile(r"(.*?):(.*?),")
            return {m[1]: m[2] for m in pat.finditer(line)}
        row1 = 'name:rohan,maths:75,phy:89,'
        row2 = 'name:rose,maths:88,phy:92,'
        assert solution(row1) == {'name': 'rohan', 'maths': '75', 'phy': '89'}
        assert solution(row2) == {'name': 'rose', 'maths': '88', 'phy': '92'}


class TestCharacterClass:
    def test_a(self):
        def solution(items: List[str]):
            return [x for x in items if re.search(r"^hand.*([sy]|le)", x)]
        items = ['-handy', 'hand', 'handy', 'unhand', 'hands', 'handle']
        assert solution(items) == ['handy', 'hands', 'handle']

    def test_b(self):
        def solution(line: str):
            return re.sub(r"\bre[ea]?d\b", "X", line)
        ip = 'redo red credible :read: rod reed'
        assert solution(ip) == 'redo X credible :X: rod X'

    def test_c(self):
        def solution(items: List[str]):
            return [x for x in items if re.search(r"[ei].*[ln]", x)]
        words = ['surrender', 'unicorn', 'newer',
                 'door', 'empty', 'eel', 'pest']
        assert solution(words) == ['surrender', 'unicorn', 'eel']

    def test_d(self):
        def solution(items: List[str]):
            pats = (r"[ei]", r"[ln]")
            return [x for x in items if all(re.search(p, x) for p in pats)]
        words = ['surrender', 'unicorn', 'newer',
                 'door', 'empty', 'eel', 'pest']
        assert solution(words) == ['surrender', 'unicorn', 'newer', 'eel']

    def test_e(self):
        def solution(line: str):
            hex_seq = re.compile(r"\b(0x)?[\da-f]+\b", flags=re.I)
            return [m[0] for m in hex_seq.finditer(line)]
        str1 = '128A foo 0xfe32 34 0xbar'
        str2 = '0XDEADBEEF place 0x0ff1ce bad'
        assert solution(str1) == ['128A', '0xfe32', '34']
        assert solution(str2) == ['0XDEADBEEF', '0x0ff1ce', 'bad']

    def test_f(self):
        def solution(line: str):
            remove_parentheses = re.compile(r"\([^()]*\)")
            return remove_parentheses.sub('', line)
        str1 = 'def factorial()'
        str2 = 'a/b(division) + c%d(#modulo) - (e+(j/k-3)*4)'
        str3 = 'Hi there(greeting). Nice day(a(b)'
        assert solution(str1) == 'def factorial'
        assert solution(str2) == 'a/b + c%d - (e+*4)'
        assert solution(str3) == 'Hi there. Nice day(a'

    def test_g(self):
        def solution(words: List[str]):
            return [w for w in words if re.search(f"^[^epu]", w)]
        words = ['surrender', 'unicorn', 'newer',
                 'door', 'empty', 'eel', 'pest']
        assert solution(words) == ['surrender', 'newer', 'door']

    def test_h(self):
        def solution(words: List[str]):
            return [w for w in words if not re.search(f"([uw]|ee|-)", w)]
        words = ['p-t', 'you', 'tea', 'heel', 'owe', 'new', 'reed', 'ear']
        assert solution(words) == ['tea', 'ear']

    def test_i(self):
        def solution(line: str):
            pat = re.compile(r"(,[^,]*){3}\Z")
            return pat.sub(",WHTSZ323", line)
        row1 = '(2),kite,12,,D,C,,'
        row2 = 'hi,bye,sun,moon'
        assert solution(row1) == '(2),kite,12,,D,WHTSZ323'
        assert solution(row2) == 'hi,WHTSZ323'

    def test_j(self):
        def solution(line: str):
            pat = re.compile(r"[\d\s]+")
            return pat.split(line)
        str1 = 'lion \t Ink32onion Nice'
        str2 = '**1\f2\n3star\t7 77\r**'
        assert solution(str1) == ['lion', 'Ink', 'onion', 'Nice']
        assert solution(str2) == ['**', 'star', '**']

    def test_k(self):
        def solution(line: str):
            return re.sub(r"<[a-zA-Z]+>", "", line)
        ip = 'a<apple> 1<> b<bye> 2<> c<cat>'
        assert solution(ip) == 'a 1<> b 2<> c'

    def test_l(self):
        """
            '\b[a-z](on | no)[a-z]\b' is same as '\b[a-z][on]{2}[a-z]\b'.
            True or False?
        """
        def solution():
            return False
        assert solution() == False

    def test_m(self):
        def solution(items: List[str]):
            def filter_gt_624(item: re.Match):
                return any(int(m[0]) > 624 for m in re.finditer(r'\d+', item))
            return [e for e in items if filter_gt_624(e)]
        items = ['hi0000432abcd', 'car00625',
                 '42_624 0512', '3.14 96 2 foo1234baz']
        assert solution(items) == ['car00625', '3.14 96 2 foo1234baz']

    def test_n(self):
        def solution(line: str):
            count = 0
            while True:
                (line, n_brace) = re.subn(r"\{[^{}]*\}", "", line)
                if n_brace == 0:
                    break
                count += 1
            if re.search(r"[{}]", line):
                return -1
            return count
        str1 = 'a*b'
        str2 = '}a+b{'
        str3 = 'a*b+{}'
        str4 = '{{a+2}*{b+c}+e}'
        str5 = '{{a+2}*{b+{c*d}}+e}'
        str6 = '{{a+2}*{\n{b+{c*d}}+e*d}}'
        str7 = 'a*{b+c*{e*3.14}}}'
        assert solution(str1) == 0
        assert solution(str2) == -1
        assert solution(str3) == 1
        assert solution(str4) == 2
        assert solution(str5) == 3
        assert solution(str6) == 4
        assert solution(str7) == -1

    def test_o(self):
        def solution(line: str):
            return re.split(r"\s+", line.strip())
        ip = ' \t\r  so  pole\t\t\t\n\nlit in to \r\n\v\f  '
        assert solution(ip) == ['so', 'pole', 'lit', 'in', 'to']

    def test_p(self):
        def solution1(line: str):
            return re.split(r"\W+", line)

        def solution2(line: str):
            return re.split(r"(\W+)", line)
        ip = 'price_42 roast^\t\n^-ice==cat\neast'
        assert solution1(ip) == ['price_42', 'roast', 'ice', 'cat', 'east']
        assert solution2(ip) == ['price_42', ' ', 'roast',
                                 '^\t\n^-', 'ice', '==', 'cat', '\n', 'east']

    def test_q(self):
        def solution(items: List[str]):
            return [x for x in items if re.search(r"^\s*[^#\s]", x)]
        items = ['    #comment', '\t\napple #42',
                 '#oops', 'sure', 'no#1', '\t\r\f']
        assert solution(items) == ['\t\napple #42', 'sure', 'no#1']


if __name__ == "__main__":
    import pytest
    pytest.main(["-v", f"{__file__}"])
