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
            'dictionary = forensicstore_stix_schemas:dictionary',
            'extension-definition = forensicstore_stix_schemas:extension_definition',
            'kill-chain-phase = forensicstore_stix_schemas:kill_chain_phase',
            'timestamp = forensicstore_stix_schemas:timestamp',
            'identifier = forensicstore_stix_schemas:identifier',
            'hex = forensicstore_stix_schemas:hex',
            'url-regex = forensicstore_stix_schemas:url_regex',
            'hashes = forensicstore_stix_schemas:hashes',
            'language-content = forensicstore_stix_schemas:language_content',
            'cyber-observable-core = forensicstore_stix_schemas:cyber_observable_core',
            'marking-definition = forensicstore_stix_schemas:marking_definition',
            'granular-marking = forensicstore_stix_schemas:granular_marking',
            'binary = forensicstore_stix_schemas:binary',
            'core = forensicstore_stix_schemas:core',
            'bundle = forensicstore_stix_schemas:bundle',
            'external-reference = forensicstore_stix_schemas:external_reference',
            'properties = forensicstore_stix_schemas:properties',
            'campaign = forensicstore_stix_schemas:campaign',
            'malware-analysis = forensicstore_stix_schemas:malware_analysis',
            'vulnerability = forensicstore_stix_schemas:vulnerability',
            'observed-data = forensicstore_stix_schemas:observed_data',
            'course-of-action = forensicstore_stix_schemas:course_of_action',
            'tool = forensicstore_stix_schemas:tool',
            'note = forensicstore_stix_schemas:note',
            'location = forensicstore_stix_schemas:location',
            'opinion = forensicstore_stix_schemas:opinion',
            'indicator = forensicstore_stix_schemas:indicator',
            'report = forensicstore_stix_schemas:report',
            'threat-actor = forensicstore_stix_schemas:threat_actor',
            'intrusion-set = forensicstore_stix_schemas:intrusion_set',
            'attack-pattern = forensicstore_stix_schemas:attack_pattern',
            'grouping = forensicstore_stix_schemas:grouping',
            'malware = forensicstore_stix_schemas:malware',
            'incident = forensicstore_stix_schemas:incident',
            'identity = forensicstore_stix_schemas:identity',
            'infrastructure = forensicstore_stix_schemas:infrastructure',
            'sighting = forensicstore_stix_schemas:sighting',
            'relationship = forensicstore_stix_schemas:relationship',
            'software = forensicstore_stix_schemas:software',
            'mutex = forensicstore_stix_schemas:mutex',
            'email-addr = forensicstore_stix_schemas:email_addr',
            'autonomous-system = forensicstore_stix_schemas:autonomous_system',
            'email-message = forensicstore_stix_schemas:email_message',
            'x509-certificate = forensicstore_stix_schemas:x509_certificate',
            'directory = forensicstore_stix_schemas:directory',
            'network-traffic = forensicstore_stix_schemas:network_traffic',
            'domain-name = forensicstore_stix_schemas:domain_name',
            'file = forensicstore_stix_schemas:file',
            'artifact = forensicstore_stix_schemas:artifact',
            'ipv4-addr = forensicstore_stix_schemas:ipv4_addr',
            'user-account = forensicstore_stix_schemas:user_account',
            'process = forensicstore_stix_schemas:process',
            'ipv6-addr = forensicstore_stix_schemas:ipv6_addr',
            'url = forensicstore_stix_schemas:url',
            'mac-addr = forensicstore_stix_schemas:mac_addr',
            'windows-registry-key = forensicstore_stix_schemas:windows_registry_key',

        ]
    }
)
