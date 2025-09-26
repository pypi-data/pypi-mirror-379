import asyncio
import copy
from datetime import datetime
import logging
import pytest
import pytest_asyncio

from aiodabpumps import (
    DabPumpsApi,
    DabPumpsApiAuthError,
    DabPumpsApiError, 
    DabPumpsInstall,
    DabPumpsDevice,
    DabPumpsConfig,
    DabPumpsParams,
    DabPumpsStatus,
    DabPumpsParamType,
    DabPumpsUserRole,
    DabPumpsHistoryItem, 
    DabPumpsHistoryDetail,
    DabPumpsLogin,
)

from . import TEST_USERNAME, TEST_PASSWORD

_LOGGER = logging.getLogger(__name__)

logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)


class TestContext:
    def __init__(self):
        self.api = None

    async def cleanup(self):
        if self.api:
            await self.api.async_logout()
            await self.api.async_close()
            assert self.api.closed == True


@pytest_asyncio.fixture
async def context():
    # Prepare
    ctx = TestContext()

    # pass objects to tests
    yield ctx

    # cleanup
    await ctx.cleanup()


@pytest.mark.asyncio
@pytest.mark.usefixtures("context")
@pytest.mark.parametrize(
    "name, method, usr, pwd, exp_except",
    [
        ("ok",   'Any',           TEST_USERNAME, TEST_PASSWORD, None),
        ("ok",   'H2D_app',       TEST_USERNAME, TEST_PASSWORD, None),
        ("ok",   'DabLive_app_0', TEST_USERNAME, TEST_PASSWORD, None),
        ("ok",   'DabLive_app_1', TEST_USERNAME, TEST_PASSWORD, None),
        ("ok",   'DConnect_app',  TEST_USERNAME, TEST_PASSWORD, None),
        ("ok",   'DConnect_web',  TEST_USERNAME, TEST_PASSWORD, None),
        ("fail", 'Any',           "dummy_usr",   "wrong_pwd",   DabPumpsApiAuthError),
        ("fail", 'H2D_app',       "dummy_usr",   "wrong_pwd",   DabPumpsApiAuthError),
        ("fail", 'DabLive_app_0', "dummy_usr",   "wrong_pwd",   DabPumpsApiAuthError),
        ("fail", 'DabLive_app_1', "dummy_usr",   "wrong_pwd",   DabPumpsApiAuthError),
        ("fail", 'DConnect_app',  "dummy_usr",   "wrong_pwd",   DabPumpsApiAuthError),
        ("fail", 'DConnect_web',  "dummy_usr",   "wrong_pwd",   DabPumpsApiAuthError),
    ]
)
async def test_login(name, method, usr, pwd, exp_except, request):
    context = request.getfixturevalue("context")
    assert context.api is None

    context.api = DabPumpsApi(usr, pwd)
    assert context.api.closed == False

    if exp_except is None:
        assert context.api.login_method is None

        match method:
            case 'Any':
                await context.api.async_login()

                assert context.api.login_method is not None
                
            case 'H2D_app':
                await context.api._async_login_h2d_app()

                assert context.api._access_token is not None
                assert context.api._access_expiry > datetime.min
                assert context.api._refresh_token is not None
                assert context.api._refresh_expiry > datetime.min

            case 'DabLive_app_0':
                await context.api._async_login_dablive_app(isDabLive=0)

            case 'DabLive_app_1':
                await context.api._async_login_dablive_app(isDabLive=1)

            case 'DConnect_app':
                await context.api._async_login_dconnect_app()

            case 'DConnect_web':
                await context.api._async_login_dconnect_web()

        assert context.api.install_map is not None
        assert context.api.device_map is not None
        assert context.api.config_map is not None
        assert context.api.status_map is not None
        assert context.api.string_map is not None
        assert len(context.api.install_map) == 0
        assert len(context.api.device_map) == 0
        assert len(context.api.config_map) == 0
        assert len(context.api.status_map) == 0
        assert len(context.api.string_map) == 0

    else:
        with pytest.raises(exp_except):
            match method:
                case 'Any':             await context.api.async_login()
                case 'H2D_app':         await context.api._async_login_h2d_app()
                case 'DabLive_app_0':   await context.api._async_login_dablive_app(isDabLive=0)
                case 'DabLive_app_1':   await context.api._async_login_dablive_app(isDabLive=1)
                case 'DConnect_app':    await context.api._async_login_dconnect_app()
                case 'DConnect_web':    await context.api._async_login_dconnect_web()


