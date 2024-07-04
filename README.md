## Ansible network resource module: OpenGear CM71xx

Currently only supports facts gathering.

```yaml
- name: Gather facts
  hosts:
    - opengear-console
  vars:
    ansible_connection: ansible.netcommon.httpapi
    ansible_network_os: opengear.cm71xx.cm71xx
    ansible_httpapi_password: "{{ lookup('ansible.builtin.env', 'console_password') }}"
    ansible_httpapi_username: username
    ansible_httpapi_use_ssl: true
    ansible_httpapi_port: 443
  gather_facts: no
  tasks:
    - name: Gather OpenGear facts
      opengear.cm71xx.cm71xx_facts:
        gather_network_resources:
          - all
#         - auth
#         - groups
#         - ports
#         - node_description
#         - system
#         - users
      delegate_facts: true
    - name: Show facts
      ansible.builtin.debug:
        var: ansible_facts
```
