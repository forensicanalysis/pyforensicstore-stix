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
            'grouping = forensicstore_stix_schemas:grouping',
            'intrusion-set = forensicstore_stix_schemas:intrusion_set',
            'identity = forensicstore_stix_schemas:identity',
            'observed-data = forensicstore_stix_schemas:observed_data',
            'note = forensicstore_stix_schemas:note',
            'opinion = forensicstore_stix_schemas:opinion',
            'tool = forensicstore_stix_schemas:tool',
            'report = forensicstore_stix_schemas:report',
            'location = forensicstore_stix_schemas:location',
            'threat-actor = forensicstore_stix_schemas:threat_actor',
            'attack-pattern = forensicstore_stix_schemas:attack_pattern',
            'campaign = forensicstore_stix_schemas:campaign',
            'malware = forensicstore_stix_schemas:malware',
            'course-of-action = forensicstore_stix_schemas:course_of_action',
            'malware-analysis = forensicstore_stix_schemas:malware_analysis',
            'infrastructure = forensicstore_stix_schemas:infrastructure',
            'vulnerability = forensicstore_stix_schemas:vulnerability',
            'indicator = forensicstore_stix_schemas:indicator',
            'sighting = forensicstore_stix_schemas:sighting',
            'relationship = forensicstore_stix_schemas:relationship',
            'properties = forensicstore_stix_schemas:properties',
            'granular-marking = forensicstore_stix_schemas:granular_marking',
            'bundle = forensicstore_stix_schemas:bundle',
            'identifier = forensicstore_stix_schemas:identifier',
            'cyber-observable-core = forensicstore_stix_schemas:cyber_observable_core',
            'dictionary = forensicstore_stix_schemas:dictionary',
            'kill-chain-phase = forensicstore_stix_schemas:kill_chain_phase',
            'hex = forensicstore_stix_schemas:hex',
            'marking-definition = forensicstore_stix_schemas:marking_definition',
            'url-regex = forensicstore_stix_schemas:url_regex',
            'binary = forensicstore_stix_schemas:binary',
            'external-reference = forensicstore_stix_schemas:external_reference',
            'hashes = forensicstore_stix_schemas:hashes',
            'language-content = forensicstore_stix_schemas:language_content',
            'timestamp = forensicstore_stix_schemas:timestamp',
            'core = forensicstore_stix_schemas:core',
            'directory = forensicstore_stix_schemas:directory',
            'windows-registry-key = forensicstore_stix_schemas:windows_registry_key',
            'file = forensicstore_stix_schemas:file',
            'software = forensicstore_stix_schemas:software',
            'email-message = forensicstore_stix_schemas:email_message',
            'process = forensicstore_stix_schemas:process',
            'artifact = forensicstore_stix_schemas:artifact',
            'user-account = forensicstore_stix_schemas:user_account',
            'autonomous-system = forensicstore_stix_schemas:autonomous_system',
            'mutex = forensicstore_stix_schemas:mutex',
            'x509-certificate = forensicstore_stix_schemas:x509_certificate',
            'mac-addr = forensicstore_stix_schemas:mac_addr',
            'ipv4-addr = forensicstore_stix_schemas:ipv4_addr',
            'domain-name = forensicstore_stix_schemas:domain_name',
            'email-addr = forensicstore_stix_schemas:email_addr',
            'url = forensicstore_stix_schemas:url',
            'ipv6-addr = forensicstore_stix_schemas:ipv6_addr',
            'network-traffic = forensicstore_stix_schemas:network_traffic',

        ]
    }
)