@pytest.mark.asyncio
@pytest.mark.usefixtures("context")
@pytest.mark.parametrize(
    "name, usr, pwd, exp_except",
    [
        ("login multi", TEST_USERNAME, TEST_PASSWORD, None),
    ]
)
async def test_login_seq(name, usr, pwd, exp_except, request):
    context = request.getfixturevalue("context")
    assert context.api is None

    # First call with wrong pwd
    context.api = DabPumpsApi(usr, "wrong_pwd")
    assert context.api.closed == False
    assert context.api.login_method is None

    with pytest.raises(DabPumpsApiAuthError):
        await context.api.async_login()

    # Next call with correct pwd
    context.api = DabPumpsApi(usr, pwd)
    assert context.api.closed == False
    assert context.api.login_method is None

    if exp_except is None:
        await context.api.async_login()

        assert context.api.login_method is not None
        assert context.api.install_map is not None
        assert context.api.device_map is not None
        assert context.api.config_map is not None
        assert context.api.status_map is not None
        assert context.api.string_map is not None
        assert len(context.api.install_map) == 0
        assert len(context.api.device_map) == 0
        assert len(context.api.config_map) == 0
        assert len(context.api.status_map) == 0
        assert len(context.api.string_map) == 0

    else:
        with pytest.raises(exp_except):
            await context.api.async_login()


