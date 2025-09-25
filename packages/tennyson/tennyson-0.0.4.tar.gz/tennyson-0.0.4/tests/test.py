#!/usr/bin/env python3
import os
import tempfile
from click.testing import CliRunner

from tennyson import *
import tennyson.cli
import tennyson.password


class TestPrinting:

    def test_logger(self):
        log = mklog()
        assert log.name in ['<unknown>', __file__]
        log = mklog('asdf')
        assert log.name == 'asdf'

    def test_timestamps_run(self):
        date_stamp()
        datetime_stamp()
        datetime_zone_stamp()

    def test_atomic_write(self):
        pass


class TestEmail:

    def test_email(self):
        if os.environ.get('TEST_SEND_EMAILS', False):
            send_email_exn(recipients=['tennysontaylorbardwell@gmail.com'],
                           subject='Test 1/3', text='Test 1/3')
            alert_exn(message='Test 2/3', subject='Test 2/3')
            try:
                raise RuntimeError('Test 3/3')
            except Exception as e:
                error_email_exn(e)


class TestSafety:

    def test_atomic_write(self):
        with tempfile.TemporaryDirectory() as dir_:
            a = os.path.join(dir_, 'a')
            b = os.path.join(dir_, 'b')

            with open_atomic(a, 'w') as fp:
                fp.write('abc')
            with open(a) as fp:
                assert fp.read() == 'abc'

            try:
                with open_atomic(b, 'w') as fp:
                    fp.write('abc')
                    raise RuntimeError()
            except RuntimeError:
                assert not os.path.isfile(b)

            try:
                with open_atomic(a, 'w') as fp:
                    fp.write('xyz')
                    raise RuntimeError()
            except RuntimeError:
                with open(a) as fp:
                    assert fp.read() == 'abc'

    # def test_time_limit(self):
    #     time_limit()
    #     try:
    #         pass
    #     except TimeoutException:
    #         pass


class TestCommon:

    def test_mkdir_p(self):
        with tempfile.TemporaryDirectory() as dir_:
            d = os.path.join(dir_, 'a', 'b', 'c', 'd')
            assert not os.path.isdir(d)
            mkdir_p(d)
            assert os.path.isdir(d)

    def test_json(self):
        with tempfile.TemporaryDirectory() as dir_:
            f = os.path.join(dir_, 'a.json')
            o = ['a', 'b']
            j_dump(o, f)
            assert j_load(f) == o


class TestConfigAndSecrets:

    def test_get_config(self):
        assert type(get_config()) == dict

    # def test_get_settings(self):
    #     assert type(get_secrets()) == dict


class TestPassword:

    def test_password(self):
        tennyson.password.password()


class TestCLI:

    def test_entry_point(self):
        runner = CliRunner()
        result = runner.invoke(tennyson.cli.main, ['--help'])
        assert result.exit_code == 0
        result = runner.invoke(tennyson.cli.main, ['password'])
        assert result.exit_code == 0
