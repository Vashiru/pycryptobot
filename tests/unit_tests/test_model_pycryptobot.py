import json, os, pytest, sys

sys.path.append('.')
# pylint: disable=import-error
from models.PyCryptoBot import PyCryptoBot

def test_instantiate_model_without_error():
    if not os.path.exists('config.json'):

#        this is now covered by creating config.json by default
#        with pytest.raises(ValueError) as execinfo:
#            PyCryptoBot()
#        assert str(execinfo.value) == "Invalid config.json: [Errno 2] No such file or directory: 'config.json'"

        config = {
            "binance": {
                "api_url": "https://api.binance.com",
                "api_key": "0000000000000000000000000000000000000000000000000000000000000000",
                "api_secret": "0000000000000000000000000000000000000000000000000000000000000000",
            },
            "coinbasepro": {
                "api_url": "https://api.pro.coinbase.com",
                "api_key": "00000000000000000000000000000000",
                "api_secret": "0000/0000000000/0000000000000000000000000000000000000000000000000000000000/00000000000==",
                "api_passphrase": "00000000000"
            }
        }

        try:
            config_json = json.dumps(config, indent=4)
            fh = open('config.json', 'w')
            fh.write(config_json)
            fh.close()
        except Exception as err:
            print (err)

    app = PyCryptoBot()
    assert type(app) is PyCryptoBot

    with open('config.json', 'r') as fh:
        config = fh.read()
        config_json = json.loads(config)

        if 'binance' in config_json:
            app = PyCryptoBot(exchange='binance')
            assert type(app) is PyCryptoBot
            assert app.getExchange() == 'binance'

        if 'coinbasepro' in config_json:
            app = PyCryptoBot(exchange='coinbasepro')
            assert type(app) is PyCryptoBot
            assert app.getExchange() == 'coinbasepro'

        if 'dummy' in config_json:
            app = PyCryptoBot(exchange='dummy')
            assert type(app) is PyCryptoBot
            assert app.getExchange() == 'dummy'

    app = PyCryptoBot(filename='config.json')
    assert type(app) is PyCryptoBot

def test_configjson_binance():
    config = {
        "binance": {
            "api_url": "https://api.binance.com",
            "api_key": "0000000000000000000000000000000000000000000000000000000000000000",
            "api_secret": "0000000000000000000000000000000000000000000000000000000000000000",
        }
    }

    try:
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.getExchange() == 'binance'

    if os.path.exists('tests/unit_tests/data/pycryptobot_pytest_config.json'):
        os.remove('tests/unit_tests/data/pycryptobot_pytest_config.json')

def test_configjson_binance_invalid_api_url():
    config = {
        "binance": {
            "api_url": "ERROR",
            "api_key": "0000000000000000000000000000000000000000000000000000000000000000",
            "api_secret": "0000000000000000000000000000000000000000000000000000000000000000",
        }
    }

    try:
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    with pytest.raises(ValueError) as execinfo:
        PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert str(execinfo.value) == 'Invalid config.json: Binance API URL is invalid'

    if os.path.exists('tests/unit_tests/data/pycryptobot_pytest_config.json'):
        os.remove('tests/unit_tests/data/pycryptobot_pytest_config.json')

def test_configjson_binance_invalid_api_key():
    config = {
        "binance": {
            "api_url": "https://api.binance.com",
            "api_key": "ERROR",
            "api_secret": "0000000000000000000000000000000000000000000000000000000000000000",
        }
    }

    try:
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    with pytest.raises(TypeError) as execinfo:
        PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert str(execinfo.value) == 'Binance API key is invalid'

    if os.path.exists('tests/unit_tests/data/pycryptobot_pytest_config.json'):
        os.remove('tests/unit_tests/data/pycryptobot_pytest_config.json')

def test_configjson_binance_invalid_api_secret():
    config = {
        "binance": {
            "api_url": "https://api.binance.com",
            "api_key": "0000000000000000000000000000000000000000000000000000000000000000",
            "api_secret": "ERROR",
        }
    }

    try:
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    with pytest.raises(TypeError) as execinfo:
        PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert str(execinfo.value) == 'Binance API secret is invalid'

    if os.path.exists('tests/unit_tests/data/pycryptobot_pytest_config.json'):
        os.remove('tests/unit_tests/data/pycryptobot_pytest_config.json')