@pytest.mark.asyncio
@pytest.mark.usefixtures("context")
@pytest.mark.parametrize(
    "name, method, loop, exp_except",
    [
        ("ok",  'Auto',                      0, None),
        ("ok",  DabPumpsLogin.H2D_APP,       0, None),
        ("ok",  DabPumpsLogin.DABLIVE_APP_0, 0, None),
        ("ok",  DabPumpsLogin.DABLIVE_APP_1, 0, None),
        ("ok",  DabPumpsLogin.DCONNECT_APP,  0, None),
        ("ok",  DabPumpsLogin.DCONNECT_WEB,  0, None),
        ("24h", "Auto",                      24*60, None),    # Run 1 full day
        ("24h", DabPumpsLogin.H2D_APP,       24*60, None),    # Run 1 full day
        ("24h", DabPumpsLogin.DABLIVE_APP_1, 24*60, None),    # Run 1 full day
        ("24h", DabPumpsLogin.DCONNECT_APP,  24*60, None),    # Run 1 full day
        ("24h", DabPumpsLogin.DCONNECT_WEB,  24*60, None),    # Run 1 full day
    ]
)
async def test_get_data(name, method, loop, exp_except, request):
    context = request.getfixturevalue("context")
    context.api = DabPumpsApi(TEST_USERNAME, TEST_PASSWORD)
    assert context.api.closed == False

    # Try set diagnostics callback function
    context.api.set_diagnostics(lambda context,item,detail,data: None)

    # Login
    match method:
        case 'Auto':                        await context.api.async_login()
        case DabPumpsLogin.H2D_APP:         await context.api._async_login_h2d_app()
        case DabPumpsLogin.DABLIVE_APP_0:   await context.api._async_login_dablive_app(isDabLive=0)
        case DabPumpsLogin.DABLIVE_APP_1:   await context.api._async_login_dablive_app(isDabLive=1)
        case DabPumpsLogin.DCONNECT_APP:    await context.api._async_login_dconnect_app()
        case DabPumpsLogin.DCONNECT_WEB:    await context.api._async_login_dconnect_web()

    login_method_org = context.api.login_method

    # Get install list
    await context.api.async_fetch_install_list()

    assert context.api.install_map is not None
    assert type(context.api.install_map) is dict
    assert len(context.api.install_map) > 0

    for install_id,install in context.api.install_map.items():
        assert type(install_id) is str
        assert type(install) is DabPumpsInstall
        assert install.id is not None    
        assert install.name is not None  

    # Get install details, config metadata and initial statuses (just for the first install)
    await context.api.async_fetch_install_details(install_id)

    assert context.api.device_map is not None
    assert type(context.api.device_map) is dict
    assert len(context.api.device_map) > 0

    for device_serial,device in context.api.device_map.items():
        assert type(device_serial) is str
        assert type(device) is DabPumpsDevice
        assert device.id is not None    
        assert device.serial is not None    
        assert device.name is not None  
        assert device.config_id is not None  
        assert device.install_id is not None  
        assert device.sw_version is not None

    assert context.api.config_map is not None
    assert type(context.api.config_map) is dict
    assert len(context.api.config_map) > 0

    for config_id,config in context.api.config_map.items():
        assert type(config_id) is str
        assert type(config) is DabPumpsConfig
        assert config.id is not None
        assert config.label is not None

        assert config.meta_params is not None
        assert type(config.meta_params) is dict
        assert len(config.meta_params) > 0

        for param_name,param in config.meta_params.items():
            assert type(param_name) is str
            assert type(param) is DabPumpsParams
            assert param.key is not None

            assert context.api.status_map is not None
            assert type(context.api.status_map) is dict
            assert len(context.api.status_map) > 0

    for status_id,status in context.api.status_map.items():
        assert type(status_id) is str
        assert type(status) is DabPumpsStatus
        assert status.serial is not None
        assert status.key is not None
        assert status.name is not None

    counter_success: int = 0
    counter_fail: int = 0
    reason_fail: dict[str,int] = {}
    for idx in range(1,loop+1):
        # Get fresh device statuses
        try:
            # Check access-token and refresh or re-login if needed
            await context.api.async_login()
            assert login_method_org == context.api.login_method

            await context.api.async_fetch_install_statuses(install_id)

            assert context.api.status_map is not None
            assert type(context.api.status_map) is dict
            assert len(context.api.status_map) > 0

            for status_id,status in context.api.status_map.items():
                assert type(status_id) is str
                assert type(status) is DabPumpsStatus
                assert status.serial is not None
                assert status.key is not None
                assert status.name is not None

            counter_success += 1
        
        except Exception as ex:
            counter_fail += 1
            reason = str(ex)
            reason_fail[reason] = reason_fail[reason]+1 if reason in reason_fail else 1
            _LOGGER.warning(f"Fail: {ex}")

        if loop:
            # Simulate failure to recover from
            #if idx % 6 == 0:
            #    await context.api._async_logout("simulate failure")
            #elif idx % 3 == 0:
            #    await context.api._async_logout("login force refresh", DabPumpsLogin.ACCESS_TOKEN)

            if method != "Auto":
                context.api._login_method = method

            _LOGGER.debug(f"Loop test, {idx} of {loop} (success={counter_success}, fail={counter_fail})")
            await asyncio.sleep(60)

    _LOGGER.info(f"Fail summary after {loop} loops:")
    for reason,count in reason_fail.items():
        _LOGGER.info(f"  {count}x {reason}")

    assert counter_fail == 0


