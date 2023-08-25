test:
	bazel test //calculator/...
test2:
	bazel test //calculator:calc_test

build:
	 bazel build --package_path .
builder:
	bazel build //calculator/...

run:
	bazel run //calculator:calc_test
main:
	bazel run //app:main