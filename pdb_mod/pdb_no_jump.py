def f(n):
    if n < 0:
        raise ValueError('Invalid n: {}'.format(n))
    result = []
    j = 0
    for i in range(n):
        j = i * n + j
        j += n
        result.append(j)
    return result


if __name__ == '__main__':
    try:
        print(f(5))
    finally:
        print('Always printed')

    try:
        print(f(-5))
    except Exception as e:
        print('There was an error')
    else:
        print('There was no error')

    print('Last statement')