@pytest.mark.asyncio
@pytest.mark.usefixtures("context")
@pytest.mark.parametrize(
    "method, key, codes, exp_code, exp_except",
    [
        ('Auto',                      "PowerShowerBoost",        ["20","30"],   "=", None),
        ('Auto',                      "PowerShowerDuration",     ["300","360"], "=", None),
        ('Auto',                      "SleepModeEnable",         ["0", "1"],    "=", None),
        ('Auto',                      "RF_EraseHistoricalFault", ["1"],         "0", None), # Falls back to 0 after STATUS_UPDATE_HOLD
        (DabPumpsLogin.H2D_APP,       "PowerShowerBoost",        ["20","30"],   "=", None),
        (DabPumpsLogin.H2D_APP,       "PowerShowerDuration",     ["300","360"], "=", None),
        (DabPumpsLogin.H2D_APP,       "SleepModeEnable",         ["0", "1"],    "=", None),
        (DabPumpsLogin.H2D_APP,       "RF_EraseHistoricalFault", ["1"],         "0", None), # Falls back to 0 after STATUS_UPDATE_HOLD
        (DabPumpsLogin.DABLIVE_APP_1, "PowerShowerBoost",        ["20","30"],   "=", None),
        (DabPumpsLogin.DABLIVE_APP_1, "PowerShowerDuration",     ["300","360"], "=", None),
        (DabPumpsLogin.DABLIVE_APP_1, "SleepModeEnable",         ["0", "1"],    "=", None),
        (DabPumpsLogin.DABLIVE_APP_1, "RF_EraseHistoricalFault", ["1"],         "0", None), # Falls back to 0 after STATUS_UPDATE_HOLD
        (DabPumpsLogin.DCONNECT_APP,  "PowerShowerBoost",        ["20","30"],   "=", None),
        (DabPumpsLogin.DCONNECT_APP,  "PowerShowerDuration",     ["300","360"], "=", None),
        (DabPumpsLogin.DCONNECT_APP,  "SleepModeEnable",         ["0", "1"],    "=", None),
        (DabPumpsLogin.DCONNECT_APP,  "RF_EraseHistoricalFault", ["1"],         "0", None), # Falls back to 0 after STATUS_UPDATE_HOLD
        (DabPumpsLogin.DCONNECT_WEB,  "PowerShowerBoost",        ["20","30"],   "=", None),
        (DabPumpsLogin.DCONNECT_WEB,  "PowerShowerDuration",     ["300","360"], "=", None),
        (DabPumpsLogin.DCONNECT_WEB,  "SleepModeEnable",         ["0", "1"],    "=", None),
        (DabPumpsLogin.DCONNECT_WEB,  "RF_EraseHistoricalFault", ["1"],         "0", None), # Falls back to 0 after STATUS_UPDATE_HOLD
    ]
)
async def test_set_data(method, key, codes, exp_code, exp_except, request):
    context = request.getfixturevalue("context")
    context.api = DabPumpsApi(TEST_USERNAME, TEST_PASSWORD)
    assert context.api.closed == False

    # Login
    match method:
        case 'Auto':                        await context.api.async_login()
        case DabPumpsLogin.H2D_APP:         await context.api._async_login_h2d_app()
        case DabPumpsLogin.DABLIVE_APP_0:   await context.api._async_login_dablive_app(isDabLive=0)
        case DabPumpsLogin.DABLIVE_APP_1:   await context.api._async_login_dablive_app(isDabLive=1)
        case DabPumpsLogin.DCONNECT_APP:    await context.api._async_login_dconnect_app()
        case DabPumpsLogin.DCONNECT_WEB:    await context.api._async_login_dconnect_web()

    # Get install list
    await context.api.async_fetch_install_list()

    assert context.api.install_map is not None
    assert type(context.api.install_map) is dict
    assert len(context.api.install_map) > 0

    # Get install details, metadata and initial statuses
    for install_id in context.api.install_map:
        await context.api.async_fetch_install_details(install_id)

    # Find current code and value and find a new code to change into
    status = next( (status for status in context.api.status_map.values() if status.key==key), None)
    assert status is not None

    old_code = status.code
    new_code = next( (code for code in codes if code != old_code), None )

    # Change device status and do immediate test of changed value. 
    # We hold the changed value while the backend is processing the change.
    changed = await context.api.async_change_device_status(status.serial, status.key, code=new_code)
    if changed:
        await context.api.async_fetch_install_statuses(install_id)

        status = next( (status for status in context.api.status_map.values() if status.key==key), None)
        assert status.code == new_code
        assert status.update_ts is not None
        _LOGGER.debug(f"Found value changed from {old_code} to {new_code}")

        # Wait until the backend has processed the change and test again
        _LOGGER.debug(f"Wait for DAB Servers to process the change")
        await asyncio.sleep(40)
        await context.api.async_login()

    # Test after change has been processed by backend
    await context.api.async_fetch_install_statuses(install_id)

    status = next( (status for status in context.api.status_map.values() if status.key==key), None)
    assert status.code == new_code if exp_code == "=" else exp_code
    assert status.update_ts is None

    _LOGGER.debug(f"Found value still changed from {old_code} to {new_code}")

    # Change back to original value and do immediate test of changed value
    changed = await context.api.async_change_device_status(status.serial, status.key, code=old_code)
    if changed:
        await context.api.async_fetch_install_statuses(install_id)

        status = next( (status for status in context.api.status_map.values() if status.key==key), None)
        assert status.code == old_code
        assert status.update_ts is not None

        _LOGGER.debug(f"Found value changed back from {new_code} to {old_code}")