def test_configjson_coinbasepro():
    config = {
        "coinbasepro": {
            "api_url": "https://api.pro.coinbase.com",
            "api_key": "00000000000000000000000000000000",
            "api_secret": "0000/0000000000/0000000000000000000000000000000000000000000000000000000000/00000000000==",
            "api_passphrase": "00000000000"
        }
    }

    try:
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.getExchange() == 'coinbasepro'

    if os.path.exists('tests/unit_tests/data/pycryptobot_pytest_config.json'):
        os.remove('tests/unit_tests/data/pycryptobot_pytest_config.json')

def test_configjson_coinbasepro_legacy():
    config = {
        "api_url": "https://api.pro.coinbase.com",
        "api_key": "00000000000000000000000000000000",
        "api_secret": "0000/0000000000/0000000000000000000000000000000000000000000000000000000000/00000000000==",
        "api_passphrase": "00000000000"
    }

    try:
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.getExchange() == 'coinbasepro'

    if os.path.exists('tests/unit_tests/data/pycryptobot_pytest_config.json'):
        os.remove('tests/unit_tests/data/pycryptobot_pytest_config.json')

def test_configjson_coinbasepro_invalid_api_url():
    config = {
        "coinbasepro": {
            "api_url": "ERROR",
            "api_key": "00000000000000000000000000000000",
            "api_secret": "0000/0000000000/0000000000000000000000000000000000000000000000000000000000/00000000000==",
            "api_passphrase": "00000000000"
        }
    }

    try:
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    with pytest.raises(ValueError) as execinfo:
        PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert str(execinfo.value) == 'Invalid config.json: Coinbase Pro API URL is invalid'

    if os.path.exists('tests/unit_tests/data/pycryptobot_pytest_config.json'):
        os.remove('tests/unit_tests/data/pycryptobot_pytest_config.json')

def test_configjson_coinbasepro_invalid_api_key():
    config = {
        "coinbasepro": {
            "api_url": "https://api.pro.coinbase.com",
            "api_key": "ERROR",
            "api_secret": "0000/0000000000/0000000000000000000000000000000000000000000000000000000000/00000000000==",
            "api_passphrase": "00000000000"
        }
    }

    try:
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    with pytest.raises(TypeError) as execinfo:
        PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert str(execinfo.value) == 'Coinbase Pro API key is invalid'

    if os.path.exists('tests/unit_tests/data/pycryptobot_pytest_config.json'):
        os.remove('tests/unit_tests/data/pycryptobot_pytest_config.json')

def test_configjson_coinbasepro_invalid_api_secret():
    config = {
        "coinbasepro": {
            "api_url": "https://api.pro.coinbase.com",
            "api_key": "00000000000000000000000000000000",
            "api_secret": "ERROR",
            "api_passphrase": "00000000000"
        }
    }

    try:
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    with pytest.raises(TypeError) as execinfo:
        PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert str(execinfo.value) == 'Coinbase Pro API secret is invalid'

    if os.path.exists('tests/unit_tests/data/pycryptobot_pytest_config.json'):
        os.remove('tests/unit_tests/data/pycryptobot_pytest_config.json')

def test_configjson_coinbasepro_invalid_api_passphrase():
    config = {
        "coinbasepro": {
            "api_url": "https://api.pro.coinbase.com",
            "api_key": "00000000000000000000000000000000",
            "api_secret": "0000/0000000000/0000000000000000000000000000000000000000000000000000000000/00000000000==",
            "api_passphrase": "ERROR"
        }
    }

    try:
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    with pytest.raises(TypeError) as execinfo:
        PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert str(execinfo.value) == 'Coinbase Pro API passphrase is invalid'

    if os.path.exists('tests/unit_tests/data/pycryptobot_pytest_config.json'):
        os.remove('tests/unit_tests/data/pycryptobot_pytest_config.json')

