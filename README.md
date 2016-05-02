# Raspberry-Pi-Deployer
Easily deploy &amp; manage apps on a raspberry pi

# Setup
Firstly set up `setup.json` file with all repositories you want to deploy along with their related cronjobs:
```
{
  "username": "pi",
  "apps": [
    {
      "description": "Morning LED strip",
      "repo": "https://github.com/Manoj-nathwani/energenie-raspberry-pi",
      "cronjobs": [
        {
          "schedule": "45 7 * * *",
          "command": "python energenie-raspberry-pi/energenie.py 1=on"
        },
        {
          "schedule": "30 8 * * *",
          "command": "python energenie-raspberry-pi/energenie.py 1=off"
        }
      ]
    },
    {
      "description": "Morning alarm clock",
      "repo": "https://github.com/Manoj-nathwani/fitbit-alarm-clock",
      "cronjobs": [
        {
          "schedule": "45 7 * * 1-5",
          "command": "omxplayer /home/pi/Downloads/morning.mp3"
        },
        {
          "schedule": "45 7 * * 1-5",
          "command": "python fitbit-alarm-clock main.py"
        }
      ]
    }
  ]
}

```

Then clone this repo onto your raspberry pi and run `python app.py` to deploy all your apps
