from demo import app


class TestSound:
    def test_dog(self):
        got = app.sound(app.Animal.dog)
        want = "bark"
        assert got == want

    def test_cat(self):
        got = app.sound(app.Animal.cat)
        want = "meow"
        assert got == want