def test_configjson_binance_granularity():
    config = {
       "binance": {
            "api_url": "https://api.binance.com",
            "api_key": "0000000000000000000000000000000000000000000000000000000000000000",
            "api_secret": "0000000000000000000000000000000000000000000000000000000000000000",
            "config": {}
        }
    }

    try:
        granularity = '1m'
        config['binance']['config']['granularity'] = granularity
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()

        app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
        assert type(app) is PyCryptoBot
        assert app.getExchange() == 'binance'
        assert app.getGranularity() == 60

        if os.path.exists('tests/unit_tests/data/pycryptobot_pytest_config.json'):
            os.remove('tests/unit_tests/data/pycryptobot_pytest_config.json')
    except Exception as err:
        print (err)

    try:
        granularity = '5m'
        config['binance']['config']['granularity'] = granularity
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()

        app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
        assert type(app) is PyCryptoBot
        assert app.getExchange() == 'binance'
        assert app.getGranularity() == 300

        if os.path.exists('tests/unit_tests/data/pycryptobot_pytest_config.json'):
            os.remove('tests/unit_tests/data/pycryptobot_pytest_config.json')
    except Exception as err:
        print (err)

    try:
        granularity = '15m'
        config['binance']['config']['granularity'] = granularity
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()

        app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
        assert type(app) is PyCryptoBot
        assert app.getExchange() == 'binance'
        assert app.getGranularity() == 900

        if os.path.exists('tests/unit_tests/data/pycryptobot_pytest_config.json'):
            os.remove('tests/unit_tests/data/pycryptobot_pytest_config.json')
    except Exception as err:
        print (err)

    try:
        granularity = '1h'
        config['binance']['config']['granularity'] = granularity
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()

        app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
        assert type(app) is PyCryptoBot
        assert app.getExchange() == 'binance'
        assert app.getGranularity() == 3600

        if os.path.exists('tests/unit_tests/data/pycryptobot_pytest_config.json'):
            os.remove('tests/unit_tests/data/pycryptobot_pytest_config.json')
    except Exception as err:
        print (err)

    try:
        granularity = '6h'
        config['binance']['config']['granularity'] = granularity
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()

        app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
        assert type(app) is PyCryptoBot
        assert app.getExchange() == 'binance'
        assert app.getGranularity() == 21600

        if os.path.exists('tests/unit_tests/data/pycryptobot_pytest_config.json'):
            os.remove('tests/unit_tests/data/pycryptobot_pytest_config.json')
    except Exception as err:
        print (err)

    try:
        granularity = '1d'
        config['binance']['config']['granularity'] = granularity
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()

        app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
        assert type(app) is PyCryptoBot
        assert app.getExchange() == 'binance'
        assert app.getGranularity() == 86400

        if os.path.exists('tests/unit_tests/data/pycryptobot_pytest_config.json'):
            os.remove('tests/unit_tests/data/pycryptobot_pytest_config.json')
    except Exception as err:
        print (err)

def test_configjson_binance_invalid_granularity():
    config = {
       "binance": {
            "api_url": "https://api.binance.com",
            "api_key": "0000000000000000000000000000000000000000000000000000000000000000",
            "api_secret": "0000000000000000000000000000000000000000000000000000000000000000",
            "config": {}
        }
    }

    try:
        config['binance']['config']['granularity'] = 60
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.getExchange() == 'binance'
    assert app.getGranularity() == 3600 # default if invalid

    if os.path.exists('tests/unit_tests/data/pycryptobot_pytest_config.json'):
        os.remove('tests/unit_tests/data/pycryptobot_pytest_config.json')

