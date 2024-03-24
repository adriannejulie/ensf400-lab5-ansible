import ansible_runner
import os

# Run plays from hello.yml
run_config = ansible_runner.RunnerConfig(
     playbook='./hello.yml',
     envvars={'ANSIBLE_CONFIG': './ansible.cfg'}
 )
run_config.prepare()
ansible_runner.run_command('docker compose up -d')
r = ansible_runner.Runner(config=run_config)
r.run()

print("Verifying that apps are working:")
for _ in range(6):  
    result = os.popen("curl --silent http://0.0.0.0").read()
    print(result)