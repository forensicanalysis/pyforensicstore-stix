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
            'software = forensicstore_stix_schemas:software',
            'process = forensicstore_stix_schemas:process',
            'file = forensicstore_stix_schemas:file',
            'mutex = forensicstore_stix_schemas:mutex',
            'user-account = forensicstore_stix_schemas:user_account',
            'mac-addr = forensicstore_stix_schemas:mac_addr',
            'network-traffic = forensicstore_stix_schemas:network_traffic',
            'windows-registry-key = forensicstore_stix_schemas:windows_registry_key',
            'artifact = forensicstore_stix_schemas:artifact',
            'ipv6-addr = forensicstore_stix_schemas:ipv6_addr',
            'autonomous-system = forensicstore_stix_schemas:autonomous_system',
            'directory = forensicstore_stix_schemas:directory',
            'domain-name = forensicstore_stix_schemas:domain_name',
            'url = forensicstore_stix_schemas:url',
            'email-addr = forensicstore_stix_schemas:email_addr',
            'x509-certificate = forensicstore_stix_schemas:x509_certificate',
            'ipv4-addr = forensicstore_stix_schemas:ipv4_addr',
            'email-message = forensicstore_stix_schemas:email_message',
            'bundle = forensicstore_stix_schemas:bundle',
            'granular-marking = forensicstore_stix_schemas:granular_marking',
            'dictionary = forensicstore_stix_schemas:dictionary',
            'binary = forensicstore_stix_schemas:binary',
            'cyber-observable-core = forensicstore_stix_schemas:cyber_observable_core',
            'properties = forensicstore_stix_schemas:properties',
            'kill-chain-phase = forensicstore_stix_schemas:kill_chain_phase',
            'timestamp = forensicstore_stix_schemas:timestamp',
            'url-regex = forensicstore_stix_schemas:url_regex',
            'marking-definition = forensicstore_stix_schemas:marking_definition',
            'core = forensicstore_stix_schemas:core',
            'external-reference = forensicstore_stix_schemas:external_reference',
            'language-content = forensicstore_stix_schemas:language_content',
            'identifier = forensicstore_stix_schemas:identifier',
            'hex = forensicstore_stix_schemas:hex',
            'extension-definition = forensicstore_stix_schemas:extension_definition',
            'hashes = forensicstore_stix_schemas:hashes',
            'location = forensicstore_stix_schemas:location',
            'opinion = forensicstore_stix_schemas:opinion',
            'malware = forensicstore_stix_schemas:malware',
            'tool = forensicstore_stix_schemas:tool',
            'observed-data = forensicstore_stix_schemas:observed_data',
            'grouping = forensicstore_stix_schemas:grouping',
            'threat-actor = forensicstore_stix_schemas:threat_actor',
            'incident = forensicstore_stix_schemas:incident',
            'indicator = forensicstore_stix_schemas:indicator',
            'course-of-action = forensicstore_stix_schemas:course_of_action',
            'note = forensicstore_stix_schemas:note',
            'infrastructure = forensicstore_stix_schemas:infrastructure',
            'report = forensicstore_stix_schemas:report',
            'malware-analysis = forensicstore_stix_schemas:malware_analysis',
            'campaign = forensicstore_stix_schemas:campaign',
            'attack-pattern = forensicstore_stix_schemas:attack_pattern',
            'intrusion-set = forensicstore_stix_schemas:intrusion_set',
            'vulnerability = forensicstore_stix_schemas:vulnerability',
            'identity = forensicstore_stix_schemas:identity',

        ]
    }
)
