# BirdGen

BirdGen Bot - Describe a bird in your mind! 🐥🕊🦆

[![Demo Video on Youtube](https://user-images.githubusercontent.com/35123241/46577927-e0947e80-ca2c-11e8-82a2-2529b5a46373.png)](http://www.youtube.com/watch?v=k8LdmURnlXk "BirdGen Telegram Bot - Describe a bird in your mind!")

* Try BirdGen on Telegram - https://telegram.me/BirdGenBot


## Getting Started

BirdGen is a [BotHub.Studio](https://bothub.studio) project. [Get a free account](https://app.bothub.studio/register) and make interesting bots like BirdGen in few hours. No server required.

*Note: BirdGen bot uses two private DeepNatural APIs*
* *Bird API*
* *Sentiment API*

*If you're interested in private DeepNatural APIs, contact anson@deepnatural.io to get the free-tier API key.*

### Prerequisites

```
python3
pip
```

### Installing

Install the BotHub.Studio command line tool.

```sh
$ pip install bothub-cli
$ bothub --version
0.1.18
```

Enter your BotHub.Studio ID and Password

```sh
$ bothub configure
Please enter your BotHub.Studio login credentials:
username: <your-account-name>
password: <your-password>

Connecting to server...
Identified.
```

Start a new bot project. This will create a basic echo bot.

```sh
$ bothub new
Initialize a new project.
Project name: <your-bot-project-name>
```

Implement the `default_handler` and other features. BotHub.Studio currently supports python3.

```sh
$ cd <your-bot-project-name>
$ vim bothub/bot.py
```


## Local Test

You can run the bot on your local machine. It's very helpful when you actively develop new features before deploying it to the BotHub.Studio cloud.

```sh
$ bothub test

Bothub Test Console
-------------------

Commands:

  /help              Print help menu
  /updateproperties  Update local project properties from server
  /exit              Exit the test console

BotHub> Hi there.
```

## Add messenger channels

Which messenger channel do you want to integrate your bot with? You may choose one or all of them!

Supported channels are:
* [Facebook Messenger](https://medium.com/bothub-studio/build-a-facebook-chatbot-in-python-3b6c7a671c6c)
* [Telegram](https://medium.com/bothub-studio/build-a-telegram-chatbot-with-python-2dafd6c033bd)
* [Slack](https://medium.com/bothub-studio/build-a-slack-chatbot-in-python-eadc27dea15e)
* [KakaoTalk](https://medium.com/bothub-studio/build-a-kakaotalk-chatbot-in-python-c3b49b58e307)
* LINE (soon)

```sh
$ bothub channel add telegram --api-key=<api-key>
$ bothub channel add facebook --app-id=<app-id> --app-secret=<app-secret> --page-access-token=<page-access-token>
$ bothub channel add slack --client-id=<client-id> --client-secret=<client-secret) --signing-secret=<signing-secret>
$ bothub channel add kakao
```

Check the official document:
https://bothub.studio/docs/bothub-cli/#channel-management


## Deployment

```sh
$ bothub deploy
```

That's it! Your bot is live and people can user your bot via the channels you


### Debugging

You can check the runtime error logs like this:

```sh
$ bothub logs
```

## Built With

* BotHub SDK - https://github.com/bothub-studio/bothub-sdk-python
* BotHub CLI - https://github.com/bothub-studio/bothub-cli


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
