# Copyright 2023-2025 Geoffrey R. Scheller
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pythonic_fp.circulararray.auto import CA, ca


class TestCircularArrayResizing:
    """Functionality testing"""

    def test_mutate_returns_none(self) -> None:
        """Test for builtin behaviors"""
        ca1: CA[int] = ca()
        assert ca1.pushl(1) is None  # type: ignore[func-returns-value]
        ca1.pushl(0)
        ca1.pushr(2)
        ca1.pushr(3)
        assert ca1.popld(-1) == 0
        ca1.pushr(4)
        ca2 = ca1.map(lambda x: x + 1)
        assert ca1 is not ca2
        assert ca1 != ca2
        assert len(ca1) == len(ca2)
        assert ca1.popld(-1) == 1
        while ca1:
            assert ca1.popld(-1) == ca2.popld(-2)
        assert len(ca1) == 0
        assert len(ca2) == 1
        assert ca2.popr() == 5
        try:
            assert ca2.popr()
        except ValueError as ve:
            assert True
            assert str(ve) == 'Method popr called on an empty CA'
        else:
            assert False

    def test_push_then_pop(self) -> None:
        """Functionality test"""
        ca0: CA[str] = ca()
        pushed1 = '42'
        ca0.pushl(pushed1)
        popped1 = ca0.popl()
        assert pushed1 == popped1
        assert len(ca0) == 0
        try:
            ca0.popl()
        except ValueError as ve:
            assert str(ve) == 'Method popl called on an empty CA'
        else:
            assert False
        pushed1 = '0'
        ca0.pushl(pushed1)
        popped1 = ca0.popr()
        assert pushed1 == popped1 == '0'
        assert not ca0
        pushed1 = '0'
        ca0.pushr(pushed1)
        popped1 = ca0.popld('666')
        assert popped1 != '666'
        assert pushed1 == popped1
        assert len(ca0) == 0
        pushed2 = ''
        ca0.pushr(pushed2)
        popped2 = ca0.poprd('42')
        assert popped2 != '42'
        assert pushed2 == popped2
        assert len(ca0) == 0
        ca0.pushr('first')
        ca0.pushr('second')
        ca0.pushr('last')
        assert ca0.popld('error') == 'first'
        assert ca0.poprd('error') == 'last'
        assert ca0
        assert len(ca0) == 1
        ca0.popl()
        assert len(ca0) == 0

    def test_rotate(self) -> None:
        """Functionality test"""
        ca0 = CA[int]()
        ca0.rotl(42)
        assert ca0 == ca()

        ca1 = ca(42)
        ca1.rotr()
        assert ca1 == CA((42,))

        ca9 = ca(1, 2, 3, 4, 5, 6, 7, 8, 9)
        ca9.rotl()
        assert ca9 == ca(2, 3, 4, 5, 6, 7, 8, 9, 1)
        ca9.rotr()
        assert ca9 == ca(1, 2, 3, 4, 5, 6, 7, 8, 9)
        ca9.rotl(5)
        assert ca9 == ca(6, 7, 8, 9, 1, 2, 3, 4, 5)
        ca9.rotr(6)
        assert ca9 == ca(9, 1, 2, 3, 4, 5, 6, 7, 8)

    def test_iterators(self) -> None:
        """Functionality test"""
        data: list[int] = [*range(100)]
        c: CA[int] = CA(data)
        ii = 0
        for item in c:
            assert data[ii] == item
            ii += 1
        assert ii == 100

        data.append(100)
        c = CA(data)
        data.reverse()
        ii = 0
        for item in reversed(c):
            assert data[ii] == item
            ii += 1
        assert ii == 101

        c0: CA[object] = ca()
        for _ in c0:
            assert False
        for _ in reversed(c0):
            assert False

        data2: list[str] = []
        c0 = CA(data2)
        for _ in c0:
            assert False
        for _ in reversed(c0):
            assert False

    def test_equality(self) -> None:
        """Functionality test"""
        c1: CA[object] = ca(1, 2, 3, 'Forty-Two', (7, 11, 'foobar'))
        c2: CA[object] = ca(2, 3, 'Forty-Two')
        c2.pushl(1)
        c2.pushr((7, 11, 'foobar'))
        assert c1 == c2

        tup2 = c2.popr()
        assert c1 != c2

        c2.pushr((42, 'foofoo'))
        assert c1 != c2

        c1.popr()
        c1.pushr((42, 'foofoo'))
        c1.pushr(tup2)
        c2.pushr(tup2)
        assert c1 == c2

        hold_a = c1.popl()
        c1.resize(42)
        hold_b = c1.popl()
        hold_c = c1.popr()
        c1.pushl(hold_b)
        c1.pushr(hold_c)
        c1.pushl(hold_a)
        c1.pushl(200)
        c2.pushl(200)
        assert c1 == c2

    def test_map(self) -> None:
        """Functionality test"""
        c0: CA[int] = ca(1, 2, 3, 10)
        c1 = CA(c0)
        c2 = c1.map(lambda x: str(x * x - 1))
        assert c2 == ca('0', '3', '8', '99')
        assert c1 != c2
        assert c1 == c0
        assert c1 is not c0
        assert len(c1) == len(c2) == 4

    def test_get_set_items(self) -> None:
        """Functionality test"""
        c1 = ca('a', 'b', 'c', 'd')
        c2 = CA(c1)
        assert c1 == c2
        c1[2] = 'cat'
        c1[-1] = 'dog'
        assert c2.popr() == 'd'
        assert c2.popr() == 'c'
        c2.pushr('cat')
        try:
            c2[3] = 'dog'  # no such index
        except IndexError:
            assert True
        else:
            assert False
        assert c1 != c2
        c2.pushr('dog')
        assert c1 == c2
        c2[1] = 'bob'
        assert c1 != c2
        assert c1.popld('error') == 'a'
        c1[0] = c2[1]
        assert c1 != c2
        assert c2.popld('error') == 'a'
        assert c1 == c2

    def test_foldl(self) -> None:
        """Functionality test"""
        c1: CA[int] = ca()
        try:
            c1.foldl(lambda x, y: x + y)
        except ValueError:
            assert True
        else:
            assert False
        assert c1.foldl(lambda x, y: x + y, 42) == 42
        assert c1.foldl(lambda x, y: x + y, 0) == 0

        c3: CA[int] = CA(range(1, 11))
        assert c3.foldl(lambda x, y: x + y) == 55
        assert c3.foldl(lambda x, y: x + y, 10) == 65

        c4: CA[int] = CA((0, 1, 2, 3, 4))

        def f(vs: list[int], v: int) -> list[int]:
            vs.append(v)
            return vs

        empty: list[int] = []
        assert c4.foldl(f, empty) == [0, 1, 2, 3, 4]

    def test_foldr(self) -> None:
        """Functionality test"""
        c1: CA[int] = CA()
        try:
            c1.foldr(lambda x, y: x * y)
        except ValueError:
            assert True
        else:
            assert False
        assert c1.foldr(lambda x, y: x * y, 42) == 42

        c2: CA[int] = CA(range(1, 6))
        assert c2.foldr(lambda x, y: x * y) == 120
        assert c2.foldr(lambda x, y: x * y, 10) == 1200

        def f(v: int, vs: list[int]) -> list[int]:
            vs.append(v)
            return vs

        c3: CA[int] = CA(range(5))
        empty: list[int] = []
        assert c3 == ca(0, 1, 2, 3, 4)
        assert c3.foldr(f, empty) == [4, 3, 2, 1, 0]

    def test_pop_tuples(self) -> None:
        """Functionality test"""
        ca1 = CA(range(100))
        zero, one, two, *rest = ca1.poplt(10)
        assert zero == 0
        assert one == 1
        assert two == 2
        assert rest == [3, 4, 5, 6, 7, 8, 9]
        assert len(ca1) == 90

        last, next_to_last, *rest = ca1.poprt(5)
        assert last == 99
        assert next_to_last == 98
        assert rest == [97, 96, 95]
        assert len(ca1) == 85

        ca2 = CA(ca1)
        assert len(ca1.poprt(0)) == 0
        assert ca1 == ca2

    def test_fold(self) -> None:
        """Functionality test"""
        ca1 = CA(range(1, 101))
        assert ca1.foldl(lambda acc, d: acc + d) == 5050
        assert ca1.foldr(lambda d, acc: d + acc) == 5050

        def fl(acc: int, d: int) -> int:
            return acc * acc - d

        def fr(d: int, acc: int) -> int:
            return acc * acc - d

        ca2 = ca(2, 3, 4)
        assert ca2.foldl(fl) == -3
        assert ca2.foldr(fr) == 167

    def test_readme(self) -> None:
        """Functionality test"""
        ca0 = ca(1, 2, 3)
        assert ca0.popl() == 1
        assert ca0.popr() == 3
        ca0.pushr(42, 0)
        ca0.pushl(0, 1)
        assert repr(ca0) == 'ca(1, 0, 2, 42, 0)'
        assert str(ca0) == '(|1, 0, 2, 42, 0|)'

        ca0 = CA(range(1, 11))
        assert repr(ca0) == 'ca(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)'
        assert str(ca0) == '(|1, 2, 3, 4, 5, 6, 7, 8, 9, 10|)'
        assert len(ca0) == 10
        tup3 = ca0.poplt(3)
        tup4 = ca0.poprt(4)
        assert tup3 == (1, 2, 3)
        assert tup4 == (10, 9, 8, 7)

        assert ca0 == ca(4, 5, 6)
        four, *rest = ca0.poplt(1000)
        assert four == 4
        assert rest == [5, 6]
        assert len(ca0) == 0

    def test_pop(self) -> None:
        """Functionality test"""
        ca1 = ca(1, 2, 3)
        assert ca1.popld(42) == 1
        assert ca1.poprd(42) == 3
        assert ca1.popld(42) == 2
        assert ca1.poprd(42) == 42
        assert ca1.popld(42) == 42
        assert len(ca1) == 0

        ca2: CA[int] = ca(0, 1, 2, 3, 4, 5, 6)
        assert ca2.popl() == 0
        assert ca2.popr() == 6
        assert ca2 == ca(1, 2, 3, 4, 5)
        ca2.pushl(0)
        ca2.pushr(6)
        assert ca2 == ca(0, 1, 2, 3, 4, 5, 6)
        ca2.pushl(10, 11, 12)
        assert ca2 == ca(12, 11, 10, 0, 1, 2, 3, 4, 5, 6)
        ca2.pushr(86, 99)
        assert ca2 == ca(12, 11, 10, 0, 1, 2, 3, 4, 5, 6, 86, 99)
        control = ca2.poprt(2)
        assert control == (99, 86)
        assert ca2 == ca(12, 11, 10, 0, 1, 2, 3, 4, 5, 6)

        ca3: CA[int] = CA(range(1, 10001))
        ca3_l_first100 = ca3.poplt(100)
        ca3_r_last100 = ca3.poprt(100)
        ca3_l_prev10 = ca3.poplt(10)
        ca3_r_prev10 = ca3.poprt(10)
        assert ca3_l_first100 == tuple(range(1, 101))
        assert ca3_r_last100 == tuple(range(10000, 9900, -1))
        assert ca3_l_prev10 == tuple(range(101, 111))
        assert ca3_r_prev10 == tuple(range(9900, 9890, -1))

        ca4: CA[int] = CA(range(1, 10001))
        ca4_l_first100 = ca4.poplt(100)
        ca4_l_next100 = ca4.poplt(100)
        ca4_l_first10 = ca4.poplt(10)
        ca4_l_next10 = ca4.poplt(10)
        assert ca4_l_first100 == tuple(range(1, 101))
        assert ca4_l_next100 == tuple(range(101, 201))
        assert ca4_l_first10 == tuple(range(201, 211))
        assert ca4_l_next10 == tuple(range(211, 221))

        # Below seems to show CPython tuples are evaluated left to right
        ca5: CA[int] = CA(range(1, 10001))
        ca5_l_first100, ca5_l_next100, ca5_l_first10, ca5_l_next10 = (
            ca5.poplt(100),
            ca5.poplt(100),
            ca5.poplt(10),
            ca5.poplt(10),
        )
        assert ca5_l_first100 == tuple(range(1, 101))
        assert ca5_l_next100 == tuple(range(101, 201))
        assert ca5_l_first10 == tuple(range(201, 211))
        assert ca5_l_next10 == tuple(range(211, 221))

    def test_state_caching(self) -> None:
        """Guarantee test"""
        expected = ca(
            (0, 0),
            (0, 1),
            (0, 2),
            (0, 3),
            (0, 4),
            (1, 0),
            (1, 1),
            (1, 2),
            (1, 3),
            (1, 4),
            (1, 1),
            (2, 0),
            (2, 1),
            (2, 2),
            (2, 3),
            (2, 4),
            (2, 1),
            (3, 0),
            (3, 1),
            (3, 2),
            (3, 3),
            (3, 4),
            (3, 1),
            (3, 3),
            (4, 0),
            (4, 1),
            (4, 2),
            (4, 3),
            (4, 4),
            (4, 1),
            (4, 3),
        )
        foo = ca(0, 1, 2, 3, 4)
        bar = CA[tuple[int, int]]()

        for ii in foo:
            if ii % 2 == 1:
                foo.pushr(ii)
            for jj in foo:
                bar.pushr((ii, jj))

        assert bar == expected  # if foo were a list, outer loop above never returns

    def test_indexing(self) -> None:
        """Functionality test"""
        baz: CA[int] = ca()
        try:
            bar = baz[0]
            assert bar == 666
        except IndexError as err:
            assert isinstance(err, IndexError)
            assert not baz
        else:
            assert False

        foo = CA(range(1042)).map(lambda i: i * i)
        for ii in range(0, 1042):
            assert ii * ii == foo[ii]
        for ii in range(-1042, 0):
            assert foo[ii] == foo[1042 + ii]
        assert foo[0] == 0
        assert foo[1041] == 1041 * 1041
        assert foo[-1] == 1041 * 1041
        assert foo[-1042] == 0
        try:
            bar = foo[1042]
            assert bar == -1
        except IndexError as err:
            assert isinstance(err, IndexError)
        else:
            assert False
        try:
            bar = foo[-1043]
            assert bar == -1
        except IndexError as err:
            assert isinstance(err, IndexError)
        else:
            assert False
        try:
            bar = foo[0]
        except IndexError:
            assert False
        else:
            assert bar == 0

    def test_slicing(self) -> None:
        """Functionality test"""
        baz: CA[int] = ca()
        assert baz == CA[int]()
        assert baz[1:-1] == baz
        assert baz[42:666:17] == baz

        foo = CA(range(101))
        foo[5] = 666
        assert foo[5] == 666
        foo[10:21:5] = 42, 42, 42
        bar = foo[9:22]
        assert bar == ca(9, 42, 11, 12, 13, 14, 42, 16, 17, 18, 19, 42, 21)

        baz = CA(range(11))
        assert baz == ca(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        baz[5::2] = baz[0:3]
        assert baz == ca(0, 1, 2, 3, 4, 0, 6, 1, 8, 2, 10)
        baz[0:3] = baz[3:0:-1]
        assert baz == ca(3, 2, 1, 3, 4, 0, 6, 1, 8, 2, 10)
        del baz[6:10:2]
        assert baz == ca(3, 2, 1, 3, 4, 0, 1, 2, 10)
