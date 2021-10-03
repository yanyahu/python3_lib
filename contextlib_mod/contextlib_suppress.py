import contextlib


class NonFatalError(Exception):
    pass


def non_idempotent_operation():
    raise NonFatalError(
        'The operation failed because of existing state'
    )


with contextlib.suppress(NonFatalError):
    print('trying non-idempotent operation')
    non_idempotent_operation()
    print('succeeded!')

print('done')

"""
该try:except表单可以替换 contextlib.suppress()为更明确地抑制发生在with块中任何位置的一类异常。
"""
