# GLFW for Py++
a [Py++](https://pypp-docs.readthedocs.io/) library for GLFW

## Examples
### Opening a window
With this library installed, the following Py++ code works to open a window. This is the typical example given in the docs for the glfw C++ and Python libraries.

```python
from pypp_glfw import glfw, GLFWwindowPtr
from pypp_python import to_c_string, NULL


def glfw_test():
    if not glfw.init():
        raise Exception("Failed to initialize GLFW")

    window: GLFWwindowPtr = glfw.create_window(
        640, 480, to_c_string("Hello World"), NULL, NULL
    )
    if not window:
        glfw.terminate()
        raise Exception("Failed to create GLFW window")

    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        # Render here, e.g. using pyOpenGL

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    glfw_test()
```

### Opening a window and handling inputs
```python
from pypp_glfw import glfw, GLFWwindowPtr
from pypp_python import to_c_string, NULL


def key_callback(
    _window: GLFWwindowPtr, key: int, _scancode: int, action: int, _mods: int
):
    if action == glfw.PRESS:
        print(f"Key {key} pressed")
    elif action == glfw.RELEASE:
        print(f"Key {key} released")


def mouse_button_callback(_window: GLFWwindowPtr, button: int, action: int, _mods: int):
    if action == glfw.PRESS:
        print(f"Mouse button {button} pressed")
    elif action == glfw.RELEASE:
        print(f"Mouse button {button} released")


def cursor_position_callback(_window: GLFWwindowPtr, xpos: float, ypos: float):
    print(f"Mouse moved to ({xpos}, {ypos})")


def glfw_test_2():
    if not glfw.init():
        raise Exception("Failed to initialize GLFW")

    window: GLFWwindowPtr = glfw.create_window(
        640, 480, to_c_string("Hello World"), NULL, NULL
    )
    if not window:
        glfw.terminate()
        raise Exception("Failed to create GLFW window")

    glfw.make_context_current(window)

    glfw.set_key_callback(window, key_callback)
    glfw.set_mouse_button_callback(window, mouse_button_callback)
    glfw.set_cursor_pos_callback(window, cursor_position_callback)

    while not glfw.window_should_close(window):
        # Render here, e.g. using pyOpenGL

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    glfw_test_2()
```

## API

For the API, refer to [pyGLFW](https://github.com/FlorianRhiem/pyGLFW).

## Supported GLFW attributes and functions

Only the attributes and functions which are shown in the above examples are tested. However, its very likely that others will work also, and you will most easily find out by trying them in your code.

When you find an attribute or function which does not work, it would be really helpful if you submit a feature request with title `support for glfw.<some_name>`. Thanks in advance for if you do that.

## Bug reports

Report bugs to the Issues tab on this github repo using the `bug` label.

## Feature requests

Submit feature requests to the Issues tab on this github repo using the `feature request` label.
