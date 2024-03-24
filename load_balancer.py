import ansible_runner
import time 

if __name__ == "__main__":
    ansible_runner.run_command(envvars={'ANSIBLE_CONFIG': './ansible.cfg'}, executable_cmd='docker compose up -d')

    out, err, code = ansible_runner.get_inventory(
        action='list',
        inventories=['./hosts.yml'],
        response_format='json',
        envvars={'ANSIBLE_CONFIG': './ansible.cfg'}
    )

    if code != 0:
        print("Error running the playbook")
        print(err)
        exit(1)

    for host, info in out["_meta"]["hostvars"].items():
        ip_address = info["ansible_host"]
        group_name = list(out.keys())[2]
        print(f"Host: {host}")
        print(f"IP Address: {ip_address}")
        print(f"Group: {group_name}")
    time.sleep(10)

    response, error, code = ansible_runner.run_command(envvars={'ANSIBLE_CONFIG': './ansible.cfg'}, 
                                                       executable_cmd='ansible all:localhost -m ping')
    
    if code != 0:
        print("Error when pinging hosts")
        print(error)
        exit(1)