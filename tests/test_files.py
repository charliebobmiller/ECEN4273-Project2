from pytest import mark


class TestFiles:
    def test_fail(self):
        assert 1 == 0

    def test_pass(self):
        assert 0 == 0

    @mark.skip("skip")
    def test_skip(self):
        pass
