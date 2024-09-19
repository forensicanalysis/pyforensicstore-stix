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
            'relationship = forensicstore_stix_schemas:relationship',
            'sighting = forensicstore_stix_schemas:sighting',
            'email-message = forensicstore_stix_schemas:email_message',
            'x509-certificate = forensicstore_stix_schemas:x509_certificate',
            'network-traffic = forensicstore_stix_schemas:network_traffic',
            'ipv6-addr = forensicstore_stix_schemas:ipv6_addr',
            'file = forensicstore_stix_schemas:file',
            'email-addr = forensicstore_stix_schemas:email_addr',
            'url = forensicstore_stix_schemas:url',
            'directory = forensicstore_stix_schemas:directory',
            'software = forensicstore_stix_schemas:software',
            'mutex = forensicstore_stix_schemas:mutex',
            'domain-name = forensicstore_stix_schemas:domain_name',
            'process = forensicstore_stix_schemas:process',
            'mac-addr = forensicstore_stix_schemas:mac_addr',
            'ipv4-addr = forensicstore_stix_schemas:ipv4_addr',
            'artifact = forensicstore_stix_schemas:artifact',
            'autonomous-system = forensicstore_stix_schemas:autonomous_system',
            'windows-registry-key = forensicstore_stix_schemas:windows_registry_key',
            'user-account = forensicstore_stix_schemas:user_account',
            'external-reference = forensicstore_stix_schemas:external_reference',
            'hashes = forensicstore_stix_schemas:hashes',
            'identifier = forensicstore_stix_schemas:identifier',
            'binary = forensicstore_stix_schemas:binary',
            'timestamp = forensicstore_stix_schemas:timestamp',
            'extension-definition = forensicstore_stix_schemas:extension_definition',
            'kill-chain-phase = forensicstore_stix_schemas:kill_chain_phase',
            'cyber-observable-core = forensicstore_stix_schemas:cyber_observable_core',
            'hex = forensicstore_stix_schemas:hex',
            'granular-marking = forensicstore_stix_schemas:granular_marking',
            'bundle = forensicstore_stix_schemas:bundle',
            'marking-definition = forensicstore_stix_schemas:marking_definition',
            'properties = forensicstore_stix_schemas:properties',
            'core = forensicstore_stix_schemas:core',
            'language-content = forensicstore_stix_schemas:language_content',
            'url-regex = forensicstore_stix_schemas:url_regex',
            'dictionary = forensicstore_stix_schemas:dictionary',
            'opinion = forensicstore_stix_schemas:opinion',
            'campaign = forensicstore_stix_schemas:campaign',
            'identity = forensicstore_stix_schemas:identity',
            'indicator = forensicstore_stix_schemas:indicator',
            'attack-pattern = forensicstore_stix_schemas:attack_pattern',
            'incident = forensicstore_stix_schemas:incident',
            'note = forensicstore_stix_schemas:note',
            'observed-data = forensicstore_stix_schemas:observed_data',
            'infrastructure = forensicstore_stix_schemas:infrastructure',
            'course-of-action = forensicstore_stix_schemas:course_of_action',
            'grouping = forensicstore_stix_schemas:grouping',
            'location = forensicstore_stix_schemas:location',
            'intrusion-set = forensicstore_stix_schemas:intrusion_set',
            'malware = forensicstore_stix_schemas:malware',
            'vulnerability = forensicstore_stix_schemas:vulnerability',
            'report = forensicstore_stix_schemas:report',
            'tool = forensicstore_stix_schemas:tool',
            'threat-actor = forensicstore_stix_schemas:threat_actor',
            'malware-analysis = forensicstore_stix_schemas:malware_analysis',

        ]
    }
)