@pytest.mark.asyncio
@pytest.mark.usefixtures("context")
@pytest.mark.parametrize(
    "method, exp_except",
    [
        ('Auto',                      None),
        (DabPumpsLogin.H2D_APP,       None),
        (DabPumpsLogin.DABLIVE_APP_1, None),
        (DabPumpsLogin.DCONNECT_APP,  None),
        (DabPumpsLogin.DCONNECT_WEB,  None),
    ]
)
async def test_set_role(method, exp_except, request):
    context = request.getfixturevalue("context")
    context.api = DabPumpsApi(TEST_USERNAME, TEST_PASSWORD)
    assert context.api.closed == False

    # Login
    match method:
        case 'Auto':                        await context.api.async_login()
        case DabPumpsLogin.H2D_APP:         await context.api._async_login_h2d_app()
        case DabPumpsLogin.DABLIVE_APP_0:   await context.api._async_login_dablive_app(isDabLive=0)
        case DabPumpsLogin.DABLIVE_APP_1:   await context.api._async_login_dablive_app(isDabLive=1)
        case DabPumpsLogin.DCONNECT_APP:    await context.api._async_login_dconnect_app()
        case DabPumpsLogin.DCONNECT_WEB:    await context.api._async_login_dconnect_web()

    # Get install list
    await context.api.async_fetch_install_list()

    assert context.api.install_map is not None
    assert type(context.api.install_map) is dict
    assert len(context.api.install_map) > 0

    # Get first install details, metadata and initial statuses
    install = next( (install for install in context.api.install_map.values()), None)
    assert install is not None
    install_id = install.id

    # Find current role and determine new role to change into
    old_role = install.role
    new_role = next( (role for role in DabPumpsUserRole if role != old_role), None )

    # Change role and do immediate test of changed value. 
    # We hold the changed value while the backend is processing the change.
    changed = await context.api.async_change_install_role(install_id, old_role, new_role)
    if changed:
        await context.api.async_fetch_install_list()

        install = next( (install for install in context.api.install_map.values() if install.id == install_id), None)
        assert install is not None
        assert install.role == new_role
        _LOGGER.debug(f"Found role changed from {old_role} to {new_role}")

        # Wait until the backend has processed the change and test again
        _LOGGER.debug(f"Wait for DAB Servers to process the change")
        await asyncio.sleep(40)
        await context.api.async_login()

    # Test after change has been processed by backend
    await context.api.async_fetch_install_list()

    install = next( (install for install in context.api.install_map.values() if install.id == install_id), None)
    assert install is not None
    assert install.role == new_role
    _LOGGER.debug(f"Found role still changed from {old_role} to {new_role}")

    # Change back to original value and do immediate test of changed value
    changed = await context.api.async_change_install_role(install_id, new_role, old_role)
    if changed:
        await context.api.async_fetch_install_list()

        install = next( (install for install in context.api.install_map.values() if install.id == install_id), None)
        assert install is not None
        assert install.role == old_role
        _LOGGER.debug(f"Found role changed back from {new_role} to {old_role}")


