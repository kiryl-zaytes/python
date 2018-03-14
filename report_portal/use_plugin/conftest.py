import random

import pytest
pytest_plugins = 'pytest_plugin.pytest_erp_plugin'

@pytest.fixture(scope='class', autouse=True)
def class_fixture(request):
    print('class fixture')
    def gg():
        print('f')
    request.addfinalizer(gg)

@pytest.fixture(scope='module', autouse=True)
def module_fixture(request):
    print('module fixture')
    def end_module_fixture():
        print('f')
    request.addfinalizer(end_module_fixture)

@pytest.fixture(scope='session')
def get_smth(request):
    """
    Super global fixture
    :param request:
    :return:
    """
    def end_get_smth():
        print('fff')
    request.addfinalizer(end_get_smth)
    return random.randint(1,100)


@pytest.fixture()
def not_usefull_feature(request):
    print('not usefull feature')
    def not_usefull_feature_end():
        print('finalizer feature')
    request.addfinalizer(not_usefull_feature_end)

@pytest.fixture(scope='function')
def usefull_fixture(request, get_smth): #not_usefull_feature
    print('usefull feature')
    def usefull_fixture_end():
        print('finalizer feature')
    request.addfinalizer(usefull_fixture_end)

@pytest.fixture(scope='function', autouse=True)
def autouse_feature(request):
    def finita():
        """
        teardown autouse f
        """
        print('fff')
    request.addfinalizer(finita)
    assert 1==1

@pytest.fixture(scope='session', autouse=True)
def autouse_class_feature(request):
    """
    Other one super global
    """
    def autouse_class_feature_final():
        print('fefe')
    request.addfinalizer(autouse_class_feature_final)
    print('fixture tesxt')
    return random.randint(1,100)

