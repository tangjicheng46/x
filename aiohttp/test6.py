def generate_sequence(start, end):
    while start <= end:
        yield start * start
        start += 1

start_value = 3
end_value = 7

g = generate_sequence(start_value, end_value)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# print(next(g))

# for num in g:
#     print(num)