def test_configjson_coinbasepro_granularity():
    config = {
        "coinbasepro": {
            "api_url": "https://api.pro.coinbase.com",
            "api_key": "00000000000000000000000000000000",
            "api_secret": "0000/0000000000/0000000000000000000000000000000000000000000000000000000000/00000000000==",
            "api_passphrase": "00000000000",
            "config": {}
        }
    }

    try:
        granularity = 60
        config['coinbasepro']['config']['granularity'] = granularity
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()

        app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
        assert type(app) is PyCryptoBot
        assert app.getExchange() == 'coinbasepro'
        assert app.getGranularity() == granularity

        if os.path.exists('tests/unit_tests/data/pycryptobot_pytest_config.json'):
            os.remove('tests/unit_tests/data/pycryptobot_pytest_config.json')
    except Exception as err:
        print (err)

    try:
        granularity = 300
        config['coinbasepro']['config']['granularity'] = granularity
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()

        app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
        assert type(app) is PyCryptoBot
        assert app.getExchange() == 'coinbasepro'
        assert app.getGranularity() == granularity

        if os.path.exists('tests/unit_tests/data/pycryptobot_pytest_config.json'):
            os.remove('tests/unit_tests/data/pycryptobot_pytest_config.json')
    except Exception as err:
        print (err)

    try:
        granularity = 900
        config['coinbasepro']['config']['granularity'] = granularity
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()

        app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
        assert type(app) is PyCryptoBot
        assert app.getExchange() == 'coinbasepro'
        assert app.getGranularity() == granularity

        if os.path.exists('tests/unit_tests/data/pycryptobot_pytest_config.json'):
            os.remove('tests/unit_tests/data/pycryptobot_pytest_config.json')
    except Exception as err:
        print (err)

    try:
        granularity = 3600
        config['coinbasepro']['config']['granularity'] = granularity
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()

        app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
        assert type(app) is PyCryptoBot
        assert app.getExchange() == 'coinbasepro'
        assert app.getGranularity() == granularity

        if os.path.exists('tests/unit_tests/data/pycryptobot_pytest_config.json'):
            os.remove('tests/unit_tests/data/pycryptobot_pytest_config.json')
    except Exception as err:
        print (err)

    try:
        granularity = 21600
        config['coinbasepro']['config']['granularity'] = granularity
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()

        app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
        assert type(app) is PyCryptoBot
        assert app.getExchange() == 'coinbasepro'
        assert app.getGranularity() == granularity

        if os.path.exists('tests/unit_tests/data/pycryptobot_pytest_config.json'):
            os.remove('tests/unit_tests/data/pycryptobot_pytest_config.json')
    except Exception as err:
        print (err)

    try:
        granularity = 86400
        config['coinbasepro']['config']['granularity'] = granularity
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()

        app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
        assert type(app) is PyCryptoBot
        assert app.getExchange() == 'coinbasepro'
        assert app.getGranularity() == granularity

        if os.path.exists('tests/unit_tests/data/pycryptobot_pytest_config.json'):
            os.remove('tests/unit_tests/data/pycryptobot_pytest_config.json')
    except Exception as err:
        print (err)

def test_configjson_coinbasepro_invalid_granularity():
    config = {
        "coinbasepro": {
            "api_url": "https://api.pro.coinbase.com",
            "api_key": "00000000000000000000000000000000",
            "api_secret": "0000/0000000000/0000000000000000000000000000000000000000000000000000000000/00000000000==",
            "api_passphrase": "00000000000",
            "config": {}
        }
    }

    try:
        config['coinbasepro']['config']['granularity'] = '1m'
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.getExchange() == 'coinbasepro'
    assert app.getGranularity() == 3600 # default if invalid

    if os.path.exists('tests/unit_tests/data/pycryptobot_pytest_config.json'):
        os.remove('tests/unit_tests/data/pycryptobot_pytest_config.json')

def test_configjson_binance_islive():
    config = {
       "binance": {
            "api_url": "https://api.binance.com",
            "api_key": "0000000000000000000000000000000000000000000000000000000000000000",
            "api_secret": "0000000000000000000000000000000000000000000000000000000000000000",
            "config": {}
        }
    }

    try:
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.getExchange() == 'binance'
    assert not app.isLive()

    try:
        config['binance']['config']['live'] = 1
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.isLive()

    app.setLive(0)
    assert not app.isLive()

    if os.path.exists('tests/unit_tests/data/pycryptobot_pytest_config.json'):
        os.remove('tests/unit_tests/data/pycryptobot_pytest_config.json')

def test_configjson_coinbasepro_islive():
    config = {
        "coinbasepro": {
            "api_url": "https://api.pro.coinbase.com",
            "api_key": "00000000000000000000000000000000",
            "api_secret": "0000/0000000000/0000000000000000000000000000000000000000000000000000000000/00000000000==",
            "api_passphrase": "00000000000",
            "config": {}
        }
    }

    try:
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.getExchange() == 'coinbasepro'
    assert not app.isLive()

    try:
        config['coinbasepro']['config']['live'] = 1
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.isLive()

    app.setLive(0)
    assert not app.isLive()

    if os.path.exists('tests/unit_tests/data/pycryptobot_pytest_config.json'):
        os.remove('tests/unit_tests/data/pycryptobot_pytest_config.json')

