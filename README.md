# API library and command-line interface for Banyan Security
[![Build Status](https://travis-ci.org/banyansecurity/pybanyan.svg?branch=master)](https://travis-ci.org/banyansecurity/pybanyan)
[![codecov](https://codecov.io/gh/banyansecurity/pybanyan/branch/master/graph/badge.svg)](https://codecov.io/gh/banyansecurity/pybanyan)
[![PyPI version](https://badge.fury.io/py/pybanyan.svg)](https://badge.fury.io/py/pybanyan)


## Prerequisites
Python 3.7 or 3.8 must be installed.

## Installation 
### Installing the easy way

```console
$ pip install pybanyan
```

### Installing the hard way

```console
$ git clone https://github.com/banyansecurity/pybanyan.git
$ cd pybanyan
$ pip install -r requirements.txt
$ python setup.py install
```

## Usage

This package contains both an API client and a CLI tool.
To use either one, you need to [generate] an API token from the Banyan Command Center.

### API library

Here's a sample script that uses the library to print the names of every service registered in Banyan:

```python
from banyan.api import BanyanApiClient

c = BanyanApiClient()
for service in c.services.list():
    print(service.name)
```

Output:
```console
$ python examples/list_services.py
jira
jupyter
kube
mysql
rds-mysql
rds-pgsql
```

The `BanyanApiClient` class accepts optional arguments to specify the API server and refresh token. If not provided, 
it gets them from environment variables named `BANYAN_API_URL` and `BANYAN_REFRESH_TOKEN`.

Full API documentation will be available soon.

### Banyan CLI tool

Before you use the CLI, create a file called `~/.banyan.conf` in your home directory and paste in your API token:

```ini
[banyan]
api_url = https://net.banyanops.com
refresh_token = MY_API_TOKEN
```

The CLI is invoked with the `banyan` tool. It contains a number of commands and sub-commands to help you work
with policies, roles, services, users, and other objects in Banyan. 

Run the `banyan` tool by itself to see the available commands.

```console
$ banyan
usage: banyan [options] <command> <subcommand> [<subcommand> ...] [parameters]

API library and command-line interface for Banyan Security

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           full application debug mode
  -q, --quiet           suppress all console output
  -v, --version         show program's version number and exit
  --api-url API_URL     URL for the Banyan API server. Can also be configured
                        via the BANYAN_API_URL environment variable.
  --refresh-token REFRESH_TOKEN
                        API token used for the initial authentication to the
                        Banyan API server. Can also be configured via the
                        BANYAN_REFRESH_TOKEN environment variable.
  --output-format {table,json,yaml}, -o {table,json,yaml}
                        desired output format (table, json, yaml)

Commands:
  {event,admin,device,user,netagent,shield,policy,role,service}
    event               report on security and audit events
    admin               manage administrator accounts
    device              manage devices
    user                manage user accounts
    netagent            manage netagents (AccessTiers and HostAgents)
    shield              manage Banyan Shield clusters
    policy              manage authorization policies for users and workloads
    role                manage user and workload roles
    service             manage web and TCP services and workloads
```

Each of the commands has multiple subcommands. For example, `banyan service` allows you to list services, 
create/delete, enable/disable, etc. Run the command without any subcommand to see the options:

```console
$ banyan service
usage: banyan service [-h]
                      {attach-policy,create,delete,detach-policy,disable,enable,get,list,test,update}
                      ...

optional arguments:
  -h, --help            show this help message and exit

sub-commands:
  {attach-policy,create,delete,detach-policy,disable,enable,get,list,test,update}
    attach-policy       attach a policy to a service
    create              create a new service from a JSON specification
    delete              delete a service
    detach-policy       detach the active policy from a service
    disable             disable a service
    enable              enable a service
    get                 show the definition of a registered service
    list                list registered services
    test                run sanity checks on a service
    update              update an existing service from a JSON specification
```

To see the full help available for any command, just add the `-h` or `--help` option to the end of the command. 
For example:

```console
$ banyan service attach-policy --help
usage: banyan service attach-policy [-h] [--permissive] [--enforcing]
                                    service_name_or_id policy_name_or_id

positional arguments:
  service_name_or_id  Name or ID of the service to attach a policy to.
  policy_name_or_id   Name or ID of the policy to attach to the service.

optional arguments:
  -h, --help          show this help message and exit
  --permissive        Set the policy to permissive mode (allow all traffic and
                      log any unauthorized access).
  --enforcing         Set the policy to enforcing mode (deny unauthorized
                      access).
```

## Development

To work on the pybanyan code, follow the instructions in the [documentation][devel]. 

## Support

This API library and its accompanying CLI utility are provided free of charge and without support. To report 
issues with the library, please create a new [issue in Github][github-issue].

## Contributions

We welcome your contributions in the form of pull requests! Please follow the standard [Github pull request 
workflow][github-pr].

[generate]: https://net.banyanops.com/app/myprofile
[github-pr]: https://gist.github.com/Chaser324/ce0505fbed06b947d962
[github-issue]: https://github.com/banyansecurity/pybanyan/issues/new
[devel]: https://pybanyan.readthedocs.io/development.html