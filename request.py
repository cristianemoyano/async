from tasks import add

for i in range(0, 100):
    add.apply_async((i, 2))
