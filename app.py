import json, os
from crontab import CronTab

settings = json.load(open("setup.json", "r"))
username = settings['username']
cron = CronTab(user=username)

def crontab_init():
    cron.remove_all()
    cron.write()

def process_setup_file():
    for app in settings["apps"]:
        print "----- Deploying {} -----".format(app["description"])
        if "repo" in app:
            clone_repo(app["repo"])
        if "cronjobs" in app:
            add_cronjobs(app["description"], app["cronjobs"])

def clone_repo(repo):
    repo_name = repo.split("/")[-1]
    repo_directory = "/home/{}/{}".format(username, repo_name)
    os.system("rm -rf " + repo_directory)
    os.system("git clone {} {}".format(repo, repo_directory))

def add_cronjobs(description, cronjobs):
    for cronjob in cronjobs:
        job  = cron.new(
            command=cronjob['command'],
            comment=description)
        job.setall(cronjob['schedule'])
        cron.write()

crontab_init()
process_setup_file()
