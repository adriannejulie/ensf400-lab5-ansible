import ansible_runner
import os

# Run plays from hello.yml
f = open("./secrets/id_rsa", "r")
ssh = f.read()
private_data_dir = '.'
run_config = ansible_runner.RunnerConfig(
    inventory="./hosts.yml",
    playbook='./hello.yml',
    private_data_dir=private_data_dir,
    ssh_key=ssh
 )
error = run_config.prepare()

if error:
    print("Error running the playbook")
    print(error)
    exit (1)

ansible_runner.run_command('docker compose up -d')
r = ansible_runner.Runner(config=run_config)
result = r.run()

print("Verifying that apps are working:")
for _ in range(6):  
    result = os.popen("curl --silent http://0.0.0.0").read()
    print(result)