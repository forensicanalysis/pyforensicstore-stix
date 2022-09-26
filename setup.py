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
            'x509-certificate = forensicstore_stix_schemas:x509_certificate',
            'ipv4-addr = forensicstore_stix_schemas:ipv4_addr',
            'ipv6-addr = forensicstore_stix_schemas:ipv6_addr',
            'domain-name = forensicstore_stix_schemas:domain_name',
            'directory = forensicstore_stix_schemas:directory',
            'artifact = forensicstore_stix_schemas:artifact',
            'email-addr = forensicstore_stix_schemas:email_addr',
            'network-traffic = forensicstore_stix_schemas:network_traffic',
            'windows-registry-key = forensicstore_stix_schemas:windows_registry_key',
            'mutex = forensicstore_stix_schemas:mutex',
            'software = forensicstore_stix_schemas:software',
            'email-message = forensicstore_stix_schemas:email_message',
            'file = forensicstore_stix_schemas:file',
            'user-account = forensicstore_stix_schemas:user_account',
            'autonomous-system = forensicstore_stix_schemas:autonomous_system',
            'process = forensicstore_stix_schemas:process',
            'mac-addr = forensicstore_stix_schemas:mac_addr',
            'url = forensicstore_stix_schemas:url',
            'sighting = forensicstore_stix_schemas:sighting',
            'relationship = forensicstore_stix_schemas:relationship',
            'indicator = forensicstore_stix_schemas:indicator',
            'infrastructure = forensicstore_stix_schemas:infrastructure',
            'observed-data = forensicstore_stix_schemas:observed_data',
            'incident = forensicstore_stix_schemas:incident',
            'location = forensicstore_stix_schemas:location',
            'threat-actor = forensicstore_stix_schemas:threat_actor',
            'tool = forensicstore_stix_schemas:tool',
            'opinion = forensicstore_stix_schemas:opinion',
            'identity = forensicstore_stix_schemas:identity',
            'vulnerability = forensicstore_stix_schemas:vulnerability',
            'report = forensicstore_stix_schemas:report',
            'course-of-action = forensicstore_stix_schemas:course_of_action',
            'intrusion-set = forensicstore_stix_schemas:intrusion_set',
            'note = forensicstore_stix_schemas:note',
            'malware = forensicstore_stix_schemas:malware',
            'malware-analysis = forensicstore_stix_schemas:malware_analysis',
            'campaign = forensicstore_stix_schemas:campaign',
            'grouping = forensicstore_stix_schemas:grouping',
            'attack-pattern = forensicstore_stix_schemas:attack_pattern',
            'properties = forensicstore_stix_schemas:properties',
            'external-reference = forensicstore_stix_schemas:external_reference',
            'kill-chain-phase = forensicstore_stix_schemas:kill_chain_phase',
            'timestamp = forensicstore_stix_schemas:timestamp',
            'granular-marking = forensicstore_stix_schemas:granular_marking',
            'cyber-observable-core = forensicstore_stix_schemas:cyber_observable_core',
            'binary = forensicstore_stix_schemas:binary',
            'bundle = forensicstore_stix_schemas:bundle',
            'marking-definition = forensicstore_stix_schemas:marking_definition',
            'extension-definition = forensicstore_stix_schemas:extension_definition',
            'hex = forensicstore_stix_schemas:hex',
            'url-regex = forensicstore_stix_schemas:url_regex',
            'dictionary = forensicstore_stix_schemas:dictionary',
            'identifier = forensicstore_stix_schemas:identifier',
            'hashes = forensicstore_stix_schemas:hashes',
            'core = forensicstore_stix_schemas:core',
            'language-content = forensicstore_stix_schemas:language_content',

        ]
    }
)
