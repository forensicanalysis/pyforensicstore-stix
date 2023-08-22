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
            'observed-data = forensicstore_stix_schemas:observed_data',
            'course-of-action = forensicstore_stix_schemas:course_of_action',
            'malware = forensicstore_stix_schemas:malware',
            'indicator = forensicstore_stix_schemas:indicator',
            'opinion = forensicstore_stix_schemas:opinion',
            'vulnerability = forensicstore_stix_schemas:vulnerability',
            'grouping = forensicstore_stix_schemas:grouping',
            'identity = forensicstore_stix_schemas:identity',
            'location = forensicstore_stix_schemas:location',
            'report = forensicstore_stix_schemas:report',
            'intrusion-set = forensicstore_stix_schemas:intrusion_set',
            'incident = forensicstore_stix_schemas:incident',
            'campaign = forensicstore_stix_schemas:campaign',
            'infrastructure = forensicstore_stix_schemas:infrastructure',
            'threat-actor = forensicstore_stix_schemas:threat_actor',
            'malware-analysis = forensicstore_stix_schemas:malware_analysis',
            'attack-pattern = forensicstore_stix_schemas:attack_pattern',
            'note = forensicstore_stix_schemas:note',
            'tool = forensicstore_stix_schemas:tool',
            'relationship = forensicstore_stix_schemas:relationship',
            'sighting = forensicstore_stix_schemas:sighting',
            'software = forensicstore_stix_schemas:software',
            'email-addr = forensicstore_stix_schemas:email_addr',
            'windows-registry-key = forensicstore_stix_schemas:windows_registry_key',
            'email-message = forensicstore_stix_schemas:email_message',
            'autonomous-system = forensicstore_stix_schemas:autonomous_system',
            'mac-addr = forensicstore_stix_schemas:mac_addr',
            'directory = forensicstore_stix_schemas:directory',
            'domain-name = forensicstore_stix_schemas:domain_name',
            'x509-certificate = forensicstore_stix_schemas:x509_certificate',
            'file = forensicstore_stix_schemas:file',
            'ipv4-addr = forensicstore_stix_schemas:ipv4_addr',
            'mutex = forensicstore_stix_schemas:mutex',
            'artifact = forensicstore_stix_schemas:artifact',
            'network-traffic = forensicstore_stix_schemas:network_traffic',
            'process = forensicstore_stix_schemas:process',
            'ipv6-addr = forensicstore_stix_schemas:ipv6_addr',
            'user-account = forensicstore_stix_schemas:user_account',
            'url = forensicstore_stix_schemas:url',
            'url-regex = forensicstore_stix_schemas:url_regex',
            'core = forensicstore_stix_schemas:core',
            'binary = forensicstore_stix_schemas:binary',
            'language-content = forensicstore_stix_schemas:language_content',
            'timestamp = forensicstore_stix_schemas:timestamp',
            'extension-definition = forensicstore_stix_schemas:extension_definition',
            'external-reference = forensicstore_stix_schemas:external_reference',
            'dictionary = forensicstore_stix_schemas:dictionary',
            'bundle = forensicstore_stix_schemas:bundle',
            'identifier = forensicstore_stix_schemas:identifier',
            'hashes = forensicstore_stix_schemas:hashes',
            'properties = forensicstore_stix_schemas:properties',
            'kill-chain-phase = forensicstore_stix_schemas:kill_chain_phase',
            'marking-definition = forensicstore_stix_schemas:marking_definition',
            'hex = forensicstore_stix_schemas:hex',
            'granular-marking = forensicstore_stix_schemas:granular_marking',
            'cyber-observable-core = forensicstore_stix_schemas:cyber_observable_core',

        ]
    }
)
