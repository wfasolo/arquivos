import sonoff
import typing


class Config(typing.NamedTuple):
    username: str
    password: str
    api_region: str
    grace_period: int


config = Config('wfasolo@gmail.com', 'giana0803', 'sa', 600)

print(f"config = {config}")

s = sonoff.Sonoff(config.username, config.password, config.api_region)
s.do_login()
devices =  s.get_devices()


print(devices)
# We found a device, lets turn something on
device_id = devices[0]['deviceid']
s.switch('on', device_id, 0),
