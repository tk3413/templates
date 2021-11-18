# python3 generic code template

## description

generic template repository to include the following:

- [x] unit test suite
- [x] end to end test suite
- [ ] logger
- [x] linter
- [ ] script to package module

## local setup

linux:
```
pip3 install virtualenv --user
python3 -m virtualenv venv
make install
```

## unit tests
```
make utest
```

## end to end tests
```
make etest
```

## lint
```
make lint
```
