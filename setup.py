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
            'location = forensicstore_stix_schemas:location',
            'indicator = forensicstore_stix_schemas:indicator',
            'observed-data = forensicstore_stix_schemas:observed_data',
            'attack-pattern = forensicstore_stix_schemas:attack_pattern',
            'malware = forensicstore_stix_schemas:malware',
            'incident = forensicstore_stix_schemas:incident',
            'tool = forensicstore_stix_schemas:tool',
            'vulnerability = forensicstore_stix_schemas:vulnerability',
            'threat-actor = forensicstore_stix_schemas:threat_actor',
            'report = forensicstore_stix_schemas:report',
            'campaign = forensicstore_stix_schemas:campaign',
            'note = forensicstore_stix_schemas:note',
            'infrastructure = forensicstore_stix_schemas:infrastructure',
            'identity = forensicstore_stix_schemas:identity',
            'grouping = forensicstore_stix_schemas:grouping',
            'opinion = forensicstore_stix_schemas:opinion',
            'intrusion-set = forensicstore_stix_schemas:intrusion_set',
            'course-of-action = forensicstore_stix_schemas:course_of_action',
            'malware-analysis = forensicstore_stix_schemas:malware_analysis',
            'kill-chain-phase = forensicstore_stix_schemas:kill_chain_phase',
            'binary = forensicstore_stix_schemas:binary',
            'granular-marking = forensicstore_stix_schemas:granular_marking',
            'language-content = forensicstore_stix_schemas:language_content',
            'hex = forensicstore_stix_schemas:hex',
            'timestamp = forensicstore_stix_schemas:timestamp',
            'dictionary = forensicstore_stix_schemas:dictionary',
            'bundle = forensicstore_stix_schemas:bundle',
            'cyber-observable-core = forensicstore_stix_schemas:cyber_observable_core',
            'marking-definition = forensicstore_stix_schemas:marking_definition',
            'extension-definition = forensicstore_stix_schemas:extension_definition',
            'properties = forensicstore_stix_schemas:properties',
            'core = forensicstore_stix_schemas:core',
            'url-regex = forensicstore_stix_schemas:url_regex',
            'hashes = forensicstore_stix_schemas:hashes',
            'external-reference = forensicstore_stix_schemas:external_reference',
            'identifier = forensicstore_stix_schemas:identifier',
            'ipv6-addr = forensicstore_stix_schemas:ipv6_addr',
            'email-addr = forensicstore_stix_schemas:email_addr',
            'domain-name = forensicstore_stix_schemas:domain_name',
            'ipv4-addr = forensicstore_stix_schemas:ipv4_addr',
            'url = forensicstore_stix_schemas:url',
            'windows-registry-key = forensicstore_stix_schemas:windows_registry_key',
            'directory = forensicstore_stix_schemas:directory',
            'x509-certificate = forensicstore_stix_schemas:x509_certificate',
            'network-traffic = forensicstore_stix_schemas:network_traffic',
            'autonomous-system = forensicstore_stix_schemas:autonomous_system',
            'user-account = forensicstore_stix_schemas:user_account',
            'software = forensicstore_stix_schemas:software',
            'mac-addr = forensicstore_stix_schemas:mac_addr',
            'artifact = forensicstore_stix_schemas:artifact',
            'email-message = forensicstore_stix_schemas:email_message',
            'file = forensicstore_stix_schemas:file',
            'process = forensicstore_stix_schemas:process',
            'mutex = forensicstore_stix_schemas:mutex',
            'relationship = forensicstore_stix_schemas:relationship',
            'sighting = forensicstore_stix_schemas:sighting',

        ]
    }
)