def test_configjson_binance_graphs():
    config = {
       "binance": {
            "api_url": "https://api.binance.com",
            "api_key": "0000000000000000000000000000000000000000000000000000000000000000",
            "api_secret": "0000000000000000000000000000000000000000000000000000000000000000",
            "config": {}
        }
    }

    try:
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.getExchange() == 'binance'
    assert not app.shouldSaveGraphs()

    try:
        config['binance']['config']['graphs'] = 1
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.getExchange() == 'binance'
    assert app.shouldSaveGraphs()

    if os.path.exists('tests/unit_tests/data/pycryptobot_pytest_config.json'):
        os.remove('tests/unit_tests/data/pycryptobot_pytest_config.json')

def test_configjson_coinbasepro_graphs():
    config = {
        "coinbasepro": {
            "api_url": "https://api.pro.coinbase.com",
            "api_key": "00000000000000000000000000000000",
            "api_secret": "0000/0000000000/0000000000000000000000000000000000000000000000000000000000/00000000000==",
            "api_passphrase": "00000000000",
            "config": {}
        }
    }

    try:
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.getExchange() == 'coinbasepro'
    assert not app.shouldSaveGraphs()

    try:
        config['coinbasepro']['config']['graphs'] = 1
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.getExchange() == 'coinbasepro'
    assert app.shouldSaveGraphs()

    if os.path.exists('tests/unit_tests/data/pycryptobot_pytest_config.json'):
        os.remove('tests/unit_tests/data/pycryptobot_pytest_config.json')

def test_configjson_binance_isverbose():
    config = {
       "binance": {
            "api_url": "https://api.binance.com",
            "api_key": "0000000000000000000000000000000000000000000000000000000000000000",
            "api_secret": "0000000000000000000000000000000000000000000000000000000000000000",
            "config": {}
        }
    }

    try:
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.getExchange() == 'binance'
    assert not app.isVerbose()

    try:
        config['binance']['config']['verbose'] = 1
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.getExchange() == 'binance'
    assert app.isVerbose()

    if os.path.exists('tests/unit_tests/data/pycryptobot_pytest_config.json'):
        os.remove('tests/unit_tests/data/pycryptobot_pytest_config.json')

def test_configjson_coinbasepro_isverbose():
    config = {
        "coinbasepro": {
            "api_url": "https://api.pro.coinbase.com",
            "api_key": "00000000000000000000000000000000",
            "api_secret": "0000/0000000000/0000000000000000000000000000000000000000000000000000000000/00000000000==",
            "api_passphrase": "00000000000",
            "config": {}
        }
    }

    try:
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.getExchange() == 'coinbasepro'
    assert not app.isVerbose()

    try:
        config['coinbasepro']['config']['verbose'] = 1
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.getExchange() == 'coinbasepro'
    assert app.isVerbose()

    if os.path.exists('tests/unit_tests/data/pycryptobot_pytest_config.json'):
        os.remove('tests/unit_tests/data/pycryptobot_pytest_config.json')

def test_configjson_binance_sellatloss():
    config = {
       "binance": {
            "api_url": "https://api.binance.com",
            "api_key": "0000000000000000000000000000000000000000000000000000000000000000",
            "api_secret": "0000000000000000000000000000000000000000000000000000000000000000",
            "config": {}
        }
    }

    try:
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.getExchange() == 'binance'
    assert app.allowSellAtLoss()

    try:
        config['binance']['config']['sellatloss'] = 0
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.getExchange() == 'binance'
    assert not app.allowSellAtLoss()

    if os.path.exists('tests/unit_tests/data/pycryptobot_pytest_config.json'):
        os.remove('tests/unit_tests/data/pycryptobot_pytest_config.json')

def test_configjson_coinbasepro_sellatloss():
    config = {
        "coinbasepro": {
            "api_url": "https://api.pro.coinbase.com",
            "api_key": "00000000000000000000000000000000",
            "api_secret": "0000/0000000000/0000000000000000000000000000000000000000000000000000000000/00000000000==",
            "api_passphrase": "00000000000",
            "config": {}
        }
    }

    try:
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.getExchange() == 'coinbasepro'
    assert app.allowSellAtLoss()

    try:
        config['coinbasepro']['config']['sellatloss'] = 0
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.getExchange() == 'coinbasepro'
    assert not app.allowSellAtLoss()

    if os.path.exists('tests/unit_tests/data/pycryptobot_pytest_config.json'):
        os.remove('tests/unit_tests/data/pycryptobot_pytest_config.json')

