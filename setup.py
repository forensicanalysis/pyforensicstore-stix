
from setuptools import setup

setup(
    name="forensicstore_stix_schemas",
    author="Demian Kellermann",
    author_email="demian.kellermann@siemens.com",
    url="https://github.com/forensicanalysis/pyforensicstore_stix",
    description="STIX 2.1 JSON schemas as a python provider",
    version="2.1.0",
    py_modules=['forensicstore_stix_schemas'],
    entry_points={
        'forensicstore_schemas': [
            'note = forensicstore_stix_schemas:note',
            'malware = forensicstore_stix_schemas:malware',
            'threat-actor = forensicstore_stix_schemas:threat_actor',
            'infrastructure = forensicstore_stix_schemas:infrastructure',
            'report = forensicstore_stix_schemas:report',
            'intrusion-set = forensicstore_stix_schemas:intrusion_set',
            'identity = forensicstore_stix_schemas:identity',
            'course-of-action = forensicstore_stix_schemas:course_of_action',
            'malware-analysis = forensicstore_stix_schemas:malware_analysis',
            'tool = forensicstore_stix_schemas:tool',
            'vulnerability = forensicstore_stix_schemas:vulnerability',
            'indicator = forensicstore_stix_schemas:indicator',
            'location = forensicstore_stix_schemas:location',
            'opinion = forensicstore_stix_schemas:opinion',
            'observed-data = forensicstore_stix_schemas:observed_data',
            'campaign = forensicstore_stix_schemas:campaign',
            'attack-pattern = forensicstore_stix_schemas:attack_pattern',
            'grouping = forensicstore_stix_schemas:grouping',
            'autonomous-system = forensicstore_stix_schemas:autonomous_system',
            'domain-name = forensicstore_stix_schemas:domain_name',
            'ipv6-addr = forensicstore_stix_schemas:ipv6_addr',
            'ipv4-addr = forensicstore_stix_schemas:ipv4_addr',
            'file = forensicstore_stix_schemas:file',
            'user-account = forensicstore_stix_schemas:user_account',
            'software = forensicstore_stix_schemas:software',
            'mac-addr = forensicstore_stix_schemas:mac_addr',
            'directory = forensicstore_stix_schemas:directory',
            'email-addr = forensicstore_stix_schemas:email_addr',
            'url = forensicstore_stix_schemas:url',
            'email-message = forensicstore_stix_schemas:email_message',
            'x509-certificate = forensicstore_stix_schemas:x509_certificate',
            'process = forensicstore_stix_schemas:process',
            'windows-registry-key = forensicstore_stix_schemas:windows_registry_key',
            'network-traffic = forensicstore_stix_schemas:network_traffic',
            'artifact = forensicstore_stix_schemas:artifact',
            'mutex = forensicstore_stix_schemas:mutex',
            'relationship = forensicstore_stix_schemas:relationship',
            'sighting = forensicstore_stix_schemas:sighting',
            'kill-chain-phase = forensicstore_stix_schemas:kill_chain_phase',
            'bundle = forensicstore_stix_schemas:bundle',
            'hashes = forensicstore_stix_schemas:hashes',
            'external-reference = forensicstore_stix_schemas:external_reference',
            'granular-marking = forensicstore_stix_schemas:granular_marking',
            'identifier = forensicstore_stix_schemas:identifier',
            'url-regex = forensicstore_stix_schemas:url_regex',
            'marking-definition = forensicstore_stix_schemas:marking_definition',
            'hex = forensicstore_stix_schemas:hex',
            'cyber-observable-core = forensicstore_stix_schemas:cyber_observable_core',
            'dictionary = forensicstore_stix_schemas:dictionary',
            'binary = forensicstore_stix_schemas:binary',
            'core = forensicstore_stix_schemas:core',
            'properties = forensicstore_stix_schemas:properties',
            'language-content = forensicstore_stix_schemas:language_content',
            'timestamp = forensicstore_stix_schemas:timestamp',

        ]
    }
)