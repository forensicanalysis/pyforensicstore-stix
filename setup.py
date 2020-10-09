# Copyright (c) 2020 Siemens AG
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# Author(s): Demian Kellermann

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
            'sighting = forensicstore_stix_schemas:sighting',
            'relationship = forensicstore_stix_schemas:relationship',
            'ipv6-addr = forensicstore_stix_schemas:ipv6_addr',
            'email-addr = forensicstore_stix_schemas:email_addr',
            'file = forensicstore_stix_schemas:file',
            'x509-certificate = forensicstore_stix_schemas:x509_certificate',
            'mutex = forensicstore_stix_schemas:mutex',
            'domain-name = forensicstore_stix_schemas:domain_name',
            'url = forensicstore_stix_schemas:url',
            'autonomous-system = forensicstore_stix_schemas:autonomous_system',
            'user-account = forensicstore_stix_schemas:user_account',
            'directory = forensicstore_stix_schemas:directory',
            'mac-addr = forensicstore_stix_schemas:mac_addr',
            'windows-registry-key = forensicstore_stix_schemas:windows_registry_key',
            'email-message = forensicstore_stix_schemas:email_message',
            'artifact = forensicstore_stix_schemas:artifact',
            'software = forensicstore_stix_schemas:software',
            'ipv4-addr = forensicstore_stix_schemas:ipv4_addr',
            'network-traffic = forensicstore_stix_schemas:network_traffic',
            'process = forensicstore_stix_schemas:process',
            'hashes = forensicstore_stix_schemas:hashes',
            'binary = forensicstore_stix_schemas:binary',
            'kill-chain-phase = forensicstore_stix_schemas:kill_chain_phase',
            'core = forensicstore_stix_schemas:core',
            'timestamp = forensicstore_stix_schemas:timestamp',
            'properties = forensicstore_stix_schemas:properties',
            'identifier = forensicstore_stix_schemas:identifier',
            'language-content = forensicstore_stix_schemas:language_content',
            'url-regex = forensicstore_stix_schemas:url_regex',
            'hex = forensicstore_stix_schemas:hex',
            'granular-marking = forensicstore_stix_schemas:granular_marking',
            'marking-definition = forensicstore_stix_schemas:marking_definition',
            'bundle = forensicstore_stix_schemas:bundle',
            'dictionary = forensicstore_stix_schemas:dictionary',
            'external-reference = forensicstore_stix_schemas:external_reference',
            'cyber-observable-core = forensicstore_stix_schemas:cyber_observable_core',
            'malware = forensicstore_stix_schemas:malware',
            'intrusion-set = forensicstore_stix_schemas:intrusion_set',
            'attack-pattern = forensicstore_stix_schemas:attack_pattern',
            'vulnerability = forensicstore_stix_schemas:vulnerability',
            'grouping = forensicstore_stix_schemas:grouping',
            'report = forensicstore_stix_schemas:report',
            'identity = forensicstore_stix_schemas:identity',
            'note = forensicstore_stix_schemas:note',
            'threat-actor = forensicstore_stix_schemas:threat_actor',
            'course-of-action = forensicstore_stix_schemas:course_of_action',
            'indicator = forensicstore_stix_schemas:indicator',
            'malware-analysis = forensicstore_stix_schemas:malware_analysis',
            'infrastructure = forensicstore_stix_schemas:infrastructure',
            'campaign = forensicstore_stix_schemas:campaign',
            'tool = forensicstore_stix_schemas:tool',
            'observed-data = forensicstore_stix_schemas:observed_data',
            'opinion = forensicstore_stix_schemas:opinion',
            'location = forensicstore_stix_schemas:location',

        ]
    }
)