def test_configjson_binance_sellupperpcnt():
    config = {
       "binance": {
            "api_url": "https://api.binance.com",
            "api_key": "0000000000000000000000000000000000000000000000000000000000000000",
            "api_secret": "0000000000000000000000000000000000000000000000000000000000000000",
            "config": {}
        }
    }

    try:
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.getExchange() == 'binance'
    assert app.sellUpperPcnt() is None

    try:
        config['binance']['config']['sellupperpcnt'] = 10
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.getExchange() == 'binance'
    assert type(app.sellUpperPcnt() == 'float')
    assert app.sellUpperPcnt() == 10

    try:
        config['binance']['config']['sellupperpcnt'] = '10.5'
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.getExchange() == 'binance'
    assert type(app.sellUpperPcnt() == 'float')
    assert app.sellUpperPcnt() == 10.5

    if os.path.exists('tests/unit_tests/data/pycryptobot_pytest_config.json'):
        os.remove('tests/unit_tests/data/pycryptobot_pytest_config.json')

    try:
        config['binance']['config']['sellupperpcnt'] = -0.1
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    with pytest.raises(ValueError) as execinfo:
        PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert str(execinfo.value) == 'Invalid config.json: sellupperpcnt must be positive'

    try:
        config['binance']['config']['sellupperpcnt'] = '-0.2'
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    with pytest.raises(ValueError) as execinfo:
        PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert str(execinfo.value) == 'Invalid config.json: sellupperpcnt must be positive'

    try:
        config['binance']['config']['sellupperpcnt'] = 0
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    with pytest.raises(ValueError) as execinfo:
        PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert str(execinfo.value) == 'Invalid config.json: sellupperpcnt must be positive'

    try:
        config['binance']['config']['sellupperpcnt'] = -1
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    with pytest.raises(ValueError) as execinfo:
        PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert str(execinfo.value) == 'Invalid config.json: sellupperpcnt must be positive'

def test_configjson_coinbasepro_sellupperpcnt():
    config = {
        "coinbasepro": {
            "api_url": "https://api.pro.coinbase.com",
            "api_key": "00000000000000000000000000000000",
            "api_secret": "0000/0000000000/0000000000000000000000000000000000000000000000000000000000/00000000000==",
            "api_passphrase": "00000000000",
            "config": {}
        }
    }

    try:
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.getExchange() == 'coinbasepro'
    assert app.sellUpperPcnt() is None

    try:
        config['coinbasepro']['config']['sellupperpcnt'] = 10
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.getExchange() == 'coinbasepro'
    assert type(app.sellUpperPcnt() == 'float')
    assert app.sellUpperPcnt() == 10

    try:
        config['coinbasepro']['config']['sellupperpcnt'] = '10.5'
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.getExchange() == 'coinbasepro'
    assert type(app.sellUpperPcnt() == 'float')
    assert app.sellUpperPcnt() == 10.5

    if os.path.exists('tests/unit_tests/data/pycryptobot_pytest_config.json'):
        os.remove('tests/unit_tests/data/pycryptobot_pytest_config.json')

    try:
        config['coinbasepro']['config']['sellupperpcnt'] = -0.1
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    with pytest.raises(ValueError) as execinfo:
        PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert str(execinfo.value) == 'Invalid config.json: sellupperpcnt must be positive'

    try:
        config['coinbasepro']['config']['sellupperpcnt'] = '-0.2'
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    with pytest.raises(ValueError) as execinfo:
        PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert str(execinfo.value) == 'Invalid config.json: sellupperpcnt must be positive'

    try:
        config['coinbasepro']['config']['sellupperpcnt'] = 0
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    with pytest.raises(ValueError) as execinfo:
        PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert str(execinfo.value) == 'Invalid config.json: sellupperpcnt must be positive'

    try:
        config['coinbasepro']['config']['sellupperpcnt'] = -1
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    with pytest.raises(ValueError) as execinfo:
        PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert str(execinfo.value) == 'Invalid config.json: sellupperpcnt must be positive'

