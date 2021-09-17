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
            'ipv6-addr = forensicstore_stix_schemas:ipv6_addr',
            'x509-certificate = forensicstore_stix_schemas:x509_certificate',
            'mac-addr = forensicstore_stix_schemas:mac_addr',
            'artifact = forensicstore_stix_schemas:artifact',
            'directory = forensicstore_stix_schemas:directory',
            'email-addr = forensicstore_stix_schemas:email_addr',
            'email-message = forensicstore_stix_schemas:email_message',
            'user-account = forensicstore_stix_schemas:user_account',
            'domain-name = forensicstore_stix_schemas:domain_name',
            'mutex = forensicstore_stix_schemas:mutex',
            'process = forensicstore_stix_schemas:process',
            'url = forensicstore_stix_schemas:url',
            'network-traffic = forensicstore_stix_schemas:network_traffic',
            'file = forensicstore_stix_schemas:file',
            'windows-registry-key = forensicstore_stix_schemas:windows_registry_key',
            'autonomous-system = forensicstore_stix_schemas:autonomous_system',
            'ipv4-addr = forensicstore_stix_schemas:ipv4_addr',
            'software = forensicstore_stix_schemas:software',
            'cyber-observable-core = forensicstore_stix_schemas:cyber_observable_core',
            'language-content = forensicstore_stix_schemas:language_content',
            'core = forensicstore_stix_schemas:core',
            'marking-definition = forensicstore_stix_schemas:marking_definition',
            'bundle = forensicstore_stix_schemas:bundle',
            'kill-chain-phase = forensicstore_stix_schemas:kill_chain_phase',
            'identifier = forensicstore_stix_schemas:identifier',
            'timestamp = forensicstore_stix_schemas:timestamp',
            'external-reference = forensicstore_stix_schemas:external_reference',
            'properties = forensicstore_stix_schemas:properties',
            'hashes = forensicstore_stix_schemas:hashes',
            'binary = forensicstore_stix_schemas:binary',
            'extension-definition = forensicstore_stix_schemas:extension_definition',
            'granular-marking = forensicstore_stix_schemas:granular_marking',
            'dictionary = forensicstore_stix_schemas:dictionary',
            'hex = forensicstore_stix_schemas:hex',
            'url-regex = forensicstore_stix_schemas:url_regex',
            'infrastructure = forensicstore_stix_schemas:infrastructure',
            'opinion = forensicstore_stix_schemas:opinion',
            'observed-data = forensicstore_stix_schemas:observed_data',
            'grouping = forensicstore_stix_schemas:grouping',
            'course-of-action = forensicstore_stix_schemas:course_of_action',
            'report = forensicstore_stix_schemas:report',
            'intrusion-set = forensicstore_stix_schemas:intrusion_set',
            'vulnerability = forensicstore_stix_schemas:vulnerability',
            'attack-pattern = forensicstore_stix_schemas:attack_pattern',
            'malware-analysis = forensicstore_stix_schemas:malware_analysis',
            'identity = forensicstore_stix_schemas:identity',
            'note = forensicstore_stix_schemas:note',
            'incident = forensicstore_stix_schemas:incident',
            'malware = forensicstore_stix_schemas:malware',
            'location = forensicstore_stix_schemas:location',
            'threat-actor = forensicstore_stix_schemas:threat_actor',
            'indicator = forensicstore_stix_schemas:indicator',
            'campaign = forensicstore_stix_schemas:campaign',
            'tool = forensicstore_stix_schemas:tool',
            'relationship = forensicstore_stix_schemas:relationship',
            'sighting = forensicstore_stix_schemas:sighting',

        ]
    }
)
