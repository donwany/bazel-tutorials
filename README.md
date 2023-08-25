### Goal:
   - Bazel was then used to build the source code, 
   - run a unit test, and 
   - run the main application in the browser.

### Build Project
```shell
bazel build //calculator/...
```

### Test Project
```shell
bazel test //calculator/...
```

### Building and Running Application
```shell
bazel run //calculator:calc_test

bazel run //app:main
```

### EarthlyFile
  - All builds are self-contained, consistent, portable and language agnostic

### Install
```shell
brew install earthly && earthly 

earthly github.com/earthly/hello-world+hello
```
```shell
earthly +all
```

### References:
  - https://earthly.dev/
  - https://github.com/earthly/earthly
  - https://bazel.build/
  - https://github.com/kriscfoster/multi-language-bazel-monorepo/tree/main