def test_configjson_binance_selllowerpcnt():
    config = {
       "binance": {
            "api_url": "https://api.binance.com",
            "api_key": "0000000000000000000000000000000000000000000000000000000000000000",
            "api_secret": "0000000000000000000000000000000000000000000000000000000000000000",
            "config": {}
        }
    }

    try:
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.getExchange() == 'binance'
    assert app.sellLowerPcnt() is None

    try:
        config['binance']['config']['selllowerpcnt'] = -10
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.getExchange() == 'binance'
    assert type(app.sellLowerPcnt() == 'float')
    assert app.sellLowerPcnt() == -10

    try:
        config['binance']['config']['selllowerpcnt'] = '-10.5'
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.getExchange() == 'binance'
    assert type(app.sellLowerPcnt() == 'float')
    assert app.sellLowerPcnt() == -10.5

    if os.path.exists('tests/unit_tests/data/pycryptobot_pytest_config.json'):
        os.remove('tests/unit_tests/data/pycryptobot_pytest_config.json')

    try:
        config['binance']['config']['selllowerpcnt'] = 0.1
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    with pytest.raises(ValueError) as execinfo:
        PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert str(execinfo.value) == 'Invalid config.json: selllowerpcnt must be negative'

    try:
        config['binance']['config']['selllowerpcnt'] = '0.2'
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    with pytest.raises(ValueError) as execinfo:
        PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert str(execinfo.value) == 'Invalid config.json: selllowerpcnt must be negative'

    try:
        config['binance']['config']['selllowerpcnt'] = 0
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    with pytest.raises(ValueError) as execinfo:
        PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert str(execinfo.value) == 'Invalid config.json: selllowerpcnt must be negative'

    try:
        config['binance']['config']['selllowerpcnt'] = 1
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    with pytest.raises(ValueError) as execinfo:
        PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert str(execinfo.value) == 'Invalid config.json: selllowerpcnt must be negative'

def test_configjson_coinbasepro_selllowerpcnt():
    config = {
        "coinbasepro": {
            "api_url": "https://api.pro.coinbase.com",
            "api_key": "00000000000000000000000000000000",
            "api_secret": "0000/0000000000/0000000000000000000000000000000000000000000000000000000000/00000000000==",
            "api_passphrase": "00000000000",
            "config": {}
        }
    }

    try:
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.getExchange() == 'coinbasepro'
    assert app.sellLowerPcnt() is None

    try:
        config['coinbasepro']['config']['selllowerpcnt'] = -10
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.getExchange() == 'coinbasepro'
    assert type(app.sellLowerPcnt() == 'float')
    assert app.sellLowerPcnt() == -10

    try:
        config['coinbasepro']['config']['selllowerpcnt'] = '-10.5'
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.getExchange() == 'coinbasepro'
    assert type(app.sellLowerPcnt() == 'float')
    assert app.sellLowerPcnt() == -10.5

    if os.path.exists('tests/unit_tests/data/pycryptobot_pytest_config.json'):
        os.remove('tests/unit_tests/data/pycryptobot_pytest_config.json')

    try:
        config['coinbasepro']['config']['selllowerpcnt'] = 0.1
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    with pytest.raises(ValueError) as execinfo:
        PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert str(execinfo.value) == 'Invalid config.json: selllowerpcnt must be negative'

    try:
        config['coinbasepro']['config']['selllowerpcnt'] = '0.2'
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    with pytest.raises(ValueError) as execinfo:
        PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert str(execinfo.value) == 'Invalid config.json: selllowerpcnt must be negative'

    try:
        config['coinbasepro']['config']['selllowerpcnt'] = 0
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    with pytest.raises(ValueError) as execinfo:
        PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert str(execinfo.value) == 'Invalid config.json: selllowerpcnt must be negative'

    try:
        config['coinbasepro']['config']['selllowerpcnt'] = 1
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    with pytest.raises(ValueError) as execinfo:
        PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert str(execinfo.value) == 'Invalid config.json: selllowerpcnt must be negative'