@pytest.mark.asyncio
@pytest.mark.usefixtures("context")
@pytest.mark.parametrize(
    "name, lang, exp_lang",
    [
        ("strings en", 'en', 'en'),
        ("strings nl", 'nl', 'nl'),
        ("strings xx", 'xx', 'en'),
    ]
)
async def test_strings(name, lang, exp_lang, request):
    context = request.getfixturevalue("context")
    context.api = DabPumpsApi("dummy_usr", "wrong_pwd") # no login needed

    # Get strings
    await context.api.async_fetch_strings(lang)

    assert context.api.string_map is not None
    assert type(context.api.string_map) is dict
    assert len(context.api.string_map) > 0

    assert context.api.string_map_lang == exp_lang


@pytest.mark.parametrize(
    "name, attr, exp_id",
    [
        ("multi", ['abc', 'DEF', '123'], 'abc_def_123'),
        ("spaces", ['abc DEF', '123'], 'abc_def_123'),
        ("underscore", ['abc_DEF', '123'], 'abc_def_123'),
        ('ignored start', ['@%^_DEF', '123'], '_def_123'),
        ('ignored mid', ['@bc_DE#', '123'], 'bc_de_123'),
        ('ignored end', ['abc_DEF', '!&'], 'abc_def_'),
    ]
)
def test_create_id(name, attr, exp_id, request):

    id = DabPumpsApi.create_id(*attr)
    assert id == exp_id


@pytest_asyncio.fixture
async def device_map():
    device_map = {
        "SERIAL": DabPumpsDevice(
            vendor = 'DAB Pumps',
            name = 'test device',
            id = DabPumpsApi.create_id('test device'),
            serial = 'SERIAL',
            product = 'test product',
            hw_version = 'test hw version',
            config_id = 'CONFIG_ID',
            install_id = 'INSTALL_ID',
            sw_version = 'test sw version',
            mac_address = 'test mac',
        ),
    }
    yield device_map

@pytest_asyncio.fixture
async def config_map():
    config_map = {
        "CONFIG_ID": DabPumpsConfig(
            id = 'CONFIG_ID',
            label = 'test label',
            description = 'test description',
            meta_params = {
                "KEY_ENUM":  DabPumpsParams(key='KEY_ENUM',  name='NameEnum',  type=DabPumpsParamType.ENUM,    unit=None, weight=None, values={'1':'one', '2':'two', '3':'three'}, min=1, max=3, family='f', group='g', view='CSIR', change='', log='', report=''),
                "KEY_FLOAT": DabPumpsParams(key='KEY_FLOAT', name='NameFloat', type=DabPumpsParamType.MEASURE, unit='F',  weight=0.1,  values=None, min=0, max=1,  family='f', group='g', view='CSIR', change='', log='', report=''),
                "KEY_INT":   DabPumpsParams(key='KEY_INT',   name='NameInt',   type=DabPumpsParamType.MEASURE, unit='I',  weight=1,    values=None, min=0, max=10, family='f', group='g', view='CSIR', change='', log='', report=''),
                "KEY_LABEL": DabPumpsParams(key='KEY_LABEL', name='NameLabel', type=DabPumpsParamType.LABEL,   unit='',   weight=None, values=None, min=0, max=0,  family='f', group='g', view='CSIR', change='', log='', report=''),
            }
        ),
    }
    yield config_map

@pytest_asyncio.fixture
async def status_map():
    status_map = {
        'serial_key_enum': DabPumpsStatus('SERIAL', 'KEY_ENUM', 'NameEnum', '1', 'one', None, None, None),
        'serial_key_float': DabPumpsStatus('SERIAL', 'KEY_FLOAT', 'NameFloat', '1', 0.1, 'F', None, None),
        'serial_key_int': DabPumpsStatus('SERIAL', 'KEY_INT', 'NameInt', '1', 1, 'I', None, None),
        'serial_key_label': DabPumpsStatus('SERIAL', 'KEY_LABEL', 'NameLabel', 'ABC', 'ABC', None, None, None),
    }
    yield status_map

