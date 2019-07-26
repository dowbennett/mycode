#!/usr/bin/env python3

ANSIBLE_METADATA = {
        'metadata_version' : '1.1',
        'status' : ['preview'],
        'supported_by' : 'community'
        }

DOCUMENTATION = '''
---
module: my_new_test_module

short_description: This is my sample module

version_added: "2.4"

description: 
    - "This is my longer description explaining my sample module"

options:
    name:
        descriptions:
            - This is the message to send to the sampl module
        required: true
    new:
        description:
            - Control to demo if the result of this module is changed or not
        required: false
    author:
        - Dow Bennett
'''

EXAMPLES = '''
#Pass in a message
- name: Test with a message
  my_new_test_module:
    name: hello world

#Pass in message and have changed true
- name: Test with a message and changed output
  my_new_test_module:
    name: hello world
    new: true

#Fail the module
- name: Test failure of the module
  my_new_test_module:
    name: fail me
'''

RETURN = '''
Original_message:
    description: The original name param that was passed in
    type: str
message:
    description: The output message that the sample module generates
'''

from ansible.module_utils.basic import AnsibleModule

def run_module():
    module_args = dict(
        name=dict(type='str', required=True),
        new=dict(type='bool', required=False, default=False)
    )

    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        return result

    result['original_message'] = module.params['name']
    result['message'] = 'goodbye'

    if module.params['new']:
        result['changed'] = True

    if module.params['name'] == 'fail me':
        module.fail_json(msg='You requested this to fail', **result)

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
