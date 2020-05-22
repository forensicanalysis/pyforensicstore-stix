
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
            'relationship = forensicstore_stix_schemas:relationship',
            'sighting = forensicstore_stix_schemas:sighting',
            'granular-marking = forensicstore_stix_schemas:granular_marking',
            'properties = forensicstore_stix_schemas:properties',
            'language-content = forensicstore_stix_schemas:language_content',
            'timestamp = forensicstore_stix_schemas:timestamp',
            'hex = forensicstore_stix_schemas:hex',
            'url-regex = forensicstore_stix_schemas:url_regex',
            'kill-chain-phase = forensicstore_stix_schemas:kill_chain_phase',
            'core = forensicstore_stix_schemas:core',
            'binary = forensicstore_stix_schemas:binary',
            'marking-definition = forensicstore_stix_schemas:marking_definition',
            'dictionary = forensicstore_stix_schemas:dictionary',
            'external-reference = forensicstore_stix_schemas:external_reference',
            'bundle = forensicstore_stix_schemas:bundle',
            'cyber-observable-core = forensicstore_stix_schemas:cyber_observable_core',
            'identifier = forensicstore_stix_schemas:identifier',
            'hashes = forensicstore_stix_schemas:hashes',
            'threat-actor = forensicstore_stix_schemas:threat_actor',
            'opinion = forensicstore_stix_schemas:opinion',
            'report = forensicstore_stix_schemas:report',
            'attack-pattern = forensicstore_stix_schemas:attack_pattern',
            'malware-analysis = forensicstore_stix_schemas:malware_analysis',
            'vulnerability = forensicstore_stix_schemas:vulnerability',
            'campaign = forensicstore_stix_schemas:campaign',
            'infrastructure = forensicstore_stix_schemas:infrastructure',
            'observed-data = forensicstore_stix_schemas:observed_data',
            'intrusion-set = forensicstore_stix_schemas:intrusion_set',
            'malware = forensicstore_stix_schemas:malware',
            'identity = forensicstore_stix_schemas:identity',
            'indicator = forensicstore_stix_schemas:indicator',
            'course-of-action = forensicstore_stix_schemas:course_of_action',
            'grouping = forensicstore_stix_schemas:grouping',
            'tool = forensicstore_stix_schemas:tool',
            'location = forensicstore_stix_schemas:location',
            'note = forensicstore_stix_schemas:note',
            'windows-registry-key = forensicstore_stix_schemas:windows_registry_key',
            'network-traffic = forensicstore_stix_schemas:network_traffic',
            'ipv4-addr = forensicstore_stix_schemas:ipv4_addr',
            'ipv6-addr = forensicstore_stix_schemas:ipv6_addr',
            'mutex = forensicstore_stix_schemas:mutex',
            'software = forensicstore_stix_schemas:software',
            'directory = forensicstore_stix_schemas:directory',
            'file = forensicstore_stix_schemas:file',
            'url = forensicstore_stix_schemas:url',
            'domain-name = forensicstore_stix_schemas:domain_name',
            'email-addr = forensicstore_stix_schemas:email_addr',
            'artifact = forensicstore_stix_schemas:artifact',
            'email-message = forensicstore_stix_schemas:email_message',
            'process = forensicstore_stix_schemas:process',
            'autonomous-system = forensicstore_stix_schemas:autonomous_system',
            'x509-certificate = forensicstore_stix_schemas:x509_certificate',
            'user-account = forensicstore_stix_schemas:user_account',
            'mac-addr = forensicstore_stix_schemas:mac_addr',

        ]
    }
)