@pytest_asyncio.fixture
async def string_map():
    string_map = {
        'one': 'een',
        'two': 'twee',
        'three': 'drie',
        'ABC': 'aa bee cee',
    }
    yield string_map


@pytest.mark.asyncio
@pytest.mark.usefixtures("context", "device_map", "config_map", "string_map")
@pytest.mark.parametrize(
    "name, serial, key, translate, code, exp_value",
    [
        ("device unknown", 'SERIAL_XX', 'KEY_ENUM', True, '2', ('2', '')),
        ("key unknown", 'SERIAL', 'KEY_XX', True, '2', ('2', '')),
        ("enum ok", "SERIAL", 'KEY_ENUM', False, '2', ('two', None)),
        ("enum ok", "SERIAL", 'KEY_ENUM', True, '2', ('twee', None)),
        ("enum no", "SERIAL", 'KEY_ENUM', False, '4', ('4', None)),
        ("enum no", "SERIAL", 'KEY_ENUM', True, '4', ('4', None)),
        ("float ok", "SERIAL", 'KEY_FLOAT', True, '2', (0.2, 'F')),
        ("float min", "SERIAL", 'KEY_FLOAT', True, '-1', (-0.1, 'F')),
        ("float max", "SERIAL", 'KEY_FLOAT', True, '11', (1.1, 'F')),
        ("int ok", "SERIAL", 'KEY_INT', True, '2', (2, 'I')),
        ("int min", "SERIAL", 'KEY_INT', True, '-1', (-1, 'I')),
        ("int max", "SERIAL", 'KEY_INT', True, '11', (11, 'I')),
        ("label ok", "SERIAL", 'KEY_LABEL', True, 'ABC', ('ABC', '')),
    ]
)
async def test_decode(name, serial, key, translate, code, exp_value, request):
    context = request.getfixturevalue("context")
    context.api = DabPumpsApi("dummy_usr", "wrong_pwd") # no login needed

    context.api._device_map = request.getfixturevalue("device_map")
    context.api._config_map = request.getfixturevalue("config_map")
    if translate:
        context.api._string_map = request.getfixturevalue("string_map")

    value = context.api._decode_status_value(serial, key, code)
    assert value == exp_value
    assert type(value) == type(exp_value)


@pytest.mark.asyncio
@pytest.mark.usefixtures("context", "device_map", "config_map")
@pytest.mark.parametrize(
    "name, serial, key, value, exp_code",
    [
        ("device unknown", 'SERIAL_XX', 'KEY_ENUM', 'two', 'two'),
        ("device unknown", 'SERIAL_XX', 'KEY_ENUM', 'two', 'two'),
        ("key unknown", 'SERIAL', 'KEY_XX', 'two', 'two'),
        ("enum ok", "SERIAL", 'KEY_ENUM', 'two', '2'),
        ("enum no", "SERIAL", 'KEY_ENUM', 'four', 'four'),
        ("float ok", "SERIAL", 'KEY_FLOAT', 0.2, '2'),
        ("float min", "SERIAL", 'KEY_FLOAT', -0.1, '-1'),
        ("float max", "SERIAL", 'KEY_FLOAT', 1.1, '11'),
        ("int ok", "SERIAL", 'KEY_INT', 2, '2'),
        ("int min", "SERIAL", 'KEY_INT', -1, '-1'),
        ("int max", "SERIAL", 'KEY_INT', 11, '11'),
        ("label ok", "SERIAL", 'KEY_LABEL', 'ABC', 'ABC'),
    ]
)
async def test_encode(name, serial, key, value, exp_code, request):
    context = request.getfixturevalue("context")
    context.api = DabPumpsApi("dummy_usr", "wrong_pwd") # no login needed

    context.api._device_map = request.getfixturevalue("device_map")
    context.api._config_map = request.getfixturevalue("config_map")

    code = context.api._encode_status_value(serial, key, value)
    assert code == exp_code
    assert type(code) == type(exp_code)


