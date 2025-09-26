## Overview

This module is intended to be installed on the production NCS nodes and imported in other services/actions that need to gather state from the network.  It uses the NCS device manager and the standard python `multiprocessing` library to connect to devices in-parallel and issue commands, returning results as structured data.

## Usage information

Basic usage example in an NCS callback:

``` python
from umnet_pyncs.state import StateManager
...


class DemoAction(Action):
    @Action.action
    def cb_action(self, uinfo, name, kp, input, output, trans):
        ...
        with StateManager() as m:
            interfaces = m.get_state(al_devices, ["get-interface-details"])
            arp = m.get_state(dl_devices, ["get-arp-table"])
            ...
```

## Supported commands

Currently supported commands are:
- `get-mac-table`
- `get-arp-table`
- `get-interface-details`
- `get-transciever-details`
- `get-lldp-neighbors`
- `get-bfd-neighbors`
- `get-ospf-neighbors`

## Developer testing

Use the `run_cmds` script to start a session with the local `ncs` daemon and test the various state gathering commands

``` shell
[grundler@ncs-1 umnet-pyncs]$ ./run_cmds -h
usage: run_cmds [-h] -c CMD -d DEV

optional arguments:
  -h, --help            show this help message and exit
  -c CMD, --cmd CMD
  -d DEV, --device DEV
[grundler@ncs-1 umnet-pyncs]$
[grundler@ncs-1 umnet-pyncs]$
[grundler@ncs-1 umnet-pyncs]$ ./run_cmds -d s-ehall-2012p-1 -c get-interface-details
INFO:root:connecting to ncs...
INFO:root:transaction started...
INFO:root:submitting commands to worker pool (1)
DEBUG:root:pid: 19275: invoking get-interface-details against s-ehall-2012p-1
DEBUG:root:sending 'show interfaces' to s-ehall-2012p-1
...
```

For any given command, the various platform-specific models are responsible for implementing how the data is fetched and parsed from the remote device.  Each command corresponds to a method that can be invoked to retrieve the data, e.g. `get-interface-details` maps to the `get_interface_details()` instance method of the model(s).

For Cisco IOS and NXOS devices (which use CLI-based NEDs), the built-in NCS `live-status` action(s) are used to send raw CLI commands to the device.  For example, the `get_mac_address()` method will send a `show mac address-table` CLI command.  For both IOS and NXOS we use [ntc_templates](https://github.com/networktocode/ntc-templates) to parse the raw text output into structured data.

For Juniper devices, since the NED uses NETCONF for all device communications, we instead call the `<get-ethernet-switching-table-information>` RPC directly.  Since this RPC is modelled in YANG, we can then parse the results directly using the maagic API.

All the nitty-gritty details of parsing the data retrieved directly from the remote device is handled by the platform-specific model implementation for that device.  Each model normalizes the data using the dataclasses defined in [base.py](./umnet_pyncs/state/models/base.py).  The intention is to makes it simpler for NCS actions/services to use this module, as well as making it easier to develop/maintain.

**NB**: this implementation currently relies on an additional template for NXOS that handles parsing `show ip arp detail vrf all` -- see [PR# 1204](https://github.com/networktocode/ntc-templates/pull/1204).
