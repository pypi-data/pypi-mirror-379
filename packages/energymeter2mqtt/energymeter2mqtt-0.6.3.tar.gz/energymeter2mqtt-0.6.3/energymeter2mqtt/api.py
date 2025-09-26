import logging
from decimal import Decimal

# from ha_services.mqtt4homeassistant.data_classes import HaValue
from pymodbus import FramerType
from pymodbus.client import ModbusSerialClient
from pymodbus.exceptions import ModbusException
from pymodbus.pdu import ExceptionResponse
from pymodbus.pdu.register_message import ReadHoldingRegistersResponse
from rich.pretty import pprint

from energymeter2mqtt.user_settings import EnergyMeter


logger = logging.getLogger(__name__)


def get_modbus_client(energy_meter: EnergyMeter, definitions: dict, verbosity: int) -> ModbusSerialClient:
    conn_settings = definitions['connection']

    print(f'Connect to {energy_meter.port}...')
    conn_kwargs = dict(
        baudrate=conn_settings['baudrate'],
        bytesize=conn_settings['bytesize'],
        parity=conn_settings['parity'],
        stopbits=conn_settings['stopbits'],
        timeout=energy_meter.timeout,
        retries=energy_meter.retries,
    )
    if verbosity:
        print('Connection arguments:')
        pprint(conn_kwargs)

    client = ModbusSerialClient(energy_meter.port, framer=FramerType.RTU, **conn_kwargs)
    if verbosity > 1:
        print('connected:', client.connect())
        print(client)

    return client


def get_ha_values(*, client: ModbusSerialClient, parameters, device_id: int) -> dict:
    # parameters = [{'register': 28,
    #                 'reg_count': 2,
    #                 'name': 'Energy Counter Total',
    #                 'class': 'energy',
    #                 'state_class': 'total',
    #                 'uom': 'kWh',
    #                 'scale': 0.01},
    #                {...
    register2values = {}
    for parameter in parameters:
        logger.debug('Parameters: %r', parameter)
        parameter_name = parameter['name']
        address = parameter['register']
        count = parameter.get('count', 1)
        logger.debug('Read register %i (dez, count: %i, slave id: %i)', address, count, device_id)

        response = client.read_holding_registers(address=address, count=count, device_id=device_id)
        if isinstance(response, (ExceptionResponse, ModbusException)):
            logger.error(
                'Error read register %i (dez, count: %i, slave id: %i): %s', address, count, device_id, response
            )
        else:
            assert isinstance(response, ReadHoldingRegistersResponse), f'{response=}'
            registers = response.registers
            logger.debug('Register values: %r', registers)
            value = registers[0]
            if count > 1:
                value += registers[1] * 65536

            if scale := parameter.get('scale'):
                logger.debug('Scale %s: %r * %r', parameter_name, value, scale)
                scale = Decimal(str(scale))
                value = float(value * scale)
                logger.debug('Scaled %s results in: %r', parameter_name, value)

            register2values[address] = value
            logger.debug('%s address %r has value: %r', parameter_name, address, value)
    return register2values