@pytest.mark.asyncio
@pytest.mark.usefixtures("context", "device_map", "config_map", "status_map", "string_map")
@pytest.mark.parametrize(
    "name, serial, key, exp_code, exp_value, exp_unit",
    [
        ("device unknown", 'SERIAL_XX', 'KEY_ENUM', None, None, None),
        ("device unknown", 'SERIAL_XX', 'KEY_ENUM', None, None, None),
        ("key unknown", 'SERIAL', 'KEY_XX', None, None, None),
        ("enum ok", "SERIAL", 'KEY_ENUM', '1', 'one', None),
        ("float ok", "SERIAL", 'KEY_FLOAT', '1', 0.1, 'F'),
        ("int ok", "SERIAL", 'KEY_INT', '1', 1, 'I'),
        ("label ok", "SERIAL", 'KEY_LABEL', 'ABC', 'ABC', None),
    ]
)
async def test_status(name, serial, key, exp_code, exp_value, exp_unit, request):
    context = request.getfixturevalue("context")
    context.api = DabPumpsApi("dummy_usr", "wrong_pwd") # no login needed

    context.api._device_map = request.getfixturevalue("device_map")
    context.api._config_map = request.getfixturevalue("config_map")
    context.api._status_actual_map = request.getfixturevalue("status_map")
    context.api._status_static_map = {}
    context.api._string_map = request.getfixturevalue("string_map")

    status = context.api.get_status_value(serial, key)
    if exp_code is None:
        assert status is None
    else:
        assert status is not None
        assert status.serial == serial
        assert status.key == key
        assert status.code == exp_code
        assert status.value == exp_value
        assert status.unit == exp_unit


@pytest.mark.asyncio
@pytest.mark.usefixtures("context", "device_map", "config_map", "status_map", "string_map")
@pytest.mark.parametrize(
    "name, serial, key, translate, exp_type, exp_values, exp_unit",
    [
        ("device unknown", 'SERIAL_XX', 'KEY_ENUM', False, None, None, None),
        ("device unknown", 'SERIAL_XX', 'KEY_ENUM', False, None, None, None),
        ("key unknown", 'SERIAL', 'KEY_XX', False, None, None, None),
        ("enum ok", "SERIAL", 'KEY_ENUM', False, DabPumpsParamType.ENUM, {'1':'one', '2':'two', '3':'three'}, None),
        ("enum ok", "SERIAL", 'KEY_ENUM', True, DabPumpsParamType.ENUM, {'1':'een', '2':'twee', '3':'drie'}, None),
        ("float ok", "SERIAL", 'KEY_FLOAT', False, DabPumpsParamType.MEASURE, None, 'F'),
        ("int ok", "SERIAL", 'KEY_INT', False, DabPumpsParamType.MEASURE, None, 'I'),
        ("label ok", "SERIAL", 'KEY_LABEL', False, DabPumpsParamType.LABEL, None, ''),
    ]
)
async def test_metadata(name, serial, key, translate, exp_type, exp_values, exp_unit, request):
    context = request.getfixturevalue("context")
    context.api = DabPumpsApi("dummy_usr", "wrong_pwd") # no login needed

    context.api._device_map = request.getfixturevalue("device_map")
    context.api._config_map = request.getfixturevalue("config_map")
    context.api._status_actual_map = request.getfixturevalue("status_map")
    context.api._status_static_map = {}
    context.api._string_map = request.getfixturevalue("string_map")

    params = context.api.get_status_metadata(serial, key, translate=translate)
    if exp_type is None:
        assert params is None
    else:
        assert params is not None
        assert params.key == key
        assert params.type == exp_type
        assert params.unit == exp_unit

        if exp_values is None:
            assert params.values is None
        else:
            assert params.values is not None
            assert len(params.values) == len(exp_values)
            for k,v in exp_values.items():
                assert k in params.values
                assert params.values[k] == v
