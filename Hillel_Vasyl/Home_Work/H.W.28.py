def geom_prog(val, pas):
    yield val
    for item in range(10):
        result = val * pow(pas, item + 1)
        yield result


g = geom_prog(10, 3)
for i in g:
    print(i)


g = geom_prog(-2, -5)
for i in g:
    print(i)
