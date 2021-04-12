from typing import List
import copy
from time import sleep

from cement import Controller, ex

from banyan.controllers.base import Base

from banyan.api.discovered_resource import DiscoveredResourceAPI
from banyan.model.discovered_resource import DiscoveredResource, DiscoveredResourceInfo

from banyan.api.service import ServiceAPI
from banyan.model.service import ServiceInfo, Service
from banyan.model.service import Tags as ServiceTags, Metadata as ServiceMetadata, Spec as ServiceSpec
from banyan.model.service import FrontendAddress, Attributes, BackendTarget, Backend, CustomTLSCert, CertSettings, OIDCSettings, HttpSettings

from banyan.api.policy import PolicyAPI
from banyan.model.policy import PolicyInfo, Policy
from banyan.model.policy import Tags as PolicyTags, Metadata as PolicyMetadata, Spec as PolicySpec
from banyan.model.policy import Options, PolicyException, Conditions, L7Access, Rules, Access

class DiscoveredResourceController(Controller):
    class Meta:
        label = 'discovered_resource'
        aliases = ['dr']
        stacked_type = 'nested'
        stacked_on = 'base'
        help = 'manage discovered resources'

    @property
    def _client(self) -> DiscoveredResourceAPI:
        return self.app.client.discovered_resources

    @ex(help='list discovered_resources',
        arguments=[
            (['--tag_name'], 
            {
                'help': 'Filter discovered resource by Tag Name.'
            }),
        ])
    def list(self):
        d_resources: List[DiscoveredResourceInfo] = self._client.list(params={'include_tags': 'true', 'tag_name': self.app.pargs.tag_name})
        results = list()
        headers = ['Name', 'ID', 'Cloud', 'Region', 'Type', 'Private IP', 'Public IP', '# Tags']
        for res in d_resources:
            new_res = [res.name, res.resource_udid, res.cloud_provider, res.region,
                    res.resource_type, res.private_ip, res.public_ip, len(res.tags)]
            results.append(new_res)
        self.app.render(results, handler='tabulate', headers=headers, tablefmt='simple')


    #TODO-API: argument should be UDID not tag_name
    @ex(help='show details & tags of a discovered_resource', 
        arguments=[
            (['tag_name'],
            {
                'help': 'Filter discovered resource by Tag Name.'
            }),
            (['--tag_value'],
            {
                'help': 'Filter discovered resource by Tag Value.',
                'default': ''
            }),
            (['--resource_uuid'],
            {
                'help': 'Filter discovered resource by Banyan UUID.'
            }),            
        ])
    def get(self):
        params = {
            'include_tags': 'true', 
            'tag_name': self.app.pargs.tag_name,
            'tag_value': self.app.pargs.tag_value
        }
        d_resources: List[DiscoveredResourceInfo] = self._client.list(params=params)
        d_resource: DiscoveredResourceInfo = None
        if len(d_resources):
            d_resource = d_resources[0]
            print(vars(d_resource))
        else:
            print('No discovered_resource found.')


    @ex(help='create a new discovered_resource',
        arguments=[
            (['resources_json'], 
            {
                'help': 'JSON blob describing the new discovered resource(s) to be created, or a filename '
                         'containing JSON prefixed by "@" (example: @res.json).'
            }),
        ])
    def create(self):
        d_resource = Base.get_json_input(self.app.pargs.resources_json)
        info = self._client.create(d_resource)
        print(info)


    @ex(help='sync discovered_resources with AWS',
        arguments=[
            (['resource_type'],
            {
                'help': 'Type of AWS Resource - EC2 | RDS | LB | ALL.'
            }),
            (['--tag_name'],
            {
                'help': 'Only sync resources with specific tag name'
            }),
            (['--tag_value'],
            {
                'help': 'Only sync resources with specific tag values ("*" is allowed).'
            })

        ])
    def sync_aws(self):
        try:
            from banyan.ext.aws.ec2 import Ec2Controller, Ec2Model
        except Exception as ex:
            raise NotImplementedError("AWS SDK not configured correctly > %s" % ex.args[0])

        ec2 = Ec2Controller()
        instances = ec2.list()

        print('\n--> List of AWS Resources')
        results = list()
        for instance in instances:
            allvars = vars(copy.copy(instance))
            allvars['tags'] = len(allvars['tags'])
            results.append(allvars)
        self.app.render(results, handler='tabulate', headers='keys', tablefmt='simple')

        for instance in instances:
            res_tags = []
            for tag in instance.tags:
                res_tag = {
                    'name': tag['Key'],
                    'value': tag['Value']
                }
                res_tags.append(res_tag)

            res = DiscoveredResource(instance.cloud_provider,
                                     instance.region,
                                     instance.resource_id,
                                     instance.resource_name,
                                     instance.resource_type,
                                     instance.public_ip,
                                     instance.private_ip,
                                     res_tags
                                     )
            print('\n--> Syncing Discovered Resource')
            self.app.render(DiscoveredResource.Schema().dump(res), handler='json')
            info = self._client.create(res)
            print('\n-->', info)
            sleep(0.05)

    #TODO-API: argument should be UDID not tag_name
    @ex(help='use discovered_resource to create a new service',
        arguments=[
            (['service_name'],
            {
                'help': 'Name of service to create.'
            }),
            (['service_domain'],
            {
                'help': 'Domain name of service, ex: corp.org.com (no https://).'
            }),                  
            (['service_type'],
            {
                'help': 'Type of service - WEB | SSH | RDS | GENERIC_TCP.'
            }),
            (['tag_name'],
            {
                'help': 'Tag name of discovered resource.'
            }),
            (['--tag_value'],
            {
                'help': 'Tag value of discovered resource.',
                'default': ''
            }),
            (['--resource_uuid'],
            {
                'help': 'Banyan UDID of the discovered resource to use.'
            }),                           
            (['--backend_port'],
            {
                'help': 'Specify if backend port is non-standard.'
            }),
            (['--backend_tls'],
            {
                'default': False,
                'help': 'Specify if backend requires TLS.'
            })            
        ])
    def publish(self):
        params = {
            'include_tags': 'true', 
            'tag_name': self.app.pargs.tag_name,
            'tag_value': self.app.pargs.tag_value
        }
        d_resources: List[DiscoveredResourceInfo] = self._client.list(params=params)
        d_resource: DiscoveredResourceInfo = None
        if len(d_resources):
            d_resource = d_resources[0]
            print('\n--> Discovered Resource')
            print(vars(d_resource))
        else:
            raise RuntimeError('No discovered_resource found')

        svc_name = self.app.pargs.service_name
        svc_domain = self.app.pargs.service_domain
        svc_type = self.app.pargs.service_type
        bknd_port = self.app.pargs.backend_port
        bknd_tls = self.app.pargs.backend_tls

        bknd_ip_or_name = d_resource.private_ip
        bknd_port = 80
        svc_port = 443
        svc_tags = ServiceTags('https', svc_domain, True, 'WEB_USER', svc_type, 'leanpub', svc_port)
        svc_metadata = ServiceMetadata(svc_name, 'pybanyan publish flow', 'cluster1', svc_tags)
        frontend_address = FrontendAddress(svc_port, '')
        host_tag_selector = {"com.banyanops.hosttag.site_name": "*"}
        attributes = Attributes([svc_domain], [frontend_address], [host_tag_selector])
        backend_target = BackendTarget(bknd_ip_or_name, '', bknd_port, bknd_tls)
        backend = Backend(backend_target, {}, [])
        custom_tls_cert = CustomTLSCert()
        cert_settings = CertSettings(custom_tls_cert, [svc_domain])
        oidc_settings = OIDCSettings(True, 'https://' + svc_domain)
        http_settings = HttpSettings(True, oidc_settings, {}, {}, {})
        svc_spec = ServiceSpec(attributes, backend, cert_settings, http_settings, {})
        svc = Service('rbac.banyanops.com/v1', 'BanyanService', 'origin', svc_metadata, svc_spec)

        print('\n--> Service spec to create')
        service_json = Service.Schema().dump(svc)
        self.app.render(service_json, handler='json', indent=2, sort_keys=True)

        print('\n--> Creating service')
        service_info = self._client.create_service(svc)
        print(service_info)
        service_create_json = ServiceInfo.Schema().dump(service_info)
        self.app.render(service_create_json, handler='json', indent=2, sort_keys=True)

        pol_tags = PolicyTags('USER')
        pol_metadata = PolicyMetadata('policy-%s' % svc_name, 'pybanyan publish flow', pol_tags)
        options = Options(True, 'http')
        exception = PolicyException()
        conditions = Conditions('')
        l7_access = L7Access(["*"], ["*"])
        rules = Rules(conditions,[l7_access])
        access = Access(rules, ["ANY"])
        pol_spec = PolicySpec(options, exception, [access])
        pol = Policy('rbac.banyanops.com/v1', 'BanyanService', 'USER', pol_metadata, pol_spec)
        print(pol)

        print('\n--> Policy spec to create')
        policy_json = Policy.Schema().dump(pol)
        self.app.render(policy_json, handler='json', indent=2, sort_keys=True)

        print('\n--> Creating policy')
        policy_info = self._client.create_policy(pol)
        print(policy_info)
        policy_create_json = PolicyInfo.Schema().dump(policy_info)
        self.app.render(policy_create_json, handler='json', indent=2, sort_keys=True)

        print('\n--> Attaching policy to service')
        result = self._client.attach_service_policy(policy_info, service_info, True)
        mode = 'ENFORCING' if result.enabled else 'PERMISSIVE'
        self.app.print(f'Policy {result.policy_id} attached to service {result.service_id} in {mode} mode.')


    @ex(help='add a discovered_resource to an existing service',
        arguments=[
            (['service_name'],
            {
                'help': 'Name of service whose whitelist should be updated.'
            }),          
            (['tag_name'],
            {
                'help': 'Name of Tag of the discovered resources to use.'
            }),
            (['tag_value'],
            {
                'help': 'Value of Tag of the discovered resources to use ("*" is allowed).'
            })
        ])
    def whitelist(self):
        #TODO: get resource(s), check service if it has whitelist
        return