def test_configjson_binance_trailingstoploss():
    config = {
       "binance": {
            "api_url": "https://api.binance.com",
            "api_key": "0000000000000000000000000000000000000000000000000000000000000000",
            "api_secret": "0000000000000000000000000000000000000000000000000000000000000000",
            "config": {}
        }
    }

    try:
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.getExchange() == 'binance'
    assert app.trailingStopLoss() is None

    try:
        config['binance']['config']['trailingstoploss'] = -10
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.getExchange() == 'binance'
    assert type(app.trailingStopLoss() == 'float')
    assert app.trailingStopLoss() == -10

    try:
        config['binance']['config']['trailingstoploss'] = '-10.5'
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.getExchange() == 'binance'
    assert type(app.trailingStopLoss() == 'float')
    assert app.trailingStopLoss() == -10.5

    if os.path.exists('tests/unit_tests/data/pycryptobot_pytest_config.json'):
        os.remove('tests/unit_tests/data/pycryptobot_pytest_config.json')

    try:
        config['binance']['config']['trailingstoploss'] = 0.1
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    with pytest.raises(ValueError) as execinfo:
        PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert str(execinfo.value) == 'Invalid config.json: trailingstoploss must be negative'

    try:
        config['binance']['config']['trailingstoploss'] = '0.2'
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    with pytest.raises(ValueError) as execinfo:
        PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert str(execinfo.value) == 'Invalid config.json: trailingstoploss must be negative'

    try:
        config['binance']['config']['trailingstoploss'] = 0
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    with pytest.raises(ValueError) as execinfo:
        PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert str(execinfo.value) == 'Invalid config.json: trailingstoploss must be negative'

    try:
        config['binance']['config']['trailingstoploss'] = 1
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    with pytest.raises(ValueError) as execinfo:
        PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert str(execinfo.value) == 'Invalid config.json: trailingstoploss must be negative'

def test_configjson_coinbasepro_trailingstoploss():
    config = {
        "coinbasepro": {
            "api_url": "https://api.pro.coinbase.com",
            "api_key": "00000000000000000000000000000000",
            "api_secret": "0000/0000000000/0000000000000000000000000000000000000000000000000000000000/00000000000==",
            "api_passphrase": "00000000000",
            "config": {}
        }
    }

    try:
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.getExchange() == 'coinbasepro'
    assert app.trailingStopLoss() is None

    try:
        config['coinbasepro']['config']['trailingstoploss'] = -10
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.getExchange() == 'coinbasepro'
    assert type(app.trailingStopLoss() == 'float')
    assert app.trailingStopLoss() == -10

    try:
        config['coinbasepro']['config']['trailingstoploss'] = '-10.5'
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    app = PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert type(app) is PyCryptoBot
    assert app.getExchange() == 'coinbasepro'
    assert type(app.trailingStopLoss() == 'float')
    assert app.trailingStopLoss() == -10.5

    if os.path.exists('tests/unit_tests/data/pycryptobot_pytest_config.json'):
        os.remove('tests/unit_tests/data/pycryptobot_pytest_config.json')

    try:
        config['coinbasepro']['config']['trailingstoploss'] = 0.1
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    with pytest.raises(ValueError) as execinfo:
        PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert str(execinfo.value) == 'Invalid config.json: trailingstoploss must be negative'

    try:
        config['coinbasepro']['config']['trailingstoploss'] = '0.2'
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    with pytest.raises(ValueError) as execinfo:
        PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert str(execinfo.value) == 'Invalid config.json: trailingstoploss must be negative'

    try:
        config['coinbasepro']['config']['trailingstoploss'] = 0
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    with pytest.raises(ValueError) as execinfo:
        PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert str(execinfo.value) == 'Invalid config.json: trailingstoploss must be negative'

    try:
        config['coinbasepro']['config']['trailingstoploss'] = 1
        config_json = json.dumps(config, indent=4)
        fh = open('tests/unit_tests/data/pycryptobot_pytest_config.json', 'w')
        fh.write(config_json)
        fh.close()
    except Exception as err:
        print (err)

    with pytest.raises(ValueError) as execinfo:
        PyCryptoBot(filename='tests/unit_tests/data/pycryptobot_pytest_config.json')
    assert str(execinfo.value) == 'Invalid config.json: trailingstoploss must be negative'