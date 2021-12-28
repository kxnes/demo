from demo import app


class TestSound(object):
    def test_dog(self) -> None:
        got = app.sound(app.Animal.dog)
        want = 'bark'
        assert got == want

    def test_cat(self) -> None:
        got = app.sound(app.Animal.cat)
        want = 'meow'
        assert got == want
