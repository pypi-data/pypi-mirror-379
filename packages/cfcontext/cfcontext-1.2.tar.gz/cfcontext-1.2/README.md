# cfcontext

`cfcontext` is a lightweight library for managing shared contexts within a Python application. It allows you to create, replace, and handle dynamic contextual objects that are inherited across the call stack frames, ensuring consistency throughout nested function calls and asynchronous tasks.

## Installation

```bash
pip install cfcontext
```

## Features

- **Shared Context Management**: A global context can be created and accessed anywhere in your application.
- **Context Inheritance**: Contexts are inherited across the call stack, so child functions and tasks can automatically access the parent context.
- **Unlinked Contexts**: Create separate contexts to avoid conflicts or temporarily replace the current context.
- **Asynchronous Support**: Manage context within async tasks, ensuring consistent shared data.

## Usage

### 1. Creating and Using a Context

The context can be initialized with specific attributes:

```python
from cfcontext import Context

ctx = Context(abc=123)
print(ctx.abc)  # 123
```

Once created, the context can be accessed anywhere in your code, even in nested functions:

```python
def some_function():
    print(Context().abc)  # 123

some_function()
```

### 2. Creating a Separate Context

You can create a distinct, unlinked context using the `__create_only` parameter:

```python
ctx1 = Context(oi='io')
ctx2 = Context.create()

print(ctx1.oi)  # 'io'
print(ctx2.oi)  # None
```

### 3. Replacing the Current Context

To temporarily replace the current context with another one:

```python
ctx = Context.create()
ctx.abc = 123456
replace_context(ctx)

print(Context().abc)  # 123456
```

### 4. Using with Asynchronous Tasks

`cfcontext` manages context within async tasks, inheriting context values even in concurrent environments. Contextual data is shared and can be modified across different tasks:

```python
import asyncio
from cfcontext import Context

async def async_task(a, b, n):
    Context(n=n)
    assert Context().a == a
    assert Context().b == b
    Context().b = 'Ok!'

async def async_main(a):
    Context(a=2, b='Ok')
    await async_task(2, 'Ok', 0)
    t1 = asyncio.create_task(async_task(a, None, 1))
    t2 = asyncio.create_task(async_task(2, 'Ok', 2), context=Context())
    await asyncio.sleep(1)

Context(a=1)
asyncio.run(async_main(1))
print(Context().a)  # 1
```

### 5. Tests

The library is tested with scenarios covering linked, unlinked, and asynchronous context management. To run the tests:

```bash
pytest tests.py
```