import re


def simplify_path(path):
    path_stack = []
    path = re.sub("/+", "/", path).rstrip("/")
    for filename in path.split("/"):
        if not filename: continue
        if filename == ".": continue
        if filename == "..":
            if path_stack: path_stack.pop()
            continue
        path_stack.append(filename)
    path = "/" + "/".join(path_stack)
    return path


if __name__ == "__main__":
    assert(simplify_path("/home//foo/") == "/home/foo")
    assert(simplify_path("/a/./b/../../c/") == "/c")
    assert(simplify_path("/../") == "/")
    print("All examples passed")