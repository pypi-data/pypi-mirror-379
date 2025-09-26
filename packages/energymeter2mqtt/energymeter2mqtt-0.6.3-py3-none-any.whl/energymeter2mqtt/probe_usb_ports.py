import logging
from decimal import Decimal

from pymodbus.exceptions import ModbusIOException
from pymodbus.pdu import ExceptionResponse
from pymodbus.pdu.register_message import ReadHoldingRegistersResponse
from rich import get_console, print  # noqa
from rich.pretty import pprint

from energymeter2mqtt.api import get_modbus_client


logger = logging.getLogger(__name__)


def print_parameter_values(client, parameters, device_id: int, verbosity):
    for parameter in parameters:
        print(f'{parameter["name"]:>30}', end=' ')
        address = parameter['register']
        count = parameter.get('count', 1)
        if verbosity:
            print(f'(Register dez: {address:02} hex: {address:04x}, {count=})', end=' ')
        response = client.read_holding_registers(address=address, count=count, device_id=device_id)
        if isinstance(response, (ExceptionResponse, ModbusIOException)):
            print('Error:', response)
        else:
            assert isinstance(response, ReadHoldingRegistersResponse), f'{response=}'
            value = response.registers[0]
            if count > 1:
                value += response.registers[1] * 65536

            scale = Decimal(str(parameter['scale']))
            value = value * scale
            print(f'{value} [blue]{parameter.get("uom", "")}')
    print('\n')


def probe_one_port(energy_meter, definitions, verbosity):
    client = get_modbus_client(energy_meter, definitions, verbosity)

    parameters = definitions['parameters']
    if verbosity > 1:
        pprint(parameters)

    device_id = energy_meter.device_id
    print(f'{device_id=}')

    print_parameter_values(client, parameters, device_id, verbosity)
